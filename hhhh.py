import sys
from PySide2.QtWidgets import QApplication, QPushButton
from PySide2.QtCore import Slot
from PySide2.QtWidgets import QApplication, QMessageBox
from PySide2.QtUiTools import QUiLoader

class Stats:

    def __init__(self):
        # 从文件中加载UI定义
        # 从 UI 定义中动态 创建一个相应的窗口对象
        # 注意：里面的控件对象也成为窗口对象的属性了
        # 比如 self.ui.button , self.ui.textEdit
        self.ui = QUiLoader().load('untitled.ui')
        self.ui.pushButton_4.clicked.connect(self.handleCalc)

    def handleCalc(self):
        print("Button clicked")
        #self.ui.layout.addWidget(pushButton_5)

app = QApplication([])
stats = Stats()
stats.ui.show()
app.exec_()