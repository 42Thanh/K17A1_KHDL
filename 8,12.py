def is_prime(number):
    if number <= 1:
        return False
    for i in range(2, int(number**0.5) + 1):
        if number % i == 0:
            return False
        return True
#Nhập số từ người dùng
x = int(input("Nhập một số:"))
#Kiểm tra xem x có phải là số nguyên tố hay không
if is_prime(x):
    print(f"{x} là số nguyên tố.")
else:
    print(f"{x} không phải lầ số nguyên tố.")