import sys
import os
import xlwt
import webbrowser
from ui import Ui_dashMain
from PyQt5.QtWidgets import QMainWindow, QApplication, QCheckBox, QTableWidgetItem, QFileDialog, QMessageBox, QLabel
from PyQt5.QtCore import QUrl, QThread, pyqtSignal, Qt
from PyQt5 import QtNetwork, QtWebKit, QtPrintSupport
from ui.pbarReport import Ui_pbarReport
from database import data


class Dashboard(QMainWindow, Ui_dashMain):
    db = data
    
    def __init__(self):
        super(Dashboard, self).__init__()
        self.setupUi(self)
        
        #signals and slots
        self.btnViewReport.clicked.connect(self.show_report)
        self.btnBack.clicked.connect(self.go_back)
        self.btnForward.clicked.connect(self.go_forward)
        self.btnViewChart.clicked.connect(self.load_parameters)
        self.btnExport.clicked.connect(self.export_table)
        self.btnCompare.clicked.connect(self.compare_selected)
        self.btnCompareIE.clicked.connect(self.compare_selected)
        self.btnOpenReport.clicked.connect(self.open_rpt_browser)
        
        #check boxes for hiding and showing columns
        self.chkFeaturedProduct.clicked.connect(self.toggle_columns)
        self.chkDropDate.clicked.connect(self.toggle_columns)
        self.chkCutOff.clicked.connect(self.toggle_columns)
        self.chkListVendor.clicked.connect(self.toggle_columns)
        self.chkListSelection.clicked.connect(self.toggle_columns)
        self.chkModelRank.clicked.connect(self.toggle_columns)
        self.chkListCost.clicked.connect(self.toggle_columns)
        
       
        #list types drop down
        cb_types = self.db.get_list_types()
        self.cbListType.addItems(cb_types)
        
        #list sub types drop down.
        cb_stypes = self.db.get_list_subtypes()
        self.cbListSubType.addItems(cb_stypes)
        
        #category drop down
        cb_cat = self.db.get_categories()
        self.cbCategory.addItems(cb_cat)
        
        #vendor drop down
        cb_vend = self.db.get_vendors()
        self.cbVendor.addItems(cb_vend)
        
        #populate year check boxes
        self.radio_button_year()
        #populate quarter check boxes
        self.radio_button_qtr()
        
        #self.cbSearchHistoryTable.currentIndexChanged.connect(self.load_search_history) 
        self.get_search_history()
        self.cbSearchHistoryTable.currentTextChanged.connect(self.load_search_history)
        self.cbSearchHistoryRpt.currentTextChanged.connect(self.load_search_history)
        
    def get_camp_ids(self, source=None, bench=None):
        #if the line edits for source and benchmark are not sent, and the line edits are respectively empty we want to 
        #grab the selection(s) from self.tblReport to use, fill in the corresponding line edits, and return the results
        #to the caller
        if not source:
            source = self.leSourceCodeSubj.text()
        else:
            self.leSourceCodeSubj.setText(source)
        
        if not bench:
            bench = self.leSourceCodeBench.text()
        else:
            self.leSourceCodeBench.setText(bench) 
            
        return source, bench       

    def open_rpt_browser(self, source=None, bench=None):
        #get-set campaign ids being compared
        source, bench = self.get_camp_ids(source, bench)
        
        #Open the report outside the tool in IE so it can be printed or exported properly
        ie = webbrowser.get(webbrowser.iexplore)
        ie.open('http://sqlrptserver/ReportServer_SQLREPORTS/Pages/ReportViewer.aspx?%2fInkPixi+Reports%2fPostcard+Campaign+Dashboard&sourceCodeSubj='+str(source)+'&sourceCodeBench='+str(bench)+'&rs:Command=Render&rc:Parameters=Collapsed', 1600, 1200 )
        
    def show_report(self, source=None, bench=None):
        #get-set campaign ids being compared
        source, bench = self.get_camp_ids(source, bench)
        
        #Open the report inside the QApp
        self.report = self.webView
        #Progress bar thread.
        self.report.loadProgress.connect(self.report_progress)
        self.report.loadFinished.connect(self.report_loaded)
        #load report
        self.report.load((QUrl('http://sqlrptserver/ReportServer_SQLREPORTS/Pages/ReportViewer.aspx?%2fInkPixi+Reports%2fPostcard+Campaign+Dashboard&sourceCodeSubj='+str(source)+'&sourceCodeBench='+str(bench)+'&rs:Command=Render&rc:Parameters=Collapsed&rc:Toolbar=false')))
        #add to history
        self.db.insert_search_history('report', source + ' - ' + bench)
        self.get_search_history('report')
        
    def report_progress(self):
        #Turn on progress bar
        self.showProgress = ReportProgressBar()
        self.showProgress.show()
        
    def report_loaded(self):
        #when report is finished turn off the progress bar.
        self.showProgress.hide()

    def go_back(self):
        self.webView.back()
        
    def go_forward(self):
        self.webView.forward()

    def radio_button_year(self):
        #get list of available years in DB.
        ls_year = self.db.get_campaign_year()
        #create a placeholder to create checkboxes from database.
        self.chkYear = {}
        
        row = 0
        col = 0
        for i in range(len(ls_year)):
            #after three rows down we want to switch columns by added one to the column count and 
            #reset the row count.
            if row == 3:
                col = col +1
                row = 0
            self.chkYear[i] = QCheckBox(ls_year[i])
            self.chkYear[i].setObjectName(ls_year[i])
            #self.vboxYear.addWidget(self.chkYear[i])
            self.grdYear.addWidget(self.chkYear[i], row, col)
            row = row +1
            
    def radio_button_qtr(self):
        #Create a list of available quarters, these are always going to be the same.
        ls_qtr = ['Q1', 'Q2', 'Q3', 'Q4']
        #create check box placeholder
        self.chkQtr = {}
        #add quarter check boxes to the layout
        for i in range(len(ls_qtr)):
            self.chkQtr[i] = QCheckBox(ls_qtr[i])
            self.vboxQtr.addWidget(self.chkQtr[i])    
            
    def load_parameters(self):
        rpt_years = []
        rpt_qtrs = []
        
        #This iterates through the "Year" Group Box and grabs any year that was selected.  If none
        #were selected then it uses all years available.
        if self.gbYear.isChecked():
            widgets = (self.grdYear.itemAt(i).widget() for i in range(self.grdYear.count()))
            for w in widgets:
                if isinstance(w, QCheckBox):
                    if w.isChecked():
                        rpt_years.append(w.text())
        else:
            rpt_years = self.db.get_campaign_year()
        
        #This iterates through the "Quarter" Group Box and grabs any year that was selected.  If none
        #were selected then it uses all 4 quarters.
        if self.gbQtr.isChecked():
            widgets = (self.vboxQtr.itemAt(i).widget() for i in range(self.vboxQtr.count()))
            for w in widgets:
                if isinstance(w, QCheckBox):
                    if w.isChecked():
                        rpt_qtrs.append(w.text())      
        else:
            rpt_qtrs = ['Q1', 'Q2', 'Q3', 'Q4']
            
        strYrs = ','.join(rpt_years)
        strQtr = ','.join(rpt_qtrs)  

        #These next lines grab the values from each of the combo boxes in the app.  If the combo wasn't changed
        #or 'All' was selected then it grabs all the available items for that combo box.
        if self.cbListType.currentText() != '-- List Type --' and self.cbListType.currentText() != 'All':
            lst_type = self.cbListType.currentText()
        else:  
            lst_type = None
            
        if self.cbCategory.currentText() != '-- Category --' and self.cbCategory.currentText() != 'All':
            lst_cat = self.cbCategory.currentText()
        else:
            lst_cat = None
            
        if self.cbListSubType.currentText() != '-- List Sub Types --' and self.cbListSubType.currentText() != 'All':
            lst_sub = self.cbListSubType.currentText()
        else:
            lst_sub = None
            
        if self.cbVendor.currentText() != '-- Vendor --' and self.cbVendor.currentText() != 'All':
            vendor = self.cbVendor.currentText()
        else:
            vendor = None
        
        #in case the group box for years or quarters is checked and no check box is checked.     
        if len(rpt_years) == 0:
            QMessageBox.information(self, 'Make Year Selection', 'Please make a selection for Year or uncheck the box...', QMessageBox.Ok)
        elif len(rpt_qtrs) == 0:
            QMessageBox.information(self, 'Make Quarter Selection', 'Please make a selection for Quarter or uncheck the box...', QMessageBox.Ok)
        else:
            self.load_report(strQtr, strYrs, lst_type, lst_cat, lst_sub, vendor)  
        

        
        searchParams = '[' + strQtr + ']^^^[' + strYrs + ']'
        if lst_type is not None:
            searchParams += '^^^' + lst_type
        else:
            searchParams += '^^^' + 'All'
        if lst_cat is not None:
            searchParams += '^^^' + lst_cat
        else:
            searchParams += '^^^' + 'All'            
        if lst_sub is not None:
            searchParams += '^^^' + lst_sub
        else:
            searchParams += '^^^' + 'All'
        if vendor is not None:
            searchParams += '^^^' + vendor
        else:
            searchParams += '^^^' + 'All'                   

        self.db.insert_search_history('table', searchParams)
        self.get_search_history('table')
         
        
    def load_report(self, qtrs, yrs, lst_type, lst_cat, lst_sub, vendor):
        #Assign the Thread to a variable, and connect the signals and slots.
        self.load = BuildReport(self.tblReport, qtrs, yrs, lst_type, lst_cat, lst_sub, vendor)
        self.load.rpt_finished.connect(self.show_table)
        
        #assign the progress bar thread
        self.progress = ReportProgressBar()
        #start building the report and show the progress bar.
        self.load.start()
        self.progress.show()
        
    def show_table(self, data, data_avg):
        #hide the progress bar
        self.progress.hide()
        
        #set up labels with the roll ups for averages from data_avg.
        self.lblAvgResponse.setText('Avg Response Rate: ' + str(data_avg[0][0]))
        self.lblAvgProdPerCard.setText('Avg Product Sales Per Card: ' + str(data_avg[0][1]))
        self.lblAvgProdOrder.setText('Avg Product Sales Per Order: ' + str(data_avg[0][2]))
        self.lblAvgGrossCard.setText('Avg Gross Sales Per Card: ' + str(data_avg[0][3]))
        self.lblAvgGrossOrder.setText('Avg Gross Sales Per Order: ' + str(data_avg[0][4]))
        self.lblGrossMargin.setText('Total Gross Margin: ' + str(data_avg[0][5]))
        
    def export_table(self):
        #choose path with the dialog
        path = QFileDialog.getSaveFileName(self, 'Choose File', '', ".xls(*.xls)")
        filename = os.path.abspath(path[0])
        #create instance of an excel workbook.
        wbk = xlwt.Workbook() 
        #create first sheet for roll ups.
        sheet_rollup = wbk.add_sheet('Rollup', cell_overwrite_ok=True)
        #grab the roll ups from the group box and add them to a list.
        lst_rollup = []
        widgets = (self.grdRollup.itemAt(i).widget() for i in range(self.grdRollup.count()))
        for w in widgets:
            if isinstance(w, QLabel):
                lst_rollup.append(w.text())
        #create another list to split and parse out the first list.
        lbl_txt = []
        for i in range(len(lst_rollup)):
            lbl_txt.append([lst_rollup[i].split(':')])
        
        #write the roll up labels to the first sheet in the workbook.
        for i in range(len(lbl_txt)):
            sheet_rollup.write(i, 0, lbl_txt[i][0][0])
            sheet_rollup.write(i, 1, lbl_txt[i][0][1])
        
        #create new sheet for table.
        sheet = wbk.add_sheet("Table Export", cell_overwrite_ok=True)
        #create a list of the headers from the table to write to the sheet.
        lst_headers = []
        for h in range(self.tblReport.columnCount()):
            lst_headers.append(self.tblReport.horizontalHeaderItem(h).text())
        
        #write the headers to the worksheet.
        for i in range(len(lst_headers)):
            sheet.write(0, i, lst_headers[i])
        
        self.pop_sheet(sheet)
        wbk.save(filename)
        
    def pop_sheet(self, sheet):
        for currentColumn in range(self.tblReport.columnCount()):
            for currentRow in range(self.tblReport.rowCount()):
                try:
                    txt = str(self.tblReport.item(currentRow, currentColumn).text())
                    sheet.write(currentRow +1, currentColumn, txt)
                except AttributeError:
                    pass
                
    def compare_selected(self):
        #grab the objectName of the button that made the call.
        view = self.sender().objectName()

        rows = []
        for idx in self.tblReport.selectionModel().selectedRows():
            rows.append(idx.row())
        ids = []
        for row in rows:
            ids.append(self.tblReport.item(row, 0).text())
        
        if len(ids) == 2:
            if view == self.btnCompare.objectName():
                self.tabReport.setCurrentIndex(0)
                self.show_report(ids[0], ids[1])
            elif view == self.btnCompareIE.objectName():
                self.open_rpt_browser(ids[0], ids[1])
        elif len(ids) == 1:
            if view == self.btnCompare.objectName(): 
                self.tabReport.setCurrentIndex(0)
                self.show_report(ids[0], None)
            elif view == self.btnCompareIE.objectName():
                self.open_rpt_browser(ids[0], None)
        else:
            QMessageBox.information(self, 'Choose Properly', 'Please choose 1 or 2 source codes from the table.', QMessageBox.Ok)
            
        if ids:
            self.db.insert_search_history('report', ' - '.join(ids))
            self.get_search_history('report')

    def toggle_columns(self, checked):
        #dictionary of columns and corresponding indexes
        dict_idx = {'Featured Product': 2, 'Drop Date': 3, 'Cut Off Date': 4, 'List Vendor': 5, 'List Selection': 6, 'Model Tier Rank': 7, 'List Cost': 8}
        #get the index from the dictionary for the sending check box.
        col = dict_idx[self.sender().text()]
        #use the index, and whether or not box is checked (signal from checked) to hide or unhide the column 
        self.tblReport.setColumnHidden(col, checked)

    def get_search_history(self, tab=None):
        if tab == 'table':
            self.cbSearchHistoryTable.clear()
            #table search history combo box
            self.cbSearchHistoryTable.addItem('-- Search History --')
            self.cbSearchHistoryTable.addItems(self.db.get_search_history('table'))
        elif tab == 'report':
            self.cbSearchHistoryRpt.clear()
            self.cbSearchHistoryRpt.addItem('-- Search History --')
            self.cbSearchHistoryRpt.addItems(self.db.get_search_history('report'))
        else:
            self.cbSearchHistoryRpt.clear()
            self.cbSearchHistoryRpt.addItem('-- Search History --')
            self.cbSearchHistoryRpt.addItems(self.db.get_search_history('report'))
            
            self.cbSearchHistoryTable.clear()
            self.cbSearchHistoryTable.addItem('-- Search History --')
            self.cbSearchHistoryTable.addItems(self.db.get_search_history('table'))            
            
    def load_search_history(self, txt_search):
        params = txt_search.split(' - ')
        if txt_search != '' and txt_search != '-- Search History --':
            if len(params) == 7:
                qtrs = params[1].replace('[', '').replace(']', '')
                yrs = params[2].replace('[', '').replace(']', '')
                 
                if params[3] != 'All':lst_type = params[3]
                else: lst_type = None
                 
                if params[4] != 'All': lst_cat = params[4]
                else: lst_cat = None
                 
                if params[5] != 'All': lst_sub = params[5]
                else: lst_sub = None
                 
                if params[6] != 'All': vendor = params[6]
                else: vendor = None
                 
                self.load_report(qtrs, yrs, lst_type, lst_cat, lst_sub, vendor)
                self.toggle_search_widgets(qtrs, yrs, lst_type, lst_cat, lst_sub, vendor)
            else:
                self.leSourceCodeSubj.setText(params[0])
                self.leSourceCodeBench.setText(params[1])
                self.show_report(params[1], params[2])
            
    def toggle_search_widgets(self, qtrs, yrs, lst_type, lst_cat, lst_sub, vendor):
        #set the group box for quarters and the check boxes inside if needed.
        if len(qtrs) == 11:
            self.gbQtr.setChecked(False)
        else:
            self.gbQtr.setChecked(True)
            chkBoxes = (self.vboxQtr.itemAt(i).widget() for i in range(self.vboxQtr.count()))
            for cbox in chkBoxes:
                if isinstance(cbox, QCheckBox):
                    if cbox.text() in qtrs:
                        cbox.setChecked(True)
                    else: cbox.setChecked(False)
                        
        #same as above, grab the yrs that need to be checked.                        
        if len(yrs) == 24:
            self.gbYear.setChecked(False)
        else:
            self.gbYear.setChecked(True)
            yrBoxes = (self.grdYear.itemAt(i).widget() for i in range(self.grdYear.count()))
            for yrBox in yrBoxes:
                if isinstance(yrBox, QCheckBox):
                    if yrBox.text() in yrs:
                        yrBox.setChecked(True)
                    else: yrBox.setChecked(False)
        
        if lst_type != None:
            self.cbListType.setCurrentText(lst_type)
        else:
            self.cbListType.setCurrentText('All')
            
        if lst_cat != None:
            self.cbCategory.setCurrentText(lst_cat)
        else:
            self.cbCategory.setCurrentText('All')
        
        if lst_sub != None:
            self.cbListSubType.setCurrentText(lst_sub)
        else:
            self.cbListSubType.setCurrentText('All')
        
        if vendor != None:
            self.cbVendor.setCurrentText(vendor)
        else:
            self.cbVendor.setCurrentText('All')
        
