import os

# FILE UTILITIES
# Handles reading data from a text file into a Python list
def load_list(filename):
    if not os.path.exists(filename):
        return [] # Return an empty list if the file doesn't exist yet
    with open(filename, "r") as f:
        # Read lines, remove whitespace, and ignore empty lines
        return [line.strip() for line in f if line.strip()]

# Handles writing the current list back to the text file for permanent storage
def save_list(filename, data):
    with open(filename, "w") as f:
        for item in data:
            f.write(item + "\n") # Save each item on a new line

# DATA MODEL
# Defines what a 'Product' is and how it behaves
class Product:
    def __init__(self, name):
        self.name = name

    def get_name(self):
        return self.name

    def set_name(self, new_name):
        self.name = new_name

    # Controls how the product looks when printed (e.g., print(product))
    def __str__(self):
        return self.name

# USER INTERFACE / CONTROLLER
# Manages the menu logic and interactions with the product list
class ProductMenu:
    def __init__(self, products):
        # Store a reference to the list so changes persist outside the class
        self.products_ref = products

    def execute(self):
        # Main application loop; keeps the menu running until user exits
        while True:
            print("\n--- Product Menu ---")
            print("  0: Return to main menu")
            print("  1: View all products")
            print("  2: Add a new product")
            print("  3: Update a product")
            print("  4: Delete a product")

            choice = input("\nEnter option: ").strip()

            # Route the user's choice to the appropriate internal method
            if choice == "0":
                return False # Exit the loop and return to main code
            elif choice == "1":
                self._print_products()
            elif choice == "2":
                self._create_product()
            elif choice == "3":
                self._update_product()
            elif choice == "4":
                self._delete_product()
            else:
                print("Invalid option.")

    # Helper to display the current list with numeric indices
    def _print_products(self):
        if not self.products_ref:
            print("No products found.")
            return
        print("\n--- Products ---")
        for i, product in enumerate(self.products_ref):
            print(f"  {i}: {product}")

    # Logic to add a new Product object to the list
    def _create_product(self):
        name = input("Enter new product name: ").strip()
        if name:
            self.products_ref.append(Product(name))
            print(f"'{name}' added.")
        else:
            print("Product name cannot be empty.")

    # Logic to select an existing product and change its name
    def _update_product(self):
        self._print_products()
        try:
            index = int(input("Enter index of product to update: "))
            new_name = input("Enter new product name: ").strip()
            if 0 <= index < len(self.products_ref):
                if new_name:
                    self.products_ref[index].set_name(new_name)
                    print(f"Product updated to '{new_name}'.")
                else:
                    print("Name cannot be empty.")
            else:
                print("Invalid index.")
        except ValueError:
            print("Please enter a valid number.") # Prevents crash on non-integer input

    # Logic to remove a product from the list by its index
    def _delete_product(self):
        self._print_products()
        try:
            index = int(input("Enter index of product to delete: "))
            if 0 <= index < len(self.products_ref):
                removed = self.products_ref.pop(index)
                print(f"'{removed}' deleted.")
            else:
                print("Invalid index.")
        except ValueError:
            print("Please enter a valid number.")

# MAIN EXECUTION FLOW
# 1. Load existing data from file
raw_list = load_list("products.txt")
# 2. Convert raw strings into a list of Product objects
products = [Product(name) for name in raw_list]

# 3. Initialise and run the menu system
menu = ProductMenu(products)
menu.execute()

# 4. Once finished, extract names from objects and save back to the file
save_list("products.txt", [p.get_name() for p in products])
print("Products saved!")