from PyQt6.QtWidgets import QApplication, QWidget, QGridLayout, QLabel, QLineEdit, QPushButton
import sys
from datetime import *

class CalculateAge(QWidget):

    def __init__(self):
        super().__init__()
        self.setWindowTitle("Age Calculator")
        grid = QGridLayout()
        #Create Widgets
        label1 = QLabel("Name :")
        self.name = QLineEdit()

        label2 = QLabel("DOB in MM/DD/YYYY :")
        self.dob = QLineEdit()

        button1 = QPushButton("Calculate")
        button1.clicked.connect(self.calculate_age)

        self.answer = QLabel("")

        # Add widgets to grid.
        grid.addWidget(label1, 0, 0)
        grid.addWidget(self.name, 0, 1)
        grid.addWidget(label2, 1, 0)
        grid.addWidget(self.dob, 1, 1)
        grid.addWidget(button1,2,0,1,2)
        grid.addWidget(self.answer,3,0,1,2)

        self.setLayout(grid)

    def calculate_age(self):
        cy = datetime.now().year
        dob = self.dob.text()
        by = datetime.strptime(dob,"%m/%d/%Y").date().year
        age = cy-by
        self.answer.setText(f"{self.name.text()}, your age is {age}")

app = QApplication(sys.argv)
age_calculator= CalculateAge()
age_calculator.show()
app.exec()
