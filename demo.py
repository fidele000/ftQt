from PyQt5.QtCore import QPropertyAnimation,Qt
from PyQt5.QtWidgets import QApplication,QPushButton,QWidget
from ftQt.layout import Row,Column
#

class Window(QWidget):

    def __init__(self, *args, **kwargs):
        super(Window, self).__init__(*args, **kwargs)
        self.resize(400, 400)
        column=Column()
        row=Row(self)
        row.add(QPushButton("Yooo"))
        column.add(QPushButton("Column"))
        column.add(QPushButton("Column"))
        column.tobottom()
        row.add(column)


if __name__ == '__main__':
    import sys

    app = QApplication(sys.argv)
    w = Window()
    w.show()
    sys.exit(app.exec_())
