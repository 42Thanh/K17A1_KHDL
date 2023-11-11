so= int(input("nhập số tự nhiên N:"))
if so <= 0:
    print("nhập một số tự nhiên lớn hơn 0.")
else:
    print(f"Các số nguyên từ 1 đến {so}:")
    for i in range(1, so+1):
        print(i)