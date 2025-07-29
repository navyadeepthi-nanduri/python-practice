



contacts = {}

while True:
    print("\n--- Contact Book ---")
    print("1. Add Contact")
    print("2. Search Contact")
    print("3. Delete Contact")
    print("4. Show All Contacts")
    print("5. Total Number of Contacts")
    print("6. Clear All Contacts")
    print("7. Copy Contact Book")
    print("8. Show All Names")
    print("9. Show All Phone Numbers")
    print("10. Add Multiple Contacts")
    print("11. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        name = input("Enter name: ")
        phone = input("Enter phone number: ")
        contacts[name] = phone
        print("Contact added successfully!")

    elif choice == "2":
        name = input("Enter name to search: ")
        # Using .get() for safe search
        result = contacts.get(name)
        if result:
            print(f"{name}'s number is {result}")
        else:
            print("Contact not found.")

    elif choice == "3":
        name = input("Enter name to delete: ")
        if name in contacts:
            # Using .pop() instead of del
            removed = contacts.pop(name)
            print(f"{name} deleted (number: {removed}).")
        else:
            print("Contact not found.")

    elif choice == "4":
        if not contacts:
            print("No contacts to display.")
        else:
            for name, phone in contacts.items():
                print(f"{name}: {phone}")

    elif choice == "5":
        print(f"Total contacts: {len(contacts)}")

    elif choice == "6":
        confirm = input("Are you sure you want to delete all contacts? (yes/no): ")
        if confirm.lower() == "yes":
            contacts.clear()
            print("All contacts cleared.")
        else:
            print("Operation cancelled.")

    elif choice == "7":
        copied_contacts = contacts.copy()
        print("Copied Contact Book:")
        for name, phone in copied_contacts.items():
            print(f"{name}: {phone}")

    elif choice == "8":
        print("All Names:")
        for name in contacts.keys():
            print(name)

    elif choice == "9":
        print("All Phone Numbers:")
        for phone in contacts.values():
            print(phone)

    elif choice == "10":
        more_contacts = {
            "Navya": "9876543210",
            "Bhavya": "8765432109"
        }
        contacts.update(more_contacts)
        print("Multiple contacts added successfully!")

    elif choice == "11":
        print("Exiting Contact Book. Goodbye!")
        break

    else:
        print("Invalid choice. Try again.")

