from PyQt5.QtCore import QLine
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QFormLayout, QLineEdit, QHBoxLayout, QTextEdit, \
    QVBoxLayout, QRadioButton, QListWidget, QComboBox
import sys

class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.resize(400, 300)
        self.setWindowTitle('嘟嘟')

        # # 文本控件
        # f_layout = QFormLayout()    # 表单布局
        # username = QLineEdit('嘟嘟', self)
        # password = QLineEdit()
        # password.setEchoMode(QLineEdit.Password)
        #
        # f_layout.addRow('用户名', username)
        # f_layout.addRow('密码', password)

        # # 按钮控件
        # h_layout = QHBoxLayout()    # 水平布局
        # btn1 = QPushButton('登录', self)
        # btn2 = QPushButton('取消', self)
        # h_layout.addStretch(2)
        # h_layout.addWidget(btn1)
        # h_layout.addStretch(1)
        # h_layout.addWidget(btn2)
        # h_layout.addStretch(2)
        #
        # f_layout.addRow(h_layout)

        # # 多行文本控件
        # text_input = QTextEdit(self)
        # f_layout.addRow(text_input)

        # self.setLayout(f_layout)    # 设置布局

        # # 单选按钮
        # v_layout = QHBoxLayout()
        # radio1 = QRadioButton('男')
        # radio2 = QRadioButton('女')
        # radio3 = QRadioButton('保密')
        # label = QLabel('请选择性别：', self)
        # v_layout.addWidget(label)
        # v_layout.addWidget(radio1)
        # v_layout.addWidget(radio2)
        # v_layout.addWidget(radio3)
        #
        # radio1.setChecked(True)
        # radio1.toggled.connect(self.btn_clicked)
        # radio2.toggled.connect(self.btn_clicked)
        # radio3.clicked.connect(self.btn_clicked)
        #
        # self.setLayout(v_layout)
    #
    # def btn_clicked(self):
    #     btn = self.sender()
    #     if btn.isChecked():
    #         print('选中：' + btn.text())

    #     f_layout = QFormLayout()    # 表单布局
    #     l_widget = QListWidget()
    #     l_widget.addItems(['Python', 'Java', 'C++', 'C', 'JavaScript'])
    #     label = QLabel(self)
    #     label.setText('请选择编程语言：')
    #     f_layout.addRow(label, l_widget)
    #
    #     self.setLayout(f_layout)    # 设置布局
    #
    #     l_widget.currentItemChanged.connect(self.list_cliked)
    #
    #
    # def list_cliked(self, item):
    #     print(f'选中：{item.text()}')

        # 下拉列表框
        f_layout = QFormLayout()
        combo_box = QComboBox()
        combo_box.addItems(['Python', 'Java', 'C++', 'C', 'JavaScript'])
        label = QLabel(self)
        label.setText('请选择编程语言：')
        f_layout.addRow(label, combo_box)
        self.setLayout(f_layout)    # 设置布局

        combo_box.currentIndexChanged.connect(self.combo_selected)


    def combo_selected(self, index):
        combo_box = self.sender()
        print(f'选中：{combo_box.currentText()}, index: {index}')



if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec_())
