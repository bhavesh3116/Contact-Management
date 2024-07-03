Contact_Book = {}
# Function to add name , number and Email

def add_contact(name, number, email):
    Contact_Book[name] = {'number': number, 'email': email}
    print("Contact added successfully!")

# Function to View Contact_Book
def view_contact():
    if not Contact_Book:
        print("No contacts found!")
    else:
        for name, info in Contact_Book.items():
            print(f"Name: {name}, Phone: {info['number']}, Email: {info['email']}")

# Function to Edit Contact Details
def edit_contact(name, number=None, email=None):
    if name in Contact_Book:
        if number:
            Contact_Book[name]['number'] = number 
        if email:
            Contact_Book[name]['email'] = email
        print(f"Contact '{name}' updated successfully!")
    else:
        print(f"Contact '{name}' not found!")

# Function to Delete Contact 
def del_contact(name):
    if name in Contact_Book:
        del Contact_Book[name]
        print(f"Contact '{name}' deleted successfully!")
    else:
        print(f"Contact '{name}' not found!")


if __name__ == "__main__":
    while True:
        print("\nChoose an option:")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Edit Contact")
        print("4. Delete Contact")
        print("5. Exit")
        
        choice = input("Enter choice: ")
        
        if choice == '1':
            name = input("Enter name: ")
            number = input("Enter number: ")
            email = input("Enter email: ")
            add_contact(name, number, email)
        
        elif choice == '2':
            view_contact()
        
        elif choice == '3':
            name = input("Enter name to edit: ")
            number = input("Enter new number (press Enter to skip): ")
            email = input("Enter new email (press Enter to skip): ")
            edit_contact(name, number if number else None, email if email else None)
        
        elif choice == '4':
            name = input("Enter name to delete: ")
            del_contact(name)
        
        elif choice == '5':
            print("Exiting...")
            break
        
        else:
            print("Invalid choice!")
