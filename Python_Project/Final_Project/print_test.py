from PyQt5 import QtCore, QtGui, QtWidgets

def __init__(self):
        QWidget.__init__(self)
        self.layout = QGridLayout(self)
        self.viewer = None
        
        self.x_label = QLabel("X axis:")
        self.x_chooser = QComboBox()
        self.x_chooser.setEditable(True)
        self.y_label = QLabel("Y axis:")
        self.y_chooser = QComboBox()
        self.y_chooser.setEditable(True)
        # TODO: add completers
        self.nav_reset = QPushButton("&Reset view")

        self.layout.addWidget(self.x_label, 1, 0)
        self.layout.addWidget(self.x_chooser, 1, 1)
        self.layout.addWidget(self.y_label, 1, 3)
        self.layout.addWidget(self.y_chooser, 1, 4)
        self.layout.addWidget(self.nav_reset, 1, 6)
        self.layout.setColumnStretch(1, 1)
        self.layout.setColumnStretch(4, 1)
        self.layout.setRowStretch(0, 1)

        self.nav_reset.clicked.connect(self.reset_view)
        self.x_chooser.currentIndexChanged['QString'].connect(self.set_x_from_string)
        self.y_chooser.currentIndexChanged['QString'].connect(self.set_y_from_string)
    
        self.x_chooser.activated['QString'].connect(self.set_x_from_string)
