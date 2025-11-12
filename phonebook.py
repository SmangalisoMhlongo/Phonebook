from commands import Commands
import sys

def main():
    com = Commands()
    char1 = "#" * 24
    char2 = "*" * 24
    #phonebook logic
    print(char2)
    print("WELCOME TO OUR PHONE BOOK")
    print(char2)
    print((char1)+"COMMANDS:"+(char1))
    com.display_commands()
    print((char1)+"ENJOY OUR SERVICES:"+(char1))
    #starting to ask for user input
    while True:
        try:
            user_input = input(">>>").lower()
            if user_input == "add":
                com.add()
            if user_input == "delete":
                com.delete()
            if user_input == "update":
                com.update()
            if user_input == "search":
                com.search()
            if user_input == "exit":
                sys.exit()

        except Exception:
            print("Enter the right command.")

if __name__ == "__main__":
    main()