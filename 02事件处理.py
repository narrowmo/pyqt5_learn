"""
1. 信号与槽
    - 信号：是一种事件通知机制，用于通知对象某个事件已经发生。
    - 槽：是一种回调函数，用于响应信号，并执行相应的操作。
    - 信号与槽的连接：通过信号与槽的连接，可以实现对象间的通信。
    - 信号与槽的传递：信号可以传递参数，槽也可以接收参数。
    - 方法：
        - 建立槽函数
        - 通过connect()方法连接信号与槽函数

2. 改写鼠标事件
    - 改写鼠标事件：通过重写鼠标事件，可以实现对鼠标事件的监听和处理。
    - 鼠标事件：from PyQt5.Qcore import Qt
        - mousePressEvent()：鼠标按下事件
        - mouseReleaseEvent()：鼠标释放事件
        - mouseMoveEvent()：鼠标移动事件
        - mouseDoubleClickEvent()：鼠标双击事件
        - wheelEvent()：滚轮事件
        - customEvent()：自定义事件

3. 改写键盘事件
    - 改写键盘事件：通过重写键盘事件，可以实现对键盘事件的监听和处理。
    - 键盘事件：
        - keyPressEvent()：键盘按下事件
        - keyReleaseEvent()：键盘释放事件
        - focusInEvent()：焦点进入事件
        - focusOutEvent()：焦点退出事件
        - inputMethodEvent()：输入法事件
        - inputMethodQuery()：输入法查询事件
"""
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel
from PyQt5.QtCore import Qt
import sys


# 类的形式
class MyWindow(QWidget):
    def __init__(self):
        super().__init__()

        # 设置窗口大小
        self.resize(400, 300)
        # 设置窗口位置
        self.move(600, 300)
        # 设置窗口标题
        self.setWindowTitle("My Window")

        # 创建标签
        self.label = QLabel(self)
        self.label.setText("这是标签")
        self.label.move(100, 200)

        # 创建按钮
        self.pushButton = QPushButton(self)
        self.pushButton.setText("按钮")
        self.pushButton.move(300, 200)
        # self.pushButton.clicked.connect(self.btn_click)  # 绑定槽函数

    # # 槽函数
    # def btn_click(self):
    #     self.label.setText("点击了")

    # 改写鼠标事件
    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.label.setText("鼠标左键按下")
        elif event.button() == Qt.RightButton:
            self.label.setText("鼠标右键按下")
        else:
            self.label.setText("鼠标未按下")

    def mouseReleaseEvent(self, event):
        self.label.setText("鼠标释放")

    # 改写键盘事件
    def keyPressEvent(self, event):
        self.label.setText("键盘按下")

    def keyReleaseEvent(self, event):
        self.label.setText("键盘释放")

if __name__ == '__main__':
    # 创建应用对象
    app = QApplication(sys.argv)  #
    w = MyWindow()
    w.show()    # 显示窗口
    sys.exit(app.exec_())  # 运行应用，并监听事件

