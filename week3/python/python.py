def calculate_discount(price, discount_percent=0):
    if 20 <= discount_percent <= 100:
        discount = price * (discount_percent / 100)
        final_price = price - discount
        return final_price
    else:
        return price 
price_input = input("Enter the price of the item: ")
discount_input = input("Enter the discount percentage (or press Enter for no discount): ")
try:
    price = float(price_input)
except ValueError:
    print("Invalid price input! Please enter a valid PRICE.")
    exit()
try:
    discount_percent = float(discount_input) if discount_input.strip() else 0
except ValueError:
    print("Invalid discount percentage! Please enter a dISCOUNT.")
    exit()
final_price = calculate_discount(price, discount_percent)
print(f"The final price after discount is: {final_price:.2f}")
