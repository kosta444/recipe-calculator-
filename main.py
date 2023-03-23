'''
  Name: kosta
  James Hargest College
  Programming Internal for 2.7 & 2.8 ~ 12 credits
  Due: 6 April 2023
  
  TIP: Use assessment guide to help guide you through this Internal
'''
# Prompt user for amount of money they have
budget = float(input("Enter the amount of money you have: "))

# Prompt user for number of products
num_products = int(input("Enter the number of products: "))

# Create an empty list to store products
products = []

# Loop through each product and prompt user for information
for i in range(num_products):
    print(f"\nProduct {i+1}")
    name = input("Enter product name: ")
    quantity = float(input("Enter quantity: "))
    price = float(input("Enter price: "))
    unit = input("Enter unit of measurement: ")

    # Calculate unit price
    unit_price = price / quantity

    # Add product information to list
    products.append({
        "name": name,
        "quantity": quantity,
        "price": price,
        "unit": unit,
        "unit_price": unit_price
    })

# Find the product with the best value for money
best_value = None
for product in products:
    if product["price"] <= budget:
        if best_value is None or product["unit_price"] < best_value["unit_price"]:
            best_value = product

# Display unit price for each product
print("\nUnit Prices:")
for product in products:
    print(f"{product['name']} - {product['unit_price']} per {product['unit']}")

# Display recommendation
if best_value is not None:
    print(f"\nBest value for money: {best_value['name']} - {best_value['unit_price']} per {best_value['unit']}")
else:
    print("Sorry, there are no products within your budget.")