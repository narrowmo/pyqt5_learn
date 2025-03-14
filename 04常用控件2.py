"""
常用控件2
    QListWidget：列表框
        - addItems(labels: Iterable[Optional[str]]) -> None：添加多个选项
        - addItem(aitem: Optional[QListWidgetItem]) -> None：添加单个选项
        - insertItems(row: int, labels: Iterable[str]) -> None：在指定位置插入多个选项
        - currentItemChanged() -> None：当前选项改变时触发

    QComboBox：下拉列表框
        - addItems(labels: Iterable[Optional[str]]) -> None
        - addItem(aitem: Optional[QListWidgetItem]) -> None
        - currentIdexChanged(index: int) -> None：当前选项改变时触发
        - currentText() -> str：当前文本

    QTableWidget：表格控件
        - setRowCount(rows: int) -> None：设置行数
        - setColumnCount(columns: int) -> None：设置列数
        - setHorizontalHeaderLabels(labels: Iterable[str]) -> None：设置表头
        - setFont(font: QFont) -> None：设置字体, 需要QFont对象, QFont('楷体', 12); from PyQt5.QtGui import QFont
        - setVerticalHeaderLabels(labels: Iterable[str]) -> None：设置行头
        - 转换为QTableWidgetItem类型，才能填充数据,QTableWidgetItem(data_body[row][col])
        - setItem(row: int, column: int, item: QTableWidgetItem) -> None：设置单元格内容


        - item(row: int, column: int) -> QTableWidgetItem：获取单元格内容
        - currentItem() -> QTableWidgetItem：获取当前选中单元格
        - currentRow() -> int：获取当前选中行
        - currentColumn() -> int：获取当前选中列
        - cellWidget(row: int, column: int) -> QWidget：获取单元格控件
        - setCellWidget(row: int, column: int, widget: QWidget) -> None：设置单元格控件


"""
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QApplication, QWidget, QFormLayout, QListWidget, QLabel, QComboBox, QVBoxLayout, \
    QTableWidget, QTableWidgetItem
import sys

data_headers = ['姓名', '性别', '年龄']
data_body = [
    ['张三', '男', '25'],
    ['王五', '男', '22'],
    ['李四', '女', '23'],
    ['嘟嘟', '男', '5']
]

class MyWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.resize(800, 600)
        self.setWindowTitle('嘟嘟')

        # 列表框
    #     f_layout = QFormLayout()
    #     listwidget = QListWidget()
    #     listwidget.addItems(['Python', 'Java', 'C++', 'C#', 'JavaScript'])
    #
    #     label = QLabel(self)
    #     label.setText('请选择编程语言：')
    #
    #     f_layout.addRow(label, listwidget)  # 添加到表单布局中
    #     self.setLayout(f_layout)  # 设置窗口布局
    #
    #     listwidget.currentItemChanged.connect(self.list_selected)  # 选中列表项时，设置当前行
    #
    # def list_selected(self, item):
    #     print(f'你选择的是：{item.text()}')

    #     # 下拉列表框
    #     f_layout = QFormLayout()
    #     combobox = QComboBox(self)
    #     combobox.addItems(['Python', 'Java', 'C++', 'C#', 'JavaScript'])
    #     label = QLabel(self)
    #     label.setText('请选择编程语言：')
    #     f_layout.addRow(label, combobox)  # 添加到表单布局中
    #     self.setLayout(f_layout)  # 设置窗口布局
    #     combobox.currentIndexChanged.connect(self.combo_selected)  # 选中下拉项时，设置当前文本
    #
    # def combo_selected(self, index):
    #     combobox = self.findChild(QComboBox)  # 获取下拉框对象
    #     print(f'你选择的是：{combobox.currentText()}, index: {index}')


        # 表格控件
        v_layout = QVBoxLayout()
        table = QTableWidget()
        # 设置行数和列数
        table.setRowCount(len(data_body))
        table.setColumnCount(len(data_headers))
        # 设置字体
        table.setFont(QFont('楷体', 12))  # 设置字体，需要QFont对象
        # 设置表头
        table.setHorizontalHeaderLabels(data_headers)
        # 填充数据
        for row in range(len(data_body)):
            for col in range(len(data_headers)):
                data_item = QTableWidgetItem(data_body[row][col])  # 转换为QTableWidgetItem类型，才能填充数据
                table.setItem(row, col, data_item)  # 填充数据
        v_layout.addWidget(table)

        self.setLayout(v_layout)  # 设置窗口布局

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MyWindow()
    window.show()
    sys.exit(app.exec_())


