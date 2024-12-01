from contact_manager import add_contact, view_contacts, search_contact, remove_contact
from file_handler import load_contacts, save_contacts

# Load contacts at program start
contacts = load_contacts()


def main_menu():
    while True:
        print("\nContact Book Management System")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Search Contact")
        print("4. Remove Contact")
        print("5. Exit")

        choice = input("Choose an option: ")
        if choice == "1":
            add_contact(contacts)
            save_contacts(contacts)
        elif choice == "2":
            view_contacts(contacts)
        elif choice == "3":
            search_contact(contacts)
        elif choice == "4":
            remove_contact(contacts)
            save_contacts(contacts)
        elif choice == "5":
            print("Exiting... Goodbye!")
            break
        else:
            print("Invalid option. Please try again.")


if __name__ == "__main__":
    main_menu()
