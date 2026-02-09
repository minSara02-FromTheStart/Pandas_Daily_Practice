import pandas as pd

contacts = pd.DataFrame(columns= ["ID","Name","Number","Email"])
def load_contact():
    global contacts
    try:
        contacts = pd.read_csv("contact.csv")
        print("Contact loaded successfully")
    except FileNotFoundError:
        print("File doesnt exist")
        contacts = pd.DataFrame(columns= ["ID","Name","Number","Email"])

def Save_contact():
    contacts.to_csv("contact.csv", index=False)
    print("Saving contacts has been successfully done.")

def Add_contact():
    global contacts 
    new_contacts = {"ID":input("Enter ID: "),
                    "Name": input("Enter name: "),
                    "Number": input("Enter a number: "),
                    "Email": input("Enter an email: ")}
    
    contacts.loc[len(contacts)] = new_contacts
    print("Contact Added Successfully")
    Save_contact()

def view_contact():
    if contacts.empty:
        print("There is no contact available")
        return
    print("All the existing contacts are below: ")
    print(contacts)

def search_contact():
    search_id = int(input("Enter the ID you want to search: "))
    result = contacts[contacts["ID"] == search_id]
    if result.empty:
        print("ID not found.")
    else:
        print("Contact found")
        print(result)

def update_contact():
    update_id = int(input("Enter the ID you want to update: "))
    result = contacts[contacts["ID"] == update_id]

    if result.empty:
        print("ID note found")
        return
    index = result.index[0]

    contacts.at[index, "ID"] = input("Enter new ID: ")
    contacts.at[index, "Name"] = input("Enter new Name: ")
    contacts.at[index, "Number"] = input("Enter new Number: ")
    contacts.at[index, "Email"] = input("Enter new Email: ")

    print("New Update has been uploaded.")
    Save_contact()

def delete_contact():
    delete_id = int(input("Enter the id you want to delete: "))
    result = contacts[contacts["ID"] == delete_id]

    if result.empty:
        print("ID not found")
        return
    
    index = result.index[0]
    contacts.drop(index, inplace=True)
    contacts.reset_index(drop=True, inplace=True)
    Save_contact()
    print("Contact deleted successfully!")



def main():
    while True:
        print("Welcome to Contact Book")
        print("_________________________")
        print("1.Load Previous Contact")
        print("2.Add new Contact")
        print("3.View all the existing contact")
        print("4.Search ")
        print("5.Update")
        print("6.Delete")
        print("7.exit")

        option = input("Enter the option you want: ")

        if option =='1':
            load_contact()
            
        elif option == '2':
            Add_contact()
            
        elif option == '3':
            view_contact()
        elif option =='4':
            search_contact()
        elif option == '5':
            update_contact()
        elif option == '6':
            delete_contact()
        elif option == '7':
            break
        else:
            print("Invalid Option.Please try again.")
            
main()
