import csv
import os

class Courier:
    def __init__(self, name, status="Ready to pick up"):
        self.name = name
        self.status = status

    def __repr__(self):
        return f"{self.name} | Status: {self.status}"

class CourierManager:
    def __init__(self, filename='couriers.csv'):
        self.filename = filename
        self.couriers = []
        self.load_data()

    def load_data(self):
        """Pulls information from the CSV file."""
        if not os.path.exists(self.filename):
            # Create file with headers if it doesn't exist
            self.save_data()
            return

        self.couriers = []
        with open(self.filename, mode='r', newline='') as file:
            reader = csv.DictReader(file)
            for row in reader:
                self.couriers.append(Courier(row['name'], row['status']))

    def save_data(self):
        """Saves current courier list back to the CSV."""
        with open(self.filename, mode='w', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=['name', 'status'])
            writer.writeheader()
            for c in self.couriers:
                writer.writerow({'name': c.name, 'status': c.status})

    def add_courier(self, name):
        if name:
            self.couriers.append(Courier(name))
            self.save_data()
            print(f"Courier {name} added.")
        else:
            print("Name cannot be empty.")

    def update_name(self, index, new_name):
        if 0 <= index < len(self.couriers):
            self.couriers[index].name = new_name
            self.save_data()
            print("Name updated.")
        else:
            print("Invalid index.")

    def update_status(self, index):
        if 0 <= index < len(self.couriers):
            statuses = ["Ready to pick up", "En route", "Delivered"]
            print("\nSelect new status:")
            for i, s in enumerate(statuses):
                print(f"{i}: {s}")
            
            try:
                choice = int(input("Choice: "))
                self.couriers[index].status = statuses[choice]
                self.save_data()
                print(f"Status updated to {statuses[choice]}.")
            except (ValueError, IndexError):
                print("Invalid status selection.")
        else:
            print("Invalid courier index.")

# --- UI Logic ---
manager = CourierManager()

def show_menu():
    print("\n--- Courier Management System ---")
    print("1. View all couriers")
    print("2. Add a new courier")
    print("3. Update courier name")
    print("4. Update courier status")
    print("0. Exit")

while True:
    show_menu()
    choice = input("\nEnter your choice: ")

    if choice == "1":
        print(f"\n{'ID':<3} | {'Name':<15} | Status")
        print("-" * 40)
        for i, c in enumerate(manager.couriers):
            print(f"{i:<3} | {c}")

    elif choice == "2":
        name = input("Enter courier name: ").strip()
        manager.add_courier(name)

    elif choice == "3":
        try:
            idx = int(input("Enter courier index to rename: "))
            new_name = input("Enter new name: ").strip()
            manager.update_name(idx, new_name)
        except ValueError:
            print("Please enter a valid number.")

    elif choice == "4":
        try:
            idx = int(input("Enter courier index to update status: "))
            manager.update_status(idx)
        except ValueError:
            print("Please enter a valid number.")

    elif choice == "0":
        print("Saving and exiting...")
        break
    else:
        print("Invalid choice.")