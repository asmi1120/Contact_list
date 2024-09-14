def display_menu():
    print("\nContact List")
    print("1. Add Contact")
    print("2. View Contacts")
    print("3. Search Contact")
    print("4. Update Contact")
    print("5. Delete Contact")
    print("6. Exit")
def add_contact(contacts):
    name = input("Enter contact name: ")
    phone = input("Enter contact phone number: ")
    email = input("Enter contact email: ")
    address = input("Enter contact address: ")
    contacts[name] = {
        'phone': phone,
        'email': email,
        'address': address
    }
    print(f"Contact {name} added successfully.")
def view_contacts(contacts):
    if not contacts:
        print("No contacts available.")
    else:
        print("\nContacts List:")
        for name, details in contacts.items():
            print(f"Name: {name}")
            print(f"Phone: {details['phone']}")
            print(f"Email: {details['email']}")
            print(f"Address: {details['address']}")
            print()
def search_contact(contacts):
    search_term = input("Enter name or phone number to search: ")
    found = False
    for name, details in contacts.items():
        if search_term.lower() in name.lower() or search_term in details['phone']:
            print(f"\nFound Contact:")
            print(f"Name: {name}")
            print(f"Phone: {details['phone']}")
            print(f"Email: {details['email']}")
            print(f"Address: {details['address']}")
            print()
            found = True
    if not found:
        print("No contact found with the provided search term.")
def update_contact(contacts):
    name = input("Enter the name of the contact to update: ")
    if name in contacts:
        print(f"Updating contact {name}:")
        phone = input("Enter new phone number (or press Enter to keep current): ")
        email = input("Enter new email (or press Enter to keep current): ")
        address = input("Enter new address (or press Enter to keep current): ")
        
        if phone:
            contacts[name]['phone'] = phone
        if email:
            contacts[name]['email'] = email
        if address:
            contacts[name]['address'] = address
        
        print(f"Contact {name} updated successfully.")
    else:
        print(f"Contact {name} does not exist.")
def delete_contact(contacts):
    name = input("Enter the name of the contact to delete: ")
    if name in contacts:
        del contacts[name]
        print(f"Contact {name} deleted successfully.")
    else:
        print(f"Contact {name} does not exist.")
def main():
    contacts = {}
    while True:
        display_menu()
        choice = input("Enter your choice: ")
        if choice == '1':
            add_contact(contacts)
        elif choice == '2':
            view_contacts(contacts)
        elif choice == '3':
            search_contact(contacts)
        elif choice == '4':
            update_contact(contacts)
        elif choice == '5':
            delete_contact(contacts)
        elif choice == '6':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 6.")
if __name__ == "__main__":
    main()
