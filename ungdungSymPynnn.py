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

        self.limit_button = QPushButton("Tính giới hạn")
        self.limit_button.clicked.connect(self.calculate_limit)
        self.layout.addWidget(self.limit_button)

        self.integral_button = QPushButton("Nguyên hàm")
        self.integral_button.clicked.connect(self.calculate_integral)
        self.layout.addWidget(self.integral_button)

        self.solve_button = QPushButton("Giải")
        self.solve_button.clicked.connect(self.solve_equation)
        self.layout.addWidget(self.solve_button)

        self.result_label = QLabel("Kết quả:")
        self.layout.addWidget(self.result_label)

        self.result_text = QTextEdit()
        self.layout.addWidget(self.result_text)

        self.limit_label = QLabel("Tính giới hạn (x tiến đến):")
        self.layout.addWidget(self.limit_label)

        self.limit_input = QLineEdit()
        self.layout.addWidget(self.limit_input)

      

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
    
    def calculate_limit(self):
        equation_str = self.equation_input.text()
        limit_value_str = self.limit_input.text()
        try:
            x = sym.symbols('x')
            equation = sym.sympify(equation_str)
            limit_value = sym.limit(equation, x, float(limit_value_str))
            self.result_text.setPlainText(f"Giới hạn khi x tiến đến {limit_value_str} là: {limit_value}")
        except Exception as e:
            self.result_text.setPlainText(f"Lỗi: {e}")

    def calculate_integral(self):
        equation_str = self.equation_input.text()
        try:
            x = sym.symbols('x')
            equation = sym.sympify(equation_str)
            integral = sym.integrate(equation, x)
            self.result_text.setPlainText(f"Nguyên hàm của phương trình là: {integral}")
        except Exception as e:
            self.result_text.setPlainText(f"Lỗi: {e}")

    def daoham(self):
        equation_str = self.equation_input.text()
        n = int(self.cap_dao_ham.text())  # Lấy cấp đạo hàm từ người dùng
        try:
            x = sym.symbols('x')
            equation = sym.Eq(sym.sympify(equation_str), 0)
            # Tính đạo hàm cấp n của phương trình
            derivative = sym.diff(equation.lhs, x, n)
            # Hiển thị kết quả đạo hàm trên giao diện
            self.result_text.setPlainText(str(derivative))
        except Exception as e:
            self.result_text.setPlainText(f"Lỗi: {e}")
    

def main():
    app = QApplication(sys.argv)
    window = EquationSolverApp()
    window.show()
    app.exec()

if __name__ == "__main__":
    main()
