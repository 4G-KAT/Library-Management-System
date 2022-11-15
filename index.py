from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.uic import loadUiType
import mysql.connector as ConDb
import sys

ui, _ = loadUiType('library.ui')

class MainApp(QMainWindow, ui):
    def __init__(self):
        QMainWindow.__init__(self)
        self.setupUi(self)
        self.Handle_Ui_Changes()
        self.Handle_Buttons()

    def Handle_Ui_Changes(self):
        self.Hide_Themes()
        self.tabWidget.tabBar().setVisible(False)

        self.Show_Category()
        self.Show_Author()
        self.Show_Publisher()

        self.ComboB_Show_Category()
        self.ComboB_Show_Author()
        self.ComboB_Show_Publisher()

    def Handle_Buttons(self):
        self.pushButton_5.clicked.connect(self.Show_Themes)
        self.pushButton_22.clicked.connect(self.Hide_Themes)

        self.pushButton.clicked.connect(self.Open_Day_To_Day_Tab)
        self.pushButton_2.clicked.connect(self.Open_Books_Tab)
        self.pushButton_3.clicked.connect(self.Open_Users_Tab)
        self.pushButton_4.clicked.connect(self.Open_Settings_Tab)

        self.pushButton_15.clicked.connect(self.Add_Category)
        self.pushButton_16.clicked.connect(self.Add_Author)
        self.pushButton_17.clicked.connect(self.Add_Publisher)

        self.pushButton_6.clicked.connect(self.Add_New_Book)



    def Show_Themes(self):
        self.groupBox_3.show()

    def Hide_Themes(self):
        self.groupBox_3.hide()

    ########################################
    ########Opening Tabs####################

    def Open_Day_To_Day_Tab(self):
        self.tabWidget.setCurrentIndex(0)

    def Open_Books_Tab(self):
        self.tabWidget.setCurrentIndex(1)

    def Open_Users_Tab(self):
        self.tabWidget.setCurrentIndex(2)

    def Open_Settings_Tab(self):
        self.tabWidget.setCurrentIndex(3)

    ########################################
    ############# Books Tab#################

    def Add_New_Book(self):
        self.db = ConDb.connect(
           host="localhost",
           user="root",
           passwd="Serendip!ty342:)",
           database="library_database.sql"
        )
        self.cur = self.db.cursor()

        book_title = self.lineEdit_5.text()
        book_description = self.textEdit.toPlainText()
        book_code = self.lineEdit_3.text()
        book_category = self.comboBox_6.currentIndex()
        book_author = self.comboBox_5.currentIndex()
        book_publisher = self.comboBox_2.currentIndex()
        book_price = self.lineEdit_4.text()

        self.cur.execute('''
            INSERT INTO book (book_name,book_description,book_code,book_category,book_author,book_publisher,book_price)
            VALUES (%s, %s, %s, %s, %s, %s, %s)
            ''',(book_title, book_description, book_code, book_category, book_author, book_publisher, book_price))
        self.db.commit()
        self.statusBar().showMessage("New Book Added")

        self.lineEdit_5.setText('')
        self.lineEdit_3.setText('')
        self.lineEdit_4.setText('')
        self.textEdit.setPainText('')
        self.comboBox_6.setCurrentIndex(0)
        self.comboBox_5.setCurrentIndex(0)

    def Search_Books(self):
        pass

    def Edit_Books(self):
        pass

    def Delete_Books(self):
        pass

    ########################################
    ############# Users Tab#################

    def Add_New_User(self):
        pass
    def Login(self):
        pass
    def Edit_User(self):
        pass

    ########################################
    ############# Settings Tab#################

    def Add_Category(self):
        self.db = ConDb.connect(
            host="localhost",
            user="root",
            passwd="Serendip!ty342:)",
            database="library"
        )
        self.cur = self.db.cursor()

        category_name = self.lineEdit_21.text()

        self.cur.execute('''
                INSERT INTO categories (category_name) VALUES (%s)
            ''',(category_name,))

        self.db.commit()
        self.lineEdit_21.setText('')
        self.statusBar().showMessage("New Category Added")
        self.Show_Category()
        self.ComboB_Show_Category()

    def Show_Category(self):
        self.db = ConDb.connect(
            host="localhost",
            user="root",
            passwd="Serendip!ty342:)",
            database="library"
        )
        self.cur = self.db.cursor()

        self.cur.execute('''SELECT category_name FROM categories''')
        data = self.cur.fetchall()

        if data:
            self.tableWidget.setRowCount(0)
            self.tableWidget.insertRow(0)
            for row, form in enumerate(data):
                for column, item in enumerate(form):
                    self.tableWidget.setItem(row, column, QTableWidgetItem(str(item)))
                    column += 1

                row_position = self.tableWidget.rowCount()
                self.tableWidget.insertRow(row_position)

    def Add_Author(self):
        self.db = ConDb.connect(
            host="localhost",
            user="root",
            passwd="Serendip!ty342:)",
            database="library"
        )
        self.cur = self.db.cursor()

        author_name = self.lineEdit_22.text()

        self.cur.execute('''
                               INSERT INTO authors (author_name) VALUES (%s)
                           ''', (author_name,))
        self.db.commit()
        self.lineEdit_22.setText('')
        self.statusBar().showMessage("New Author Added")
        self.Show_Author()
        self.ComboB_Show_Author()

    def Show_Author(self):
        self.db = ConDb.connect(
            host="localhost",
            user="root",
            passwd="Serendip!ty342:)",
            database="library"
        )
        self.cur = self.db.cursor()

        self.cur.execute('''SELECT author_name FROM authors''')
        data = self.cur.fetchall()

        if data:
            self.tableWidget_3.setRowCount(0)
            self.tableWidget_3.insertRow(0)
            for row, form in enumerate(data):
                for column, item in enumerate(form):
                    self.tableWidget_3.setItem(row, column, QTableWidgetItem(str(item)))
                    column += 1

                row_position = self.tableWidget_3.rowCount()
                self.tableWidget_3.insertRow(row_position)

    def Add_Publisher(self):
        self.db = ConDb.connect(
            host="localhost",
            user="root",
            passwd="Serendip!ty342:)",
            database="library"
        )
        self.cur = self.db.cursor()

        publisher_name = self.lineEdit_23.text()

        self.cur.execute('''
                        INSERT INTO publishers (publisher_name) VALUES (%s)
                    ''', (publisher_name,))
        self.db.commit()
        self.lineEdit_23.setText('')
        self.statusBar().showMessage("New Publisher Added")
        self.Show_Publisher()
        self.ComboB_Show_Publisher()

    def Show_Publisher(self):
        self.db = ConDb.connect(
            host="localhost",
            user="root",
            passwd="Serendip!ty342:)",
            database="library"
        )
        self.cur = self.db.cursor()

        self.cur.execute('''SELECT publisher_name FROM publishers''')
        data = self.cur.fetchall()

        if data:
            self.tableWidget_4.setRowCount(0)
            self.tableWidget_4.insertRow(0)
            for row, form in enumerate(data):
                for column, item in enumerate(form):
                    self.tableWidget_4.setItem(row, column, QTableWidgetItem(str(item)))
                    column += 1

                row_position = self.tableWidget_4.rowCount()
                self.tableWidget_4.insertRow(row_position)

    def ComboB_Show_Category(self):
        self.db = ConDb.connect(
            host='localhost',
            user='root',
            passwd='Serendip!ty342:)',
            database='library'
        )
        self.cur = self.db.cursor()

        self.cur.execute('''SELECT category_name FROM categories''')
        data = self.cur.fetchall()
        self.comboBox_6.clear()

        for category in data:
            self.comboBox_6.addItem(category[0])

    def ComboB_Show_Author(self):
        self.db = ConDb.connect(
            host='localhost',
            user='root',
            passwd='Serendip!ty342:)',
            database='library'
        )
        self.cur = self.db.cursor()

        self.cur.execute('''SELECT author_name FROM authors''')
        data = self.cur.fetchall()
        self.comboBox_5.clear()

        for author in data:
            self.comboBox_5.addItem(author[0])

    def ComboB_Show_Publisher(self):
        self.db = ConDb.connect(
            host='localhost',
            user='root',
            passwd='Serendip!ty342:)',
            database='library'
        )
        self.cur = self.db.cursor()

        self.cur.execute('''SELECT publisher_name FROM publishers''')
        data = self.cur.fetchall()
        self.comboBox_2.clear()

        for publisher in data:
            self.comboBox_2.addItem(publisher[0])


def main():
    app = QApplication(sys.argv)
    window = MainApp()
    window.show()
    exit(app.exec_())

if __name__ == '__main__':
    main()
