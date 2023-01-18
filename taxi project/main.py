import time
from os import system, name
from LoginSystem import LoginSystem
from taxi_system import Taxi_system
import pwinput

login_system = LoginSystem()

def main_menu():        #glowne menu: logowanie/ opcje
    system('cls')
    print("--- WELCOME TO TAXIFY! ---")
    print("1. Main menu\n2. Options\n3. Exit")
    try:
        option = int(input("Option: "))
    except ValueError:
        Valueerr_main()
    if option == 1:
        system('cls')
        print("--- TAXIFY ---")
        pre_menu()
    elif option == 2:
        system('cls')
        print("--- TAXIFY ---")
        print("1. Clear data (Code aquired)")
        print("2. Show all logged in users.")
        print("3. Go back")
        try:
            option_ = int(input("Option: "))
        except ValueError:
            Valueerr_main()
        if option_ == 1:
            system('cls')
            print("--- TAXIFY ---")
            cls()
            print("1. Go back")
            try:
                dec = int(input("Option: "))
            except ValueError:
                Valueerr_main()
            if dec == 1:
                system('cls')
                main_menu()
            else:
                print("--- TAXIFY ---")
                animation("Unrecognized command, loading main menu...")
                system('cls')
                main_menu()
        elif option_ == 2:
            system('cls')
            print("--- TAXIFY ---")
            show_all_users()
            print("\n1. Go back")
            try:
                dec_1 = int(input("Option: "))
            except ValueError:
                Valueerr_main()
            if dec_1 == 1:
                system('cls')
                main_menu()
            else:
                system('cls')
                print("--- TAXIFY ---")
                animation("Unrecognized command, loading main menu...")
                system('cls')
                main_menu()
        elif option_ == 3:
            system('cls')
            main_menu()
        else:
            system('cls') 
            animation("Unrecognized command, loading main menu...")
            system('cls')
            print("")
            main_menu()  
    else:
        system('cls')
        print("--- TAXIFY ---")
        print("Are You sure You want to exit?\n1. Yes\n2. No")
        try:
            dec = int(input("Option: "))
        except ValueError:
            Valueerr_main()
            
        if dec == 1:
            print("See You next time! :)")
            exit
        else:
            system('cls')
            print("")
            main_menu()

def pre_menu():         #opcje logowania 
    print("1. Login\n2. Register\n3. Go back to main menu")
    try:
        option = int(input("Option: "))
    except ValueError:
        Valueerr_main()
    
    if option == 1:
        system('cls')
        print("")
        login()
    elif option == 2:
        system('cls')
        print("")
        register()
    elif option == 3:
        system('cls')
        print("")
        main_menu()
    else:
        system('cls')
        print("No such option, try again.")
        print("")
        pre_menu()
    
def register():
    system('cls')
    print("--- TAXIFY ---")
    login_system.register_user(input("Create new username: "), pwinput.pwinput(prompt='Create new password: '))
    print("Successful registration! Now you can log in to Your new account.\n\nTo thank you for joining us, we are going to fund Your wallet with free $10!")
    time.sleep(4)
    system('cls')
    login()
    
def login():
    system('cls')
    print("--- TAXIFY ---")
    logged = login_system.login_user(input("Username: "), pwinput.pwinput(prompt='Password: '))
    if(logged):
        system('cls')
        print("--- TAXIFY ---")
        print("User has successfully been logged in.")
        animation("Please wait...")
        time.sleep(2)
        system('cls')
        menu()
    else:
        print("Invalid username/password! Try again.\n")   
        print("No account? If yes press '1'; if You wish to try again press '2' or '3' if You wish to exit.")
        dec = int(input("Option: "))
        system('cls')

        if dec == 2:    
            return login()
        elif dec == 1:
            register()
        else:
            main_menu()
            
def cls():              #czyszczenie danych 
    login_system.clear_data()
    
def show_all_users():
    login_system.show_users()

def animation(x):   
    anim = [
    " [=  ]",
    " [ = ]",
    " [  =]",
    " [ = ]",
    " [=  ]",
    " [ = ]",
    " [  =]",
    ]
    i = 0
    print(x)
    while i < 6:
        print(anim[i % len(anim)], end= "\r")
        time.sleep(.5)
        i += 1
    print("")

def Valueerr_main():
        print("Use numbers to navigate the program!")
        animation("Loading main menu...")
        system('cls')
        main_menu()

def Valueerr_nmain():
        print("Use numbers to navigate the program!")
        animation("Loading main menu...")
        system('cls')
        menu()

def menu():             #glowne menu aplikacji taxi  
    print("--- TAXIFY ---")
    print("1. Take a ride\n2. Wallet\n3. Become a driver!\n4. Log out")
    try:
        option = int(input("Option: "))
    except ValueError:
        Valueerr_nmain()
    if option == 1:
        system('cls')
        print("")
        oper_ride()
    elif option == 2:
        system('cls')
        print("--- TAXIFY ---")
        show_money()
        print("1. Deposit\n2. Withdraw\n3. Leave wallet")
        try:
            _option = int(input("Option: "))
        except ValueError:
            Valueerr_nmain()
            
        if _option == 1:
            system('cls')
            print("--- TAXIFY ---")
            username = login_system.get_actual_user()
            Taxi_system.add_money(username)
            print("")
            return menu()
        
        elif _option == 2:
            system('cls')
            print("--- TAXIFY ---")
            print("Are you sure?\n1. Yes\n2. No")
            try:
                dec = int(input("Option: "))
            except ValueError:
                Valueerr_nmain()
                
            if dec == 1:
                system('cls')
                username = login_system.get_actual_user()
                Taxi_system.clear_wallet(username)
                print("")
                menu()
            elif dec == 2:
                system('cls')
                print("")
                menu()
        else:
            system('cls')
            print("")
            menu()
    elif option == 3:
        system('cls')
        print("--- TAXIFY ---")
        print("To become one of the drivers we will ask you for Your: name, car brand and its model.")
        print("Are you sure You want to become one?\n1. Yes\n2. Go back")
        try:
            dec_2 = int(input("Option: "))
        except ValueError:
            Valueerr_nmain()
            
        if dec_2 == 1:
            system('cls')
            driver_apply_mode()
            time.sleep(3)
            system('cls')
            menu()
        else:
            system('cls')
            menu()
    
    else:
        system('cls')
        print("--- TAXIFY ---")
        print("Are you sure You want to log out?\n1. Yes \n2. No")
        try:
            dec_1 = int(input("Option: "))
        except ValueError:
            Valueerr_nmain()
            
        if dec_1 == 1:
            system('cls')
            print("")
            main_menu()
        else:
            system('cls')
            menu()
                
def show_money():
    username = login_system.get_actual_user()
    Taxi_system.wallet_oper(username)

def driver_apply_mode():
    Taxi_system.driver_apply(input("Your name: "), input("Yours car brand: "), input("Model: "))
    print("--- TAXIFY ---")
    print("You have successfully been added to the drivers base, wait for Your first drive!")

def class_choose():      
    Taxi_system.choose_ride()

def oper_ride():        
    system('cls')
    print("--- TAXIFY ---")
    option = Taxi_system.choose_ride()
    username = login_system.get_actual_user()
    Taxi_system.oper_ride(option, username)
    print("To continue press '1'")
    try:
        dec = int(input("Option: "))
    except ValueError:
        ValueError()
    if dec == 1:
        animation("Loading main menu...")
        system('cls')
        menu()
    else:
        animation("Unrecognized command, loading main menu...")
        menu()
    

main_menu()