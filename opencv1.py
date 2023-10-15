import cv2
import random
import numpy as np
def main():
    # Đọc ảnh
    img = cv2.imread('tenhinh.jpg')

    # Tạo cửa sổ giao diện
    cv2.namedWindow('chinhSuaAnh', cv2.WINDOW_NORMAL)

    # Tạo biến để lưu trữ trạng thái của giao diện
    rotate = False
    gray = False
    zoomin = False
    flip = False
    global dem
    global zoom
    zoom = 0
    dem = 0
    cv2.destroyWindow('chinhSuaAnh')
    # Vòng lặp chính
    while True:
        # Hiển thị ảnh
        img_1 = apply_adjustments(img, rotate, zoomin, flip,  gray)
        cv2.imshow('chinhSuaAnh', img_1)

        # Xử lý các sự kiện
        key = cv2.waitKey(1)
        if key == 27:  # ESC
            break
        elif key == ord('x'):  # Xoay ảnh
            dem = dem + 1
            if dem % 4 == 0:
                img = cv2.imread('tenhinh.jpg')
            if dem % 4 != 0:
                img = cv2.rotate(img, cv2.ROTATE_90_COUNTERCLOCKWISE)
        elif key == ord('+'):  # phóng to
            zoomin = not zoomin
        elif key == ord('f'):  # Tạo ảnh lật
            flip = not flip
        elif key == ord('g'):  # Tạo ảnh xám
            gray = not gray
        elif key == ord('s'):
            characters = "abcdefghijklmnopqrstuvwxyz0123456789"
            char = random.choice(characters)
            cv2.imwrite(char+'.jpg',img)
            break
    # Đóng cửa sổ
    cv2.destroyAllWindows()

def apply_adjustments(img, rotate,zoomin,flip, gray):
    # Xoay ảnh
    global dem
    global zoom
    if rotate:
        dem = dem + 1
        if dem % 4 == 0:
            img = cv2.imread('tenhinh.jpg')
        if dem % 4 != 0:
            img = cv2.rotate(img, cv2.ROTATE_90_COUNTERCLOCKWISE)
    if zoomin:
        img = cv2.resize(img,None,fx=1.5,fy=1.5)
    if flip:
        img = cv2.flip(img, 1)
    # Tạo ảnh xám
    if gray:
        img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    return img

if __name__ == "__main__":
    main()