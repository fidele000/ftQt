from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QVBoxLayout,QHBoxLayout
from ftQt.alignment import Align

class Column(QVBoxLayout):

    def __init__(self,*args,**kwargs):
        super(Column, self).__init__(*args,**kwargs)

    def add(self,widget):
        try:
            self.addWidget(widget)
        except Exception as e:
            self.addLayout(widget)

    def tocenter(self):
        return self.setAlignment(Qt.AlignCenter)

    def toleft(self):
        self.setAlignment(Qt.AlignLeft)

    def toright(self):
        self.setAlignment(Qt.AlignRight)

    def totop(self):
        self.setAlignment(Qt.AlignTop)

    def tobottom(self):
        self.setAlignment(Qt.AlignBottom)

    def size(self,width,height):
        pass

class Row(QHBoxLayout):

    def __init__(self,*args,**kwargs):
        super(Row, self).__init__(*args,**kwargs)

    def add(self,widget):
        try:
            self.addWidget(widget)
        except Exception as e:
            self.addLayout(widget)

    def tocenter(self):
        return self.setAlignment(Qt.AlignCenter)

    def toleft(self):
        self.setAlignment(Qt.AlignLeft)

    def toright(self):
        self.setAlignment(Qt.AlignRight)

    def totop(self):
        self.setAlignment(Qt.AlignTop)

    def tobottom(self):
        self.setAlignment(Qt.AlignBottom)

    def __str__(self):
        return 'Column'
