import argparse
import json

def parse_arguments():
   parser = argparse.ArgumentParser()
   parser.add_argument('filename', nargs='?', default='example_orders.json')
   return parser.parse_args()

def extract_customer_information(filename):
   customers = {}
   try:
        with open(filename, 'r') as file:
            orders = json.load(file)
            for order in orders:
                name = order.get("name")
                phone = order.get("phone")
                if name and phone:
                    customers[name] = phone
   except FileNotFoundError:
        print("Error: File not found.")
   except json.JSONDecodeError:
        print("Error: JSON decoding failed.")
   except Exception as e:
        print("An unexpected error occurred:", e)
   return customers
def save_customers(customers, output_filename='customers.json'):
    try:
        with open(output_filename, 'w') as file:
            json.dump(customers, file)
    except Exception as e:
        print("An unexpected error occurred while saving customers:", e)

def main():
    args = parse_arguments()
    customer_data = extract_customer_information(args.filename)
    save_customers(customer_data)
if __name__ == "__main__":
    main()
