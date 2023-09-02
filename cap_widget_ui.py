# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'cap_widget.ui'
##
## Created by: Qt User Interface Compiler version 6.5.2
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
from PySide6.QtWidgets import (QApplication, QGridLayout, QHBoxLayout, QLabel,
    QLineEdit, QPushButton, QSizePolicy, QVBoxLayout,
    QWidget)
import resource_rc

class Ui_CapWidget(object):
    def setupUi(self, CapWidget):
        if not CapWidget.objectName():
            CapWidget.setObjectName(u"CapWidget")
        CapWidget.resize(400, 250)
        CapWidget.setMaximumSize(QSize(400, 250))
        icon = QIcon()
        icon.addFile(u":/img/xndll.jpg", QSize(), QIcon.Normal, QIcon.Off)
        CapWidget.setWindowIcon(icon)
        self.gridLayout = QGridLayout(CapWidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.lineEdit_F = QLineEdit(CapWidget)
        self.lineEdit_F.setObjectName(u"lineEdit_F")
        font = QFont()
        font.setPointSize(12)
        font.setBold(True)
        self.lineEdit_F.setFont(font)
        self.lineEdit_F.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout.addWidget(self.lineEdit_F)

        self.label = QLabel(CapWidget)
        self.label.setObjectName(u"label")
        self.label.setFont(font)

        self.horizontalLayout.addWidget(self.label)


        self.verticalLayout_2.addLayout(self.horizontalLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.lineEdit_mF = QLineEdit(CapWidget)
        self.lineEdit_mF.setObjectName(u"lineEdit_mF")
        self.lineEdit_mF.setFont(font)
        self.lineEdit_mF.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_2.addWidget(self.lineEdit_mF)

        self.label_2 = QLabel(CapWidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setFont(font)

        self.horizontalLayout_2.addWidget(self.label_2)


        self.verticalLayout_2.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.lineEdit_uF = QLineEdit(CapWidget)
        self.lineEdit_uF.setObjectName(u"lineEdit_uF")
        self.lineEdit_uF.setFont(font)
        self.lineEdit_uF.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_3.addWidget(self.lineEdit_uF)

        self.label_3 = QLabel(CapWidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setFont(font)

        self.horizontalLayout_3.addWidget(self.label_3)


        self.verticalLayout_2.addLayout(self.horizontalLayout_3)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.lineEdit_nF = QLineEdit(CapWidget)
        self.lineEdit_nF.setObjectName(u"lineEdit_nF")
        self.lineEdit_nF.setFont(font)
        self.lineEdit_nF.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_4.addWidget(self.lineEdit_nF)

        self.label_4 = QLabel(CapWidget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setFont(font)

        self.horizontalLayout_4.addWidget(self.label_4)


        self.verticalLayout_2.addLayout(self.horizontalLayout_4)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.lineEdit_pF = QLineEdit(CapWidget)
        self.lineEdit_pF.setObjectName(u"lineEdit_pF")
        self.lineEdit_pF.setFont(font)
        self.lineEdit_pF.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_5.addWidget(self.lineEdit_pF)

        self.label_5 = QLabel(CapWidget)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setFont(font)

        self.horizontalLayout_5.addWidget(self.label_5)


        self.verticalLayout_2.addLayout(self.horizontalLayout_5)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.pushButton_About = QPushButton(CapWidget)
        self.pushButton_About.setObjectName(u"pushButton_About")

        self.verticalLayout.addWidget(self.pushButton_About)


        self.verticalLayout_2.addLayout(self.verticalLayout)


        self.gridLayout.addLayout(self.verticalLayout_2, 0, 0, 1, 1)


        self.retranslateUi(CapWidget)

        QMetaObject.connectSlotsByName(CapWidget)
    # setupUi

    def retranslateUi(self, CapWidget):
        CapWidget.setWindowTitle(QCoreApplication.translate("CapWidget", u"\u7535\u5bb9\u5355\u4f4d\u8f6c\u6362\u5de5\u5177-\u5c0f\u571f\u5761", None))
        self.label.setText(QCoreApplication.translate("CapWidget", u"F", None))
        self.label_2.setText(QCoreApplication.translate("CapWidget", u"mF", None))
        self.label_3.setText(QCoreApplication.translate("CapWidget", u"uF", None))
        self.label_4.setText(QCoreApplication.translate("CapWidget", u"nF", None))
        self.label_5.setText(QCoreApplication.translate("CapWidget", u"pF", None))
        self.pushButton_About.setText(QCoreApplication.translate("CapWidget", u"\u5173\u4e8e", None))
    # retranslateUi

