def display_menu():
    print("Shopping List Manager")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View List")
    print("4. Exit")

def main():
    shopping_list = []
    while True:
        display_menu()
        choice = input("Enter your choice: ")

        if choice == '1':
            item = input("Enter item to add to your list: ")
            shopping_list.append(item)
            print(f"{item} has been added to your shopping list")
            pass
        elif choice == '2':
            item = input("Enter item to be removed: ")
            shopping_list.remove(item)
            print(f"{item} has been removed from your shopping list.")
            pass
        elif choice == '3':
            print(f"These are the items in your shopping list: {shopping_list}")
            pass
        elif choice == '4':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
