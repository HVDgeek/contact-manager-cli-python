from typing import List, Optional

def add_new_contact(contacts: List, name: str, email: str, phone: str): 
    contact = {"name": name, "email": email, "phone": phone, "isFavorite": False}
    contacts.append(contact)
    print(f"Contact {name} was added!")
    return

def list_contacts(contacts: List):
    for index, contact in enumerate(contacts, start=1):
        status = "♥" if contact["isFavorite"] else "♡"
        name = contact["name"]
        email = contact["email"]
        phone = contact["phone"]
        print(f"{index}. [{status}] {name} --- {email} --- {phone}") 
    return

def edit_contact(contacts, contact_index, name:  Optional[str] = None, email: Optional[str] = None, phone:  Optional[str] = None):
    index = int(contact_index) - 1

    if 0 <= index < len(contacts):
        contact = contacts[index]
        updates = {"name": name, "email": email, "phone": phone}
        for key, value in updates.items():
            if value is not None:
                contact[key] = value
    else:
        print("Invalid contact!")
    return

def favorite_contact(contacts, contact_index):
    index = int(contact_index) - 1

    if 0 <= index < len(contacts):
        contact = contacts[index]
        contact["isFavorite"] = not contact["isFavorite"]

        if contact["isFavorite"]:
            print(f"{contact['name']} was added to favorites! ♥")
        else:
            print(f"{contact['name']} was removed from favorites. ♡")
    else:
        print("Invalid contact index. Please try again.")
    return

def list_favorite_contacts(contacts: List):
    favorites = [c for c in contacts if c.get("isFavorite", False)]

    if not favorites:
        print("No favorite contacts found.")
        return

    for index, contact in enumerate(favorites, start=1):
        name = contact["name"]
        email = contact["email"]
        phone = contact["phone"]
        print(f"{index}. {name} --- {email} --- {phone}")