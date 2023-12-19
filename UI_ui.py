# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'UI.ui'
##
## Created by: Qt User Interface Compiler version 6.6.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QGridLayout, QLabel, QLineEdit,
    QMainWindow, QPushButton, QSizePolicy, QTextEdit,
    QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(910, 511)
        MainWindow.setStyleSheet(u".QPushButton{\n"
"color:#fff;\n"
"	\n"
"	font: 18pt \"Arial Black\";\n"
"	background-color: rgb(167, 144, 28);\n"
"border-radius:5px;\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"  border: 2px solid #000;\n"
"  padding: 10px 20px;\n"
"\n"
"}\n"
"\n"
"@keyframes pulse {\n"
"  0% {\n"
"    transform: scale(1);\n"
"  }\n"
"  50% {\n"
"    transform: scale(1.2);\n"
"  }\n"
"  100% {\n"
"    transform: scale(1);\n"
"  }\n"
"\n"
"\n"
"}\n"
"QLabel{\n"
"font: 87 30pt \"Arial Black\";\n"
"text-decoration: underline;\n"
"color: rgb(162, 139, 46);\n"
"text-align: center;}\n"
"\n"
".QMainWindow{\n"
"\n"
"	background-color: rgb(255, 255, 255);\n"
"\n"
"}\n"
".QLineEdit{\n"
"\n"
"border-radius:5px;\n"
"font: 87 16pt \"Arial Black\";\n"
"color: rgb(152, 130, 19);\n"
" border-style: solid ;\n"
"   border-color: rgb(178, 132, 16);\n"
"   border-width: 5px;\n"
"}\n"
"\n"
".QTextEdit{\n"
"  padding: 20%;\n"
"\n"
"margin:20px;\n"
"border-radius:5px;\n"
"	font: 20pt \"Terminal\";\n"
"	color: rgb(194, 171, 81);\n"
"	background-color: rgb(49, 49, "
                        "49);\n"
" border-style: solid ;\n"
"   border-color: rgb(178, 132, 16);\n"
"   border-width: 5px;\n"
"  margin-left: 80px;\n"
"}\n"
"\n"
"\n"
"")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"margin:5px;")
        self.verticalLayout_2 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setStyleSheet(u"")

        self.verticalLayout.addWidget(self.label)

        self.seq = QLineEdit(self.centralwidget)
        self.seq.setObjectName(u"seq")
        self.seq.setEnabled(True)
        self.seq.setMaximumSize(QSize(16777206, 16777215))
        self.seq.setStyleSheet(u"fontsize:24pt;")
        self.seq.setAlignment(Qt.AlignCenter)
        self.seq.setDragEnabled(True)
        self.seq.setClearButtonEnabled(True)

        self.verticalLayout.addWidget(self.seq)

        self.compile = QPushButton(self.centralwidget)
        self.compile.setObjectName(u"compile")

        self.verticalLayout.addWidget(self.compile)

        self.gridLayout_2 = QGridLayout()
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.simplify = QTextEdit(self.centralwidget)
        self.simplify.setObjectName(u"simplify")

        self.gridLayout_2.addWidget(self.simplify, 3, 1, 1, 1)

        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")
        font = QFont()
        font.setFamilies([u"Arial Black"])
        font.setPointSize(30)
        font.setWeight(QFont.)
        font.setItalic(False)
        font.setUnderline(True)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet(u"")

        self.gridLayout_2.addWidget(self.label_3, 2, 1, 1, 1)

        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setFont(font)
        self.label_2.setStyleSheet(u"")

        self.gridLayout_2.addWidget(self.label_2, 2, 0, 1, 1)

        self.cnf = QTextEdit(self.centralwidget)
        self.cnf.setObjectName(u"cnf")
        self.cnf.setStyleSheet(u"")
        self.cnf.setHtml(u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Terminal'; font-size:20pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:20px; margin-bottom:0px; margin-left:40px; margin-right:20px; -qt-block-indent:0; text-indent:0px; font-family:'MS Shell Dlg 2'; font-size:8pt;\"><br /></p></body></html>")
        self.cnf.setAcceptRichText(False)

        self.gridLayout_2.addWidget(self.cnf, 3, 0, 1, 1)

        self.clear = QPushButton(self.centralwidget)
        self.clear.setObjectName(u"clear")

        self.gridLayout_2.addWidget(self.clear, 1, 0, 1, 1)

        self.Validate = QPushButton(self.centralwidget)
        self.Validate.setObjectName(u"Validate")

        self.gridLayout_2.addWidget(self.Validate, 1, 1, 1, 1)


        self.verticalLayout.addLayout(self.gridLayout_2)


        self.verticalLayout_2.addLayout(self.verticalLayout)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\">TP IV - LAI Mohadi Amar</p></body></html>", None))
        self.seq.setPlaceholderText(QCoreApplication.translate("MainWindow", u"set your formela", None))
        self.compile.setText(QCoreApplication.translate("MainWindow", u"compile", None))
        self.simplify.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Terminal'; font-size:20pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:30px; margin-bottom:0px; margin-left:30px; margin-right:30px; -qt-block-indent:0; text-indent:0px; font-family:'MS Shell Dlg 2'; font-size:8pt;\"><br /></p></body></html>", None))
        self.simplify.setPlaceholderText(QCoreApplication.translate("MainWindow", u"simplify", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\">Simplify &amp; Eval</p></body></html>", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\">CNF</p></body></html>", None))
        self.cnf.setPlaceholderText(QCoreApplication.translate("MainWindow", u"FNC", None))
        self.clear.setText(QCoreApplication.translate("MainWindow", u"clear", None))
        self.Validate.setText(QCoreApplication.translate("MainWindow", u"Eval", None))
    # retranslateUi

