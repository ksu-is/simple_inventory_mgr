filename = "inventory.txt"

# Inventory will be stored in plain text like this:
# SKU: product1 | Price: 19.99
# Lot: 10.50, 5
# Lot: 10.75, 10

# Dictionary to store inventory keyed by SKU name
# Each value is another dictionary: {"price": 0.0, "lots": [{"cost": 0.0, "qty": 0}]}
inventory = {}

# Define menu options
print("1. Add new SKU")
print("2. Add purchase lot to SKU")
print("3. Edit sale price")
print("4. View inventory")
print("5. Save and Exit")