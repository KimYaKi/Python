import pymysql
from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(405, 264)
        self.ok_calcel = QtWidgets.QDialogButtonBox(Dialog)
        self.ok_calcel.setGeometry(QtCore.QRect(90, 90, 201, 31))
        self.ok_calcel.setOrientation(QtCore.Qt.Horizontal)
        self.ok_calcel.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.ok_calcel.setObjectName("ok_calcel")
        self.listWidget = QtWidgets.QListWidget(Dialog)
        self.listWidget.setGeometry(QtCore.QRect(10, 10, 381, 241))
        self.listWidget.setObjectName("listWidget")
        self.manu_button = QtWidgets.QToolButton(Dialog)
        self.manu_button.setGeometry(QtCore.QRect(20, 150, 121, 31))
        self.manu_button.setObjectName("manu_button")
        self.name_label = QtWidgets.QLabel(Dialog)
        self.name_label.setGeometry(QtCore.QRect(100, 30, 51, 31))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.name_label.setFont(font)
        self.name_label.setObjectName("name_label")
        self.insert_button = QtWidgets.QToolButton(Dialog)
        self.insert_button.setGeometry(QtCore.QRect(150, 150, 111, 31))
        self.insert_button.setObjectName("insert_button")
        self.user_info_button = QtWidgets.QToolButton(Dialog)
        self.user_info_button.setGeometry(QtCore.QRect(270, 150, 101, 31))
        self.user_info_button.setObjectName("user_info_button")
        self.name_edit = QtWidgets.QLineEdit(Dialog)
        self.name_edit.setGeometry(QtCore.QRect(170, 30, 120, 31))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.name_edit.setFont(font)
        self.name_edit.setMaxLength(8)
        self.name_edit.setObjectName("name_edit")
        self.listWidget.raise_()
        self.manu_button.raise_()
        self.ok_calcel.raise_()
        self.name_label.raise_()
        self.insert_button.raise_()
        self.user_info_button.raise_()
        self.name_edit.raise_()

        self.retranslateUi(Dialog)
        self.ok_calcel.accepted.connect(Dialog.accept)
        self.ok_calcel.rejected.connect(Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "이름입력"))
        self.manu_button.setText(_translate("Dialog", "제조사 정보 출력"))
        self.name_label.setText(_translate("Dialog", "이름"))
        self.insert_button.setText(_translate("Dialog", "사용자 정보 입력"))
        self.user_info_button.setText(_translate("Dialog", "모든 사용자 출력"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

