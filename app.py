
from contact import add_new_contact, list_contacts, edit_contact, favorite_contact, list_favorite_contacts, delete_contact

contacts = [] 

while True:
    print("\nContact List Management")
    print("1 - Add a New Contact")
    print("2 - Show All Contacts")
    print("3 - Edit a Contact")
    print("4 - Mark/Unmark Favorite Contact")
    print("5 - Show Favorite Contacts")
    print("6 - Delete a Contact")
    print("7 - Exit")

    option = input("Choose an option: ")

    # match was added on python 3.10+
    match option:
        case "1":
            name = input("Enter the contact's name: ")
            email = input("Enter the contact's email: ")
            phone = input("Enter the contact's phone number: ")
            add_new_contact(contacts, name, email, phone)
        case "2":
            list_contacts(contacts)
        
        case "3": 
            list_contacts(contacts)
            index = input("Enter the number of the contact to edit: ")

            print("Leave blank if you don't want to change a field.")
            name = input("New name: ").strip() or None
            email = input("New email: ").strip() or None
            phone = input("New phone: ").strip() or None

            edit_contact(contacts, index, name, email, phone)
        
        case "4":
            list_contacts(contacts)
            index = input("Which contact do you want to favorite or unfavorite?")
            favorite_contact(contacts, index)
        
        case "5":
            list_favorite_contacts(contacts)
        case "6":
            list_contacts(contacts)
            index = input("Which contact do you want to remove?")
            delete_contact(contacts, index)
        case "7":
            break

print("Program finished!")