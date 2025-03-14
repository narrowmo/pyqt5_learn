"""
pip install pyqt5
pip install pyqt5-tools

- 更换pip源：
   1. 命令行：pip config set global.index-url https://pypi.tuna.tsinghua.edu.cn/simple
   2. 手动更换pip源：
    在文件资源管理器地址栏输入 %APPDATA%，进入 Roaming 文件夹。
    新建 pip 文件夹，并在其中创建 pip.ini 文件。
    编辑 pip.ini 并输入：
      [global]
      index-url = https://pypi.tuna.tsinghua.edu.cn/simple
      trusted-host = pypi.tuna.tsinghua.edu.cn

- 升级pip：pip install --upgrade pip

- 使用PyQt5：
  1. 创建应用 QApplication
  2. 创建窗口
    1. QMainWindow 大窗口
    2. QDialog 对话框
    3. QWidget 小窗口
        - 设置窗口大小：self.resize(400, 300)
        - 设置窗口位置：self.move(600, 300)
        - 设置窗口标题：self.setWindowTitle("My Window")

  3. 创建控件
    1. QPushButton 按钮
    2. QLabel 标签
    3. QLineEdit 文本框
    4. QTextEdit 多行文本框

  导入模块：
  from PyQt5.QtWidgets import QApplication, QWidget, QMianWindow, QDialog
  import sys

"""
import sys

from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow, QDialog, QPushButton, QLabel

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
        self.pushButton.move(250, 200)

if __name__ == '__main__':
    # 创建应用对象
    app = QApplication(sys.argv)  #
    w = MyWindow()
    w.show()    # 显示窗口
    sys.exit(app.exec_())  # 运行应用，并监听事件



