năm = float(input("nhập năm:"))
if (năm%4==0 and năm%100!=0) or (năm%400==0):
    print("là năm nhuận.")
else:
    print("không phải là năm nhuận.")