import time
from os import system, name 
from datetime import date
import random
import json

def clear():
    # for windows
    if name == 'nt':
        system('cls')
    # for mac and linux(here, os.name is 'posix')
    else:
        system('clear')

def load(file):
    with open(file, "r") as file:
        return json.load(file)

db = load("./database.json")

name = 0
id_number = 0
expenses = {}
earned = {}
balance = 0
password = 0

bold = '\033[1m'
normal = '\033[0m'
italic = '\x1B[3m'

gold = '\033[38;2;230;190;0m' + bold
silver = '\033[38;2;221;221;221m' + bold
copper = '\033[38;2;170;44;0m' + bold

paleyellow = '\033[38;2;255;255;215m' + bold
lime = '\033[38;2;00;255;00m' + bold
turquoise = '\033[38;2;0;255;255m' + bold
teal = '\033[38;2;0;170;170m' + bold

yellow = '\033[38;2;255;255;0m' + bold
green = '\033[38;2;00;160;00m' + bold
blue = '\033[38;2;0;40;255m' + bold
purple = '\033[38;2;130;0;250m' + bold
brown = '\033[38;2;135;62;35m' + bold
red = '\033[0;31m' + bold
orange = '\033[38;2;255;90;0m' + bold

darkgrey = '\033[38;2;100;100;100m' + bold
grey = '\033[38;2;130;130;130m' + bold

white = '\033[38;2;255;255;255m' + bold
platinum = '\033[38;2;205;192;255m' + bold
ironc = '\033[38;2;255;205;192m' + bold

def start_screen():
    print(f"{turquoise}Powered by: Replit Co.")
    time.sleep(2)
    for i in range(10):
        clear()
        print(f'''{green}$$$$$$$$\      $$$$$$$\                      $$\             $$$$$$$\  $$\                     
\__$$  __|     $$  __$$\                     $$ |            $$  __$$\ $$ |                    
   $$ |        $$ |  $$ | $$$$$$\  $$$$$$$\  $$ |  $$\       $$ |  $$ |$$ |$$\   $$\  $$$$$$$\ 
   $$ |$$$$$$\ $$$$$$$\ | \____$$\ $$  __$$\ $$ | $$  |      $$$$$$$  |$$ |$$ |  $$ |$$  _____|
   $$ |\______|$$  __$$\  $$$$$$$ |$$ |  $$ |$$$$$$  /       $$  ____/ $$ |$$ |  $$ |\$$$$$$\  
   $$ |        $$ |  $$ |$$  __$$ |$$ |  $$ |$$  _$$<        $$ |      $$ |$$ |  $$ | \____$$\ 
   $$ |        $$$$$$$  |\$$$$$$$ |$$ |  $$ |$$ | \$$\       $$ |      $$ |\$$$$$$  |$$$$$$$  |
   \__|        \_______/  \_______|\__|  \__|\__|  \__|      \__|      \__| \______/ \_______/ 
                                                                                               
                                                                                               
{blue}Loading''')
        time.sleep(0.5)
        clear()
        print(f'''{green}$$$$$$$$\      $$$$$$$\                      $$\             $$$$$$$\  $$\                     
\__$$  __|     $$  __$$\                     $$ |            $$  __$$\ $$ |                    
   $$ |        $$ |  $$ | $$$$$$\  $$$$$$$\  $$ |  $$\       $$ |  $$ |$$ |$$\   $$\  $$$$$$$\ 
   $$ |$$$$$$\ $$$$$$$\ | \____$$\ $$  __$$\ $$ | $$  |      $$$$$$$  |$$ |$$ |  $$ |$$  _____|
   $$ |\______|$$  __$$\  $$$$$$$ |$$ |  $$ |$$$$$$  /       $$  ____/ $$ |$$ |  $$ |\$$$$$$\  
   $$ |        $$ |  $$ |$$  __$$ |$$ |  $$ |$$  _$$<        $$ |      $$ |$$ |  $$ | \____$$\ 
   $$ |        $$$$$$$  |\$$$$$$$ |$$ |  $$ |$$ | \$$\       $$ |      $$ |\$$$$$$  |$$$$$$$  |
   \__|        \_______/  \_______|\__|  \__|\__|  \__|      \__|      \__| \______/ \_______/ 
                                                                                               
                                                                                               
{blue}Loading.''')
        time.sleep(0.5)
        clear()
        print(f'''{green}$$$$$$$$\      $$$$$$$\                      $$\             $$$$$$$\  $$\                     
\__$$  __|     $$  __$$\                     $$ |            $$  __$$\ $$ |                    
   $$ |        $$ |  $$ | $$$$$$\  $$$$$$$\  $$ |  $$\       $$ |  $$ |$$ |$$\   $$\  $$$$$$$\ 
   $$ |$$$$$$\ $$$$$$$\ | \____$$\ $$  __$$\ $$ | $$  |      $$$$$$$  |$$ |$$ |  $$ |$$  _____|
   $$ |\______|$$  __$$\  $$$$$$$ |$$ |  $$ |$$$$$$  /       $$  ____/ $$ |$$ |  $$ |\$$$$$$\  
   $$ |        $$ |  $$ |$$  __$$ |$$ |  $$ |$$  _$$<        $$ |      $$ |$$ |  $$ | \____$$\ 
   $$ |        $$$$$$$  |\$$$$$$$ |$$ |  $$ |$$ | \$$\       $$ |      $$ |\$$$$$$  |$$$$$$$  |
   \__|        \_______/  \_______|\__|  \__|\__|  \__|      \__|      \__| \______/ \_______/ 
                                                                                               
                                                                                               
{blue}Loading..''')
        time.sleep(0.5)
        clear()
        print(f'''{green}$$$$$$$$\      $$$$$$$\                      $$\             $$$$$$$\  $$\                     
\__$$  __|     $$  __$$\                     $$ |            $$  __$$\ $$ |                    
   $$ |        $$ |  $$ | $$$$$$\  $$$$$$$\  $$ |  $$\       $$ |  $$ |$$ |$$\   $$\  $$$$$$$\ 
   $$ |$$$$$$\ $$$$$$$\ | \____$$\ $$  __$$\ $$ | $$  |      $$$$$$$  |$$ |$$ |  $$ |$$  _____|
   $$ |\______|$$  __$$\  $$$$$$$ |$$ |  $$ |$$$$$$  /       $$  ____/ $$ |$$ |  $$ |\$$$$$$\  
   $$ |        $$ |  $$ |$$  __$$ |$$ |  $$ |$$  _$$<        $$ |      $$ |$$ |  $$ | \____$$\ 
   $$ |        $$$$$$$  |\$$$$$$$ |$$ |  $$ |$$ | \$$\       $$ |      $$ |\$$$$$$  |$$$$$$$  |
   \__|        \_______/  \_______|\__|  \__|\__|  \__|      \__|      \__| \______/ \_______/ 
                                                                                               
                                                                                               
{blue}Loading...''')
        time.sleep(0.5)
        i = i + 1
    clear()
    time.sleep(5)
               
