#Bai2 
r = 5
pt = 3.14
c = 2 * pt * r
print("Chu vi hình tròn là:", c)
# Bai 1
a =10
b = 14.88
c = "Heil, Hitler!"
print("Số nguyên là :", a)
print("Số thực là :", b)
print("Chuỗi là :", c)
#Bai3
n = int(input("Nhập một số từ 1 đến 9:"))
if 1 <= n <=9:
    print("Bảng cửu chương của", n, ":")
    for i in range(1,11):
        print(n, "x", i , "=",n*i)
else: print("Số bạn nhập không hợp lệ, vui lòng nhập lại từ số 1 đến 9.")
#Bai4
num = int(input("Nhập một số dương:"))
if num > 1:
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            print(num, "không phải là số nguyên tố.")
            break
else :
    print(num, "là số nguyên tố")

# Bai5
listmonhoc = ["Đại số tuyến tính, Cơ sở lập trình, Triết học Mác - Lênin, Tư tưởng Hồ Chí Minh"]
print("Danh sách môn học:", listmonhoc)
for i in listmonhoc:
    print(i,)
# Bai6
listfriend = ["Nguyễn Xuân Đạt, Đoàn Văn Sáng, Mẹ Lý Khô Gà"]
listfriend.append("Anh Trà Từ Tay")
print("Danh sách bạn bè sau khi thêm:", listfriend)
listfriend.pop(1)
print("Danh sách bạn bè sau khi xóa:", listfriend)
# Bai7 
def process_numbers():
    so_input = input("Nhập một danh sách số nguyên, cách nhau bằng dấu phẩy: ")
    so_tuple = tuple(int(num.strip()) for num in so_input.split(","))
    
    tong_sum = sum(so_tuple)
    lonnhat_value = max(so_tuple)
    nhonhat_value = min(so_tuple)
    
    return tong_sum, lonnhat_value, nhonhat_value
if __name__ == "__main__":
    tong_sum, lonnhat_value, nhonhat_value = process_numbers()
    print("Tổng của các số:", tong_sum)
    print("Giá trị lớn nhất:", lonnhat_value)
    print("Giá trị nhỏ nhất:", nhonhat_value)
#Bai8
class Hoa :
    def __init__(self, ten, mau):
        self.ten = ten
        self.mau = mau
    def hien_thi_thong_tin(self):
        print("Tên hoa:", self.ten)
        print("Màu sắc:", self.mau)
        if __name__ == "__main__":
            ten_hoa = input("Nhập tên hoa: ")
            mau_hoa = input("Nhập màu sắc của hoa: ")
            hoa = Hoa(ten_hoa, mau_hoa)
            hoa.hien_thi_thong_tin()

