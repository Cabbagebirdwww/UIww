import sys
from PySide2.QtWidgets import QApplication, QPushButton,QMessageBox,QWidget
from PySide2.QtUiTools import QUiLoader
from PySide2.QtCore import Qt, QMimeData,Slot
from PySide2.QtGui import QDrag

class Button(QPushButton):

    def __init__(self, title, parent):
        super().__init__(title, parent)

    def mouseMoveEvent(self, e):
        if e.buttons() != Qt.LeftButton:
            return
        mimeData = QMimeData()
        drag = QDrag(self)
        drag.setMimeData(mimeData)
        drag.setHotSpot(e.pos() - self.rect().topLeft())
        drag.exec_(Qt.MoveAction)

class Stats:

    def __init__(self):
        # 从文件中加载UI定义
        # 从 UI 定义中动态 创建一个相应的窗口对象
        # 注意：里面的控件对象也成为窗口对象的属性了
        # 比如 self.ui.button , self.ui.textEdit
        self.ui = QUiLoader().load('untitled.ui')
        self.ui.pushButton_4.clicked.connect(self.handleCalc4)
        self.ui.pushButton_5.clicked.connect(self.handleCalc5)

    def handleCalc4(self):
        print("Button4 clicked")
        #新建起始按钮
        self.ui.button1 = QPushButton('start', self.ui.frame)
        self.ui.button1.show()
    #实现拖拽
    def dragEnterEvent(self, e):
        e.accept()
    def dropEvent(self, e):
        position = e.pos()
        self.ui.button1.move(position)
        e.setDropAction(Qt.MoveAction)
        e.accept()

    #新建过程按钮
    def handleCalc5(self):
        print("Button5 clicked")
        self.button2 = QPushButton('normal', self.ui.frame)
        self.button2.show()

app = QApplication(sys.argv)
stats = Stats()
stats.ui.show()
app.exec_()