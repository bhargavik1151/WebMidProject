import json
import sys

def process_items(orders):
    items = {}
    for order in orders:
        # Assuming each order is a list of items
        for item in order.get('items', []):
            item_name = item.get('name')
            item_price = item.get('price')
            if item_name:
                if item_name not in items:
                    items[item_name] = {"price": item_price, "orders": 1}
                else:
                    # Update the orders count; assume price remains constant
                    items[item_name]["orders"] += 1
    return items

def main():
    if len(sys.argv) < 2:
        print("Usage: python script.py input_orders.json")
        sys.exit(1)

    input_file = sys.argv[1]

    try:
        with open(input_file, 'r') as f:
            orders = json.load(f)
    except FileNotFoundError:
        print(f"File '{input_file}' not found.")
        sys.exit(1)
    except json.JSONDecodeError:
        print(f"Error decoding JSON from '{input_file}'.")
        sys.exit(1)

    items = process_items(orders)

    output_file = "items.json"
    with open(output_file, 'w') as f:
        json.dump(items, f, indent=4)

    print(f"Items information has been saved to '{output_file}'.")

if __name__ == "__main__":
    main()
