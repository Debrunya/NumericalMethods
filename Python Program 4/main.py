# -*- coding: utf-8 -*-
"""
@author: znahar
"""


import os
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow

from interface import Window


def _cls():
    os.system('cls' if os.name == 'nt' else 'clear')


def main():
    _cls()
    
    app = QApplication(sys.argv)
    MainWindow = QMainWindow()
    ui = Window()
    ui.setupUi(MainWindow)
    MainWindow.show()
    
    app.setQuitOnLastWindowClosed(True)
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
