contacts = {}

def add_contact():
    """Add a new contact"""
    name = input("Enter name: ").strip()
    if name in contacts:
        print("Contact already exists!\n")
        return
    phone = input("Enter phone number: ").strip()
    email = input("Enter email: ").strip()
    contacts[name] = {"phone": phone, "email": email}
    print(f"✓ Contact '{name}' added!\n")

def search_contact():
    name = input("Enter name to search: ").strip()
    if name in contacts:
        contact = contacts[name]
        print(f"\nName: {name}")
        print(f"Phone: {contact['phone']}")
        print(f"Email: {contact['email']}\n")
    else:
        print("Contact not found!\n")

def delete_contact():
    """Delete a contact"""
    name = input("Enter name to delete: ").strip()
    if name in contacts:
        del contacts[name]
        print(f"✓ Contact '{name}' deleted!\n")
    else:
        print("Contact not found!\n")

def list_contacts():
    """List all contacts"""
    if not contacts:
        print("No contacts found!\n")
        return
    print("\n" + "=" * 50)
    print("ALL CONTACTS")
    print("=" * 50)
    for name, info in contacts.items():
        print(f"\nName: {name}")
        print(f"Phone: {info['phone']}")
        print(f"Email: {info['email']}")
    print("=" * 50 + "\n")

def main():
    """Main menu"""
    while True:
        print("--- CONTACT BOOK ---")
        print("1. Add Contact")
        print("2. Search Contact")
        print("3. Delete Contact")
        print("4. List All Contacts")
        print("5. Exit")
        
        choice = input("Choose option (1-5): ").strip()
        
        if choice == "1":
            add_contact()
        elif choice == "2":
            search_contact()
        elif choice == "3":
            delete_contact()
        elif choice == "4":
            list_contacts()
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid option! Please try again.\n")

if __name__ == "__main__":
    main()