import sys
import random
from PyQt5.QtGui import QPainter, QColor
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(300, 300, 500, 500)
        self.setWindowTitle('Случайные окружности')
        self.pushButton = QPushButton('Добавить', self)
        self.pushButton.resize(100, 30)
        self.pushButton.move(200, 400)


class MyWidget(MainWindow):
    def __init__(self):
        super().__init__()
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
        qp.setPen(QColor(random.randrange(0, 255),
                         random.randrange(0, 255), random.randrange(0, 255)))
        s = random.randrange(1, 250)
        qp.drawEllipse(random.randrange(1, 500 - s), random.randrange(1, 500 - s), s, s)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec_())
