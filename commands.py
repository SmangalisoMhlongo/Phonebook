class Commands():
    def __init__(self):
        ...
    def save(self):
        ...
    def load(self):
        ...
    def update(self):
        ...
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
        ...
    def display_commands(self):
        print("SAVE:...."+"\n"+"LOAD:...."+"\n"+"UPDATE:...."+"\n"+
              "DELETE:...."+"\n"+"ADD:...."+"\n"+"SEARCH:....")
