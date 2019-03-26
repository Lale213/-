import sys  # sys нужен для передачи argv в QApplication
import os  # Отсюда нам понадобятся методы для отображения содержимого директорий
from PyQt5 import QtWidgets
import First
import time

def main():
    app = QtWidgets.QApplication(sys.argv)  # Новый экземпляр QApplication
    window = First.Start()  # Создаём объект класса ExampleApp
    window.show()  # Показываем окно
    app.exec_()  # и запускаем приложение


if __name__ == '__main__':  # Если мы запускаем файл напрямую, а не импортируем
    main()  # то запускаем функцию main()