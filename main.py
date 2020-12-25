import sys
import random
from PyQt5 import uic
from PyQt5.QtGui import QPainter, QColor
from PyQt5.QtWidgets import QApplication, QMainWindow


class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('UI.ui', self)
        self.do_paint = False
        self.pushButton.clicked.connect(self.paint)

    def paintEvent(self, event):
        if self.do_paint:
            qp = QPainter()
            qp.begin(self)
            self.draw_ell(qp)
            qp.end()

    def paint(self):
        self.do_paint = True
        self.repaint()

    def draw_ell(self, qp):
        qp.setPen(QColor(255, 255, 0))
        s = random.randrange(1, 200)
        qp.drawEllipse(random.randrange(1, 800 - s), random.randrange(1, 600 - s), s, s)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec_())