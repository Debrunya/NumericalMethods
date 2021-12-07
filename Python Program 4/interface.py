# -*- coding: utf-8 -*-
"""
@author: znahar
"""


from PyQt5 import QtCore, QtWidgets

from PyQt5.QtGui import QIcon
from PyQt5.QtCore import Qt

import sample


class Window(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setWindowState(Qt.WindowMaximized)
        MainWindow.setWindowTitle("Нестационарное уравнение теплопроводности")
        MainWindow.setWindowIcon(QIcon('options\\favicon.ico'))
        
        
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        MainWindow.setCentralWidget(self.centralwidget)
        
        """------------------------------------------------Блок меню--------------------------------------------------"""
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1124, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        
        
        self.task_menu = QtWidgets.QAction("&О задаче")
        self.task_menu.setObjectName("task_menu")
        self.task_menu.triggered.connect(self.task)
        self.menubar.addAction(self.task_menu)
        
        
        self.method_menu = QtWidgets.QAction("&О методе")
        self.method_menu.setObjectName("method_menu")
        self.method_menu.triggered.connect(self.method)
        self.menubar.addAction(self.method_menu)
        
        
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        
        
        self.dialog_message = QtWidgets.QMessageBox()
        self.dialog_message.setStyleSheet("font: 75 14pt \"MS Shell Dlg 2\";")
        
        """---------------------------------------------Блок с таблицей----------------------------------------------"""
        self.table = QtWidgets.QTableWidget(self.centralwidget)
        self.table.setGeometry(QtCore.QRect(0, 210, 1920, 800))
        self.table.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.table.setVerticalScrollMode(QtWidgets.QAbstractItemView.ScrollPerItem)
        self.table.setShowGrid(True)
        self.table.setRowCount(500)
        self.table.setColumnCount(40)
        self.table.setObjectName("table")
        
        """-----------------------------------------------Блок кнопок------------------------------------------------"""
        self.run_button = QtWidgets.QPushButton(self.centralwidget)
        self.run_button.setGeometry(QtCore.QRect(80, 170, 130, 30))
        self.run_button.setStyleSheet("font: 75 11pt \"MS Shell Dlg 2\";\n"
"background-color: rgb(124, 255, 234);")
        self.run_button.setObjectName("run_button")
        self.run_button.setText("Рассчитать")
        self.run_button.clicked.connect(self.work)
        
        
        self.plot_button = QtWidgets.QPushButton(self.centralwidget)
        self.plot_button.setGeometry(QtCore.QRect(220, 170, 230, 30))
        self.plot_button.setStyleSheet("font: 75 11pt \"MS Shell Dlg 2\";\n"
"background-color: rgb(124, 255, 234);")
        self.plot_button.setObjectName("plot_button")
        self.plot_button.setText("Показать поверхность")
        self.plot_button.clicked.connect(self.show_surface)
        
        
        self.layer_button = QtWidgets.QPushButton(self.centralwidget)
        self.layer_button.setGeometry(QtCore.QRect(520, 170, 230, 30))
        self.layer_button.setStyleSheet("font: 75 11pt \"MS Shell Dlg 2\";\n"
"background-color: rgb(124, 255, 234);")
        self.layer_button.setObjectName("layer_button")
        self.layer_button.setText("Показать слой")
        self.layer_button.clicked.connect(self.show_layer)
        
        """-------------------------------------------Блок текстовых полей-------------------------------------------"""
        self.l_label = QtWidgets.QLabel(self.centralwidget)
        self.l_label.setGeometry(QtCore.QRect(520, 130, 50, 30))
        self.l_label.setStyleSheet("font: 75 14pt \"MS Shell Dlg 2\";")
        self.l_label.setObjectName("layer_label")
        self.l_label.setText("L = ")
        self.l_text = QtWidgets.QLineEdit(self.centralwidget)
        self.l_text.setGeometry(QtCore.QRect(570, 130, 180, 30))
        self.l_text.setObjectName("l_text")
        self.l_text.setText('0')
        
        
        self.l_label_hint = QtWidgets.QLabel(self.centralwidget)
        self.l_label_hint.setGeometry(QtCore.QRect(520, 90, 230, 30))
        self.l_label_hint.setStyleSheet("font: 75 12pt \"MS Shell Dlg 2\";")
        self.l_label_hint.setObjectName("l_label_hint")
        self.l_label_hint.setText("Введите номер слоя:")
        
        
        self.m_label = QtWidgets.QLabel(self.centralwidget)
        self.m_label.setGeometry(QtCore.QRect(20, 130, 50, 30))
        self.m_label.setStyleSheet("font: 75 14pt \"MS Shell Dlg 2\";")
        self.m_label.setObjectName("m_label")
        self.m_label.setText("m = ")
        self.m_text = QtWidgets.QLineEdit(self.centralwidget)
        self.m_text.setGeometry(QtCore.QRect(80, 130, 130, 30))
        self.m_text.setObjectName("m_text")
        self.m_text.setText('100000')
        
        
        self.n_label = QtWidgets.QLabel(self.centralwidget)
        self.n_label.setGeometry(QtCore.QRect(20, 50, 50, 30))
        self.n_label.setStyleSheet("font: 75 14pt \"MS Shell Dlg 2\";")
        self.n_label.setObjectName("n_label")
        self.n_label.setText("n =")
        self.n_text = QtWidgets.QLineEdit(self.centralwidget)
        self.n_text.setGeometry(QtCore.QRect(80, 50, 130, 30))
        self.n_text.setObjectName("n_text")
        self.n_text.setText('40')
        
        
        self.T_label = QtWidgets.QLabel(self.centralwidget)
        self.T_label.setGeometry(QtCore.QRect(20, 90, 50, 30))
        self.T_label.setStyleSheet("font: 75 14pt \"MS Shell Dlg 2\";")
        self.T_label.setObjectName("T_label")
        self.T_label.setText("T = ")
        self.T_text = QtWidgets.QLineEdit(self.centralwidget)
        self.T_text.setGeometry(QtCore.QRect(80, 90, 130, 30))
        self.T_text.setObjectName("T_text")
        self.T_text.setText('10.0')
        
        
        self.errlabel = QtWidgets.QLabel(self.centralwidget)
        self.errlabel.setGeometry(QtCore.QRect(220, 130, 350, 30))
        self.errlabel.setAcceptDrops(False)
        self.errlabel.setStyleSheet("font: 11pt \"MS Shell Dlg 2\";")
        self.errlabel.setObjectName("label")
        self.errlabel.setText("")
    
    
        self.parameters = QtWidgets.QLabel(self.centralwidget)
        self.parameters.setGeometry(QtCore.QRect(30, 10, 150, 30))
        self.parameters.setStyleSheet("font: 75 12pt \"MS Shell Dlg 2\";")
        self.parameters.setObjectName("parameters")
        self.parameters.setText("Параметры метода:")
        
        """-------------------------------------------Блок справки-------------------------------------------"""
        reference = QtWidgets.QWidget(MainWindow)
        reference.setGeometry(QtCore.QRect(900, 30, 500, 200))
        referenceQVBox = QtWidgets.QVBoxLayout()

        label_at = QtWidgets.QLabel('Справка')
        label_at.setAlignment(Qt.AlignCenter)
        self.textarea = QtWidgets.QPlainTextEdit()
        self.textarea.setFrameStyle(QtWidgets.QFrame.NoFrame)
        self.textarea.setReadOnly(True)

        referenceQVBox.addWidget(label_at)
        referenceQVBox.addWidget(self.textarea)
        reference.setLayout(referenceQVBox)

        QtCore.QMetaObject.connectSlotsByName(MainWindow)
    
    
    def task(self):
        message = '<p>Уравнение теплопроводности на отрезке<br />x &isin; [0, 1] для отрезка по времени t &isin; [0, T] \
            имеет вид:<br />u&prime;<sub>t&nbsp;</sub>= a<sup>2</sup>u&prime;&prime;<sub>xx</sub> + g(x, t), x &isin; [0, 1], t &isin; [0, T]<br />\
            где a<sup>2</sup>&nbsp;= 3, g(x, t) = t*cos(<span>&pi;x</span>)/(t+1),<br />u(x, t) &ndash; искомая функция температуры.<br />\
            Задано начальное условие: u(x, 0) = 1-x<sup>2</sup>.<br />\
            Для x = 0 задано граничное условие 1-го рода:&nbsp;u(0, t) = cos(t).<br />\
            Для x = 1 задано граничное условие 1-го рода:&nbsp;u(1, t) = sin(4t).</p>'

        self.dialog_message.setWindowTitle('Условие задачи')
        self.dialog_message.setWindowIcon(QIcon('options\\favicon.ico'))
        self.dialog_message.setText(message)
        self.dialog_message.exec()
    
    
    def method(self):
        message = '<p><b>Явная схема решения нестационарного уравнения теплопроводности</b></p>' \
                  '' \
                  '<p>v<sub>i</sub> <sub>j+1</sub> = v<sub>i</sub> <sub>j</sub> + {&#947;<sup>2</sup> * [v<sub>xx</sub>]<sub>i</sub> <sub>j</sub> + \
                      g(x<sub>i</sub>, y<sub>j</sub>)} * &#964;</p>' \
                  '' \
                  '<p>где [v<sub>xx</sub>]<sub>i</sub> <sub>j</sub> = (v<sub>i-1</sub> <sub>j</sub> - 2 * v<sub>i</sub><sub>j</sub> + \
                      v<sub>i+1</sub> <sub>j</sub>) / h<sup>2</sup> </p>' \
                  '' \
                  '<p>i = 1,2,3...n-1; j = 0,1,2...m-1</p>' \
                  '' \
                  '<p>v<sub>i</sub><sub>0</sub> = &#966;<sub>i</sub>, i = 0,1,2...n</p>' \
                  '' \
                  '<p>v<sub>0</sub><sub>j</sub> = &#956;<sub>1</sub><sub>j</sub>, j = 1,2,3...m</p>' \
                  '' \
                  '<p>v<sub>n</sub><sub>j</sub> = &#956;<sub>2</sub><sub>j</sub>, j = 1,2,3...m</p>' \

        self.dialog_message.setWindowTitle('Метод')
        self.dialog_message.setWindowIcon(QIcon('options\\favicon.ico'))
        self.dialog_message.setText(message)
        self.dialog_message.exec()
        
    
    def create_reference(self, data):
        message = '<p>Нестационарное уравнение теплопроводности</p>' \
                  f'<p>n = {int(self.n_text.text())}</p>' \
                  f'<p>x = 1</p>' \
                  f'<p>h = {data["h"]}</p>' \
                  f'<p>m = {int(self.m_text.text())}</p>' \
                  f'<p>T = {float(self.T_text.text()):.3f}</p>' \
                  f'<p>tau = {data["tau"]}</p>' \

        return message
    
        
    def data_to_table(self, data):
        
        def create_item(row: int, col: int, text: str):
            item = QtWidgets.QTableWidgetItem(str(text))
            item.setFlags(Qt.ItemIsEnabled)
            self.table.setItem(row, col, item)

        self.table.setRowCount(data['m']//100+1)
        self.table.setColumnCount(data['n']+1)
        
        zgrid = data['zgrid'].transpose()

        for i in range(data['n']+1):
            header_item = QtWidgets.QTableWidgetItem(f'{i}, {i*data["h"]:.4f}')
            self.table.setHorizontalHeaderItem(i, header_item)
            for j in range(data['m']//100+1):
                header_item = QtWidgets.QTableWidgetItem(f'{j*100}, {j*100*data["tau"]:.4f}')
                self.table.setVerticalHeaderItem(j, header_item)
                create_item(j, i, str(f'{zgrid[i][j*100]}'))
    
    
    def error_input(self, message):
        self.dialog_message.setWindowTitle('Ошибка')
        self.dialog_message.setWindowIcon(QIcon('options\\favicon.ico'))
        self.dialog_message.setText(message)
        self.dialog_message.exec()
    
    
    def except_errors(self) -> bool:
        error = False
        
        try:
            if float(self.T_text.text()) <= 0.0:
                error = True
                self.error_input('Значение параметра времени должно быть положительным')
            if int(self.m_text.text()) <= 0:
                error = True
                self.error_input('Значение параметра m должно быть положительным')
            if int(self.n_text.text()) <= 0:
                error = True
                self.error_input('Значение параметра n должно быть положительным')
            if (int(self.l_text.text()) < 0) or (int(self.l_text.text()) > int(self.m_text.text())):
                error = True
                self.error_input('Значение параметра L должно быть от 0 до m')
            
        except ValueError:
            error = True
            self.error_input('Входные данные, за исключением времени, должны быть быть целыми')
            return error
        
        data = {'n': self.n_text.text(),
                'm': self.m_text.text(),
                'T': self.T_text.text()}
        message = sample.check_grid(data)
        
        try:
            if (message['error'] != '-1'):
                error = True
                self.error_input(message['error'])
                self.errlabel.setText(f'Параметр m должен быть больше {message["norm_m"]}')
                
        except Exception:
            error = True
            self.error_input('Проверьте корректность параметра m')

        return error


    def show_surface(self):
        error = self.except_errors()        

        if not error:
            self.errlabel.setText('')
            
            data = {'n': self.n_text.text(),
                    'm': self.m_text.text(),
                    'T': self.T_text.text()}
            
            calcdata = sample.calculation(data)
            del data
            
            sample.plot_figure(calcdata)
            self.textarea.setPlainText('')
            self.textarea.appendHtml(self.create_reference(calcdata))
        
        return

    
    def show_layer(self):
        error = self.except_errors()        

        if not error:
            self.errlabel.setText('')
            
            data = {'n': self.n_text.text(),
                    'm': self.m_text.text(),
                    'T': self.T_text.text()}
            
            calcdata = sample.calculation(data)
            del data
            
            data = {'zgrid': calcdata['zgrid'],
                    'xgrid': calcdata['xgrid'],
                    'n': calcdata['n'],
                    'tau': calcdata['tau'],
                    'l': int(self.l_text.text())}
            
            sample.plot_layer(data)
            self.textarea.setPlainText('')
            self.textarea.appendHtml(self.create_reference(calcdata))
        
        return
    

    def work(self):
        error = self.except_errors()        

        if not error:
            self.errlabel.setText('')
            
            data = {'n': self.n_text.text(),
                    'm': self.m_text.text(),
                    'T': self.T_text.text()}
            
            calcdata = sample.calculation(data)
            del data
            
            self.data_to_table(calcdata)
            self.textarea.setPlainText('')
            self.textarea.appendHtml(self.create_reference(calcdata))
            
        return
    
    
    