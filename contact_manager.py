
def add_contact(contacts):
    try:
        # Validate name
        name = input("Enter Name: ").strip()
        if not name.isalpha():
            raise ValueError("The contact's name must contain only letters.")

        # Validate email
        email = input("Enter Email: ").strip()

        # Validate phone number
        phone = input("Enter Phone Number: ").strip()
        if not phone.isdigit():
            raise ValueError("The phone number must be an integer.")

        # Validate address
        address = input("Enter Address: ").strip()

        # Prevent duplicate phone numbers
        if phone in [contact['phone'] for contact in contacts]:
            print("Error: Phone number already exists.")
            return

        # Append the contact to the list
        contacts.append({"name": name, "email": email, "phone": phone, "address": address})
        print("Contact added successfully!")

    except ValueError as e:
        print(f"Error: {e}")


def view_contacts(contacts):
    if not contacts:
        print("No contacts found.")
        return

    print("\nContacts:")
    for idx, contact in enumerate(contacts, 1):
        print(f"{idx}. Name: {contact['name']}, Email: {contact['email']}, "
              f"Phone: {contact['phone']}, Address: {contact['address']}")


def search_contact(contacts):
    search_query = input("Enter name or phone number to search: ")
    results = [contact for contact in contacts if search_query in contact.values()]

    if results:
        for result in results:
            print(f"Found: {result}")
    else:
        print("No matching contacts found.")


def remove_contact(contacts):
    phone_to_remove = input("Enter the phone number of the contact to remove: ")
    for contact in contacts:
        if contact["phone"] == phone_to_remove:
            contacts.remove(contact)
            print("Contact removed successfully!")
            return
    print("Contact not found.")
