import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton, QTextEdit
import sympy as sym

class EquationSolverApp(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Phương trình và SymPy")
        self.setGeometry(100, 100, 600, 400)

        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)

        self.layout = QVBoxLayout()

        self.equation_label = QLabel("Nhập phương trình:")
        self.layout.addWidget(self.equation_label)

        self.equation_input = QLineEdit()
        self.layout.addWidget(self.equation_input)

        self.solve_button = QPushButton("Giải")
        self.solve_button.clicked.connect(self.solve_equation)
        self.layout.addWidget(self.solve_button)
        self.solve_button = QPushButton("đạo hàm")
        self.solve_button.clicked.connect(self.daoham)
        self.layout.addWidget(self.solve_button)
        self.solve_button = QPushButton("tích phân")
        self.solve_button.clicked.connect(self.tich_phan)
        self.layout.addWidget(self.solve_button)
        self.solve_button = QPushButton("hệ pt")
        self.solve_button.clicked.connect(self.hept)
        self.layout.addWidget(self.solve_button)

        self.result_label = QLabel("Kết quả:")
        self.layout.addWidget(self.result_label)

        self.result_text = QTextEdit()
        self.layout.addWidget(self.result_text)

        self.central_widget.setLayout(self.layout)

    def solve_equation(self):
        equation_str = self.equation_input.text()
        try:
            x = sym.symbols('x')
            equation = sym.Eq(sym.sympify(equation_str), 0)
            solutions = sym.solve(equation, x)
            result = ", ".join([f"x{i+1} = {sol}" for i,sol in enumerate(solutions)])
            self.result_text.setPlainText(result)
        except Exception as e:
            self.result_text.setPlainText(f"Lỗi: {e}")
    def hept(self):
        equation_str = self.equation_input.text()
        try:
            x = sym.symbols('x')
            y = sym.symbols('y')
            equation = sym.sympify(equation_str)
            solution = sym.solve(equation, (x,y))
            n1 = solution[x]
            n2 = solution[y]
            self.result_text.setPlainText(f"nghiem x la: { n1}        nghiem y la: {n2}")
        except Exception as e:
            self.result_text.setPlainText(f"Lỗi: {e}")
    def tich_phan(self):
        equation_str = self.equation_input.text()
        try:
            x = sym.symbols('x')
            equation = sym.sympify(equation_str)
            tichphan = sym.integrate(equation,x)
            self.result_text.setPlainText(f"tich phan: {tichphan}")
        except Exception as e:
            self.result_text.setPlainText(f"Lỗi: {e}")
    def daoham(self):
        equation_str = self.equation_input.text()
        try:
            x = sym.symbols('x')
            equation = sym.sympify(equation_str)
            daoham = sym.diff(equation,x)
            self.result_text.setPlainText(f"dao ham: {daoham}")
        except Exception as e:
            self.result_text.setPlainText(f"Lỗi: {e}")
def main():
    app = QApplication(sys.argv)
    window = EquationSolverApp()
    window.show()
    app.exec()

if __name__ == "__main__":
    main()
