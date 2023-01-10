# Taxify
Taxify is a simple taxi system using console to output data

Taxify contains 3 files: *main.py* which uses *LoginSystem.py* and *taxi_system.py* and their classes to run the program. 

### ! PWINPUT MODULE INSTALLATION REQUIRED: 
> cmd command: pip install pwinput

## Menu
Opening menu is simple: Main menu wherein user can register/ login; Options wherein user can see all signed up users and clear data by typing the right security code (which is 91322), if user decides to do so, all users from 'users1.txt' will be removed as so as all wallets files; or to simple Exit the program.

### Registration
One of the LoginSystem's functions is to register new user - it saves user's new login and its password to *users1.txt* (username, hashed password, date and time of register). While beeing registered, a new txt file is being created - user's wallet (*{username}_wallet.txt*) which contains user's available funds. Every user has its own wallet. Also, while typing in a password, its letters/ numbers are replaced with '*' for security reasons. 

### Login 
When new user has been registered, they can already sign in. The system is going to aquire to type the username and password (also covered by '*'). When user press 'enter' to login, the system will check if the username is located in *users1.txt* (same with hashed password). If so, the program will load main menu; if the username is not found in *users1.txt* - the program will give user few options: to create new acc/ to try again/ to go back to menu.

## Main menu 
After successfully signing in, user can choose betweend 4 options: Take a ride/Wallet/ Become a driver/ Log out

### Take a ride 
This one is the main function of the program. Firstly, the system will ask user to choose the class of a ride (cheaper or more expensive), then it will show their current localization by choosing it randomly from *localization.txt*. Then it will ask to choose the destination point: there are 2 choices (also randomly chosen from *destination.txt*). After choosing one it will show user the distance between those two places, a cost of the ride and how much money do they have left. 

### Wallet
In the wallet section the program displays the funds avaiable, user can easily deposit money by typing the amount of $ which they wish to add - the program is going to open wallet assigned to the user, read the funds they already have, and add up the number given; it is also possible to withdraw all money from your acc

### Become a rider
There is a possibility to sign up for a driver, the program will ask some question and assign user to *drivers.txt* or *lux_drivers.txt* (it depends on what car the user drives) 