start_screen()

def save_data():
    with open("./database.json", "r") as file:
        db = json.load(file)
    db['name'] = name
    db['balance'] = balance
    db['id_number'] = id_number
    db['expenses'] = expenses
    db['earned'] = earned
    db['password'] = password
    with open("./database.json", "w") as file:
        json.dump(db, file)

try:
    name = db['name']
    balance = db['balance']
    id_number = db['id_number']
    expenses = db['expenses']
    earned = db['earned']
    password = db['password']
except:
    print(f'''{white}WELCOME TO T-BANK PLUS!

A Python application with finance and banking made easy. Since you are new, create a new account to begin!
''')
    name = input("Name: ")
    time.sleep(5)
    id_number = f"{random.randint(0,9)}{random.randint(0,9)}{random.randint(0,9)}{random.randint(0,9)}{random.randint(0,9)}{random.randint(0,9)}{random.randint(0,9)}{random.randint(0,9)}"
    print(f'''Your ID number for login is {id_number}''')
    balance = int(input("Starting balance: "))
    password = str(input("Create password: "))
    for i in range(5):
        clear()
        print(f'''{blue}
Creating account''')
        time.sleep(0.5)
        clear()
        print(f'''{blue}
Creating account.''')
        time.sleep(0.5)
        clear()
        print(f'''{blue}
Creating account..''')
        time.sleep(0.5)
        clear()
        print(f'''{blue}
Creating account...''')
        time.sleep(0.5)
        i = i + 1
    clear()
    time.sleep(0.5)

print(f'''{yellow}WELCOME BACK TO T-BANK PLUS!

{white}You are previously signed in as {name}, {id_number}''')
password_to_get_in = input("Password: ")
while password_to_get_in != password:
    print(f"{red}Incorrect password!{white}")
    password_to_get_in = input("Password: ")
clear()
print(f"{green}Logging in...{white}")
save_data()
time.sleep(2)

