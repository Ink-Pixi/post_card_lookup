import sys
import ctypes
from data import remove_mailing_database
from ui import Ui_mwMailingRemove
from PyQt5.QtWidgets import QMainWindow, QApplication, QTableWidgetItem, QMessageBox, QLabel, QSizePolicy, QVBoxLayout, QWidget
from PyQt5.QtGui import QMovie
from PyQt5.QtCore import Qt, QThread, pyqtSignal

class MailingRemove(QMainWindow, Ui_mwMailingRemove):
    rmd = remove_mailing_database
    
    def __init__(self):
        super(MailingRemove, self).__init__()
        
        self.setupUi(self)
        self.btnSearch.clicked.connect(self.search_name)
        self.btnRemove.clicked.connect(self.btnRemove_clicked)
                
        self.leLastName.returnPressed.connect(self.search_name)
        self.leZipCode.returnPressed.connect(self.search_name)
               
        #hide widgets not needed until later, maybe disable them...
        self.tblResults.hide()
        self.btnRemove.hide()
        self.gbNotes.hide()
    
    def search_name(self):
        try:
            results = self.rmd.search_name(self.leFirstName.text(), self.leLastName.text(), self.leZipCode.text())
            self.show_results(results)
        except BaseException as e:
            QMessageBox.critical(self, 'I got a bad feeling about this', 'Something has gone wrong: \n' + str(e), QMessageBox.Ok)
                
    def show_results(self, results):
        lstHeader = ['', '', 'Database', 'First Name', 'Middle Name', 'Last Name', 'Company', 'Address', 'City', 'State', 'Zip']
        self.tblResults.setHorizontalHeaderLabels(lstHeader)
        if results:
            self.tblResults.setRowCount(len(results))
            for i, row in enumerate(results):
                for j, col in enumerate(row):
                    chkBox = QTableWidgetItem()
                    chkBox.setFlags(Qt.ItemIsUserCheckable | Qt.ItemIsEnabled)
                    chkBox.setCheckState(Qt.Unchecked)       
                                  
                    item = QTableWidgetItem(str(col))
                    if item.text() == 'None':
                        item.setText(None)
                    #add checkbox first
                    self.tblResults.setItem(i, 0, chkBox)
                    #add the items from the database                                               
                    self.tblResults.setItem(i, j+1, item)
                    
            self.tblResults.show()
            self.tblResults.resizeColumnsToContents()
            #self.tblResults.itemChanged.connect(self.item_checked)
            self.tblResults.hideColumn(1)
            
            self.btnRemove.show()
            self.gbNotes.show()
        else:
            QMessageBox.information(self, 'No Results Found', 'Unable to find any results', QMessageBox.Ok)
            self.tblResults.hide()
            self.btnRemove.hide()
            self.gbNotes.hide()
            
    def btnRemove_clicked(self):
        lstRemove = []
        for row in range(0, self.tblResults.rowCount()):
            chk = self.tblResults.item(row, 0)
            if chk.checkState() == 2:
                lstRemove.append([self.tblResults.item(row, 1).text(), self.tblResults.item(row, 2).text()])


        #Get the note...
        if not self.rbtnMailingNote.isChecked() and not self.rbtnPostNote.isChecked():
            QMessageBox.information(self, 'No Note', 'Please choose note type.', QMessageBox.Ok)
        else:
            if self.rbtnMailingNote.isChecked():
                note = self.rbtnMailingNote.text()
            elif self.rbtnPostNote.isChecked():
                note = self.rbtnPostNote.text()            
                       
            self.remove_start(lstRemove, note) 
        
    def remove_start(self, customer_lst, note):
                    
        self.remove = RemoveFromList(customer_lst, note)
        self.remove.finished.connect(self.remove_finished)
        self.remove.error.connect(self.remove_error)
        
        self.spinner = RemoveProgress()
        
        self.remove.start()
        self.setEnabled(False)
        self.spinner.show()
        
    def remove_finished(self):
        self.spinner.hide()
        self.setEnabled(True)
        
        QMessageBox.information(self, 'Complete', 'The selected records have been updated', QMessageBox.Ok)
        
        self.leFirstName.setText(None)
        self.leLastName.setText(None)
        self.leZipCode.setText(None)
        
        self.tblResults.hide()
        self.btnRemove.hide()
        
        self.gbNotes.hide()
    
    def remove_error(self, error):
        QMessageBox.information(self, 'Error', 'The server was unable to complete this action, please try again. \n \n' + 'Details: ' + str(error) + \
                                 '\n \n If you continue to receive this message please contact IT.', QMessageBox.Ok)
        
    
        
class RemoveFromList(QThread):
    remove_finished = pyqtSignal()
    error = pyqtSignal(str)

    def __init__(self, customer_lst, note):
        super(QThread, self).__init__()
        self.customer_lst = customer_lst
        self.note = note
        
    def run(self):
        rmd = remove_mailing_database
        
        for cust in range(len(self.customer_lst)):
            try:
                rmd.remove_from_mailing_list(self.customer_lst[cust][0], self.customer_lst[cust][1])
                rmd.insert_note(self.customer_lst[cust][0], self.customer_lst[cust][1], self.note)
            except BaseException as e:
                self.error.emit(str(e))
                break
        
        self.remove_finished.emit()   
        
class RemoveProgress(QWidget):
    #Shows a .gif while email is being sent.
    def __init__(self):
        super(RemoveProgress, self).__init__()
        
        #Sets the background to invisible.
        self.setAttribute(Qt.WA_TranslucentBackground)
        #Gets rid of frame around window.        
        self.setWindowFlags(Qt.FramelessWindowHint)
        
        #Create a movie object.
        self.movie = QMovie(self)
        
        #In case the gif is missing, display something, maybe.
        self.movieLabel = QLabel("No movie loaded")
        
        #I think there are some alignment issues here with this .gif, needs looked at, could
        #be a better way to do this.
        self.movieLabel.setAlignment(Qt.AlignAbsolute)
        self.movieLabel.setSizePolicy(QSizePolicy.Ignored, QSizePolicy.Ignored)

        #Could be a better way to do this with Qt Designer
        self.mainLayout = QVBoxLayout()
        self.mainLayout.addWidget(self.movieLabel)
        self.setLayout(self.mainLayout)

        self.resize(300, 300)
 
        self.movieLabel.setMovie(self.movie)
        self.movie.setFileName('image/gears.gif')
        
        #Start aligning the .gif on the screen, always needs fudged, there is 
        #probably a better way to do this. 
        pos = mr.pos()
 
        x = (pos.x() - ((self.width()/2) - (mr.width()/2))) 
        y = (pos.y() - ((self.height()/2) - (mr.height()/2)))
         
        self.setGeometry(x,y, 300, 300)
        #End aligning the .fig on the screen.
        
        #Start the .gif.
        self.movie.start()             
        
if __name__ == '__main__':
    myappid = 'Remove User From Mailing List'
    #Windows 7 or x64 only
    ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(myappid) 
        
    app = QApplication(sys.argv)
    app.setStyle('Plastique')
    mr = MailingRemove()
    mr.show()
    
    sys.exit(app.exec_())
