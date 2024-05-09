from PyQt6.QtWidgets import *
from gui_calculator import *


class Logic(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushButton_0.clicked.connect(lambda: self.numbers("0"))
        self.pushButton_1.clicked.connect(lambda: self.numbers("1"))
        self.pushButton_2.clicked.connect(lambda: self.numbers("2"))
        self.pushButton_3.clicked.connect(lambda: self.numbers("3"))
        self.pushButton_4.clicked.connect(lambda: self.numbers("4"))
        self.pushButton_5.clicked.connect(lambda: self.numbers("5"))
        self.pushButton_6.clicked.connect(lambda: self.numbers("6"))
        self.pushButton_7.clicked.connect(lambda: self.numbers("7"))
        self.pushButton_8.clicked.connect(lambda: self.numbers("8"))
        self.pushButton_9.clicked.connect(lambda: self.numbers("9"))
        self.pushButton_Add.clicked.connect(lambda: self.numbers("+"))
        self.pushButton_Subtract.clicked.connect(lambda: self.numbers("-"))
        self.pushButton_Multiply.clicked.connect(lambda: self.numbers("*"))
        self.pushButton_Divide.clicked.connect(lambda: self.numbers("/"))
        self.pushButton_Neg.clicked.connect(lambda: self.pos_neg())
        self.pushButton_Dot.clicked.connect(lambda: self.decimal())
        self.pushButton_Equals.clicked.connect(lambda: self.answer())
        self.pushButton_Equals.clicked.connect(lambda: self.cal_function())
        self.pushButton_Equals.clicked.connect(lambda: self.equals("="))
        self.pushButton_Advance.clicked.connect(lambda: self.function())
        self.pushButton_Clear.clicked.connect(lambda: self.calculate("C"))
        self.pushButton_Back_Space.clicked.connect(lambda: self.delete())
        self.pushButton_Square.hide()
        self.pushButton_Triangle.hide()
        self.pushButton_Rectangle.hide()
        self.pushButton_Circle.hide()
        self.label_Radius.hide()
        self.label_Width.hide()
        self.label_Length.hide()
        self.label_Side.hide()
        self.label_Side_1.hide()
        self.label_Side_2.hide()
        self.label_Side_3.hide()
        self.label_Base.hide()
        self.label_Height.hide()
        self.lineEdit_Num1.hide()
        self.lineEdit_Num2.hide()
        self.lineEdit_Num3.hide()
        self.radioButton_Circumference.hide()
        self.radioButton_Area_Triangle.hide()
        self.radioButton_Area_Rectangle.hide()
        self.radioButton_Area_Circle.hide()
        self.radioButton_Area_Square.hide()
        self.radioButton_Perimeter_Square.hide()
        self.radioButton_Perimeter_Rectangle.hide()
        self.radioButton_Perimeter_Triangle.hide()
        self.label_Error.hide()
        self.label_Circle_Area.hide()
        self.label_Circle_Circumference.hide()
        self.label_Square_Area.hide()
        self.label_Square_Perimeter.hide()
        self.label_Rectangle_Area.hide()
        self.label_Rectangle_Perimeter.hide()
        self.label_Triangle_Area.hide()
        self.label_Triangle_Perimeter.hide()

    def calculate(self, pressed):
        if pressed == "C":
            self.outputLabel.setText("0")

    def numbers(self, pressed):
        if self.outputLabel.text() == "0":
            self.outputLabel.setText("")

        if len(self.outputLabel.text()) <= 11:
            self.outputLabel.setText(f'{self.outputLabel.text()[:11]}{pressed}')

    def equals(self, pressed):
        if pressed == "=":
            if pressed == "1":
                self.outputLabel.setText("")

    def decimal(self):
        screen = self.outputLabel.text()
        possible_chars_list = ['*', '/', '-', '+']
        is_valid = True
        for i in screen:
            if i in possible_chars_list:
                is_valid = True
            elif i == ".":
                is_valid = False
        if is_valid:
            self.outputLabel.setText(f'{screen}.')

    def delete(self):
        screen = self.outputLabel.text()
        screen = screen[:-1]
        self.outputLabel.setText(screen)

    def pos_neg(self):
        screen = self.outputLabel.text()
        if "-" == screen[0]:
            screen = screen[1:]
            self.outputLabel.setText(screen)
        else:
            self.outputLabel.setText(f'-{screen}')

    def answer(self):
        screen = self.outputLabel.text()
        answer = eval(screen)
        self.label_Equation.setText(f'{str(screen)}=')
        self.outputLabel.setText(str(answer)[:12])

    def function(self):
        if self.pushButton_Circle.isHidden():
            self.pushButton_Circle.show()
            self.pushButton_Square.show()
            self.pushButton_Triangle.show()
            self.pushButton_Rectangle.show()
            self.pushButton_Circle.clicked.connect(lambda: self.circle())
            self.pushButton_Square.clicked.connect(lambda: self.square())
            self.pushButton_Rectangle.clicked.connect(lambda: self.rectangle())
            self.pushButton_Triangle.clicked.connect(lambda: self.triangle())
        else:
            self.pushButton_Circle.hide()
            self.pushButton_Square.hide()
            self.pushButton_Triangle.hide()
            self.pushButton_Rectangle.hide()
            self.radioButton_Circumference.hide()
            self.radioButton_Area_Triangle.hide()
            self.radioButton_Area_Circle.hide()
            self.radioButton_Area_Square.hide()
            self.radioButton_Perimeter_Square.hide()
            self.radioButton_Perimeter_Rectangle.hide()
            self.radioButton_Perimeter_Triangle.hide()
            self.label_Radius.hide()
            self.label_Width.hide()
            self.label_Length.hide()
            self.label_Side.hide()
            self.label_Side_1.hide()
            self.label_Side_2.hide()
            self.label_Side_3.hide()
            self.lineEdit_Num1.hide()
            self.lineEdit_Num2.hide()
            self.lineEdit_Num3.hide()
            self.radioButton_Area_Rectangle.hide()
            self.label_Base.hide()
            self.label_Height.hide()
            self.label_Error.hide()
            self.label_Circle_Area.hide()
            self.label_Circle_Circumference.hide()
            self.label_Square_Area.hide()
            self.label_Square_Perimeter.hide()
            self.label_Rectangle_Area.hide()
            self.label_Rectangle_Perimeter.hide()
            self.label_Triangle_Area.hide()
            self.label_Triangle_Perimeter.hide()

    def circle(self):
        if self.radioButton_Circumference.isHidden():
            self.radioButton_Area_Rectangle.hide()
            self.radioButton_Area_Triangle.hide()
            self.radioButton_Area_Square.hide()
            self.radioButton_Perimeter_Rectangle.hide()
            self.radioButton_Perimeter_Triangle.hide()
            self.radioButton_Perimeter_Square.hide()
            self.lineEdit_Num2.hide()
            self.lineEdit_Num3.hide()
            self.label_Width.hide()
            self.label_Length.hide()
            self.label_Side.hide()
            self.label_Side_1.hide()
            self.label_Side_2.hide()
            self.label_Side_3.hide()
            self.label_Base.hide()
            self.label_Height.hide()
            self.radioButton_Circumference.show()
            self.radioButton_Circumference.toggled.connect(lambda: self.circle_radio())
            self.radioButton_Area_Circle.show()
            self.radioButton_Area_Circle.toggled.connect(lambda: self.circle_radio())
            self.label_Radius.show()
            self.lineEdit_Num1.show()

        else:
            self.radioButton_Circumference.hide()
            self.radioButton_Area_Circle.hide()
            self.label_Radius.hide()
            self.lineEdit_Num1.hide()
            self.label_Circle_Area.hide()
            self.label_Circle_Circumference.hide()

    def square(self):
        if self.radioButton_Perimeter_Square.isHidden():
            self.radioButton_Area_Rectangle.hide()
            self.radioButton_Area_Circle.hide()
            self.radioButton_Area_Triangle.hide()
            self.radioButton_Circumference.hide()
            self.radioButton_Perimeter_Triangle.hide()
            self.radioButton_Perimeter_Rectangle.hide()
            self.label_Radius.hide()
            self.label_Width.hide()
            self.label_Length.hide()
            self.label_Side_1.hide()
            self.label_Side_2.hide()
            self.label_Side_3.hide()
            self.label_Base.hide()
            self.label_Height.hide()
            self.lineEdit_Num2.hide()
            self.lineEdit_Num3.hide()
            self.radioButton_Perimeter_Square.show()
            self.radioButton_Perimeter_Square.toggled.connect(lambda: self.square_radio())
            self.radioButton_Area_Square.show()
            self.radioButton_Area_Square.toggled.connect(lambda: self.square_radio())
            self.lineEdit_Num1.show()
            self.label_Side.show()
        else:
            self.radioButton_Perimeter_Square.hide()
            self.radioButton_Area_Square.hide()
            self.lineEdit_Num1.hide()
            self.label_Side.hide()

    def rectangle(self):
        if self.radioButton_Perimeter_Rectangle.isHidden():
            self.radioButton_Area_Circle.hide()
            self.radioButton_Area_Square.hide()
            self.radioButton_Area_Triangle.hide()
            self.radioButton_Circumference.hide()
            self.radioButton_Perimeter_Triangle.hide()
            self.radioButton_Perimeter_Square.hide()
            self.label_Radius.hide()
            self.label_Side.hide()
            self.label_Base.hide()
            self.label_Height.hide()
            self.radioButton_Perimeter_Rectangle.show()
            self.radioButton_Perimeter_Rectangle.toggled.connect(lambda: self.rectangle_radio())
            self.radioButton_Area_Rectangle.show()
            self.radioButton_Area_Rectangle.toggled.connect(lambda: self.rectangle_radio())
            self.lineEdit_Num1.show()
            self.lineEdit_Num2.show()
            self.label_Width.show()
            self.label_Length.show()
        else:
            self.radioButton_Perimeter_Rectangle.hide()
            self.radioButton_Area_Rectangle.hide()
            self.lineEdit_Num1.hide()
            self.lineEdit_Num2.hide()
            self.label_Width.hide()
            self.label_Length.hide()

    def triangle(self):
        if self.radioButton_Perimeter_Triangle.isHidden():
            self.radioButton_Area_Circle.hide()
            self.radioButton_Area_Square.hide()
            self.radioButton_Area_Triangle.hide()
            self.radioButton_Circumference.hide()
            self.radioButton_Perimeter_Triangle.hide()
            self.radioButton_Perimeter_Square.hide()
            self.label_Radius.hide()
            self.label_Side.hide()
            self.label_Width.hide()
            self.label_Length.hide()
            self.radioButton_Perimeter_Rectangle.hide()
            self.radioButton_Area_Rectangle.hide()
            self.radioButton_Perimeter_Triangle.show()
            self.radioButton_Perimeter_Triangle.toggled.connect(lambda: self.triangle_radio())
            self.radioButton_Area_Triangle.show()
            self.radioButton_Area_Triangle.toggled.connect(lambda: self.triangle_radio())
            self.lineEdit_Num1.show()
            self.lineEdit_Num2.show()
            self.label_Base.show()
            self.label_Height.show()
        else:
            self.radioButton_Area_Triangle.hide()
            self.radioButton_Perimeter_Triangle.hide()
            self.lineEdit_Num1.hide()
            self.lineEdit_Num2.hide()
            self.lineEdit_Num3.hide()
            self.label_Base.hide()
            self.label_Height.hide()

    def circle_radio(self):
        if self.radioButton_Area_Circle.isChecked():
            self.label_Triangle_Area.hide()
            self.label_Triangle_Perimeter.hide()
            self.label_Rectangle_Area.hide()
            self.label_Rectangle_Perimeter.hide()
            self.label_Square_Area.hide()
            self.label_Square_Perimeter.hide()
            self.label_Circle_Circumference.hide()
            self.label_Circle_Area.show()
        elif self.radioButton_Circumference.isChecked():
            self.label_Triangle_Area.hide()
            self.label_Triangle_Perimeter.hide()
            self.label_Rectangle_Area.hide()
            self.label_Rectangle_Perimeter.hide()
            self.label_Square_Area.hide()
            self.label_Square_Perimeter.hide()
            self.label_Circle_Circumference.show()
            self.label_Circle_Area.hide()

    def rectangle_radio(self):
        if self.radioButton_Area_Rectangle.isChecked():
            self.label_Triangle_Area.hide()
            self.label_Triangle_Perimeter.hide()
            self.label_Square_Area.hide()
            self.label_Square_Perimeter.hide()
            self.label_Circle_Circumference.hide()
            self.label_Circle_Area.hide()
            self.label_Rectangle_Perimeter.hide()
            self.label_Rectangle_Area.show()
        elif self.radioButton_Perimeter_Rectangle.isChecked():
            self.label_Triangle_Area.hide()
            self.label_Triangle_Perimeter.hide()
            self.label_Square_Area.hide()
            self.label_Square_Perimeter.hide()
            self.label_Circle_Circumference.hide()
            self.label_Circle_Area.hide()
            self.label_Rectangle_Perimeter.show()
            self.label_Rectangle_Area.hide()

    def square_radio(self):
        if self.radioButton_Area_Square.isChecked():
            self.label_Rectangle_Area.hide()
            self.label_Rectangle_Perimeter.hide()
            self.label_Triangle_Area.hide()
            self.label_Triangle_Perimeter.hide()
            self.label_Circle_Circumference.hide()
            self.label_Circle_Area.hide()
            self.label_Square_Perimeter.hide()
            self.label_Square_Area.show()
        elif self.radioButton_Perimeter_Square.isChecked():
            self.label_Rectangle_Area.hide()
            self.label_Rectangle_Perimeter.hide()
            self.label_Triangle_Area.hide()
            self.label_Triangle_Perimeter.hide()
            self.label_Circle_Circumference.hide()
            self.label_Circle_Area.hide()
            self.label_Square_Perimeter.show()
            self.label_Square_Area.hide()

    def triangle_radio(self):
        if self.radioButton_Perimeter_Triangle.isChecked():
            self.label_Rectangle_Area.hide()
            self.label_Rectangle_Perimeter.hide()
            self.label_Square_Area.hide()
            self.label_Square_Perimeter.hide()
            self.label_Circle_Circumference.hide()
            self.label_Circle_Area.hide()
            self.label_Base.hide()
            self.label_Height.hide()
            self.label_Triangle_Area.hide()
            self.lineEdit_Num3.show()
            self.label_Side_1.show()
            self.label_Side_2.show()
            self.label_Side_3.show()
            self.label_Triangle_Perimeter.show()
        elif self.radioButton_Area_Triangle.isChecked():
            self.label_Rectangle_Area.hide()
            self.label_Rectangle_Perimeter.hide()
            self.label_Square_Area.hide()
            self.label_Square_Perimeter.hide()
            self.label_Circle_Circumference.hide()
            self.label_Circle_Area.hide()
            self.lineEdit_Num3.hide()
            self.label_Triangle_Perimeter.hide()
            self.label_Base.show()
            self.label_Height.show()
            self.label_Side_1.hide()
            self.label_Side_2.hide()
            self.label_Side_3.hide()
            self.label_Triangle_Area.show()

    def cal_function(self):
        if self.radioButton_Circumference.isChecked():
            num1 = int(self.lineEdit_Num1.text())
            answer = 2 * 3.14 * num1
            self.label_Equation.setText(f'2*3.14*{num1}=')
            self.outputLabel.setText(str(answer)[:12])
            self.lineEdit_Num1.setText("")
        elif self.radioButton_Area_Circle.isChecked():
            num1 = int(self.lineEdit_Num1.text())
            answer = 3.14 * num1 * num1
            self.label_Equation.setText(f'3.14*{num1}*{num1}=')
            self.outputLabel.setText(str(answer)[:12])
            self.lineEdit_Num1.setText("")
        elif self.radioButton_Area_Rectangle.isChecked():
            num1 = int(self.lineEdit_Num1.text())
            num2 = int(self.lineEdit_Num2.text())
            answer = num1 * num2
            self.label_Equation.setText(f'{num1}*{num2}=')
            self.outputLabel.setText(str(answer)[:12])
            self.lineEdit_Num1.setText("")
            self.lineEdit_Num2.setText("")
        elif self.radioButton_Perimeter_Rectangle.isChecked():
            num1 = int(self.lineEdit_Num1.text())
            num2 = int(self.lineEdit_Num2.text())
            num3 = num1 + num2
            answer = 2 * num3
            self.label_Equation.setText(f'2*({num1}+{num2})=')
            self.outputLabel.setText(str(answer)[:12])
            self.lineEdit_Num1.setText("")
            self.lineEdit_Num2.setText("")
        elif self.radioButton_Area_Square.isChecked():
            num1 = int(self.lineEdit_Num1.text())
            answer = num1 * num1
            self.label_Equation.setText(f'{num1}*{num1}=')
            self.outputLabel.setText(str(answer)[:12])
            self.lineEdit_Num1.setText("")
        elif self.radioButton_Perimeter_Square.isChecked():
            num1 = int(self.lineEdit_Num1.text())
            answer = 4 * num1
            self.label_Equation.setText(f'4*{num1}=')
            self.outputLabel.setText(str(answer)[:12])
            self.lineEdit_Num1.setText("")
        elif self.radioButton_Area_Triangle.isChecked():
            self.lineEdit_Num1.show()
            num1 = int(self.lineEdit_Num1.text())
            num2 = int(self.lineEdit_Num2.text())
            num3 = num1 * num2
            answer = num3 / 2
            self.label_Equation.setText(f'({num1}*{num2})/2=')
            self.outputLabel.setText(str(answer)[:12])
            self.lineEdit_Num1.setText("")
            self.lineEdit_Num2.setText("")
        elif self.radioButton_Perimeter_Triangle.isChecked():
            num1 = int(self.lineEdit_Num1.text())
            num2 = int(self.lineEdit_Num2.text())
            num3 = int(self.lineEdit_Num3.text())
            answer = num1 + num2 + num3
            if num1 + num2 <= num3:
                self.label_Error.show()
                self.label_Equation.setText("")
                self.label_Error.setText(f'Invalid make sure Side 1 + Side 2 > Side 3')
            elif num1 + num3 <= num2:
                self.label_Error.show()
                self.label_Equation.setText("")
                self.label_Error.setText(f'Invalid make sure Side 1 + Side 3 > Side 2')
            else:
                self.label_Error.setText("")
                self.label_Equation.setText(f'{num1}+{num2}+{num3}=')
                self.outputLabel.setText(str(answer)[:12])
                self.lineEdit_Num1.setText("")
                self.lineEdit_Num2.setText("")
                self.lineEdit_Num3.setText("")
