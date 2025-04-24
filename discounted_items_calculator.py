# Function to calculate the final price
def calculate_discount(price, discount_percent):
    # Calculate the final price after applying the discount
    return price - (price * discount_percent / 100)

# User prompt
print("\nDiscounted Items Calculator\n")
price = float(input("Enter the original price: "))
discount = float(input("Enter the discount for this item: "))
currency =input("Enter your currency: ")

# Control flows
if discount < 0:
    print("Discount can't be negative")
elif discount >= 20:
    finalPrice = calculate_discount(price, discount)
    print(f"You're given a discount of {discount}%, you'll pay {finalPrice:.2f} {currency}")
else:
    print(f"You're not discounted, you'll pay {price:.2f} {currency} ")
    
    
