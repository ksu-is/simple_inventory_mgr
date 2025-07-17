
# Simple Inventory Manager

This version runs in the terminal and saves your inventory data to a plain text file (`inventory.txt`) that is human-readable and easily editable.

---

## Features

- Add and store SKU items
- Add multiple purchase lots to each SKU (with cost and quantity)
- Automatically calculate the average cost of each SKU
- Set and edit sale price per SKU
- View full inventory with costs and price
- Save/load inventory to/from a text file
- Terminal colors for better readability

---

## Getting Started

### Requirements

- Python 3.x

### Run the Program

```bash
python inventory_manager.py
```

The program will continue running in a loop until you choose "Save and Exit".

---

## File Structure

```
inventory_manager.py   # Main script
inventory.txt          # Data file (auto-generated after saving)
README.md              # Project description and roadmap
```

---

## Roadmap

### Step 1: Plan the Structure
 - [ ] Decide what the inventory manager should do

 - [ ] List out basic operations: add SKU, add lots, edit price, view data, save to file

### Step 2: Set Up the Data Format
- [ ] Choose Python dictionary to store SKU data

- [ ] Use a list of dictionaries to track purchase lots

- [ ] Design plain-text format for file storage

### Step 3: Build Basic Input Loop
- [ ] Use while True loop to show options and take user input

- [ ] Add input validation and user-friendly prompts

### Step 4: Implement Each Feature
- [ ] Add new SKUs

- [ ] Add lots with cost and quantity

 - [ ] Edit sale price

 - [ ] View full inventory with average cost calculation

### Step 5: Save and Load to File
- [ ] Write inventory to inventory.txt

 - [ ] Load inventory from inventory.txt on startup

### Step 6: Add Terminal Colors
 - [ ] Use ANSI escape codes for colored text output
