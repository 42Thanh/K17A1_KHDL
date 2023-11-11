n=int(input("nhập một số tự nhiên n (n>m):"))
m=int(input("nhập một số tự nhiên m:"))
if m <= 0 or n <= 0 or m >= n:
    print("nhập hai số tự nhiên hợp lệ sao cho m < n.")
else:
    print(f"các số chia hết cho {m} trong khoảng từ 1 đến {n}")
    for i in range(1,1+n):
        if i%m==0:
            print(i)