import os

os.system('cls')

phonebook = {}

def add_contact(name, phone_number):
    phonebook[name] = phone_number

def delete_contact(name):
    del phonebook[name]

def edit_contact(name, new_phone_number):
    phonebook[name] = new_phone_number

def show_phone_book(phonebook):
    if phonebook == {}:
        print("Empty")
    for name, phone_number in phonebook.items():
        print("Name: ", name)
        print("Phone number: ", phone_number)
        print("-" * 15)

print("=" * 15)
print("Welcome to your phone book!")
print("Here you can add, edit or delete your contacts")
print("=" * 15)
print()

while True:
    print("What do you want to do? | 1 - Add | 2 - Delete | 3 - Edit | 4 - Show phone book | 0 - Exit")
    user_request = input()
    os.system('cls')

    if user_request == "0":
        break

    match user_request:
        case "1":
            name = input("Enter the name of your contact: ")
            if not name:
                print("Contact name can't be empty. Try again.")
                continue
            if name not in phonebook:
                phone_number = input("Enter the phone number of your contact: ")
                add_contact(name, phone_number)
                os.system('cls')
            elif name in phonebook:
                print("Name of the contact is already in phone book. Type 3 if you want to edit a contact")
        
        case "2":
            name = input("Enter the name of the contact you want to delete: ")
            if name in phonebook:
                confirm_delete = input(f"Do you really want to delete {name}? (1 - yes | 0 - no):  ")
                if confirm_delete == "1":
                    delete_contact(name)
                os.system('cls')
            elif name not in phonebook:
                print("Contact not found. Try again")

        case "3":
            name = input("Enter the name of the contact you want to edit: ")
            if name in phonebook:
                new_phone_number = input("Enter the new phone number of the contact: ")
                edit_contact(name, new_phone_number)
                os.system('cls')
            elif name not in phonebook:
                print("Contact not found. Try again")
        
        case "4":
            show_phone_book(phonebook)
        
        case _:
            print("Command not found. Try again")
    
