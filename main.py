#!/usr/bin/env python3
"""Mini project CLI: cafe menu and basket management"""

import json
import utils


########### MAIN APPLICATION ############

class CafeApp:

   
    #Initializes the CafeApp with empty lists for products, couriers, and orders
    def __init__(self):
        self.products = []
        self.couriers = []
        self.orders = []
        self.menus = {}
        self.main_menu = None
        self.product_menu = None    
        self.basket_menu = None
        self.product_edit_menu = None   
        self.order_management_menu = None
        self.order_edit_menu = None

    
    def run(self):
        #Importing csv files and menu json
        products = utils.load_data('products.csv')
        couriers = utils.load_data('couriers.csv')
        orders = utils.load_data('orders.csv')
        menus_data = utils.load_json('Menus.json')
        # menus_names = menus_data.keys()
        # for name in menus_names:
        #     print(f"Menu name: {name}")

        # Default to a standard Menu if the key isn't in the mapping
        for name_id, menu_dict in menus_data.items():
            self.menus[name_id] = Menu(menu_dict, name=menu_dict.get('title', name_id)) 
    


        #Define Child Menus
        self.main_menu = MainMenu(self.menus['MainMenu'].menu_dict, name=self.menus['MainMenu'].name) 
        self.product_menu = ProductMenu(self.menus['ProductMenu'].menu_dict, name=self.menus['ProductMenu'].name)
        self.basket_menu = BasketMenu(self.menus['BasketMenu'].menu_dict, name=self.menus['BasketMenu'].name)
        self.product_edit_menu = ProductEditMenu(self.menus['ProductEditMenu'].menu_dict, name=self.menus['ProductEditMenu'].name)
        self.order_management_menu = OrderManagementMenu(self.menus['OrderManagementMenu'].menu_dict, name=self.menus['OrderManagementMenu'].name)
        self.order_edit_menu = OrderEditMenu(self.menus['OrderEditMenu'].menu_dict, name=self.menus['OrderEditMenu'].name)

        self.main_menu.handle() # Start the main menu loop
   
     


############### MENU #################
class Menu:
    def __init__(self, menu_dict=None, name=None):
        self.name = name
        self.menu_dict = menu_dict or {}
        self.title = self.menu_dict.get("title", "Menu")

    def __str__(self):
        result = "" 
        for key, value in self.menu_dict.items():
            result += f"Menu Key: {key} | Menu Value: {value}\n"
        
        return result.strip() # .strip() removes the very last extra newline

    def display(self):
        print(f"\n{self.title}")
        for key in self.menu_dict.keys():
            if key != "title":
                print(f"{key} - {self.menu_dict[key]}")
            else:
                continue
    
    def get_choice(self):
        valid_options = {k for k in self.menu_dict.keys() if k != "title"}
        while True:
            choice = input("Select option: ").strip()
            if choice in valid_options:
                return choice
            print(f"Invalid choice. Enter one of: {', '.join(sorted(valid_options, key=int))}")
            self.display()  # Re-display menu after invalid choice
    
    def handle(self, name=None):
        while True:
            self.display()
            choice = self.get_choice()
            if choice == '0' and name == "MainMenu":
                print("Goodbye.")
                break
            elif choice == "0":
                print("Going back to previous menu.")
                break
            return choice


class MainMenu(Menu):


    
    def handle(self):
        print(self.title)
        self.display()
        choice = self.get_choice()
        # print(f"Main menu choice: {choice}")
        # if choice == "0":
        #     print("Goodbye.")
        #     #1break
        # elif choice == "1":
        #     self.product_menu.handle()
        # elif choice == "2":
        #     self.basket_menu.handle()
        # elif choice == "3":
        #     self.product_edit_menu.handle()
        # elif choice == "4":
        #     self.order_management_menu.handle()
        # elif choice == "5":
        #     self.order_edit_menu.handle()

class ProductMenu(Menu):
    pass
# def display_items(items, title):
#     """Display a list of items with indices."""
#     print(f"\n{title}:")
#     if not items:
#         print("(none)")
#     else:
#         for idx, item in enumerate(items):
#             print(f"{idx}: {item}")

# def handle_cafe_menu(cafe_items, basket):
#     """Handle the cafe menu for ordering."""
#     while True:
#         print_cafe_menu(cafe_items)
#         if not cafe_items:
#             choice = get_choice("No items to select, enter 0 to return", {"0"})
#             if choice == "0":
#                 break
#             continue
 
