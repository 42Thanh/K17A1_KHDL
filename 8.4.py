import math
a=float(input("nhập a:"))
b=float(input("nhập b:"))
c=float(input("nhập c:"))
#nửa chu vi
s = ( a + b + c) /2
#diện tích tam giác bằng heron
dien_tich = math.sqrt(s * (s - a) * (s - b) * (s - c))
print("diện tích tam giác là:",dien_tich)