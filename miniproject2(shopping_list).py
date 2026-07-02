print("===== Simple Shopping List =====")
shopping_list = []
while True:
    print("\nChoose an option:")
    print("1. Add an item")
    print("2. Remove an item")
    print("3. View the shopping list")
    print("4. Quit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        print("\nEnter the item to add:")
        item = input().lower()
        for existing_item in shopping_list:
            if existing_item.lower() == item:
                print("Item already exists in the shopping list.")
                break
        else:
            shopping_list.append(item)
            print("Item has been added to the shopping list.")

    elif choice == 2:
        print("\nEnter the item to remove:")
        item = input().lower()
        for existing_item in shopping_list:
            if existing_item.lower() == item:
                shopping_list.remove(existing_item)
                print("Item has been removed from the shopping list.")
                break
        else:
            print("Item not found in the shopping list.")

    elif choice == 3:
        print("\nShopping List:")
        if not shopping_list:
            print("The shopping list is empty.")
        else:
            for item in shopping_list:
                print("-",item.capitalize())

    
    elif choice == 4:
        print("Thank you for using the shopping list!")
        break
    else:
        print("Invalid choice. Please try again.")
    
    continue_operation = input("Do you want to perform another operation? (y/n): ")
    if continue_operation.lower() != 'y':
        print("Thank you for using the shopping list!")
        break
       

