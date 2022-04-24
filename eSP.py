from time import sleep
import random
import os

#taken from autopy to exe stuff
#makes the exe work by linking the .data files
def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)

#seed for the flavor random stuff
random.seed()

sleep(1)
print("eSP OS")
print("Version 1.4.22")
sleep(1)

#get the skull pic

skull = open(resource_path("skull.txt"), "r")
#skull = open("./hidden/skull.txt", "r")

#read line by line, char by char
for l in skull:
    for c in l:
        print(c, end="", flush=True)
    sleep(0.1)

#newline
print("")

skull.close()

sleep(1.5)
print("ERROR! Last shutdown was unexpected.")
sleep(1.0)
print("Cold booting...")
sleep(0.5)
#printout loading bar
for x in range(0, 18):
    print("█", end="", flush=True)
    sleep(random.random())

#jump to new line
print("\nCold Boot Done!")
sleep(2)

#password before menu

pw_input = ""
pw_solution = "bananabread"

while(pw_input != pw_solution):
    pw_input = ((input("\nPlease type in password: ")).lower()).replace(" ", "")
    print("Read as:", pw_input)
    if pw_input != pw_solution:
        print("ERROR! Password incorrect.")
    else:
        sleep(0.5)
        print("\nLogon successful. Welcome RootGamer87! Opening data browser...")
        sleep(1.5)
        print("WARNING! 953 Corrupted Entries Found. Request repair or deletion from an admin.")
        sleep(2.5)
        print("3 Accessable Entries Found.")





#menu

menu = True

while menu:
    menu_input = ""

    menu_input = ((input("\nPlease enter a command, or enter !help for more info.\n")).lower()).replace(" ", "")
    #help command
    if menu_input == "!help":
        
        print("Commands available to your user: !help, !read, !quit")
        print("!help - prints list of commands user can use, as well as short descriptions.")
        print("!read - pulls up data entries available to read. Typing in an ID (ex. 123) will take you to that entry.")
        print("!quit - exits the program.")  

    #read command
    elif menu_input == "!read":

        print("954: Nearly Ready")
        print("955: Flipping the Switch")
        print("956: Results")
            
        menu_input = ((input("Please enter an ID number from the list, or enter anything else to return: ")).lower()).replace(" ", "")
        
        #unlocked entry
        if menu_input == "954":
            file_954 = open(resource_path("954.data"), "r")
            print(file_954.read())
            file_954.close()
                
        elif menu_input == "955":
            
            encode_menu = True
            encode = "funkymonkeyfriday"
            
            print("This entry is locked via passcode.")

            while encode_menu:
                
                menu_input = ((input("Please enter the passcode for this entry, or !quit to go back: ")).lower()).replace(" ", "")
                
                if menu_input == encode:
                    print("Access Granted! Opening file.")
                    file_955 = open(resource_path("955.data"), "r")
                    print(file_955.read())
                    file_955.close()
                    encode_menu = False
                    
                elif menu_input == "!quit":
                    encode_menu = False

                else:
                    print("Incorrect passcode, please try again.")
                
        elif menu_input == "956":
            
            encode_menu = True
            encode = "theapesarecoming"
            
            print("This entry is locked via passcode.")

            while encode_menu:
                
                menu_input = ((input("Please enter the passcode for this entry, or !quit to go back: ")).lower()).replace(" ", "")
                
                if menu_input == encode:
                    print("Access Granted! Opening file.")
                    file_956 = open(resource_path("956.data"), "r")
                    print(file_956.read())
                    file_956.close()
                    encode_menu = False
                    
                elif menu_input == "!quit":
                    encode_menu = False

                else:
                    print("Incorrect passcode, please try again.")

    #quit command           
    elif menu_input == "!quit":
        print("Shutting down...")
        sleep(1.5)
        print("CRITICAL ERROR! Unsaved data could be lost! Attempting to abort shutdown...")
        sleep(1.5)
        print("ERROR ERROR ERROR ERROR ERROR ERROR HELP  ERROR ERROR ERROR")
        print("ERROR ERROR ERROR ERROR ERROR ERROR ERROR ERROR ERROR ERROR")
        sleep(0.3)
        menu = False



