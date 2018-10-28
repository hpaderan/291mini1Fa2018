import getpass
import helpers as h
import ManageBookings as bookings
import OfferRide as offer


'''*******************************************
* Main function
*******************************************'''
def Main():
    ##ask if log in or register
    print('Please enter option number and press Enter.')
    print('\t1. Log In with existing account.')
    print('\t2. Register a new account.')
    startOpt = input('>>> ')
    
    if startOpt == '1':
        LogIn()
    elif startOpt == '2':
        Register()
        
    print('\tdebug: main call')
    return

'''*******************************************
* Log In
*******************************************'''
def LogIn():
    ##prompt email
    loginEmail = input('Enter Email address: ')
       #check if account exists, else direct to register
    ##prompt password
    loginPswd = input('Enter Password: ')
       #check pswd, then go to main menu, else retry 5 times
    
    MainMenu()
       
    print('\tdebug: login call')
    return

'''*******************************************
* Register
*******************************************'''
def Register():
    ##prompt email
    emailTaken = False   
    regEmail = input('Enter Email address: ')
       #check if email is free, else retry or prompt for cancel
    while emailTaken:
        if regEmail.lower() == 'cancel':
            main()  #debug for reiteration problems
        elif emailTaken:
            regEmail = input("That Email address is taken. Try again or enter 'Cancel':")
        ##prompt: name, phone, password
    if (regEmail.lower != 'cancel'):
        regName = input('Enter Full Name: ')
        regPhone = input('Enter Phone Number: ')
        regPswd = getpass.getpass('Enter Password (input is hidden): ')
        #decide if:
        print('Account has been created') 
        ##GOTO main menu
        MainMenu()
        
    print('\tdebug: register call')
    return

'''*******************************************
* Main Menu
*******************************************'''
def MainMenu():
    Divider()
    ##list all options:
    print('This is your Main Menu.')
    print('\t1. Offer a Ride')
    print('\t2. Search for Rides')
    print('\t3. Manage Bookings')
    print('\t4. Post a Ride Request')
    print('\t5. Search for Ride Requests')
    print('\t6. View current Ride Requests')
    mmOpt = input("Please enter option number or 'Quit': ")
    invalidInput = True
    
    while invalidInput:
        if mmOpt.lower() == 'quit':
            return
        elif mmOpt == '1':
            invalidInput = False
            OfferRide()
        elif mmOpt == '2':
            invalidInput = False
            SearchRides()
        elif mmOpt == '3':
            invalidInput = False
            ManageBookings()
        elif mmOpt == '4':
            invalidInput = False
            PostRideReq()
        elif mmOpt == '5':
            invalidInput = False
            SearchRideReq()
        elif mmOpt == '6':
            invalidInput = False
            ViewRideReq()
        else:
            mmOpt = input("Invalid input. Try again: ")
    
    print('\tdebug: mainmenu call')
    return

Main()