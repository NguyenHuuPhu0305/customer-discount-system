from discount import calculate_discount

# TC01
prev = 60000000
order = 2000000
discount = calculate_discount(prev)
final = order - (order * discount)
print(f"TC01 - Discount: {discount} - Tiền thanh toán: {final}")

# TC02
prev = 30000000
order = 2000000
discount = calculate_discount(prev)
final = order - (order * discount)
print(f"TC02 - Discount: {discount} - Tiền thanh toán: {final}")

# TC03
prev = 49000000
order = 2000000
discount = calculate_discount(prev)
final = order - (order * discount)
print(f"TC03 - Discount: {discount} - Tiền thanh toán: {final}")