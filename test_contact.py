import unittest
from io import StringIO
import sys
from contextlib import redirect_stdout

from contact import add_new_contact, list_contacts, edit_contact, favorite_contact, list_favorite_contacts, delete_contact

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
    

# Test Favorite and Unfavorite Contact
class TestFavoriteContact(unittest.TestCase):
    def setUp(self):
        self.contacts = [
            {"name": "Alice", "email": "alice@example.com", "phone": "1234", "isFavorite": False},
            {"name": "Bob", "email": "bob@example.com", "phone": "5678", "isFavorite": True}
        ]
    
    def test_favorite_added(self):
        captured_output = StringIO()
        sys.stdout = captured_output

        favorite_contact(self.contacts, "1") 

        sys.stdout = sys.__stdout__  

        self.assertTrue(self.contacts[0]["isFavorite"], "Alice should now be favorite")
        self.assertIn("Alice was added to favorites!", captured_output.getvalue())
    
    def test_favorite_removed(self):
        captured_output = StringIO()
        sys.stdout = captured_output

        favorite_contact(self.contacts, "2")

        sys.stdout = sys.__stdout__

        self.assertFalse(self.contacts[1]["isFavorite"], "Bob should no longer be favorite")
        self.assertIn("Bob was removed from favorites.", captured_output.getvalue())


class TestListFavoriteContacts(unittest.TestCase):
    def setUp(self):
        self.contacts = [
            {"name": "Alice", "email": "alice@example.com", "phone": "1234", "isFavorite": True},
            {"name": "Bob", "email": "bob@example.com", "phone": "5678", "isFavorite": False},
            {"name": "Carol", "email": "carol@example.com", "phone": "9012", "isFavorite": True},
        ]
    
    def test_lists_only_favorites(self):
        captured_output = StringIO()
        sys.stdout = captured_output

        list_favorite_contacts(self.contacts)

        sys.stdout = sys.__stdout__

        output = captured_output.getvalue()
        # Alice and Carol should be listed, Bob should NOT
        self.assertIn("1. Alice --- alice@example.com --- 1234", output)
        self.assertIn("2. Carol --- carol@example.com --- 9012", output)
        self.assertNotIn("Bob", output)
    
    def test_no_favorites(self):
        contacts_no_favorites = [
            {"name": "Dave", "email": "dave@example.com", "phone": "3456", "isFavorite": False}
        ]

        captured_output = StringIO()
        sys.stdout = captured_output

        list_favorite_contacts(contacts_no_favorites)

        sys.stdout = sys.__stdout__

        output = captured_output.getvalue()
        self.assertIn("No favorite contacts found.", output)

class TestDeleteContact(unittest.TestCase):
    def setUp(self):
        self.contacts = [
            {"name": "Alice", "email": "alice@example.com", "phone": "1234", "isFavorite": True},
            {"name": "Bob", "email": "bob@example.com", "phone": "5678", "isFavorite": False},
            {"name": "Carol", "email": "carol@example.com", "phone": "9012", "isFavorite": True},
        ]


    def test_contact_removed(self):
        captured_output = StringIO()
        sys.stdout = captured_output

        delete_contact(self.contacts, 2)

        list_favorite_contacts(self.contacts)
        sys.stdout = sys.__stdout__

        output = captured_output.getvalue()
        # Alice and Carol should be listed, Bob should NOT
        self.assertIn("1. Alice --- alice@example.com --- 1234", output)
        self.assertIn("2. Carol --- carol@example.com --- 9012", output)
        self.assertNotIn("Bob", output)

if __name__ == '__main__':
    unittest.main()
