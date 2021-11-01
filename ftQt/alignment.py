from PyQt5.QtCore import Qt

class Align(Qt):

    def __init__(self,*args,**kwargs):
        super(Align, self).__init__(*args,**kwargs)

    def tocenter(self):
        return Qt.AlignCenter

    def toleft(self):
        self.setAlignment(Qt.AlignLeft)

    def toright(self):
        self.setAlignment(Qt.AlignRight)

    def totop(self):
        self.setAlignment(Qt.AlignTop)

    def tobottom(self):
        self.setAlignment(Qt.AlignBottom)

    def __str__(self):
        return 'Align'
