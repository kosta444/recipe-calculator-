'''
  Name: 
  James Hargest College
  Programming Internal for 2.7 & 2.8 ~ 12 credits
  Due: 6 April 2023
  
  TIP: Use assessment guide to help guide you through this Internal
'''
import requests
import json

# Prompt user for budget
budget = float(input("Enter your budget: "))

# Make API call to retrieve products within budget
response = requests.get(f"https://exampleapi.com/products?budget={budget}")
products = json.loads(response.content)

# Display products
for product in products:
    print(product["name"])
    print(product["description"])
    print(product["price"])
    print(product["retailer"])
    print("-" * 50)

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

# Display unit price for each product
print("\nUnit Prices:")
for product in products:
    print(f"{product['name']} - {product['unit_price']} per {product['unit']}")
  