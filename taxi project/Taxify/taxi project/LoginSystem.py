import hashlib
import datetime
import os 

class LoginSystem:
    __actualuser = ""
    def __init__(self):     #slownik przetrzymujacy uzytkownikow
        self.users = {}
        with open('txt/users1.txt', 'r') as f:
            for line in f.readlines():
                split_line = line.split(',')
                if(len(split_line) == 3):
                    self.users[split_line[0]] = split_line[1]

    def register_user(self, username, password):    #rejestracja/ tworzenie portfela
        password_hash = hashlib.sha256(password.encode()).hexdigest()

        self.users[username] = password_hash

        with open('txt/users1.txt', 'a') as f:
            now = datetime.datetime.now().strftime("- %d-%m-%y %H:%M:%S")
            f.write(f"{username},{password_hash},{now}\n")
        with open(f"txt/{username}_wallet.txt", 'w') as l:
            l.write("0")

    def login_user(self, username, password):
        if username in self.users:
            password_hash = hashlib.sha256(password.encode()).hexdigest()
            
            if self.users[username] == password_hash:
                self.__actualuser = username
                return True
        return False
    
    def clear_data(self):       #usuwanie uzytkownikow i portfeli z bazy danych (plikow txt)
        code = 91322
        check = int(input("Type the code to remove data: "))
        if check == code:
            with open("txt/users1.txt",'r+') as file:
                file.truncate(0)
            for entry in os.listdir("txt/"):
                if os.path.isfile(os.path.join("txt/", entry)) and "wallet" in entry:
                    os.remove(f"txt/{entry}")
            print("Data has been succesfully removed.")
            self.users.clear()
        else:
            print("Wrong code!")
    
    def show_users(self):       #wyswietlanie zarejestrowanych uzytkownikow z poziomu aplikacji
        print(self.users)

    def get_actual_user(self):  #funkcja potrzebna do powiązania uzytkownika z jego portfelem
        return self.__actualuser