while True:
    clear()
    print(f'''{green}T-BANK PLUS
    
{white}{name}'s Account
{white}{id_number}

Balance: {green}{balance}{white}

[{blue}1{white}] Banking History
[{blue}2{white}] Add to Balance
[{blue}3{white}] Add Expense
[{blue}4{white}] Settings''')
    menu_option = int(input("> "))
    while menu_option != 1 and menu_option != 2 and menu_option != 3 and menu_option != 4:
        menu_option = int(input("> "))
    print()
    if menu_option == 1:
        category = int(input(f'''[{blue}1{white}] Gains
[{blue}2{white}] Expenses
> '''))
        while category != 1 and category != 2:
            category = int(input("> "))
        if category == 1:
            print(f'GAINS:')
            print()
            for i in earned:
                print(f'{blue}{i}{white}: {green}+{earned[i][0]}{white}, {earned[i][1]}')
                print()
        else:
            print(f'EXPENSES:')
            print()
            for i in expenses:
                print(f'{blue}{i}{white}: {red}-{expenses[i][0]}{white}, {expenses[i][1]}')
                print()
    elif menu_option == 2:
        desc = input(f'{white}Memo: ')
        cost = int(input(f'{white}Amount: '))
        earned[f'[{len(earned) + 1}] {date.today()}'] = [cost, desc]
        balance = balance + cost
        save_data()
    elif menu_option == 3:
        desc = input(f'{white}Memo: ')
        cost = int(input(f'{white}Amount: '))
        expenses[f'[{len(expenses) + 1}] {date.today()}'] = [cost, desc]
        balance = balance - cost
        save_data()
    elif menu_option == 4:
        setting = int(input(f'''[{blue}1{white}] Change Password
[{blue}2{white}] Delete Account
[{blue}3{white}] Save Data
> '''))
        while setting != 1 and setting != 2 and setting != 3:
            setting = int(input("> "))
        if setting == 1:
            password_to_get_in = input(f"{white}Old password: {white}")
            while password_to_get_in != password:
                print(f"{red}Incorrect password!{white}")
                password_to_get_in = input(f"{white}Old password: {white}")
            password = str(input(f"{white}New password: {white}"))
            password_to_get_in = input(f"{white}Confirm password: {white}")
            while password_to_get_in != password:
                print(f"{red}Incorrect password!")
                password_to_get_in = input(f"{white}Confirm password: {white}")
            print(f"{white}Password saved!{white}")
            save_data()
        elif setting == 2:
            enter = input("Are you sure? (y/n)")
            if enter == "y":
                for i in range(5):
                        clear()
                        print(f'''{red}
Deleting account{white}''')
                        time.sleep(0.5)
                        clear()
                        print(f'''{red}
Deleting account.{white}''')
                        time.sleep(0.5)
                        clear()
                        print(f'''{red}
Deleting account..{white}''')
                        time.sleep(0.5)
                        clear()
                        print(f'''{red}
Deleting account...{white}''')
                        time.sleep(0.5)
                        i = i + 1
                clear()
                time.sleep(0.5)
                name = 0
                id_number = 0
                expenses = {}
                earned = {}
                balance = 0
                password = 0
                print(f'''{white}WELCOME TO T-BANK PLUS!

A Python application with finance and banking made easy. Since you are new, create a new account to begin!
''')
                name = input("Name: ")
                time.sleep(5)
                id_number = f"{random.randint(0,9)}{random.randint(0,9)}{random.randint(0,9)}{random.randint(0,9)}{random.randint(0,9)}{random.randint(0,9)}{random.randint(0,9)}{random.randint(0,9)}"
                print(f'''Your ID number for login is {id_number}''')
                balance = int(input("Starting balance: "))
                password = str(input("Create password: "))
                for i in range(5):
                    clear()
                    print(f'''{blue}
Creating account''')
                    time.sleep(0.5)
                    clear()
                    print(f'''{blue}
Creating account.''')
                    time.sleep(0.5)
                    clear()
                    print(f'''{blue}
Creating account..''')
                    time.sleep(0.5)
                    clear()
                    print(f'''{blue}
Creating account...''')
                    time.sleep(0.5)
                    i = i + 1
                clear()
                time.sleep(0.5)
                print(f'''{yellow}WELCOME BACK TO T-BANK PLUS!{white}

You are previously signed in as {name}, {id_number}''')
                password_to_get_in = input("Password: ")
                while password_to_get_in != password:
                    print(f"{red}Incorrect password!{white}")
                    password_to_get_in = input("Password: ")
                print(f"{green}Logging in...{white}")
                save_data()
                time.sleep(2)
            else:
                pass
        elif setting == 3:
            for i in range(5):
                clear()
                print(f'''
{yellow}Saving data{white}''')
                time.sleep(0.5)
                clear()
                print(f'''
{yellow}Saving data.{white}''')
                time.sleep(0.5)
                clear()
                print(f'''
{yellow}Saving data..{white}''')
                time.sleep(0.5)
                clear()
                print(f'''
{yellow}Saving data...{white}''')
                time.sleep(0.5)
                i = i + 1
            clear()
            time.sleep(0.5)
            save_data()

    else:
        pass
    print()
    input(f"{white}Press Enter ")
