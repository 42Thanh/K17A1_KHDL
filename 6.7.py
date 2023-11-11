def c_to_f(DOC):
    DOF = (DOC * 9/5) + 32
    return DOF
DOC = float(input("Nhập nhiệt độ độ C: "))
DOF = c_to_f(DOC)
print(f"Nhiệt độ tương ứng ở độ F là: {DOF}°F")