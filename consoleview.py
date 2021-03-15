import sqlite3
from repository import Repository
from contact import Contact

db = sqlite3.connect('Contact-App.db')
cur = db.cursor()
print("Welcome to the Contact-App!\n")

choice = input("Please continue by selecting the options below: "
                 "\n1)Add contacts:"
                 "\n2)Edit contacts:"
                 "\n3)Search contacts:"
                 "\n4)Display all the contacts:"
                 "\n5)Delete contacts:\n"
                 "\nEnter your command:")

if(choice == '1' or choice =='Add'):
    first_name = input("Enter First name : ")
    last_name = input("Enter Last name : ")
    contact_number = int(input("Enter Contact number: "))
    email_id = input("Enter The Email Id : ")
    contact1 = Contact(first_name, last_name, contact_number, email_id)
    result = Repository.add_contact(None, cur, contact1.getters())
    print("Added Contact is : \nFirst name : {}.\nLast name : {}."
           "\nContact number : {}.\nEmail Id : {}.".format(result[0], result[1], result[2], result[3]))
    db.commit()
    db.close()

elif(choice == '2' or choice =='Edit'):
    first_name = input("Enter first name of the contact to edit: ")
    last_name = input("Enter last name of the contact to edit: ")
    option = (input("Edit by Name or Phone?: \n1)Edit name.\n2)Edit Contact number: "))
    if(option == '1' or option == 'Edit_name'):
        result = Repository.edit_contact_name(None, cur, first_name, last_name)
        print("Edited Contact Is : \nFirst name : {}.\nLast name : {}."
              "\nContact number : {}.\nEmail Id : {}.".format(result[0], result[1], result[2], result[3]))
        db.commit()
        db.close()

    elif(option == '2' or option == 'Edit_phone'):
        result = Repository.edit_contact_contact_number(None, cur, first_name, last_name)
        print("Following Edited contact is: \nFirst name : {}.\nLast name : {}."
              "\nContact number : {}.\nEmail Id : {}.".format(result[0], result[1], result[2], result[3]))
        db.commit()
        db.close()

    else:
        print("Select a Valid option.")

elif(choice == '3' or choice == 'Search'):
    option = input("Search by Name or Phone?:\n1)Search by name.\n2)Search by Contact number:")
    if(option == '1' or option == 'Search_name'):
        first_name = input("Enter first name of contact to search:")
        last_name = input("Enter first name of contact to search:")
        result = Repository.search_contact_by_name(None, cur, first_name, last_name)
        print("Searched contact: \nFirst Name : {}.\nLast Name : {}."
              "\nContact number : {}.\nEmail Id : {}.".format(result[0], result[1], result[2], result[3]))
        db.commit()
        db.close()

    elif (option == '2' or option == 'Search_phone'):
        contact_number = input("Enter Contact number of contact to search:")
        result = Repository.search_contact_by_contact_number(None, cur, contact_number)
        print("Searched Contact : \nFirst Name : {}.\nLast Name : {}."
              "\nContact number : {}.\nEmail Id : {}.".format(result[0], result[1], result[2], result[3]))
        db.commit()
        db.close()
    else:
        print("Enter a Valid choice.")

elif(choice == '4' or choice == 'Display'):
    result = Repository.display_all_contacts(None, cur)
    count = 1
    for i in result:
        print(str(count)+")First name : {}  "
                         "Last name : {}  "
                         "Contact number : {}  "
                         "Email Id : {}. ".format(i[0],i[1],i[2],i[3]))
        count = count + 1
    db.commit()
    db.close()

elif(choice==  '5' or choice == 'Delete'):
    first_name = input("Enter first name of contact to delete: ")
    last_name = input("Enter last name of contact to delete: ")
    result = Repository.delete_contact(None, cur, first_name, last_name)
    print("Following contact is deleted")
    db.commit()
    db.close()



