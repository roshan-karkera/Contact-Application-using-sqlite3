import sqlite3
class Repository:
    def add_contact(self ,cur, contact_details):
        cur.execute('create table if not exists' + ' contacts(firstname text,lastname text,'
                                                   'contactnumber int,emailid text)')
        cur.execute('insert into contacts values(?,?,?,?)', (contact_details[0],contact_details[1],
                                                             contact_details[2],contact_details[3]))
        cur.execute("select * from contacts where firstname==? and lastname==?",[contact_details[0],contact_details[1]])
        result_list = cur.fetchone()
        if(len(result_list) == 0):
            print("There Was An Error While Adding The Contact.")
        else:
            first_name = result_list[0]
            last_name= result_list[1]
            contact_number = result_list[2]
            email_id = result_list[3]
            return(first_name, last_name, contact_number, email_id)


    def edit_contact_name(self, cur, first_name, last_name):
        cur.execute('create table if not exists' + ' contacts(firstname text,lastname text,'
                                                   'contactnumber int,emailid text)')
        new_first_name = input("Enter New First Name For "+first_name+" "+last_name+":\n")
        new_last_name = input("Enter New Last Name For "+first_name+" "+last_name+":\n")
        cur.execute("update contacts set firstname==? where firstname==?", [new_first_name, first_name])
        cur.execute("update contacts set lastname==? where lastname==?", [new_last_name, last_name])
        cur.execute('select * from contacts where firstname==? and lastname==?', [new_first_name, new_last_name])
        result_list = cur.fetchone()
        if (len(result_list) == 0):
            print("There Was An Error While Editing The Contact.")
        else:
            first_name = result_list[0]
            last_name = result_list[1]
            contact_number = result_list[2]
            email_id = result_list[3]
            return (first_name, last_name, contact_number, email_id)

    def edit_contact_contact_number(self, cur, first_name, last_name):
        cur.execute('create table if not exists' + ' contacts(firstname text,lastname text,'
                                                   'contactnumber int,emailid text)')
        new_contact_number=int(input("Enter New Phone Number For "+first_name+" "+last_name+":\n"))
        cur.execute("update contacts set contactnumber==? where firstname==? and lastname==?", [new_contact_number, first_name, last_name])
        cur.execute('select * from contacts where firstname==? and contactnumber==?', [first_name,new_contact_number])
        result_list = cur.fetchone()
        if (len(result_list) == 0):
            print("Error!!.")
        else:
            first_name = result_list[0]
            last_name = result_list[1]
            contact_number = result_list[2]
            email_id = result_list[3]
            return (first_name, last_name, contact_number, email_id)


    def search_contact_by_name(self, cur, first_name, last_name):
        cur.execute('create table if not exists' + ' contacts(firstname text,lastname text,'
                                                   'contactnumber int,emailid text)')
        cur.execute('select * from contacts where firstname==? and lastname==?', [first_name,last_name])
        result_list = cur.fetchone()
        if (len(result_list) == 0):
            print("Error in searching or no contact present!")
        else:
            first_name = result_list[0]
            last_name = result_list[1]
            contact_number = result_list[2]
            email_id = result_list[3]
            return (first_name, last_name, contact_number, email_id)

    def search_contact_by_contact_number(self, cur, contact_number):
        cur.execute('create table if not exists' + ' contacts(firstname text,lastname text,'
                                                   'contactnumber int,emailid text)')
        cur.execute('select * from contacts where contactnumber==?', [contact_number])
        result_list = cur.fetchone()
        if (len(result_list) == 0):
            print("Error in searching or no contact present!")
        else:
            first_name = result_list[0]
            last_name = result_list[1]
            contact_number = result_list[2]
            email_id = result_list[3]
            return (first_name, last_name, contact_number, email_id)


    def display_all_contacts(self, cur):
        cur.execute('create table if not exists' + ' contacts(firstname text,lastname text,'
                                                   'contactnumber int,emailid text)')
        cur.execute('select * from contacts')
        result_list = cur.fetchall()
        if (len(result_list) == 0):
            print("No such contact present.")
        else:
            return result_list


    def delete_contact(self, cur, first_name, last_name):
        cur.execute('create table if not exists' + ' contacts(firstname text,lastname text,'
                                                   'contactnumber int,emailid text)')
        cur.execute("delete from contacts where firstname==? and lastname==?",[first_name,last_name])
        cur.execute('select * from contacts')
        result_list = cur.fetchall()
        return result_list


