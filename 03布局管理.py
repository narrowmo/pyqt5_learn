"""
布局管理
  布局管理的基本思想：把控件按照一定的顺序摆放，从而达到美观、整齐、舒适的效果。
    1. from PyQt5.QtWidgets import QVBoxLayout, QHBoxLayout
        - QVBoxLayout: 垂直布局
            - v_layout = QVBoxLayout()  # 创建垂直布局对象
            - btn1 = QPushButton('按钮1', self)  # 创建按钮
            - btn2 = QPushButton('按钮2', self)  # 创建按钮
            - btn3 = QPushButton('按钮3', self)  # 创建按钮
            - v_layout.addWidget(btn1)  # 向垂直布局中添加按钮
            - v_layout.addStretch(1)  # 增加伸缩器，比例为1
            - v_layout.addWidget(btn2)  # 向垂直布局中添加按钮
            - v_layout.addStretch(2)  # 增加伸缩器，比例为2
            - v_layout.addWidget(btn3)  # 向垂直布局中添加按钮

            - self.setLayout(v_layout)  # 设置布局

        - QHBoxLayout：水平布局
            - h_layout = QHBoxLayout()  # 创建水平布局对象
            - btn1 = QPushButton('按钮1', self)  # 创建按钮
            - btn2 = QPushButton('按钮2', self)  # 创建按钮
            - btn3 = QPushButton('按钮3', self)  # 创建按钮
            - h_layout.addWidget(btn1)  # 向水平布局中添加按钮
            - h_layout.addStretch(1)  # 增加伸缩器，比例为1
            - h_layout.addWidget(btn2)  # 向水平布局中添加按钮
            - h_layout.addStretch(2)  # 增加伸缩器，比例为1
            - h_layout.addWidget(btn3)  # 向水平布局中添加按钮

            - self.setLayout(h_layout)  # 设置布局

    2.网格布局
         - QGridLayout: 网格布局
             - g_layout = QGridLayout()  # 创建网格布局对象
             - btn1 = QPushButton('按钮1', self)  # 创建按钮
             - btn2 = QPushButton('按钮2', self)  # 创建按钮
             - btn3 = QPushButton('按钮3', self)  # 创建按钮
             - btn4 = QPushButton('按钮4', self)  # 创建按钮
             - btn5 = QPushButton('按钮5', self)  # 创建按钮
             - g_layout.addWidget(btn1, 0, 0)  # 向网格布局中添加按钮，位置为第0行第0列
             - g_layout.addWidget(btn2, 0, 1)  # 向网格布局中添加按钮，位置为第0行第1列
             - g_layout.addWidget(btn3, 0, 3)  # 向网格布局中添加按钮，位置为第0行第3列
             - g_layout.addWidget(btn4, 1, 0)  # 向网格布局中添加按钮，位置为第1行第0列
             - g_layout.addWidget(btn5, 1, 2)  # 向网格布局中添加按钮，位置为第1行第2列
             - self.setLayout(g_layout)  # 设置布局

    3. 表单布局
         - QFormLayout: 表单布局，是一种网格布局，但是可以设置行和列的间距。
         - 表单布局可以实现更复杂的布局效果，比如输入框、下拉框、单选框、多选框等。
             - f_layout = QFormLayout()  # 创建表单布局对象
             - label1 = QLabel('用户名：')  # 创建标签
             - lineEdit1 = QLineEdit()  # 创建输入框
             - f_layout.addRow(label1, lineEdit1)  # 添加一行：用户名+输入框
             - label2 = QLabel('密码：')  # 创建标签
             - lineEdit2 = QLineEdit()  # 创建输入框
             - f_layout.addRow(label2, lineEdit2)  # 添加一行：密码+输入框
             - self.setLayout(f_layout)  # 设置布局

"""
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QVBoxLayout, QHBoxLayout, QGridLayout, QFormLayout\
    , QLineEdit, QComboBox
import sys


#类的形式
class MyWindow(QWidget):
    def __init__(self):
        super().__init__()

        # 设置窗口大小
        self.resize(1000, 800)
        # 设置窗口标题
        self.setWindowTitle('嘟嘟')
        # 设置窗口位置
        self.move(100, 100)

        # # 创建标签
        # self.label = QLabel(self)
        # self.label.setText('嘟嘟小猫咪')
        # self.label.move(100, 100)
        #
        # # 创建按钮
        # self.pushButton = QPushButton(self)
        # self.pushButton.setText('点我')
        # self.pushButton.move(100, 200)

        # # 垂直布局，把按钮放入盒子
        # v_layout = QVBoxLayout()
        # btn1 = QPushButton('按钮1', self)
        # btn2 = QPushButton('按钮2', self)
        # btn3 = QPushButton('按钮3', self)
        # v_layout.addWidget(btn1)
        # v_layout.addStretch(1)  # 增加伸缩器
        # v_layout.addWidget(btn2)
        # v_layout.addStretch(2)  # 增加伸缩器
        # v_layout.addWidget(btn3)
        # # 设置布局
        # self.setLayout(v_layout)

        # # 水平布局，把按钮放入盒子
        # h_layout = QHBoxLayout()
        # btn1 = QPushButton('按钮1', self)
        # btn2 = QPushButton('按钮2', self)
        # btn3 = QPushButton('按钮3', self)
        # h_layout.addWidget(btn1)
        # h_layout.addStretch(1)  # 增加伸缩器
        # h_layout.addWidget(btn2)
        # h_layout.addStretch(2)  # 增加伸缩器
        # h_layout.addWidget(btn3)
        # # 设置布局
        # self.setLayout(h_layout)

        # # 网格布局
        # g_layout = QGridLayout()
        # btn1 = QPushButton('按钮1', self)
        # btn2 = QPushButton('按钮2', self)
        # btn3 = QPushButton('按钮3', self)
        # btn4 = QPushButton('按钮4', self)
        # btn5 = QPushButton('按钮5', self)
        #
        # g_layout.addWidget(btn1, 0, 0)
        # g_layout.addWidget(btn2, 0, 1)
        # g_layout.addWidget(btn3, 0, 3)
        # g_layout.addWidget(btn4, 1, 0)
        # g_layout.addWidget(btn5, 1, 2)
        # # 设置布局
        # self.setLayout(g_layout)

        # 表单布局
        f_label = QFormLayout()
        f_label.addRow(QLabel('用户名：'), QLineEdit())  # 添加一行:用户名+输入框
        f_label.addRow(QLabel('密码：'), QLineEdit())  # 添加一行:密码+输入框


        # 水平布局
        h_layout = QHBoxLayout()
        btn_ok = QPushButton('确定', self)
        btn_cancel = QPushButton('取消', self)
        h_layout.addStretch(1)  # 增加伸缩器
        h_layout.addWidget(btn_ok)
        h_layout.addStretch(1)  # 增加伸缩器
        h_layout.addWidget(btn_cancel)
        h_layout.addStretch(1)  # 增加伸缩器

        # 把水平布局放入表单布局
        f_label.addRow(h_layout)

        # 设置布局
        self.setLayout(f_label)


if __name__ == '__main__':
    app = QApplication(sys.argv)    # 创建QApplication对象
    window = MyWindow()
    window.show()
    sys.exit(app.exec_())
