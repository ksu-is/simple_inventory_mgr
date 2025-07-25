import os
filename = "inventory.txt"

# Inventory will be stored in plain text like this:
# SKU: product1 | Price: 19.99
# Lot: 10.50, 5
# Lot: 10.75, 10

# Dictionary to store inventory keyed by SKU name
# Each value is another dictionary: {"price": 0.0, "lots": [{"cost": 0.0, "qty": 0}]}
inventory = {}

def save_inventory():
    with open(filename, "w") as file:
        for sku in inventory:
            price = inventory[sku]["price"]
            file.write(f"SKU: {sku} | Price: {price}\n")
            for lot in inventory[sku]["lots"]:
                file.write(f"Lot: {lot['cost']}, {lot['qty']}\n")
def get_avg_cost(lots):
    total_cost = 0
    total_qty = 0
    for lot in lots:
        total_cost += lot["cost"] * lot["qty"]
        total_qty += lot["qty"]
    if total_qty == 0:
        return 0
    return total_cost / total_qty

if os.path.exists(filename):
    with open(filename, "r") as file:
        lines = file.readlines()
        current_sku = ""
        for line in lines:
            line = line.strip()
            if line.startswith("SKU:"):
                parts = line.split("|")
                current_sku = parts[0].replace("SKU:", "").strip()
                sale_price = float(parts[1].replace("Price:", "").strip())
                inventory[current_sku] = {
                    "price": sale_price,
                    "lots": []
                }
            elif line.startswith("Lot:"):
                parts = line.replace("Lot:", "").strip().split(",")
                cost = float(parts[0])
                qty = float(parts[1])
                inventory[current_sku]["lots"].append({"cost": cost, "qty": qty})

# Define menu options
while True:
    print("\n\033[1;34m-- Inventory Manager --\033[0m")
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
            avg_cost = get_avg_cost(inventory[sku]["lots"]) 
            print(f"\nSKU: {sku}")
            print(f"  Sale Price: ${price:.2f}")
            print(f"  Average Cost: \033[94m${avg_cost:.2f}\033[0m")
            for lot in inventory[sku]["lots"]:
                print(f"    Lot - Cost: ${lot['cost']} | Qty: {lot['qty']}")

    elif choice == "5":
        save_inventory()
        print("Inventory saved. Goodbye.")
        break