filename = "inventory.txt"

# Inventory will be stored in plain text like this:
# SKU: product1 | Price: 19.99
# Lot: 10.50, 5
# Lot: 10.75, 10

# Dictionary to store inventory keyed by SKU name
# Each value is another dictionary: {"price": 0.0, "lots": [{"cost": 0.0, "qty": 0}]}
inventory = {}

# Define menu options
while True:
    print("\n-- Inventory Manager --")
    print("1. Add new SKU")
    print("2. Add purchase lot to SKU")
    print("3. Edit sale price")
    print("4. View inventory")
    print("5. Save and Exit")

    choice = input("Choose an option: ")

    if choice not in ["1", "2", "3", "4", "5"]:
        print("Invalid choice. Try again.")
    
    if choice == "1":
        sku_name = input("Enter SKU name: ")
        if sku_name in inventory:
            print("SKU already exists.")
        else:
            price = float(input("Enter sale price: "))
            inventory[sku_name] = {"price": price, "lots": []}
            print("SKU added.")

    elif choice == "2":
        sku_name = input("Enter SKU to add lot to: ")
        if sku_name not in inventory:
            print("SKU not found.")
        else:
            cost = float(input("Enter cost of lot: "))
            qty = float(input("Enter quantity in lot: "))
            inventory[sku_name]["lots"].append({"cost": cost, "qty": qty})
            print("Lot added.")

    elif choice == "3":
        sku_name = input("Enter SKU to edit price: ")
        if sku_name not in inventory:
            print("SKU not found.")
        else:
            price = float(input("Enter new sale price: "))
            inventory[sku_name]["price"] = price
            print("Price updated.")

    elif choice == "4":
        for sku in inventory:
            price = inventory[sku]["price"]
            print(f"\nSKU: {sku}")
            print(f"  Sale Price: ${price:.2f}")
            for lot in inventory[sku]["lots"]:
                print(f"    Lot - Cost: ${lot['cost']} | Qty: {lot['qty']}")