import cv2
import numpy as np
import matplotlib.pyplot as plt
import tkinter as tk
from tkinter import simpledialog
from PIL import Image, ImageTk
from tkinter.simpledialog import askfloat
def resize_image(scale_factor):
    img_resized = cv2.resize(img, None, fx=scale_factor, fy=scale_factor)
    return img_resized
def rotate_image(angle):
    rows, cols, _ = img.shape
    M = cv2.getRotationMatrix2D((cols / 2, rows / 2), angle, 1)
    img_rotated = cv2.warpAffine(img, M, (cols, rows))
    return img_rotated
def update_images(scale_factor,rotation_angle):
    img_resized = resize_image(scale_factor)
    img_rotated = rotate_image(rotation_angle)
    img_pil = Image.fromarray(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
    img_resized_pil = Image.fromarray(cv2.cvtColor(img_resized, cv2.COLOR_BGR2RGB))
    img_rotated_pil = Image.fromarray(cv2.cvtColor(img_rotated, cv2.COLOR_BGR2RGB))
    
    img_tk = ImageTk.PhotoImage(img_pil)
    img_resized_tk = ImageTk.PhotoImage(img_resized_pil)
    img_rotated_tk = ImageTk.PhotoImage(img_rotated_pil)
   
    
    label_original.config(image=img_tk)
    label_resized.config(image=img_resized_tk)
    label_rotated.config(image=img_rotated_tk)
    label_original.image = img_tk
    label_resized.image = img_resized_tk
    label_rotated.image = img_rotated_tk
    
img = cv2.imread('C:/Users/ADMIN/Downloads/New folder/2.jpg', cv2.IMREAD_COLOR)
half = cv2.resize(img, (0,0), fx = 0.5, fy= 0.5)
bigger = cv2.resize (img, (1050, 1610))
stretch_near = cv2.resize (img, (780, 540), interpolation = cv2.INTER_LINEAR)
Titles =["Original", "Half", "Bigger", "Interpolation Nearest"]
images =[img, half, bigger, stretch_near]
count = 4
root = tk.Tk()
root.title("Image Resizer")

frame = tk.Frame(root)
frame.pack()
label_rotated = tk.Label(frame)
label_rotated.pack(side=tk.LEFT)
                                      
label_original = tk.Label(frame)
label_resized = tk.Label(frame)

label_original.pack(side=tk.LEFT)
label_resized.pack(side=tk.RIGHT)


scale_factor = simpledialog.askfloat("Resize Image", "e.g: 0.5 for 50% reduction):")
rotation_angle = askfloat("Rotate Image", "Enter rotation angle in degrees:")
if scale_factor is not None and rotation_angle is not None:
    update_images(scale_factor, rotation_angle)
for i in range (count) :
    plt.subplot(2, 2, i + 1)
    plt.title(Titles[i])
    plt.imshow(cv2.cvtColor(images[i], cv2.COLOR_BGR2RGB))
root.mainloop