#         selected = get_numeric_choice("Select item number to add to basket", 0, len(cafe_items))
#         if selected == 0:
#             break
 
#         item = cafe_items[selected - 1]
#         if confirm(f"Add '{item}' to basket? (y/n)"):
#             basket.append(item)
#             print(f"'{item}' added to basket.")
#         else:
#             print("Not added.")
class BasketMenu(Menu):
    pass

# def handle_basket_menu(basket):
#     while True:
#         print_basket_menu()
#         choice = get_choice("Select main option", {"0", "1", "2", "3"})

#         if choice == "0":
#             break
 
#         elif choice == "1":
#             display_items(basket, "Items in your basket")
 
#         elif choice == "2":
#             if not basket:
#                 print("Your basket is empty")
#                 continue
#             display_items(basket, "Select item to remove")
#             idx = get_numeric_choice("Enter collerating index to remove", 0, len(basket) -1)  
#             removed = basket.pop(idx)
#             print(f"Removed '{removed}' from your basket.")  
 
#         elif choice == "3":
#             if confirm("Are you you want to clear the entire basket? (y/n)"):
#                 basket.clear()
#                 print("Basket Cleared.")
class ProductEditMenu(Menu):
    pass
# def handle_add_item(cafe_items):
#     """Handle adding a new unique item to the cafe menu."""
#     new_item = input("Enter new cafe item name: ").strip()
#     if new_item:
#         if new_item in cafe_items:
#             print(f"'{new_item}' is already in the cafe menu.")
#         else:
#             cafe_items.append(new_item)
#             print(f"'{new_item}' added to cafe menu.")
#     else:
#         print("No item name entered.")
 
 
# def handle_edit_menu(cafe_items):
#     """Handle the edit menu for updating or removing items."""
#     while True:
#         print_edit_menu()
#         edit_choice = input("Select edit option: ").strip()
 
#         if edit_choice == "0":
#             break
 
#         elif edit_choice == "1":
#             if not cafe_items:
#                 print("No items to update.")
#                 continue
#             display_items(cafe_items, "Current cafe items")
#             idx = get_numeric_choice("Enter index to update", 0, len(cafe_items) - 1)
#             new_name = input("Enter new name: ").strip()
#             if new_name:
#                 old_name = cafe_items[idx]
#                 cafe_items[idx] = new_name
#                 print(f"Updated '{old_name}' to '{new_name}'")
#             else:
#                 print("No new name entered.")
 
#         elif edit_choice == "2":
#             if not cafe_items:
#                 print("No items to remove.")
#                 continue
#             display_items(cafe_items, "Current cafe items")
#             idx = get_numeric_choice("Enter index to remove", 0, len(cafe_items) - 1)
#             removed = cafe_items.pop(idx)
#             print(f"Removed '{removed}' from cafe menu.")
 
