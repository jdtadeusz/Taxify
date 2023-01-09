from LoginSystem import LoginSystem
import random
from os import system, name

class Taxi_system():
    def __innit__(self):
        self.drivers = {}
        with open('drivers.txt', 'r') as f:
            for line in f.readlines():
                split_line = line.split(',')
                if(len(split_line) == 3):
                    self.drivers[split_line[0]] = split_line[1]

    def wallet_oper(username):      #wyswietlanie stanu konta
        with open(f'txt/{username}_wallet.txt', 'r') as w:
                for line in w:
                    print("------", line, "$")
    
    def clear_wallet(username):     #wyplacanie pieniedzy z konta 
        with open(f'txt/{username}_wallet.txt', 'r+') as file:
            file.truncate(0)
            file.write("0")
        print("--- The money has been deposited ---")
    
    def add_money(username):    #wplacanie pieniedzy na konto TAXIFY
        hmuch = float(input("How much: "))
        with open(f'txt/{username}_wallet.txt', 'r') as file:
            line = file.read()
            sum = round(float(line) + hmuch, 1)
        file.close()
        with open(f'txt/{username}_wallet.txt', 'w') as f_:
            f_.write(str(sum))
        print("")
        print(hmuch, "$ has been added to you account!\nTo check money avaiable, click on Wallet tab :)")
        return sum    

    def driver_apply(username, brand, model):   #aplikowanie na kierowce TAXIFY
        if brand.lower() != "bmw":
            with open('txt/drivers.txt', 'a') as f:
                f.write(f"{username.strip()},{brand.strip()},{model.strip()}\n")

        else:
            with open('txt/lux_drivers.txt', 'a') as l:
                l.write(f"{username.strip()},{brand.strip()},{model.strip()}\n")

    def choose_ride():      #losowe wybieranie kierowcy/ wybieranie klasy przejazdu
        print("Choose the class You wish to order:\n1. Standard ($3/km)\n2. Premium($5/km)")
        class_ = int(input("Option: "))
        if class_ == 1:
            system('cls')
            with open('txt/drivers.txt', 'r') as f:
                lines = f.readlines()
                range = len(lines)
                chosen_driver_index = random.randint(0,range-1)
                chosen_driver = lines[chosen_driver_index].split(",")
            print("Your driver today is going to be", chosen_driver[0], "-",chosen_driver[1], "model",chosen_driver[2])
        elif class_ == 2:
            system('cls')
            with open('txt/lux_drivers.txt', 'r') as f:
                lines = f.readlines()
                range = len(lines)
                chosen_driver_index = random.randint(0,range-1)
                chosen_driver = lines[chosen_driver_index].split(",")
            print("\nYour driver today is going to be", chosen_driver[0], "-", chosen_driver[1], "model:", chosen_driver[2])
        
        return class_

    def oper_ride(option, username):    #losowanie poczatkowej lokalizacji, wybieranie punktu destynacji/ pobieanie pieniedzy z portfela
        chosen_loc = ""
        with open('txt/localization.txt', 'r', encoding="utf-8") as f:
            lines = f.readlines()
            range = len(lines)
            chosen_loc_index = random.randint(0,range-1)
            chosen_loc = lines[chosen_loc_index]
        print("Your current localization is:", chosen_loc)

        with open('txt/destination.txt', 'r', encoding="utf-8") as l:
            lines = l.readlines()
            range = len(lines)
            chosen_dest = ""
            chosen_dest_1 = ""
            while True:
                chosen_dest_index = random.randint(0,range-1)
                chosen_dest = lines[chosen_dest_index]
                if chosen_dest != chosen_loc:
                    break

            while True:
                chosen_dest_index_1 = random.randint(0,range-1)
                chosen_dest_1 = lines[chosen_dest_index_1]
                if chosen_dest_1 != chosen_loc and chosen_dest_1 != chosen_dest:
                    break
        print("Choose Your destination point:\n1.", chosen_dest,"\n2.", chosen_dest_1)
        dest = int(input("Option: "))
        distance = round(random.uniform(0.5, 3), 1)
        standard = round(distance * 3, 1)
        premium = round(distance * 5, 1)
        if dest == 1:
            if option == 1:
                system('cls')
                print(chosen_loc, "-->", chosen_dest)
                print(distance, "- km", "   $", standard)
                    
                with open(f'txt/{username}_wallet.txt', 'r') as k:
                    line = k.read()
                    remove = round(float(line) - standard, 1)

                with open(f'txt/{username}_wallet.txt', 'w') as p:
                    p.write(str(remove))  
                
                print("You have paid $", standard, "- You have $", remove, " left\n")
                print("Have a nice ride!")


            elif option == 2:
                system('cls')
                print(chosen_loc, "-->", chosen_dest)
                print(distance, "- km", "   $", premium)
                with open(f'txt/{username}_wallet.txt', 'r') as k:
                    line = k.read()
                    remove = round(float(line) - standard, 1)

                with open(f'txt/{username}_wallet.txt', 'w') as p:
                    p.write(str(remove))  
                print("You have paid $", premium, "- You have $", remove, "left\n")
                print("Have a nice ride!")

        elif dest == 2:
            if option == 1:
                system('cls')
                print(chosen_loc, "-->", chosen_dest)
                print(distance, "- km", "   $", standard)
                with open(f'txt/{username}_wallet.txt', 'r') as k:
                    line = k.read()
                    remove = round(float(line) - standard, 1)

                with open(f'txt/{username}_wallet.txt', 'w') as p:
                    p.write(str(remove))  
                print("You have paid $", standard, "- You have $", remove, "left\n")
                print("Have a nice ride!")
            elif option == 2:
                system('cls')
                print(chosen_loc, "-->", chosen_dest)
                print(distance, "- km", "   $", premium)
                with open(f'txt/{username}_wallet.txt', 'r') as k:
                    line = k.read()
                    remove = round(float(line) - premium, 1)

                with open(f'txt/{username}_wallet.txt', 'w') as p:
                    p.write(str(remove))  
                print("You have paid $", standard, "- You have $", remove, "left\n")
                print("Have a nice ride!")
                
        
        

                