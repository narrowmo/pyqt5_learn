"""
常用控件1:
    文本输入控件: QLineEdit单行文本输入框，QTextEdit多行文本输入框，QPlainTextEdit纯文本输入框

    单选按钮控件: QRadioButton单选按钮，QButtonGroup单选按钮组

    复选按钮控件: QCheckBox复选按钮，QGroupBox分组框，QButtonGroup复选按钮组

    进度条控件: QProgressBar进度条


"""
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QTextEdit, QFormLayout, QVBoxLayout, QHBoxLayout \
, QRadioButton
import sys

class MyWindow(QWidget):

    def __init__(self):
        super().__init__()
        self.resize(800, 600)
        self.setWindowTitle("My Window")

        # # 文本输入控件
        # f_layout = QFormLayout()
        # user_name = QLineEdit('嘟嘟',self)
        # password = QLineEdit()
        # password.setEchoMode(QLineEdit.Password)    # 密码模式
        #
        # # 多行文本输入控件
        # text_input = QTextEdit()
        #
        # # 放入布局
        # f_layout.addRow(QLabel('用户名：'), user_name)
        # f_layout.addRow(QLabel('密码：'), password)
        # f_layout.addRow(text_input)
        # self.setLayout(f_layout)     # 设置布局，放入窗体


        # 单选按钮控件
        h_layout = QHBoxLayout()
        radio1 = QRadioButton('男')
        radio2 = QRadioButton('女')
        radio3 = QRadioButton('其他')
        label = QLabel('请选择性别：')
        h_layout.addWidget(label)
        h_layout.addWidget(radio1)
        h_layout.addWidget(radio2)
        h_layout.addWidget(radio3)

        self.setLayout(h_layout)     # 设置布局，放入窗体

        radio1.setChecked(True)   # 设置默认选中项
        radio1.toggled.connect(self.btn_clicked)   # 单选按钮切换时，设置其为选中状态
        radio2.clicked.connect(self.btn_clicked)
        radio3.toggled.connect(self.btn_clicked)

    # 槽函数
    def btn_clicked(self):
        btn = self.sender()  # 获取单击的按钮
        if btn.isChecked():
            print(btn.text() + '被选中')




if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MyWindow()
    window.show()
    sys.exit(app.exec_())
