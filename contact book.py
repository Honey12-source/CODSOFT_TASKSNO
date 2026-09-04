contacts = {}

while True:
    print("\n--- CONTACT BOOK ---")
    print("1. Add Contact")
    print("2. View Contacts")
    print("3. Search Contact")
    print("4. Update Contact")
    print("5. Delete Contact")
    print("6. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        name = input("Name: ")
        phone = input("Phone: ")
        email = input("Email: ")
        address = input("Address: ")

        contacts[name] = {
            "phone": phone,
            "email": email,
            "address": address
        }
        print("Contact added!")

    elif choice == "2":
        for name, details in contacts.items():
            print(name, "-", details["phone"])

    elif choice == "3":
        name = input("Enter name to search: ")

        if name in contacts:
            print(contacts[name])
        else:
            print("Contact not found!")

    elif choice == "4":
        name = input("Enter name to update: ")

        if name in contacts:
            contacts[name]["phone"] = input("New phone: ")
            contacts[name]["email"] = input("New email: ")
            contacts[name]["address"] = input("New address: ")
            print("Contact updated!")
        else:
            print("Contact not found!")

    elif choice == "5":
        name = input("Enter name to delete: ")

        if name in contacts:
            del contacts[name]
            print("Contact deleted!")
        else:
            print("Contact not found!")

    elif choice == "6":
        print("Thank you!")
        break

    else:
        print("Invalid choice!")