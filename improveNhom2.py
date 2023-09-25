import numpy as np #import numpy

matrix = []

print("Enter the number of rows, columns of the matrix") #create matrix r*c
r = int(input("Enter rows: ")) 
c = int(input("Enter columns: "))

for i in range(r):
    row=[]
    for j in range(c):
        value = int(input(f"value({i+1},{j+1}): "))
        row.append(value)
    matrix.append(row) 

arr = np.array(matrix, ndmin = 1) #convert list into array
newarr = arr.reshape(r,c) #create a rxc 2D array
transposed_arr = np.transpose(newarr)

#DISPLAY ALL RELEVANT INFO
print("Following is the matrix you entered:")
print("---------------------------------------")
print(newarr)
print("rank:")
print(np.linalg.matrix_rank(newarr))
print("---------------------------------------")

print("Following is the transposed matrix:")
print("---------------------------------------")
print(transposed_arr)
print("rank:")
print(np.linalg.matrix_rank(transposed_arr))
print("---------------------------------------")
