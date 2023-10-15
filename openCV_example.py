import cv2
import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget, QPushButton, QVBoxLayout, QLabel, QHBoxLayout
from PyQt6.QtGui import QImage, QPixmap, QImageReader
from PyQt6.QtCore import Qt
import numpy as np
import matplotlib.pyplot as plt

class ImageApp(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Image App")
        self.setGeometry(0, 0, 2160, 720)

        self.initUI()

    def initUI(self):
        self.central_widget = QWidget(self)
        self.setCentralWidget(self.central_widget)

        self.image_label = QLabel(self)
        self.result_label = QLabel(self)
        self.image_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.result_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.btn_gray = QPushButton("Tạo ảnh xám", self)
        self.btn_cartoon = QPushButton("Tạo ảnh cartoon", self)

        self.btn_gray.clicked.connect(self.create_gray_image)
        #self.btn_cartoon.clicked.connect(self.create_cartoon_image)

        hbox1 = QHBoxLayout()
        hbox1.addWidget(self.image_label)
        hbox1.addWidget(self.result_label)

        vbox = QVBoxLayout()
        vbox.addLayout(hbox1)
        vbox.addWidget(self.btn_gray)
        vbox.addWidget(self.btn_cartoon)

        self.image_label.setPixmap(QPixmap('tenhinh.jpg'))
        self.central_widget.setLayout(vbox)

    def create_gray_image(self):
        image = cv2.imread('tenhinh.jpg')
        if image is not None:
            gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
            q_image = QImage(gray.data, gray.shape[1], gray.shape[0], 3*gray.shape[1], QImage.Format.Format_RGB888)
            pixmap = QPixmap(q_image)
            self.result_label.setPixmap(pixmap)
            self.result_label.setScaledContents(True)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = ImageApp()
    window.show()
    sys.exit(app.exec())
'''
# Đọc ảnh từ tệp tin
image = cv2.imread('tenhinh.jpg')

def gray_image(image):
     # Chuyển đổi ảnh sang ảnh xám
    g_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    return g_image 

def cartoonize (image):
  gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
  blurImage = cv2.medianBlur(gray, 5)

  edges = cv2.adaptiveThreshold(blurImage, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 9, 9)

  color = cv2.bilateralFilter(image, 9, 300, 300)

  cartoon = cv2.bitwise_and(color, color, mask = edges)

  return cartoon

def plot_histogram(image, title, mask=None):
    # Chia hình ảnh thành các kênh tương ứng, sau đó khởi tạo
	# Tuple tên kênh cùng với hình để vẽ đồ thị
	chans = cv2.split(image)
	colors = ("b", "g", "r")
	plt.figure()
	plt.title(title)
	plt.xlabel("Bins")
	plt.ylabel("# of Pixels")
	# Vòng lặp các kênh hình ảnh
	for (chan, color) in zip(chans, colors):
		# Tạo biểu đồ cho kênh hiện tại và vẽ sơ đồ đó
		hist = cv2.calcHist([chan], [0], mask, [256], [0, 256])
		plt.plot(hist, color=color)
		plt.xlim([0, 256])

# Kiểm tra xem ảnh có được đọc thành công hay không
if image is not None:

    # Hiển thị ảnh gốc
    cv2.imshow('Original image', image)

    plot_histogram(image, "Histogram for Original Image")
    # Hiển thị biểu đồ
    plt.show()

    # Hiển thị ảnh xám
    cv2.imshow('Gray image', gray_image(image))

    # Hiển thị 
    cv2.imshow("Cartoon image", cartoonize(image))

    # Đợi một phím bất kỳ và sau đó đóng cửa sổ hiển thị
    cv2.waitKey(0)
    cv2.destroyAllWindows()
else:
    print('Không thể đọc ảnh từ tệp tin.')
'''