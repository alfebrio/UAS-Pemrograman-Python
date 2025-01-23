import requests
import json

API_BASE_URL = "http://127.0.0.1:8000"

def print_response(response):
    if response.status_code in [200, 201]:
        print(json.dumps(response.json(), indent=4))
    else:
        print(f"Error {response.status_code}: {response.text}")

def create_item():
    print("Enter phone details:")
    name = input("Name: ")
    brand = input("Brand: ")
    category = input("Category: ")
    released = int(input("Released Year: "))
    display = input("Display: ")
    camera = input("Camera: ")
    ram = input("RAM: ")
    chipset = input("Chipset: ")
    battery = input("Battery: ")
    price = float(input("Price: "))

    payload = {
        "name": name,
        "brand": brand,
        "category": category,
        "released": released,
        "display": display,
        "camera": camera,
        "ram": ram,
        "chipset": chipset,
        "battery": battery,
        "price": price
    }
    response = requests.post(f"{API_BASE_URL}/phones", json=payload)
    print_response(response)

def read_all_items():
    response = requests.get(f"{API_BASE_URL}/phones")
    print_response(response)

def read_item_by_id():
    item_id = input("Enter phone ID: ")
    response = requests.get(f"{API_BASE_URL}/phones/{item_id}")
    print_response(response)

def update_item():
    item_id = input("Enter phone ID to update: ")
    print("Enter updated details:")
    name = input("Name: ")
    brand = input("Brand: ")
    category = input("Category: ")
    released = int(input("Released Year: "))
    display = input("Display: ")
    camera = input("Camera: ")
    ram = input("RAM: ")
    chipset = input("Chipset: ")
    battery = input("Battery: ")
    price = float(input("Price: "))

    payload = {
        "name": name,
        "brand": brand,
        "category": category,
        "released": released,
        "display": display,
        "camera": camera,
        "ram": ram,
        "chipset": chipset,
        "battery": battery,
        "price": price
    }
    response = requests.put(f"{API_BASE_URL}/phones/{item_id}", json=payload)
    print_response(response)

def delete_item():
    item_id = input("Enter phone ID to delete: ")
    response = requests.delete(f"{API_BASE_URL}/phones/{item_id}")
    print_response(response)

def main():
    while True:
        print("\nPhone Menu:")
        print("1. Create Phone Data")
        print("2. Read All Phones")
        print("3. Read Phone by ID")
        print("4. Update Phone")
        print("5. Delete Phone")
        print("6. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            create_item()
        elif choice == "2":
            read_all_items()
        elif choice == "3":
            read_item_by_id()
        elif choice == "4":
            update_item()
        elif choice == "5":
            delete_item()
        elif choice == "6":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
