#!/usr/bin/python3
# -*- coding: utf-8 -*-
import sys, os
from PySide2.QtWidgets import*
from PySide2.QtGui import*
from PySide2 import QtCore
import PySide2

def get_img_path():
    here = os.path.dirname(os.path.abspath(__file__))
    parent = os.path.dirname(here)
    return os.path.join(parent, 'res', 'img.png')

application = QApplication(sys.argv)
window = QWidget()
window.setWindowTitle("QScrollArea")

picture = QPixmap(get_img_path())
picture = picture.scaledToHeight(picture.height() * 20, QtCore.Qt.FastTransformation)

#label = QLabel(window)
label = QLabel()
label.setPixmap(picture)
label.setGeometry(QtCore.QRect(0, 0, picture.width(), picture.height()))
#scroller = QScrollArea(window)
scroller = QScrollArea()
scroller.setWidget(label)

layout = QGridLayout()
layout.addWidget(scroller, 0, 0)
window.setLayout(layout)

window.resize(picture.width(), picture.height())
window.show()

sys.exit(application.exec_())
