import string
class Commands():
    def __init__(self):
        self.forupdate = []
    
    def update(self):
        while True:
                try:
                    lis = []
                    with open("loadsave.txt", "r") as textfile:
                        for person in textfile:
                            str_char = person.split(",")
                            name = str_char[0]
                            lis.append(name)
                    
                    #targeting the contact to update
                    name_toupdate = input("\n👥 Next, Enter the name and surname of the person you want to update the details for: ").title()  
                    print("*" * 25)
                             
                    if name_toupdate in lis: 
                            contact_name = input("\n👥 First, Enter the updated name and surname: ").title()
                            contact_adress = input("\n👥 Next, Enter the updated place they live: ").title()
                            contact_number = input("\n👥 Next, Enter the updated number: ").title() 
                            if len(contact_number) != 0 and len(contact_adress) != 0 and contact_name.isnumeric():    
                                with open("loadsave.txt", "r") as textfile:
                                    for person_details in textfile:
                                        target_man = name_toupdate
                                        if target_man in person_details:
                                            with open("my_file.txt", "a") as f:
                                                f.write(f"\n{contact_name},{contact_adress},{contact_number}") 
                                                print("Contact has been Updated!")  
                            break  
                    else:
                         raise ValueError
                except ValueError:
                     print("The person you are looking for does not exist")
                     continue
    def delete(self):
         while True:
                try:
                    #searching for a contact through thier name and surname to dlete the contact     
                    lis = []
                    with open("loadsave.txt", "r") as textfile:
                        for person in textfile:
                            str_char = person.split(",")
                            name = str_char[0]
                            lis.append(name)
                            # print(name)   
        
                    name_todelete = input("\n👥 Next, Enter the name and surname of the person you want to search for: ").title()
                    
                    if name_todelete in lis:
                            
                            with open("loadsave.txt", "r") as textfile:
                                for person_details in textfile:
                                    target_man = name_todelete
                                    if target_man in person_details:
                                        with open("loadsave.txt", "r") as f:
                                            content = f.read()         
                                        to_modify = content.replace(person_details, "")
                                        with open("loadsave.txt", "w") as f:
                                            f.write(to_modify)   
                                        print("Contact Deleted!!")  
                                    else:
                                         raise ValueError                                                                                                
                            break
                    else:
                         raise ValueError
                except ValueError:
                     print(f"{name_todelete} does not exist as a contact!")
                     continue
    def add(self):
        while True:
                try:
                     
                    contact_name = input("\n👥 First, Enter their name and surname: ").title()
                    contact_adress = input("\n👥 Next, Enter the place they live: ").title()
                    contact_number = input("\n👥 Next, Enter their number: ").title()
                    if len(contact_number) != 0 and len(contact_adress) != 0 and len(contact_name) !=0:
                        with open("my_file.txt", "a") as f:
                            f.write(f"\n{contact_name},{contact_adress},{contact_number}") 
                            print("Contact added!")                                                                    
                        break
                    else:
                         raise ValueError
                except ValueError:
                     print("One of your entries was missing.")
                     continue
    def search(self):
        while True:
                try:
                    #searching for a contact through thier name and surname     
                    lis = []
                    with open("loadsave.txt", "r") as textfile:
                        for person in textfile:
                            str_char = person.split(",")
                            name = str_char[0]
                            lis.append(name)
                            # print(name)   
        
                    name_tosearch = input("\n👥 Next, Enter the name and surname of the person you want to search for: ").title()
                    
                    if name_tosearch in lis:
                            
                            with open("loadsave.txt", "r") as textfile:
                                for person_details in textfile:
                                    target_man = name_tosearch
                                    if target_man in person_details:
                                         spl_char1 = person_details.split(",")                         
                                print(f"\nContact Found! \nYour Contacts name is: {spl_char1[0]}\nTheir Adress is: {spl_char1[1]} \nNo: {spl_char1[2]}")                           
                                
                            break
                    else:
                         raise ValueError
                except ValueError:
                     print(f"{name_tosearch} does not exist as a contact!")
                     continue
        
    def display_commands(self):
        print(+"✏️UPDATE: For when you want to update an existing contact."+"\n"+
              "❌DELETE: For when you want to delete a contact"+"\n"+
              "➕ADD: When you want to add a new contact."+"\n"+
              "🔍SEARCH: For when you want to search for a contact via their name and surname."+"\n"+
              "Exit")
