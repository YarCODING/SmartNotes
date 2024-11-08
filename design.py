from PyQt5 import QtCore, QtGui, QtWidgets
import json


class Ui_SmartNotes(object):
    def setupUi(self, SmartNotes):
        SmartNotes.setObjectName("SmartNotes")
        SmartNotes.resize(1296, 818)
        SmartNotes.setToolTipDuration(-1)
        SmartNotes.setStyleSheet("background-color: rgb(38,38,38)")
        SmartNotes.setDocumentMode(False)
        self.centralwidget = QtWidgets.QWidget(SmartNotes)
        self.centralwidget.setObjectName("centralwidget")
        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(460, 10, 831, 791))
        self.textEdit.setStyleSheet("background-color: rgb(30, 30, 30);\n"
"border-radius: 15px;\n"
"border: 2px solid;\n"
"border-color: rgb(54, 54, 54);\n"
"color: rgb(255, 255, 255)")
        self.textEdit.setObjectName("textEdit")
        self.notes_list_lb = QtWidgets.QLabel(self.centralwidget)
        self.notes_list_lb.setGeometry(QtCore.QRect(20, 10, 91, 31))
        self.notes_list_lb.setStyleSheet("background-color: rgb(30, 30, 30);\n"
"border-radius: 5px;\n"
"border: 1px solid;\n"
"border-color: rgb(54, 54, 54);\n"
"color: rgb(255, 255, 255)")
        self.notes_list_lb.setAlignment(QtCore.Qt.AlignCenter)
        self.notes_list_lb.setObjectName("notes_list_lb")
        self.notesList = QtWidgets.QListWidget(self.centralwidget)
        self.notesList.setGeometry(QtCore.QRect(10, 50, 431, 281))
        self.notesList.setStyleSheet("background-color: rgb(30, 30, 30);\n"
"border-radius: 15px;\n"
"border: 2px solid;\n"
"border-color: rgb(54, 54, 54);\n"
"color: rgb(255, 255, 255)")
        self.notesList.setObjectName("notesList")
        self.DelNote = QtWidgets.QPushButton(self.centralwidget)
        self.DelNote.setGeometry(QtCore.QRect(250, 340, 181, 23))
        self.DelNote.setStyleSheet("background-color: rgb(30, 30, 30);\n"
"border-radius: 20px;\n"
"border: 2px solid;\n"
"border-color: rgb(54, 54, 54);\n"
"color: rgb(255, 255, 255)")
        self.DelNote.setObjectName("DelNote")
        self.SaveNote = QtWidgets.QPushButton(self.centralwidget)
        self.SaveNote.setGeometry(QtCore.QRect(60, 370, 331, 21))
        self.SaveNote.setStyleSheet("background-color: rgb(30, 30, 30);\n"
"border-radius: 20px;\n"
"border: 2px solid;\n"
"border-color: rgb(54, 54, 54);\n"
"color: rgb(255, 255, 255)")
        self.SaveNote.setObjectName("SaveNote")
        self.AddNote = QtWidgets.QPushButton(self.centralwidget)
        self.AddNote.setGeometry(QtCore.QRect(30, 340, 191, 23))
        self.AddNote.setStyleSheet("background-color: rgb(30, 30, 30);\n"
"border-radius: 20px;\n"
"border: 2px solid;\n"
"border-color: rgb(54, 54, 54);\n"
"color: rgb(255, 255, 255)")
        self.AddNote.setObjectName("AddNote")
        self.tagList = QtWidgets.QListWidget(self.centralwidget)
        self.tagList.setGeometry(QtCore.QRect(10, 440, 431, 271))
        self.tagList.setStyleSheet("background-color: rgb(30, 30, 30);\n"
"border-radius: 15px;\n"
"border: 2px solid;\n"
"border-color: rgb(54, 54, 54);\n"
"color: rgb(255, 255, 255)")
        self.tagList.setObjectName("tagList")
        self.TagEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.TagEdit.setGeometry(QtCore.QRect(20, 720, 421, 20))
        self.TagEdit.setStyleSheet("background-color: rgb(30, 30, 30);\n"
"border-radius: 15px;\n"
"border: 2px solid;\n"
"border-color: rgb(54, 54, 54);\n"
"color: rgb(255, 255, 255)")
        self.TagEdit.setObjectName("TagEdit")
        self.DelTag = QtWidgets.QPushButton(self.centralwidget)
        self.DelTag.setGeometry(QtCore.QRect(250, 750, 191, 23))
        self.DelTag.setStyleSheet("background-color: rgb(30, 30, 30);\n"
"border-radius: 20px;\n"
"border: 2px solid;\n"
"border-color: rgb(54, 54, 54);\n"
"color: rgb(255, 255, 255)")
        self.DelTag.setObjectName("DelTag")
        self.FindNote = QtWidgets.QPushButton(self.centralwidget)
        self.FindNote.setGeometry(QtCore.QRect(60, 780, 331, 21))
        self.FindNote.setStyleSheet("background-color: rgb(30, 30, 30);\n"
"border-radius: 20px;\n"
"border: 2px solid;\n"
"border-color: rgb(54, 54, 54);\n"
"color: rgb(255, 255, 255)")
        self.FindNote.setObjectName("FindNote")
        self.AddTag = QtWidgets.QPushButton(self.centralwidget)
        self.AddTag.setGeometry(QtCore.QRect(20, 750, 191, 23))
        self.AddTag.setStyleSheet("background-color: rgb(30, 30, 30);\n"
"border-radius: 20px;\n"
"border: 2px solid;\n"
"border-color: rgb(54, 54, 54);\n"
"color: rgb(255, 255, 255)")
        self.AddTag.setObjectName("AddTag")
        self.Tag_List_lb = QtWidgets.QLabel(self.centralwidget)
        self.Tag_List_lb.setGeometry(QtCore.QRect(10, 400, 91, 31))
        self.Tag_List_lb.setStyleSheet("background-color: rgb(30, 30, 30);\n"
"border-radius: 5px;\n"
"border: 1px solid;\n"
"border-color: rgb(54, 54, 54);\n"
"color: rgb(255, 255, 255)")
        self.Tag_List_lb.setAlignment(QtCore.Qt.AlignCenter)
        self.Tag_List_lb.setObjectName("Tag_List_lb")
        SmartNotes.setCentralWidget(self.centralwidget)

        self.retranslateUi(SmartNotes)
        QtCore.QMetaObject.connectSlotsByName(SmartNotes)

    def retranslateUi(self, SmartNotes):
        _translate = QtCore.QCoreApplication.translate
        SmartNotes.setWindowTitle(_translate("SmartNotes", "MainWindow"))
        self.textEdit.setHtml(_translate("SmartNotes", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.notes_list_lb.setText(_translate("SmartNotes", "Список заміток"))
        self.DelNote.setText(_translate("SmartNotes", "Видалити замітку"))
        self.SaveNote.setText(_translate("SmartNotes", "Зберегти замітку"))
        self.AddNote.setText(_translate("SmartNotes", "Створити замітку"))
        self.TagEdit.setText(_translate("SmartNotes", "Введіть тег..."))
        self.DelTag.setText(_translate("SmartNotes", "відкріпити від замітки"))
        self.FindNote.setText(_translate("SmartNotes", "шукати замітки по тегу"))
        self.AddTag.setText(_translate("SmartNotes", "Додати до замітки"))
        self.Tag_List_lb.setText(_translate("SmartNotes", "Список тегів"))

        self.show_notes()
        self.notesList.itemClicked.connect(self.show)
        self.AddNote.clicked.connect(self.create)
        self.DelNote.clicked.connect(self.delete)
        self.SaveNote.clicked.connect(self.save)
        self.AddTag.clicked.connect(self.add_tag)
        self.DelTag.clicked.connect(self.del_tag)

    def show_notes(self):
        global data
        with open('notes.json', 'r+', encoding='utf-8') as file:
            try:
                data = json.load(file)
            except:
                data = {}

        self.notesList.addItems(data.keys())

    def show(self):
        t = self.notesList.currentItem().text()
        self.textEdit.setText(data[t]["текст"])
        self.tagList.clear()
        self.tagList.addItems(data[t]['теги'])
    def create(self):
        global note_name
        note_name, ok = QtWidgets.QInputDialog.getText(SmartNotes, "Додати замітку", "Назва")

        if note_name and ok:
             data[note_name] = {"текст" : "", "теги" : []}
             self.notesList.addItem(note_name)
        
    def delete(self):
        if self.notesList.currentItem():
            t = self.notesList.currentItem().text()
            del data[t]
            with open("notes.json", 'w', encoding='utf-8') as file:
                json.dump(data, file, sort_keys=True)
            self.notesList.clear()
            self.textEdit.clear()
            self.tagList.clear()
            self.notesList.addItems(data.keys())
    
    def save(self):
        if self.notesList.currentItem():
            t = self.textEdit.toPlainText()
            t2 = self.notesList.currentItem().text()
            data[t2]['текст'] = t
            with open("notes.json", 'w', encoding='utf-8') as file:
                json.dump(data, file, sort_keys=True)
    
    def add_tag(self):
        if self.notesList.currentItem():
            tag = self.TagEdit.text()
            if tag and not(tag in data[self.notesList.currentItem().text()]['теги']):
                data[self.notesList.currentItem().text()]['теги'].append(tag)
                self.tagList.addItem(tag)
                self.TagEdit.clear()
                with open("notes.json", 'w', encoding='utf-8') as file:
                    json.dump(data, file, sort_keys=True)

    def del_tag(self):
        if self.tagList.currentItem():
                selected_tag = self.tagList.currentItem().text()
                note_name = self.notesList.currentItem().text()
                data[note_name]['теги'].remove(selected_tag)
            
        with open("notes.json", 'w', encoding='utf-8') as file:
                json.dump(data, file, sort_keys=True)
            
        self.tagList.clear()
        self.tagList.addItems(data[self.notesList.currentItem().text()]['теги'])

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    SmartNotes = QtWidgets.QMainWindow()
    ui = Ui_SmartNotes()
    ui.setupUi(SmartNotes)
    SmartNotes.show()
    sys.exit(app.exec_())
