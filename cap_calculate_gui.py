'''
电容器计算公式

`1F`（法拉）=`1000 mF`（毫法）=`10^6 μF`（微法）=`10^9nF`（纳法）=`10^12pF`（皮法）

#############################################################################
# 程序功能：
# 该程序的功能是实现电容单位换算的功能，使用方法是命令行运行程序并且提供一个参数，如：python cap_calculate.py 12pf
# 回车后程序输出结果，结果为所有单位的值
# pF nF uF mF F
'''
import sys
from PySide6.QtCore import Qt, Slot, QUrl
from PySide6.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QVBoxLayout, QTextEdit
from PySide6.QtGui import QDesktopServices
from cap_widget_ui import Ui_CapWidget

class MainDialog(QWidget):
    def __init__(self):
        super(MainDialog, self).__init__()
        self.ui = Ui_CapWidget()
        self.ui.setupUi(self)
        self.setup_ui()
    
    def setup_ui(self):
        self.ui.lineEdit_F.textEdited.connect(lambda v: self.textEdited_F(v))
        self.ui.lineEdit_mF.textEdited.connect(lambda v: self.textEdited_mF(v))
        self.ui.lineEdit_uF.textEdited.connect(lambda v: self.textEdited_uF(v))
        self.ui.lineEdit_nF.textEdited.connect(lambda v: self.textEdited_nF(v))
        self.ui.lineEdit_pF.textEdited.connect(lambda v: self.textEdited_pF(v))
        self.ui.pushButton_About.clicked.connect(lambda: QDesktopServices.openUrl(QUrl("https://gitee.com/zsf90/cap_calculate_gui")))
    
    @Slot()
    def textEdited_F(self, param):
        if param != '':
            temp = float(param)
            self.ui.lineEdit_mF.setText(str(temp * 1000))
            self.ui.lineEdit_uF.setText(str(temp * 1000 * 1000))
            self.ui.lineEdit_nF.setText(str(temp * 1000 * 1000 * 1000))
            self.ui.lineEdit_pF.setText(str(temp * 1000 * 1000 * 1000 * 1000))
        
    @Slot()
    def textEdited_mF(self, param):
        if param != '':
            temp = float(param)
            self.ui.lineEdit_F.setText(str(temp / 1000))
            self.ui.lineEdit_uF.setText(str(temp * 1000))
            self.ui.lineEdit_nF.setText(str(temp * 1000 * 1000))
            self.ui.lineEdit_pF.setText(str(temp * 1000 * 1000 * 1000))
    
    @Slot()
    def textEdited_uF(self, param):
        if param != '':
            temp = float(param)
            self.ui.lineEdit_F.setText(str(temp / 1000 / 1000))
            self.ui.lineEdit_mF.setText(str(temp / 1000))
            self.ui.lineEdit_nF.setText(str(temp * 1000))
            self.ui.lineEdit_pF.setText(str(temp * 1000 * 1000))
        
    @Slot()
    def textEdited_nF(self, param):
        if param != '':
            temp = float(param)
            self.ui.lineEdit_F.setText(str(temp / 1000 / 1000 / 1000))
            self.ui.lineEdit_mF.setText(str(temp / 1000 / 1000))
            self.ui.lineEdit_uF.setText(str(temp / 1000))
            self.ui.lineEdit_pF.setText(str(temp * 1000))
    
    @Slot()
    def textEdited_pF(self, param):
        if param != '':
            temp = float(param)
            self.ui.lineEdit_F.setText(str(temp / 1000 / 1000 / 1000 / 1000))
            self.ui.lineEdit_mF.setText(str(temp / 1000 / 1000 / 1000))
            self.ui.lineEdit_uF.setText(str(temp / 1000 / 1000))
            self.ui.lineEdit_nF.setText(str(temp / 1000))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    
    window = MainDialog()
    window.show()
    
    sys.exit(app.exec())

