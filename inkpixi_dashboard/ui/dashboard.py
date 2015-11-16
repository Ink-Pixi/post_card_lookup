# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'dashboard.ui'
#
# Created by: PyQt5 UI code generator 5.4.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_dashMain(object):
    def setupUi(self, dashMain):
        dashMain.setObjectName("dashMain")
        dashMain.setWindowModality(QtCore.Qt.NonModal)
        dashMain.resize(1600, 900)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/images/images/postcard.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        dashMain.setWindowIcon(icon)
        dashMain.setStyleSheet("QToolTip\n"
"{\n"
"     border: 1px solid black;\n"
"     background-color: #ffa02f;\n"
"     padding: 1px;\n"
"     border-radius: 3px;\n"
"     opacity: 25;\n"
"}\n"
"\n"
"QWidget\n"
"{\n"
"    color: #b1b1b1;\n"
"    background-color: #323232;\n"
"    border: none;\n"
"    outline: none;\n"
"}\n"
"\n"
"QWidget:item:hover\n"
"{\n"
"    background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #ffa02f, stop: 1 #ca0619);\n"
"    color: #000000;\n"
"}\n"
"\n"
"QWidget:item:selected\n"
"{\n"
"    background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #ffa02f, stop: 1 #d7801a);\n"
"}\n"
"\n"
"QMenuBar::item\n"
"{\n"
"    background: transparent;\n"
"}\n"
"\n"
"QMenuBar::item:selected\n"
"{\n"
"    background: transparent;\n"
"    border: 1px solid #ffaa00;\n"
"}\n"
"\n"
"QMenuBar::item:pressed\n"
"{\n"
"    background: #444;\n"
"    border: 1px solid #000;\n"
"    background-color: QLinearGradient(\n"
"        x1:0, y1:0,\n"
"        x2:0, y2:1,\n"
"        stop:1 #212121,\n"
"        stop:0.4 #343434/*,\n"
"        stop:0.2 #343434,\n"
"        stop:0.1 #ffaa00*/\n"
"    );\n"
"    margin-bottom:-1px;\n"
"    padding-bottom:1px;\n"
"}\n"
"\n"
"QMenu\n"
"{\n"
"    border: 1px solid #000;\n"
"}\n"
"\n"
"QMenu::item\n"
"{\n"
"    padding: 2px 20px 2px 20px;\n"
"}\n"
"\n"
"QMenu::item:selected\n"
"{\n"
"    color: #000000;\n"
"}\n"
"\n"
"QWidget:disabled\n"
"{\n"
"    color: #404040;\n"
"    background-color: #323232;\n"
"}\n"
"\n"
"QAbstractItemView\n"
"{\n"
"    background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #4d4d4d, stop: 0.1 #646464, stop: 1 #5d5d5d);\n"
"}\n"
"\n"
"QWidget:focus\n"
"{\n"
"    /*border: 2px solid QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #ffa02f, stop: 1 #d7801a);*/\n"
"}\n"
"\n"
"QLineEdit\n"
"{\n"
"    background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #4d4d4d, stop: 0 #646464, stop: 1 #5d5d5d);\n"
"    padding: 1px;\n"
"    border-style: solid;\n"
"    border: 1px solid #1e1e1e;\n"
"    border-radius: 5;\n"
"}\n"
"\n"
"QPushButton\n"
"{\n"
"    color: #d7801a;\n"
"    background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #565656, stop: 0.1 #525252, stop: 0.5 #4e4e4e, stop: 0.9 #4a4a4a, stop: 1 #464646);\n"
"    border-width: 1px;\n"
"    border-color: #1e1e1e;\n"
"    border-style: solid;\n"
"    border-radius: 6;\n"
"    padding: 3px;\n"
"    font-size: 12px;\n"
"    padding-left: 5px;\n"
"    padding-right: 5px;\n"
"}\n"
"\n"
"QPushButton:pressed\n"
"{\n"
"    background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #2d2d2d, stop: 0.1 #2b2b2b, stop: 0.5 #292929, stop: 0.9 #282828, stop: 1 #252525);\n"
"}\n"
"\n"
"QListView\n"
"{\n"
"    selection-background-color: #ffaa00;\n"
"    background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #565656, stop: 0.1 #525252, stop: 0.5 #4e4e4e, stop: 0.9 #4a4a4a, stop: 1 #464646);\n"
"    border-style: solid;\n"
"    border: 1px solid #1e1e1e;\n"
"    border-radius: 5;\n"
"}\n"
"\n"
"QComboBox\n"
"{\n"
"    selection-background-color: #ffaa00;\n"
"    background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #565656, stop: 0.1 #525252, stop: 0.5 #4e4e4e, stop: 0.9 #4a4a4a, stop: 1 #464646);\n"
"    border-style: solid;\n"
"    border: 1px solid #1e1e1e;\n"
"    border-radius: 5;\n"
"}\n"
"\n"
"QComboBox:hover,QPushButton:hover\n"
"{\n"
"    border: 2px solid QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #ffa02f, stop: 1 #d7801a);\n"
"}\n"
"\n"
"\n"
"QComboBox:on\n"
"{\n"
"    padding-top: 3px;\n"
"    padding-left: 4px;\n"
"    background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #2d2d2d, stop: 0.1 #2b2b2b, stop: 0.5 #292929, stop: 0.9 #282828, stop: 1 #252525);\n"
"    selection-background-color: #ffaa00;\n"
"}\n"
"\n"
"QComboBox QAbstractItemView\n"
"{\n"
"    border: 2px solid darkgray;\n"
"    selection-background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #ffa02f, stop: 1 #d7801a);\n"
"}\n"
"\n"
"QComboBox::drop-down\n"
"{\n"
"     subcontrol-origin: padding;\n"
"     subcontrol-position: top right;\n"
"     width: 15px;\n"
"\n"
"     border-left-width: 0px;\n"
"     border-left-color: darkgray;\n"
"     border-left-style: solid; /* just a single line */\n"
"     border-top-right-radius: 3px; /* same radius as the QComboBox */\n"
"     border-bottom-right-radius: 3px;\n"
" }\n"
"\n"
"QComboBox::down-arrow\n"
"{\n"
"     image: url(images/down_arrow.png);\n"
"}\n"
"\n"
"QGroupBox:focus\n"
"{\n"
"    border: 2px solid QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #ffa02f, stop: 1 #d7801a);\n"
"}\n"
"\n"
"QGroupBox {\n"
"/*    background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #ffa02f, stop: 1 #d7801a);*/\n"
"    border: 2px solid gray;\n"
"    border-radius: 5px;\n"
"    margin-top: 1ex; /* leave space at the top for the title */\n"
"    font-size: 12px;\n"
"    font-weight: bold;        \n"
"    \n"
"}\n"
"\n"
"QGroupBox::title {\n"
"    subcontrol-origin: margin;\n"
"    subcontrol-position: top center; /* position at the top center */\n"
"    padding: 0 3px;\n"
"}\n"
"\n"
"QTextEdit:focus\n"
"{\n"
"    border: 2px solid QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #ffa02f, stop: 1 #d7801a);\n"
"}\n"
"\n"
"QScrollBar:horizontal {\n"
"     border: 1px solid #222222;\n"
"     background: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0.0 #121212, stop: 0.2 #282828, stop: 1 #484848);\n"
"     height: 7px;\n"
"     margin: 0px 16px 0 16px;\n"
"}\n"
"\n"
"QScrollBar::handle:horizontal\n"
"{\n"
"      background: QLinearGradient( x1: 0, y1: 0, x2: 1, y2: 0, stop: 0 #ffa02f, stop: 0.5 #d7801a, stop: 1 #ffa02f);\n"
"      min-height: 20px;\n"
"      border-radius: 2px;\n"
"}\n"
"\n"
"QScrollBar::add-line:horizontal {\n"
"      border: 1px solid #1b1b19;\n"
"      border-radius: 2px;\n"
"      background: QLinearGradient( x1: 0, y1: 0, x2: 1, y2: 0, stop: 0 #ffa02f, stop: 1 #d7801a);\n"
"      width: 14px;\n"
"      subcontrol-position: right;\n"
"      subcontrol-origin: margin;\n"
"}\n"
"\n"
"QScrollBar::sub-line:horizontal {\n"
"      border: 1px solid #1b1b19;\n"
"      border-radius: 2px;\n"
"      background: QLinearGradient( x1: 0, y1: 0, x2: 1, y2: 0, stop: 0 #ffa02f, stop: 1 #d7801a);\n"
"      width: 14px;\n"
"     subcontrol-position: left;\n"
"     subcontrol-origin: margin;\n"
"}\n"
"\n"
"QScrollBar::right-arrow:horizontal, QScrollBar::left-arrow:horizontal\n"
"{\n"
"      border: 1px solid black;\n"
"      width: 1px;\n"
"      height: 1px;\n"
"      background: white;\n"
"}\n"
"\n"
"QScrollBar::add-page:horizontal, QScrollBar::sub-page:horizontal\n"
"{\n"
"      background: none;\n"
"}\n"
"\n"
"QScrollBar:vertical\n"
"{\n"
"      background: QLinearGradient( x1: 0, y1: 0, x2: 1, y2: 0, stop: 0.0 #121212, stop: 0.2 #282828, stop: 1 #484848);\n"
"      width: 7px;\n"
"      margin: 16px 0 16px 0;\n"
"      border: 1px solid #222222;\n"
"}\n"
"\n"
"QScrollBar::handle:vertical\n"
"{\n"
"      background: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #ffa02f, stop: 0.5 #d7801a, stop: 1 #ffa02f);\n"
"      min-height: 20px;\n"
"      border-radius: 2px;\n"
"}\n"
"\n"
"QScrollBar::add-line:vertical\n"
"{\n"
"      border: 1px solid #1b1b19;\n"
"      border-radius: 2px;\n"
"      background: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #ffa02f, stop: 1 #d7801a);\n"
"      height: 14px;\n"
"      subcontrol-position: bottom;\n"
"      subcontrol-origin: margin;\n"
"}\n"
"\n"
"QScrollBar::sub-line:vertical\n"
"{\n"
"      border: 1px solid #1b1b19;\n"
"      border-radius: 2px;\n"
"      background: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #d7801a, stop: 1 #ffa02f);\n"
"      height: 14px;\n"
"      subcontrol-position: top;\n"
"      subcontrol-origin: margin;\n"
"}\n"
"\n"
"QScrollBar::up-arrow:vertical, QScrollBar::down-arrow:vertical\n"
"{\n"
"      border: 1px solid black;\n"
"      width: 1px;\n"
"      height: 1px;\n"
"      background: white;\n"
"}\n"
"\n"
"\n"
"QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical\n"
"{\n"
"      background: none;\n"
"}\n"
"\n"
"QTextEdit\n"
"{\n"
"    background-color: #242424;\n"
"}\n"
"\n"
"QPlainTextEdit\n"
"{\n"
"    background-color: #242424;\n"
"}\n"
"\n"
"QHeaderView::section\n"
"{\n"
"    background-color: QLinearGradient(x1:0, y1:0, x2:0, y2:1, stop:0 #616161, stop: 0.5 #505050, stop: 0.6 #434343, stop:1 #656565);\n"
"    color: white;\n"
"    padding-left: 4px;\n"
"    border: 1px solid #6c6c6c;\n"
"}\n"
"\n"
"QCheckBox:disabled\n"
"{\n"
"color: #414141;\n"
"}\n"
"\n"
"QDockWidget::title\n"
"{\n"
"    text-align: center;\n"
"    spacing: 3px; /* spacing between items in the tool bar */\n"
"    background-color: QLinearGradient(x1:0, y1:0, x2:0, y2:1, stop:0 #323232, stop: 0.5 #242424, stop:1 #323232);\n"
"}\n"
"\n"
"QDockWidget::close-button, QDockWidget::float-button\n"
"{\n"
"    text-align: center;\n"
"    spacing: 1px; /* spacing between items in the tool bar */\n"
"    background-color: QLinearGradient(x1:0, y1:0, x2:0, y2:1, stop:0 #323232, stop: 0.5 #242424, stop:1 #323232);\n"
"}\n"
"\n"
"QDockWidget::close-button:hover, QDockWidget::float-button:hover\n"
"{\n"
"    background: #242424;\n"
"}\n"
"\n"
"QDockWidget::close-button:pressed, QDockWidget::float-button:pressed\n"
"{\n"
"    padding: 1px -1px -1px 1px;\n"
"}\n"
"\n"
"QMainWindow::separator\n"
"{\n"
"    background-color: QLinearGradient(x1:0, y1:0, x2:0, y2:1, stop:0 #161616, stop: 0.5 #151515, stop: 0.6 #212121, stop:1 #343434);\n"
"    color: white;\n"
"    padding-left: 4px;\n"
"    border: 1px solid #4c4c4c;\n"
"    spacing: 3px; /* spacing between items in the tool bar */\n"
"}\n"
"\n"
"QMainWindow::separator:hover\n"
"{\n"
"\n"
"    background-color: QLinearGradient(x1:0, y1:0, x2:0, y2:1, stop:0 #d7801a, stop:0.5 #b56c17 stop:1 #ffa02f);\n"
"    color: white;\n"
"    padding-left: 4px;\n"
"    border: 1px solid #6c6c6c;\n"
"    spacing: 3px; /* spacing between items in the tool bar */\n"
"}\n"
"\n"
"QToolBar::handle\n"
"{\n"
"     spacing: 3px; /* spacing between items in the tool bar */\n"
"     background: url(images/handle.png);\n"
"}\n"
"\n"
"QMenu::separator\n"
"{\n"
"    height: 2px;\n"
"    background-color: QLinearGradient(x1:0, y1:0, x2:0, y2:1, stop:0 #161616, stop: 0.5 #151515, stop: 0.6 #212121, stop:1 #343434);\n"
"    color: white;\n"
"    padding-left: 4px;\n"
"    margin-left: 10px;\n"
"    margin-right: 5px;\n"
"}\n"
"\n"
"QProgressBar\n"
"{\n"
"    border: 2px solid grey;\n"
"    border-radius: 5px;\n"
"    text-align: center;\n"
"}\n"
"\n"
"QProgressBar::chunk\n"
"{\n"
"    background-color: #d7801a;\n"
"    width: 2.15px;\n"
"    margin: 0.5px;\n"
"}\n"
"\n"
"\n"
"QTabBar::tab {\n"
"    color: #b1b1b1;\n"
"    border: 1px solid #444;\n"
"    border-bottom-style: none;\n"
"    background-color: #323232;\n"
"    padding-left: 10px;\n"
"    padding-right: 10px;\n"
"    padding-top: 3px;\n"
"    padding-bottom: 2px;\n"
"    margin-right: -1px;\n"
"}\n"
"\n"
"QTabWidget::pane {\n"
"    color: #b1b1b1;\n"
"    background-color: #323232;\n"
"    border: 1px solid #444;\n"
"    top: 1px;\n"
"}\n"
"\n"
"QTabBar::tab:last\n"
"{\n"
"    margin-right: 0; /* the last selected tab has nothing to overlap with on the right */\n"
"    border-top-right-radius: 3px;\n"
"}\n"
"\n"
"QTabBar::tab:first:!selected\n"
"{\n"
"    margin-left: 0px; /* the last selected tab has nothing to overlap with on the right */\n"
"    border-top-left-radius: 3px;\n"
"}\n"
"\n"
"QTabBar::tab:!selected\n"
"{\n"
"    color: #b1b1b1;\n"
"    border-bottom-style: solid;\n"
"    margin-top: 3px;\n"
"    background-color: QLinearGradient(x1:0, y1:0, x2:0, y2:1, stop:1 #212121, stop:.4 #343434);\n"
"}\n"
"\n"
"QTabBar::tab:selected\n"
"{\n"
"    border-top-left-radius: 3px;\n"
"    border-top-right-radius: 3px;\n"
"    margin-bottom: 0px;\n"
"}\n"
"\n"
"QTabBar::tab:!selected:hover\n"
"{\n"
"    /*border-top: 2px solid #ffaa00;\n"
"    padding-bottom: 3px;*/\n"
"    border-top-left-radius: 3px;\n"
"    border-top-right-radius: 3px;\n"
"    background-color: QLinearGradient(x1:0, y1:0, x2:0, y2:1, stop:1 #212121, stop:0.4 #343434, stop:0.2 #343434, stop:0.1 #ffaa00);\n"
"}\n"
"\n"
"QRadioButton::indicator:checked, QRadioButton::indicator:unchecked{\n"
"    color: #b1b1b1;\n"
"    background-color: #323232;\n"
"    border: 1px solid #b1b1b1;\n"
"    border-radius: 6px;\n"
"}\n"
"\n"
"QRadioButton::indicator:checked\n"
"{\n"
"    background-color: qradialgradient(\n"
"        cx: 0.5, cy: 0.5,\n"
"        fx: 0.5, fy: 0.5,\n"
"        radius: 1.0,\n"
"        stop: 0.25 #ffaa00,\n"
"        stop: 0.3 #323232\n"
"    );\n"
"}\n"
"\n"
"QCheckBox::indicator{\n"
"    color: #b1b1b1;\n"
"    background-color: #323232;\n"
"    border: 1px solid #b1b1b1;\n"
"    width: 9px;\n"
"    height: 9px;\n"
"}\n"
"\n"
"QRadioButton::indicator\n"
"{\n"
"    border-radius: 6px;\n"
"}\n"
"\n"
"QRadioButton::indicator:hover, QCheckBox::indicator:hover\n"
"{\n"
"    border: 1px solid #ffaa00;\n"
"}\n"
"\n"
"QCheckBox::indicator:checked\n"
"{\n"
"    image: url(images/checkbox.png);\n"
"}\n"
"\n"
"QCheckBox::indicator:disabled, QRadioButton::indicator:disabled\n"
"{\n"
"    border: 1px solid #444;\n"
"}            \n"
"\n"
"QToolButton\n"
"{\n"
"    font-size: 14px;\n"
"    font-weight: bold;\n"
"}\n"
"")
        self.centralwidget = QtWidgets.QWidget(dashMain)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.lblTitle = QtWidgets.QLabel(self.centralwidget)
        self.lblTitle.setText("")
        self.lblTitle.setPixmap(QtGui.QPixmap(":/images/images/pixi_logo_new.png"))
        self.lblTitle.setObjectName("lblTitle")
        self.horizontalLayout_3.addWidget(self.lblTitle)
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("color: rgb(146, 199, 62);")
        self.label_2.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_3.addWidget(self.label_2)
        spacerItem = QtWidgets.QSpacerItem(1433, 13, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem)
        self.verticalLayout_3.addLayout(self.horizontalLayout_3)
        self.tabReport = QtWidgets.QTabWidget(self.centralwidget)
        self.tabReport.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.tabReport.setStyleSheet("QTabBar::tab {\n"
"    color: #b1b1b1;\n"
"    border: 1px solid #444;\n"
"    border-bottom-style: none;\n"
"    background-color: #323232;\n"
"    padding-left: 10px;\n"
"    padding-right: 10px;\n"
"    padding-top: 3px;\n"
"    padding-bottom: 2px;\n"
"    margin-right: -1px;\n"
"}\n"
"\n"
"QTabWidget::pane {\n"
"    border: 1px solid #444;\n"
"    top: 1px;\n"
"}\n"
"\n"
"QTabBar::tab:last\n"
"{\n"
"    margin-right: 0; /* the last selected tab has nothing to overlap with on the right */\n"
"    border-top-right-radius: 3px;\n"
"}\n"
"\n"
"QTabBar::tab:first:!selected\n"
"{\n"
"    margin-left: 0px; /* the last selected tab has nothing to overlap with on the right */\n"
"    border-top-left-radius: 3px;\n"
"}\n"
"\n"
"QTabBar::tab:!selected\n"
"{\n"
"    color: #b1b1b1;\n"
"    border-bottom-style: solid;\n"
"    margin-top: 3px;\n"
"    background-color: QLinearGradient(x1:0, y1:0, x2:0, y2:1, stop:1 #212121, stop:.4 #343434);\n"
"}\n"
"\n"
"QTabBar::tab:selected\n"
"{\n"
"    border-top-left-radius: 3px;\n"
"    border-top-right-radius: 3px;\n"
"    margin-bottom: 0px;\n"
"}\n"
"\n"
"QTabBar::tab:!selected:hover\n"
"{\n"
"    /*border-top: 2px solid #ffaa00;\n"
"    padding-bottom: 3px;*/\n"
"    border-top-left-radius: 3px;\n"
"    border-top-right-radius: 3px;\n"
"    background-color: QLinearGradient(x1:0, y1:0, x2:0, y2:1, stop:1 #212121, stop:0.4 #343434, stop:0.2 #343434, stop:0.1 #ffaa00);\n"
"}\n"
"")
        self.tabReport.setObjectName("tabReport")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.tab)
        self.gridLayout_2.setObjectName("gridLayout_2")
        spacerItem1 = QtWidgets.QSpacerItem(1200, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem1, 0, 3, 1, 2)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.leSourceCodeSubj = QtWidgets.QLineEdit(self.tab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.leSourceCodeSubj.sizePolicy().hasHeightForWidth())
        self.leSourceCodeSubj.setSizePolicy(sizePolicy)
        self.leSourceCodeSubj.setMinimumSize(QtCore.QSize(150, 0))
        self.leSourceCodeSubj.setObjectName("leSourceCodeSubj")
        self.horizontalLayout_2.addWidget(self.leSourceCodeSubj)
        self.leSourceCodeBench = QtWidgets.QLineEdit(self.tab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.leSourceCodeBench.sizePolicy().hasHeightForWidth())
        self.leSourceCodeBench.setSizePolicy(sizePolicy)
        self.leSourceCodeBench.setMinimumSize(QtCore.QSize(150, 0))
        self.leSourceCodeBench.setObjectName("leSourceCodeBench")
        self.horizontalLayout_2.addWidget(self.leSourceCodeBench)
        self.cbSearchHistoryRpt = QtWidgets.QComboBox(self.tab)
        self.cbSearchHistoryRpt.setMinimumSize(QtCore.QSize(250, 0))
        self.cbSearchHistoryRpt.setObjectName("cbSearchHistoryRpt")
        self.cbSearchHistoryRpt.addItem("")
        self.horizontalLayout_2.addWidget(self.cbSearchHistoryRpt)
        self.btnViewReport = QtWidgets.QPushButton(self.tab)
        self.btnViewReport.setObjectName("btnViewReport")
        self.horizontalLayout_2.addWidget(self.btnViewReport)
        self.btnOpenReport = QtWidgets.QPushButton(self.tab)
        self.btnOpenReport.setObjectName("btnOpenReport")
        self.horizontalLayout_2.addWidget(self.btnOpenReport)
        self.gridLayout_2.addLayout(self.horizontalLayout_2, 0, 1, 1, 1)
        self.btnForward = QtWidgets.QPushButton(self.tab)
        self.btnForward.setObjectName("btnForward")
        self.gridLayout_2.addWidget(self.btnForward, 0, 6, 1, 1)
        self.btnBack = QtWidgets.QPushButton(self.tab)
        self.btnBack.setObjectName("btnBack")
        self.gridLayout_2.addWidget(self.btnBack, 0, 5, 1, 1)
        self.webView = QtWebKitWidgets.QWebView(self.tab)
        self.webView.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.webView.setUrl(QtCore.QUrl("about:blank"))
        self.webView.setObjectName("webView")
        self.gridLayout_2.addWidget(self.webView, 2, 0, 1, 7)
        self.tabReport.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.gridLayout = QtWidgets.QGridLayout(self.tab_2)
        self.gridLayout.setObjectName("gridLayout")
        self.tblReport = QtWidgets.QTableWidget(self.tab_2)
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(False)
        font.setWeight(50)
        self.tblReport.setFont(font)
        self.tblReport.setStyleSheet("color: rgb(0, 0, 0);\n"
"background-color: rgb(234, 234, 234);")
        self.tblReport.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tblReport.setAlternatingRowColors(True)
        self.tblReport.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.tblReport.setObjectName("tblReport")
        self.tblReport.setColumnCount(17)
        self.tblReport.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tblReport.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tblReport.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tblReport.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tblReport.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tblReport.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tblReport.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tblReport.setHorizontalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.tblReport.setHorizontalHeaderItem(7, item)
        item = QtWidgets.QTableWidgetItem()
        self.tblReport.setHorizontalHeaderItem(8, item)
        item = QtWidgets.QTableWidgetItem()
        self.tblReport.setHorizontalHeaderItem(9, item)
        item = QtWidgets.QTableWidgetItem()
        self.tblReport.setHorizontalHeaderItem(10, item)
        item = QtWidgets.QTableWidgetItem()
        self.tblReport.setHorizontalHeaderItem(11, item)
        item = QtWidgets.QTableWidgetItem()
        self.tblReport.setHorizontalHeaderItem(12, item)
        item = QtWidgets.QTableWidgetItem()
        self.tblReport.setHorizontalHeaderItem(13, item)
        item = QtWidgets.QTableWidgetItem()
        self.tblReport.setHorizontalHeaderItem(14, item)
        item = QtWidgets.QTableWidgetItem()
        self.tblReport.setHorizontalHeaderItem(15, item)
        item = QtWidgets.QTableWidgetItem()
        self.tblReport.setHorizontalHeaderItem(16, item)
        self.gridLayout.addWidget(self.tblReport, 2, 0, 1, 2)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.gbQtr = QtWidgets.QGroupBox(self.tab_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.gbQtr.sizePolicy().hasHeightForWidth())
        self.gbQtr.setSizePolicy(sizePolicy)
        self.gbQtr.setMinimumSize(QtCore.QSize(90, 110))
        self.gbQtr.setCheckable(True)
        self.gbQtr.setChecked(False)
        self.gbQtr.setObjectName("gbQtr")
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(self.gbQtr)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(10, 20, 71, 81))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.vboxQtr = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.vboxQtr.setContentsMargins(0, 0, 0, 0)
        self.vboxQtr.setObjectName("vboxQtr")
        self.horizontalLayout.addWidget(self.gbQtr)
        self.gbYear = QtWidgets.QGroupBox(self.tab_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.gbYear.sizePolicy().hasHeightForWidth())
        self.gbYear.setSizePolicy(sizePolicy)
        self.gbYear.setMinimumSize(QtCore.QSize(180, 110))
        self.gbYear.setCheckable(True)
        self.gbYear.setChecked(False)
        self.gbYear.setObjectName("gbYear")
        self.gridLayoutWidget_3 = QtWidgets.QWidget(self.gbYear)
        self.gridLayoutWidget_3.setGeometry(QtCore.QRect(9, 19, 161, 81))
        self.gridLayoutWidget_3.setObjectName("gridLayoutWidget_3")
        self.grdYear = QtWidgets.QGridLayout(self.gridLayoutWidget_3)
        self.grdYear.setContentsMargins(0, 0, 0, 0)
        self.grdYear.setObjectName("grdYear")
        self.horizontalLayout.addWidget(self.gbYear)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.cbListType = QtWidgets.QComboBox(self.tab_2)
        self.cbListType.setMinimumSize(QtCore.QSize(200, 0))
        self.cbListType.setObjectName("cbListType")
        self.cbListType.addItem("")
        self.cbListType.addItem("")
        self.verticalLayout.addWidget(self.cbListType)
        self.cbCategory = QtWidgets.QComboBox(self.tab_2)
        self.cbCategory.setMinimumSize(QtCore.QSize(200, 0))
        self.cbCategory.setObjectName("cbCategory")
        self.cbCategory.addItem("")
        self.cbCategory.addItem("")
        self.verticalLayout.addWidget(self.cbCategory)
        self.cbListSubType = QtWidgets.QComboBox(self.tab_2)
        self.cbListSubType.setMinimumSize(QtCore.QSize(200, 0))
        self.cbListSubType.setObjectName("cbListSubType")
        self.cbListSubType.addItem("")
        self.cbListSubType.addItem("")
        self.verticalLayout.addWidget(self.cbListSubType)
        self.cbVendor = QtWidgets.QComboBox(self.tab_2)
        self.cbVendor.setMinimumSize(QtCore.QSize(200, 0))
        self.cbVendor.setObjectName("cbVendor")
        self.cbVendor.addItem("")
        self.cbVendor.addItem("")
        self.verticalLayout.addWidget(self.cbVendor)
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.groupBox = QtWidgets.QGroupBox(self.tab_2)
        self.groupBox.setMinimumSize(QtCore.QSize(290, 0))
        self.groupBox.setObjectName("groupBox")
        self.gridLayoutWidget_2 = QtWidgets.QWidget(self.groupBox)
        self.gridLayoutWidget_2.setGeometry(QtCore.QRect(10, 20, 272, 88))
        self.gridLayoutWidget_2.setObjectName("gridLayoutWidget_2")
        self.gridLayout_7 = QtWidgets.QGridLayout(self.gridLayoutWidget_2)
        self.gridLayout_7.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_7.setObjectName("gridLayout_7")
        self.chkCutOff = QtWidgets.QCheckBox(self.gridLayoutWidget_2)
        self.chkCutOff.setChecked(False)
        self.chkCutOff.setObjectName("chkCutOff")
        self.gridLayout_7.addWidget(self.chkCutOff, 2, 0, 1, 1)
        self.chkDropDate = QtWidgets.QCheckBox(self.gridLayoutWidget_2)
        self.chkDropDate.setChecked(False)
        self.chkDropDate.setObjectName("chkDropDate")
        self.gridLayout_7.addWidget(self.chkDropDate, 1, 0, 1, 1)
        self.chkFeaturedProduct = QtWidgets.QCheckBox(self.gridLayoutWidget_2)
        self.chkFeaturedProduct.setChecked(False)
        self.chkFeaturedProduct.setObjectName("chkFeaturedProduct")
        self.gridLayout_7.addWidget(self.chkFeaturedProduct, 0, 0, 1, 1)
        self.chkListVendor = QtWidgets.QCheckBox(self.gridLayoutWidget_2)
        self.chkListVendor.setChecked(False)
        self.chkListVendor.setObjectName("chkListVendor")
        self.gridLayout_7.addWidget(self.chkListVendor, 3, 0, 1, 1)
        self.chkListSelection = QtWidgets.QCheckBox(self.gridLayoutWidget_2)
        self.chkListSelection.setChecked(False)
        self.chkListSelection.setObjectName("chkListSelection")
        self.gridLayout_7.addWidget(self.chkListSelection, 0, 1, 1, 1)
        self.chkModelRank = QtWidgets.QCheckBox(self.gridLayoutWidget_2)
        self.chkModelRank.setChecked(False)
        self.chkModelRank.setObjectName("chkModelRank")
        self.gridLayout_7.addWidget(self.chkModelRank, 1, 1, 1, 1)
        self.chkListCost = QtWidgets.QCheckBox(self.gridLayoutWidget_2)
        self.chkListCost.setChecked(False)
        self.chkListCost.setObjectName("chkListCost")
        self.gridLayout_7.addWidget(self.chkListCost, 2, 1, 1, 1)
        self.horizontalLayout.addWidget(self.groupBox)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem2)
        self.groupBox_2 = QtWidgets.QGroupBox(self.tab_2)
        self.groupBox_2.setMinimumSize(QtCore.QSize(550, 0))
        self.groupBox_2.setObjectName("groupBox_2")
        self.gridLayoutWidget = QtWidgets.QWidget(self.groupBox_2)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(20, 20, 521, 81))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.grdRollup = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.grdRollup.setContentsMargins(-1, 5, -1, 5)
        self.grdRollup.setVerticalSpacing(0)
        self.grdRollup.setObjectName("grdRollup")
        self.lblAvgProdOrder = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.lblAvgProdOrder.setFont(font)
        self.lblAvgProdOrder.setObjectName("lblAvgProdOrder")
        self.grdRollup.addWidget(self.lblAvgProdOrder, 1, 1, 1, 1)
        self.lblGrossMargin = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.lblGrossMargin.setFont(font)
        self.lblGrossMargin.setObjectName("lblGrossMargin")
        self.grdRollup.addWidget(self.lblGrossMargin, 4, 2, 1, 1)
        self.lblAvgResponse = QtWidgets.QLabel(self.gridLayoutWidget)
        self.lblAvgResponse.setMinimumSize(QtCore.QSize(250, 0))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.lblAvgResponse.setFont(font)
        self.lblAvgResponse.setObjectName("lblAvgResponse")
        self.grdRollup.addWidget(self.lblAvgResponse, 4, 1, 1, 1)
        self.lblAvgProdPerCard = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.lblAvgProdPerCard.setFont(font)
        self.lblAvgProdPerCard.setObjectName("lblAvgProdPerCard")
        self.grdRollup.addWidget(self.lblAvgProdPerCard, 0, 1, 1, 1)
        self.lblAvgGrossOrder = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.lblAvgGrossOrder.setFont(font)
        self.lblAvgGrossOrder.setObjectName("lblAvgGrossOrder")
        self.grdRollup.addWidget(self.lblAvgGrossOrder, 1, 2, 1, 1)
        self.lblAvgGrossCard = QtWidgets.QLabel(self.gridLayoutWidget)
        self.lblAvgGrossCard.setMinimumSize(QtCore.QSize(250, 0))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.lblAvgGrossCard.setFont(font)
        self.lblAvgGrossCard.setObjectName("lblAvgGrossCard")
        self.grdRollup.addWidget(self.lblAvgGrossCard, 0, 2, 1, 1)
        self.horizontalLayout.addWidget(self.groupBox_2)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem3)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setContentsMargins(-1, 0, -1, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.btnViewChart = QtWidgets.QPushButton(self.tab_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnViewChart.sizePolicy().hasHeightForWidth())
        self.btnViewChart.setSizePolicy(sizePolicy)
        self.btnViewChart.setMaximumSize(QtCore.QSize(100, 16777215))
        self.btnViewChart.setObjectName("btnViewChart")
        self.verticalLayout_2.addWidget(self.btnViewChart)
        self.btnExport = QtWidgets.QPushButton(self.tab_2)
        self.btnExport.setObjectName("btnExport")
        self.verticalLayout_2.addWidget(self.btnExport)
        self.btnCompare = QtWidgets.QPushButton(self.tab_2)
        self.btnCompare.setObjectName("btnCompare")
        self.verticalLayout_2.addWidget(self.btnCompare)
        self.btnCompareIE = QtWidgets.QPushButton(self.tab_2)
        self.btnCompareIE.setObjectName("btnCompareIE")
        self.verticalLayout_2.addWidget(self.btnCompareIE)
        self.horizontalLayout.addLayout(self.verticalLayout_2)
        self.gridLayout.addLayout(self.horizontalLayout, 0, 0, 1, 1)
        self.cbSearchHistoryTable = QtWidgets.QComboBox(self.tab_2)
        self.cbSearchHistoryTable.setMaximumSize(QtCore.QSize(483, 16777215))
        self.cbSearchHistoryTable.setObjectName("cbSearchHistoryTable")
        self.gridLayout.addWidget(self.cbSearchHistoryTable, 1, 0, 1, 1)
        self.tabReport.addTab(self.tab_2, "")
        self.verticalLayout_3.addWidget(self.tabReport)
        dashMain.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(dashMain)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1600, 21))
        self.menubar.setObjectName("menubar")
        dashMain.setMenuBar(self.menubar)

        self.retranslateUi(dashMain)
        self.tabReport.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(dashMain)

    def retranslateUi(self, dashMain):
        _translate = QtCore.QCoreApplication.translate
        dashMain.setWindowTitle(_translate("dashMain", "InkPixi Postcard Dashboard"))
        self.label_2.setText(_translate("dashMain", "Postcard Campaign Dashboard"))
        self.leSourceCodeSubj.setPlaceholderText(_translate("dashMain", "Source Campaign"))
        self.leSourceCodeBench.setPlaceholderText(_translate("dashMain", "Benchmark Campaign"))
        self.cbSearchHistoryRpt.setItemText(0, _translate("dashMain", "-- Search History --"))
        self.btnViewReport.setText(_translate("dashMain", "View in Dash"))
        self.btnOpenReport.setText(_translate("dashMain", "Open in Browser"))
        self.btnForward.setText(_translate("dashMain", "Foward"))
        self.btnBack.setText(_translate("dashMain", "Back"))
        self.tabReport.setTabText(self.tabReport.indexOf(self.tab), _translate("dashMain", "Report"))
        item = self.tblReport.horizontalHeaderItem(0)
        item.setText(_translate("dashMain", "Source Code"))
        item = self.tblReport.horizontalHeaderItem(1)
        item.setText(_translate("dashMain", "Root SKU"))
        item = self.tblReport.horizontalHeaderItem(2)
        item.setText(_translate("dashMain", "Featured Product"))
        item = self.tblReport.horizontalHeaderItem(3)
        item.setText(_translate("dashMain", "Drop Date"))
        item = self.tblReport.horizontalHeaderItem(4)
        item.setText(_translate("dashMain", "Cut Off Date"))
        item = self.tblReport.horizontalHeaderItem(5)
        item.setText(_translate("dashMain", "List Vendor"))
        item = self.tblReport.horizontalHeaderItem(6)
        item.setText(_translate("dashMain", "List Selection"))
        item = self.tblReport.horizontalHeaderItem(7)
        item.setText(_translate("dashMain", "Model Tier Rank"))
        item = self.tblReport.horizontalHeaderItem(8)
        item.setText(_translate("dashMain", "List Cost / M Net"))
        item = self.tblReport.horizontalHeaderItem(9)
        item.setText(_translate("dashMain", "Printed Quantity"))
        item = self.tblReport.horizontalHeaderItem(10)
        item.setText(_translate("dashMain", "Response Rate"))
        item = self.tblReport.horizontalHeaderItem(11)
        item.setText(_translate("dashMain", "Product Total Per Card"))
        item = self.tblReport.horizontalHeaderItem(12)
        item.setText(_translate("dashMain", "Product Total Per Order"))
        item = self.tblReport.horizontalHeaderItem(13)
        item.setText(_translate("dashMain", "Gross Sales Per Card"))
        item = self.tblReport.horizontalHeaderItem(14)
        item.setText(_translate("dashMain", "Gross Sales Per Order"))
        item = self.tblReport.horizontalHeaderItem(15)
        item.setText(_translate("dashMain", "Contribution Margin"))
        item = self.tblReport.horizontalHeaderItem(16)
        item.setText(_translate("dashMain", "20% Adjustment Non Campaign"))
        self.gbQtr.setTitle(_translate("dashMain", "Quater"))
        self.gbYear.setTitle(_translate("dashMain", "Year"))
        self.cbListType.setItemText(0, _translate("dashMain", "-- List Type --"))
        self.cbListType.setItemText(1, _translate("dashMain", "All"))
        self.cbCategory.setItemText(0, _translate("dashMain", "-- Category --"))
        self.cbCategory.setItemText(1, _translate("dashMain", "All"))
        self.cbListSubType.setItemText(0, _translate("dashMain", "-- List Sub Types --"))
        self.cbListSubType.setItemText(1, _translate("dashMain", "All"))
        self.cbVendor.setItemText(0, _translate("dashMain", "-- Vendor --"))
        self.cbVendor.setItemText(1, _translate("dashMain", "All"))
        self.groupBox.setTitle(_translate("dashMain", "Hide Columns"))
        self.chkCutOff.setText(_translate("dashMain", "Cut Off Date"))
        self.chkDropDate.setText(_translate("dashMain", "Drop Date"))
        self.chkFeaturedProduct.setText(_translate("dashMain", "Featured Product"))
        self.chkListVendor.setText(_translate("dashMain", "List Vendor"))
        self.chkListSelection.setText(_translate("dashMain", "List Selection"))
        self.chkModelRank.setText(_translate("dashMain", "Model Tier Rank"))
        self.chkListCost.setText(_translate("dashMain", "List Cost"))
        self.groupBox_2.setTitle(_translate("dashMain", "Rollup"))
        self.lblAvgProdOrder.setText(_translate("dashMain", "Avg Product Sales Per Order: "))
        self.lblGrossMargin.setText(_translate("dashMain", "Total Gross Margin: "))
        self.lblAvgResponse.setText(_translate("dashMain", "Avg Response Rate: "))
        self.lblAvgProdPerCard.setText(_translate("dashMain", "Avg Product Sales Per Card: "))
        self.lblAvgGrossOrder.setText(_translate("dashMain", "Avg Gross Sales Per Order: "))
        self.lblAvgGrossCard.setText(_translate("dashMain", "Avg Gross Sales Per Card: "))
        self.btnViewChart.setText(_translate("dashMain", "View Results"))
        self.btnExport.setText(_translate("dashMain", "Export Results"))
        self.btnCompare.setText(_translate("dashMain", "Compare in Dash"))
        self.btnCompareIE.setText(_translate("dashMain", "Compare in IE"))
        self.tabReport.setTabText(self.tabReport.indexOf(self.tab_2), _translate("dashMain", "Stat Table"))

from PyQt5 import QtWebKitWidgets
import resources_rc
