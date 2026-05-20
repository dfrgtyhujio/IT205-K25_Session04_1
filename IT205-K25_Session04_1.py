total_amount = int(input("Nhập tổng tiền hóa đơn ban đầu: "))

if total_amount >= 500000:
    discount_amount = total_amount * 10 // 100
else:
    discount_amount = 0

final_amount = total_amount - discount_amount

print("--- HÓA ĐƠN THANH TOÁN RIKKEI STORE ---")
print("Số tiền được giảm giá:", discount_amount, "VND")
print("Tổng tiền khách phải trả:", final_amount, "VND")