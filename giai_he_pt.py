import numpy as np

# Nhập số phương trình và số ẩn n
n = int(input("Nhập số phương trình và số ẩn n: "))

# Tạo ma trận ngẫu nhiên A kích thước nxn và véc-tơ ngẫu nhiên B kích thước nx1
A = np.random.rand(n, n)
B = np.random.rand(n, 1)
C = np.random.rand(2*n, 2*n)


# Hiển thị ma trận A và véc-tơ B
print("Ma trận A:")
print(A)
print("\nVéc-tơ B:")
print(B)
print("\nma tran C:")
print(C)

# Tính định thức của ma trận A
determinant = np.linalg.det(A)
determinant1 = np.linalg.det(C)

# Kiểm tra xem định thức có bằng 0 hay không
if determinant == 0:
    print("Ma trận A là ma trận suy biến và có vô số nghiệm.")
else:
    print("Ma trận A không phải là ma trận suy biến và có một nghiệm duy nhất.")
if determinant1 == 0:
    print("Ma trận C là ma trận suy biến và có vô số nghiệm.")
else:
    print("Ma trận C không phải là ma trận suy biến và có một nghiệm duy nhất.")
'''
# Giải hệ phương trình Ax = B
x = np.linalg.solve(A, B)

# Hiển thị nghiệm của hệ phương trình
print("\nNghiệm của hệ phương trình:")
print(x)
'''

