import numpy as np #import numpy

matrix = []

print("Enter the number of rows, columns of the matrix") #create matrix r*c
r = int(input("Enter rows: ")) 
c = int(input("Enter columns: "))

for x in range(r*c):
    matrix.append(int(input("Enter value "+ str(x) +" : "))) #created empty list and enter value

arr = np.array(matrix, ndmin = 1) #convert list into array
newarr = arr.reshape(r,c) #create a rxc 2D array
x = newarr.copy() #create copy of rxc array

#DISPLAY ALL RELEVANT INFO
print("Following is the matrix you entered:")
print("---------------------------------------")
print(newarr)
print("rank:")
print(np.linalg.matrix_rank(newarr))
print("---------------------------------------")

print("Following is the transposed matrix:")
print("---------------------------------------")
print(x)
print("rank:")
print(np.linalg.matrix_rank(x))
print("---------------------------------------")