class BuildReport(QThread):
    rpt_finished = pyqtSignal(object, object)
    db = data
    def __init__(self, tblReport, qtrs, yrs, lst_type, lst_cat, lst_sub, vendor):
        super(QThread, self).__init__()
        self.tblReport, self.qtrs, self.yrs, self.lst_type, self.lst_cat, self.lst_sub, self.vendor = tblReport, qtrs, yrs, lst_type, lst_cat, lst_sub, vendor
        
    def run(self):
        data, data_avg = self.db.get_report(self.qtrs, self.yrs, self.lst_type, self.lst_cat, self.lst_sub, self.vendor)

        if data:
            self.tblReport.setRowCount(len(data))
            for i, row in enumerate(data):
                for j, col in enumerate(row):
                    item = QTableWidgetItem(str(col))
                    if item.text() == "None":
                        item.setText("")
                    self.tblReport.setItem(i, j, item)
        else:
            self.tblReport.setRowCount(1)
            item = QTableWidgetItem()
            item.setText("No Results")
            self.tblReport.setItem(0, 0, item)        
        
        self.tblReport.resizeColumnsToContents()
        self.tblReport.setSortingEnabled(True)       
        
        self.rpt_finished.emit(self.tblReport, data_avg)

class ReportProgressBar(QMainWindow, Ui_pbarReport):
    canceled = pyqtSignal()
    
    def __init__(self):
        super(ReportProgressBar, self).__init__()
        self.setupUi(self)        
        self.btnCancel.clicked.connect(self.cancel)
        self.pbarLoading.setRange(0,0)
        self.setWindowFlags(Qt.FramelessWindowHint | Qt.WindowStaysOnTopHint)

        
    def cancel(self):
        self.close()
        self.canceled.emit()

               
if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setStyle('plastique')
    
    db = Dashboard()
    db.show()
    
    sys.exit(app.exec_())        

