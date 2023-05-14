contacts = {}

while True:
    print("\n---- Contact Book ----")
    print("1. Add contact Name")
    print("2. Remove contact")
    print("3. Show contacts")
    print("4. Exit")

    choice = input("Enter your choice (add,remove,show, or exit): ")

    if choice == "add":
        name = input("Enter name: ")
        number = input("Enter phone number: ")
        contacts[name] = number
        print(f"{name} added to contacts")
    elif choice == "remove":
        name = input("Enter name to remove: ")
        if name in contacts:
            del contacts[name]
            print(f"{name} removed from contacts")
        else:
            print(f"{name} not found in contacts")
    elif choice == "show":
        print("\n---- Contacts ----")
        for name, number in contacts.items():
            print(f"{name}: {number}")
    elif choice == "exit":
        print("Exiting contact list...")
        print("THANK YOU")
        break
    else:
        print("Invalid choice. Try again.")
