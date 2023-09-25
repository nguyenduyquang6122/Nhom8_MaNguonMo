import numpy as np
import tkinter as tk
from tkinter import ttk

# Hàm để xử lý việc hiển thị kết quả
def display_result():
    matrix = []
    r = int(rows_entry.get())
    c = int(columns_entry.get())

    for i in range(r):
        row = []
        for j in range(c):
            value = int(entry_values[i][j].get())
            row.append(value)
        matrix.append(row)

    arr = np.array(matrix)
    newarr = arr.reshape(r, c)
    transposed_arr = np.transpose(newarr)

    result_text.config(state="normal")
    result_text.delete("1.0", tk.END)
    result_text.insert(tk.END, "Following is the matrix you entered:\n")
    result_text.insert(tk.END, str(newarr) + "\n")
    result_text.insert(tk.END, "Rank:\n")
    result_text.insert(tk.END, str(np.linalg.matrix_rank(newarr)) + "\n")
    result_text.insert(tk.END, "Following is the transposed matrix:\n")
    result_text.insert(tk.END, str(transposed_arr) + "\n")
    result_text.insert(tk.END, "Rank:\n")
    result_text.insert(tk.END, str(np.linalg.matrix_rank(transposed_arr)) + "\n")
    result_text.config(state="disabled")

# Tạo cửa sổ Tkinter
root = tk.Tk()
root.title("Matrix Operations")

# Nhập số hàng và số cột
rows_label = tk.Label(root, text="Number of rows:")
rows_label.grid(row=0, column=0)
rows_entry = tk.Entry(root)
rows_entry.grid(row=0, column=1)

columns_label = tk.Label(root, text="Number of columns:")
columns_label.grid(row=1, column=0)
columns_entry = tk.Entry(root)
columns_entry.grid(row=1, column=1)

# Tạo ô để nhập giá trị cho ma trận
entry_values = []
for i in range(3):
    row_entries = []
    for j in range(3):
        entry = tk.Entry(root)
        entry.grid(row=i+2, column=j)
        row_entries.append(entry)
    entry_values.append(row_entries)

# Nút để tính toán và hiển thị kết quả
calculate_button = tk.Button(root, text="Calculate", command=display_result)
calculate_button.grid(row=5, column=0, columnspan=3)

# Kết quả hiển thị trong ô văn bản
result_text = tk.Text(root, height=15, width=40, state="disabled")
result_text.grid(row=6, column=0, columnspan=3)

root.mainloop()