#         else:
#             print("Invalid edit menu choice.")
class OrderManagementMenu(Menu):
    def handle(self, app_instance):
        while True:
            self.display()
            choice = self.get_choice()

            if choice == "0":
                break
            elif choice == "1": #View orders
                self.view_orders(app_instance)
            elif choice == "2": #Create Orders
                self.create_order(app_instance)
            elif choice == "3": #Update Existing Orders' status
                self.update_order_status(app_instance)
            elif choice == "4": #Edit Orders
                self.edit_order(app_instance)
            elif choice == "5": #Delete Orders
                self.delete_order(app_instance)

    #Choice 2 Creating Orders
    def create_order(self, app_instance):
        print("\n--- Create New Order ---")
        cust_name = input("Customer Name: ")
        cust_address = input("Customer Address: ")
        cust_phone = input("Customer Phone: ")
    
        #Print products with index
        print("\nAvailable Products:")
        for i, prod in enumerate(app_instance.products):
            print(f"[{i}] {prod['name']}")
        items = input("Enter product indexes (e.g. 1,2,5): ")

        #Print couriers with index
        print("\nAvailable Couriers:")
        for i, cour in enumerate(app_instance.couriers):
            print(f"[{i}] {cour['name']}")
        courier_idx = input("Select courier index: ")

        #Create dictionary and append
        new_order = {
            "customer_name": cust_name,
            "customer_address": cust_address,
            "customer_phone": cust_phone,
            "courier": courier_idx,
            "status": "preparing",
            "items": items
        }
        app_instance.orders.append(new_order)
        print("Order created successfully!")

    #Choice 3 Updating Order Status
    def update_order_status(self, app_instance):
        for i, order in enumerate(app_instance.orders):
            print(f"[{i}] {order['customer_name']} - {order['status']}")
        
        order_idx = int(input("Select order index to update: "))
        
        #Shows status for orders
        statuses = ["preparing", "ready", "out for delivery", "delivered"]
        for i, stat in enumerate(statuses):
            print(f"[{i}] {stat}")
        
        stat_idx = int(input("Select new status index: "))
        app_instance.orders[order_idx]['status'] = statuses[stat_idx]
        print("Status updated!")
    
    #Choice 4 Editing Orders
    def edit_order(self, app_instance):
        for i, order in enumerate(app_instance.orders):
            print(f"[{i}] {order['customer_name']}")
        
        order_idx = int(input("Select order index to edit: "))
        selected_order = app_instance.orders[order_idx]

        for key, value in selected_order.items():
            if key == "status": continue 
            new_val = input(f"Enter new {key} (Current: {value}) [Leave blank to keep]: ")
            if new_val.strip() != "":
                selected_order[key] = new_val
        print("Order updated!")
    
    #Choice 5 Deleting Orders
    def delete_order(self, app_instance):
        print("\n--- Delete Order ---")
        
        if not app_instance.orders:
            print("No orders to delete.")
            return

        for i, order in enumerate(app_instance.orders):
            print(f"[{i}] {order['customer_name']} - {order['status']}")

        try:
            order_idx = int(input("\nEnter order index to delete: "))
            deleted_order = app_instance.orders.pop(order_idx)
            print(f"Successfully deleted order for: {deleted_order['customer_name']}")
            
        except (ValueError, IndexError):
            print("Invalid index. No order was deleted.")

# # View all orders in orders.txt
# # Displays all orders with their details to the console
# # Inputs: None
# # Output: None (prints to console)
# def view_orders():
#     orders = load_orders()
#     if not orders:
#         print("No orders found.")
#         return
#     for i, order in enumerate(orders, 1):
#         print(f"Order {i}:")
#         print(f"  Name: {order.get('customer_name', 'N/A')}")
#         print(f"  Address: {order.get('customer_address', 'N/A')}")
#         print(f"  Phone: {order.get('customer_phone', 'N/A')}")
#         print(f"  Status: {order.get('status', 'N/A')}")
#         print()

# def handle_orders():
#     while True:
#         print("\nORDER MANAGEMENT")
#         print("1 - Create Order")
#         print("2 - View Orders")
#         print("3 - Edit Order")
#         print("4 - Delete Order")
#         print("0 - Back to main menu")
#         choice = get_choice("Select option", {"0", "1", "2", "3", "4"})
#         if choice == "0":
#             break
#         elif choice == "1":
#             create_order()
#             print("Order created.")
#         elif choice == "2":
#             view_orders()
#         elif choice == "3":
#             orders_list = load_orders()
#             if not orders_list:
#                 print("No orders to edit.")
#                 continue
#             view_orders()
#             idx = get_numeric_choice("Enter order number to edit", 1, len(orders_list))
#             edit_order(idx)
#         elif choice == "4":
#             orders_list = load_orders()
#             if not orders_list:
#                 print("No orders to delete.")
#                 continue
#             view_orders()
#             idx = get_numeric_choice("Enter order number to delete", 1, len(orders_list))
#             delete_order(idx)
 
class OrderEditMenu(Menu):
    pass

