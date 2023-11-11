# Hàm tính tổng các chữ số của số nguyên
def tinh_tong_chu_so(N):
    chuoi_so = str(N)
    tong = 0
    for chu_so in chuoi_so:
        tong += int(chu_so)
    return tong
so_nguyen = int(input("Nhập một số nguyên: "))
tong_chu_so = tinh_tong_chu_so(so_nguyen)
print(f"Tổng các chữ số của {so_nguyen} là: {tong_chu_so}")