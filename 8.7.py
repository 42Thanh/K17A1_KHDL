def tinh_tien_dien(kwh):
    gia_ban_dien = {
        1 : 1678, #Bậc 1: chokwh từ 0-50
        2 : 1734, #BẬc 2: cho kwh từ 51-100
        3 : 2014, #Bậc 3: cho kwh từ 101-200
        4 : 2536, #Bậc 4: cho kwh từ 201-300
        5 : 2834, #Bậc 5: cho kwh từ 301-400
        6 : 2927, #Bậc 6: cho kwh từ 401 trở lên
    }
    tong_tien = 0
    for b, gia in gia_ban_dien.items():
        if kwh <= 0:
            break
        elif kwh <= 50:
            tong_tien += kwh * gia
            break
        else:
            tong_tien += 50 * gia
            kwh -= 50
    return tong_tien
#Nhập số kwh tiêu thụ từ người dùng
kwh = float(input("Nhập số kwh tiêu thụ:"))
#Tính tổng số tiền điện
tong_tien = tinh_tien_dien(kwh)
#Xuất kết quả
print("Tổng sô tiền điện là:",tong_tien,"đồng")