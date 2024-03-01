# WebMidProject
This Python script is designed to analyze the orders received by a Dosa restaurant over a period of time. It processes the order data from a JSON file and creates two new JSON files containing customer information and item details.

# Features
1. customers.json: Contains a list of customers along with their phone numbers.

2. items.json: Provides information about the menu items, including their prices and the number of times each item has been ordered.

# Requirements
  Python 3.x

# Usage
1. Clone this repository or download customer.py, items.py and example_orders.json
2. Place the JSON file containing order data (example_orders.json) in the same directory as the .py files(customer.py, items.py).
3. Open a terminal or command prompt and navigate to the directory containing the customer.py, items.py and the JSON file, or open the folder in the VScode.
4. Run the code by executing the following commands:
   python customer.py example_orders.json
   python items.py example_orders.json
5. After execution, two new JSON files (customers.json and items.json) will be created in the same directory, containing the extracted customer information and item details, respectively.

# Sample Output
customers.json

{
    "609-555-0124": "Karl",
    "732-555-1234": "Mike",
    ...
}

items.json

{
    "Butter Masala Dosa": {
        "price": 12.95,
        "orders": 52
    },
    "Butter Mysore Masala Dosa": {
        "price": 11.95,
        "orders": 12
    },
    ...
}