# Edit an order by index (1-based)
# # Allows the user to modify specific fields of an order interactively
# # Inputs: index (int, 1-based order number)
# # Output: None (modifies file and prints status)
# def edit_order(index):
#     orders = load_orders()
#     if index < 1 or index > len(orders):
#         print("Invalid order index.")
#         return
#     order = orders[index - 1]
#     print("Current order:")
#     print(f"  Name: {order.get('customer_name', 'N/A')}")
#     print(f"  Address: {order.get('customer_address', 'N/A')}")
#     print(f"  Phone: {order.get('customer_phone', 'N/A')}")
#     print(f"  Status: {order.get('status', 'N/A')}")
#     print()
#     # Define available fields for editing
#     fields = {
#         '1': ('customer_name', 'Name'),
#         '2': ('customer_address', 'Address'),
#         '3': ('customer_phone', 'Phone'),
#         '4': ('status', 'Status')
#     }
#     # Loop to allow multiple edits until user chooses to stop
#     while True:
#         print("Which field do you want to change?")
#         for k, v in fields.items():
#             print(f"{k} - {v[1]}")
#         print("0 - Done editing")
#         choice = get_choice("Enter choice", {"0", "1", "2", "3", "4"})
#         if choice == '0':
#             break
#         elif choice in fields:
#             key, label = fields[choice]
#             new_value = input(f"Enter new {label.lower()}: ").strip()
#             if new_value:
#                 order[key] = new_value
#                 print(f"{label} updated.")
#             else:
#                 print("No change made.")
#         else:
#             # This shouldn't happen since get_choice validates
#             print("Invalid choice.")
#     save_orders(orders)
#     print("Order updated.")

            
 

 
 
# def get_valid_index(items, prompt):
#     """Prompt for a valid index within the items list."""
#     while True:
#         idx_input = input(f"{prompt} (0-{len(items)-1}): ").strip()
#         if not idx_input.isdigit():
#             print("Invalid input. Please enter a number.")
#             continue
#         idx = int(idx_input)
#         if idx < 0 or idx >= len(items):
#             print("Index out of range.")
#             continue
#         return idx
 
 
# def confirm(prompt):
#     """Ask user to confirm yes/no."""
#     return get_choice(prompt, {"y", "n"}) == "y"
 
 
# def get_numeric_choice(prompt, minimum, maximum):
#     """Prompt for numeric choice inside range."""
#     while True:
#         value = input(f"{prompt} ({minimum}-{maximum}): ").strip()
#         if not value.isdigit():
#             print("Invalid input. Please enter a number.")
#             continue
#         num = int(value)
#         if num < minimum or num > maximum:
#             print("Number out of range.")
#             continue
#         return num
 
 

 
 

 
 

 
# ################# ORDER FUNCTIONS #################
# # List to store all orders
# orders = []

# # Create a new order by getting customer information from user input
# # Inputs: None (gets input from user)
# # Output: dict - the created order dictionary
# def create_order():
#     name = input("Enter customer name: ")
#     address = input("Enter customer address: ")
#     phone = input("Enter customer phone: ")
#     order = {
#         'customer_name': name,
#         'customer_address': address,
#         'customer_phone': phone,
#         'status': 'pending'
#     }
#     orders.append(order)
#     save_orders(orders)
#     return order


# # Helper function to load orders from orders.txt
# # Loads and parses all orders from the file into a list of dictionaries
# # Inputs: None
# # Output: list of order dictionaries
# def load_orders():
#     try:
#         with open('orders.txt', 'r') as f:
#             content = f.read()
#         orders = []
#         # Split by '}\n\n' to get individual order blocks
#         blocks = content.strip().split('}\n\n')
#         for block in blocks:
#             if block.strip():
#                 block = block.strip()
#                 # Ensure the block ends with '}' for valid JSON
#                 if not block.endswith('}'):
#                     block += '}'
#                 if block.startswith('{'):
#                     order = json.loads(block)
#                     orders.append(order)
#         return orders
#     except FileNotFoundError:
#         print("orders.txt not found.")
#         return []
#     except json.JSONDecodeError as e:
#         print(f"Error parsing orders.txt: {e}")
#         return []

# # Helper function to save orders to orders.txt
# # Writes the list of orders back to the file in JSON format
# # Inputs: orders (list of dictionaries)
# # Output: None
# def save_orders(orders):
#     with open('orders.txt', 'w') as f:
#         for order in orders:
#             json.dump(order, f, indent=4)
#             f.write('\n\n')



# 

# # Delete an order by index (1-based)
# # Removes the specified order from the file
# # Inputs: index (int, 1-based order number)
# # Output: None (modifies file and prints confirmation)
# def delete_order(index):
#     orders = load_orders()
#     if index < 1 or index > len(orders):
#         print("Invalid order index.")
#         return
#     del orders[index - 1]
#     save_orders(orders)
#     print("Order deleted.")






# ################# MAIN APPLICATION LOOP #################

 
 
 
if __name__ == "__main__":
    app = CafeApp()
    app.run()


