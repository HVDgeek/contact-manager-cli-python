import unittest
from io import StringIO
import sys
from contextlib import redirect_stdout

from contact import add_new_contact, list_contacts, edit_contact

# Test Add New Contact
class TestAddNewContact(unittest.TestCase):

    def test_adds_contact_correctly(self):
        contacts = []

        with redirect_stdout(StringIO()):
            # any print here will be ignored in the terminal
            add_new_contact(contacts, "Alice", "alice@example.com", "123456789")

        self.assertEqual(len(contacts), 1)
        self.assertEqual(contacts[0]['name'], "Alice")
        self.assertEqual(contacts[0]['email'], "alice@example.com")
        self.assertEqual(contacts[0]['phone'], "123456789")
        self.assertFalse(contacts[0]['isFavorite'])

    def test_output_message(self):
        contacts = []
        captured_output = StringIO()
        sys.stdout = captured_output

        add_new_contact(contacts, "Bob", "bob@example.com", "987654321")

        sys.stdout = sys.__stdout__
        self.assertIn("Contact Bob was added!", captured_output.getvalue())

# Test List Contacts
class TestListContacts(unittest.TestCase):
    def test_prints_formatted_contact_list(self):
        contacts = [
            {"name": "Alice", "email": "alice@example.com", "phone": "123", "isFavorite": False},
            {"name": "Bob", "email": "bob@example.com", "phone": "456", "isFavorite": True}
        ]

        expected_output = (
            "1. [♡] Alice --- alice@example.com --- 123\n"
            "2. [♥] Bob --- bob@example.com --- 456\n"
        )

        output = StringIO()
        with redirect_stdout(output):
            list_contacts(contacts)

        self.assertEqual(output.getvalue(), expected_output)

# Test Edit Contact
class TestEditContact(unittest.TestCase):
    def setUp(self):
        self.contacts = [
            {"name": "Alice", "email": "alice@example.com", "phone": "111-111-1111"},
            {"name": "Bob", "email": "bob@example.com", "phone": "222-222-2222"},
            {"name": "Charlie", "email": "charlie@example.com", "phone": "333-333-3333"}
        ]

    def test_edit_name_and_phone(self):
        edit_contact(self.contacts, 2, name="Roberto", phone="999-999-9999")
        self.assertEqual(self.contacts[1]["name"], "Roberto")
        self.assertEqual(self.contacts[1]["email"], "bob@example.com")
        self.assertEqual(self.contacts[1]["phone"], "999-999-9999")

    def test_edit_all_fields(self):
        edit_contact(self.contacts, 1, name="Aline", email="aline@new.com", phone="000-000-0000")
        self.assertEqual(self.contacts[0], {
            "name": "Aline",
            "email": "aline@new.com",
            "phone": "000-000-0000"
        })
    
    def test_invalid_index(self):
        output = StringIO()
        with redirect_stdout(output):
            edit_contact(self.contacts, 10, name="Ghost")

        self.assertEqual(output.getvalue(), "Invalid contact!\n") 
    


if __name__ == '__main__':
    unittest.main()
