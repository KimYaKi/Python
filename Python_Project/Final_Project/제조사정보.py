# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\rlawl\Desktop\제조사정보.ui'
#
# Created by: PyQt5 UI code generator 5.9
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Frame(object):
    def setupUi(self, Frame):
        Frame.setObjectName("Frame")
        Frame.resize(860, 191)
        Frame.setInputMethodHints(QtCore.Qt.ImhHiddenText)
        Frame.setFrameShape(QtWidgets.QFrame.Box)
        Frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.ok_cancel = QtWidgets.QDialogButtonBox(Frame)
        self.ok_cancel.setGeometry(QtCore.QRect(320, 130, 193, 28))
        self.ok_cancel.setInputMethodHints(QtCore.Qt.ImhSensitiveData)
        self.ok_cancel.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.ok_cancel.setObjectName("ok_cancel")
        self.combo = QtWidgets.QComboBox(Frame)
        self.combo.setGeometry(QtCore.QRect(20, 70, 120, 30))
        font = QtGui.QFont()
        font.setStrikeOut(False)
        self.combo.setFont(font)
        self.combo.setContextMenuPolicy(QtCore.Qt.PreventContextMenu)
        self.combo.setAcceptDrops(False)
        self.combo.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.combo.setInputMethodHints(QtCore.Qt.ImhSensitiveData)
        self.combo.setInsertPolicy(QtWidgets.QComboBox.InsertAtTop)
        self.combo.setModelColumn(0)
        self.combo.setObjectName("combo")
        self.combo.addItem("")
        self.name_view = QtWidgets.QTableView(Frame)
        self.name_view.setGeometry(QtCore.QRect(170, 70, 180, 30))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.name_view.setFont(font)
        self.name_view.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.name_view.setDefaultDropAction(QtCore.Qt.IgnoreAction)
        self.name_view.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectColumns)
        self.name_view.setObjectName("name_view")
        self.page_view = QtWidgets.QTableView(Frame)
        self.page_view.setGeometry(QtCore.QRect(370, 70, 271, 30))
        self.page_view.setObjectName("page_view")
        self.hp_view = QtWidgets.QTableView(Frame)
        self.hp_view.setGeometry(QtCore.QRect(660, 70, 150, 30))
        self.hp_view.setObjectName("hp_view")
        self.manu_name = QtWidgets.QLabel(Frame)
        self.manu_name.setGeometry(QtCore.QRect(215, 30, 90, 20))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.manu_name.setFont(font)
        self.manu_name.setObjectName("manu_name")
        self.manu_addr = QtWidgets.QLabel(Frame)
        self.manu_addr.setGeometry(QtCore.QRect(460, 30, 90, 20))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.manu_addr.setFont(font)
        self.manu_addr.setObjectName("manu_addr")
        self.manu_hp = QtWidgets.QLabel(Frame)
        self.manu_hp.setGeometry(QtCore.QRect(690, 30, 90, 20))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.manu_hp.setFont(font)
        self.manu_hp.setObjectName("manu_hp")

        self.retranslateUi(Frame)
        self.combo.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Frame)

    def retranslateUi(self, Frame):
        _translate = QtCore.QCoreApplication.translate
        Frame.setWindowTitle(_translate("Frame", "Frame"))
        self.combo.setItemText(0, _translate("Frame", "--제조사 코드--"))
        self.manu_name.setText(_translate("Frame", "제조사 이름"))
        self.manu_addr.setText(_translate("Frame", "제조사 주소"))
        self.manu_hp.setText(_translate("Frame", "제조사 번호"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Frame = QtWidgets.QFrame()
    ui = Ui_Frame()
    ui.setupUi(Frame)
    Frame.show()
    sys.exit(app.exec_())

