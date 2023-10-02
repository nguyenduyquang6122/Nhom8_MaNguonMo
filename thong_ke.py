import pandas as pd
from numpy import array
import matplotlib.pyplot as plt
import numpy as np
df=pd.read_csv('diemPython.csv',index_col=0,header = 0)
in_data = array(df.iloc[:,:])
print(in_data)
print('Tong so sinh vien di thi :')
tongsv= in_data[:,1]
print(np.sum(tongsv))
print("hello")
SUMSV = np.sum(tongsv)

print("Ty le % sinh vien dat :") #thêm tỷ lệ phần trăm
svF = in_data[:,10]
svDat = np.subtract(tongsv,svF)
tyle = np.divide(np.sum(svDat),np.sum(tongsv))*100
print(str(tyle) + "%")

diemA = in_data[:,3]
diemBc = in_data[:,4]
diemF = in_data[:,10]
tongsvF = np.sum(diemF)
SoSvQuaMon = (1 - tongsvF/SUMSV)*100
print(f"So sinh vien truot mon la: {(tongsvF/SUMSV)*100}%")
print(f"Trung binh so sv qua mon la: {SoSvQuaMon}%")
print('Tong sv:',tongsv)
maxa = diemA.max()
i, = np.where(diemA == maxa)
print('lop co nhieu diem A la {0} co {1} sv dat diem A'.format(in_data[i,0],maxa))

#so sanh điểm A với B+
tongA = diemA.sum()
tongBc=diemBc.sum()
print('so sv diem A ',tongA)
print('so sv diem B+',tongBc)
if tongA <= tongBc:
    print('it sv diem A hon B+')
else:
    print('nhieu sv diem A hon B+')

plt.plot(range(len(diemA)),diemA,'r-',label="Diem A")
plt.plot(range(len(diemBc)),diemBc,'g-',label="Diem B +")
plt.xlabel('Lơp')
plt.ylabel(' So sv dat diem ')
plt.legend(loc='upper right')
plt.show()
      
