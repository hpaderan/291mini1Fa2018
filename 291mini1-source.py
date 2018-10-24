import getpass

'''*******************************************
* Main function
*******************************************'''
def main():
    ##ask if log in or register
    print('Please enter option number and press Enter.')
    print('\t1. Log In with existing account.')
    print('\t2. Register a new account.')
    startOpt = input('>>> ')
    
    if startOpt == '1':
        logIn()
    elif startOpt == '2':
        register()
        
    print('\tdebug: main call')
    return

'''*******************************************
* Log In
*******************************************'''
def logIn():
    ##prompt email
    loginEmail = input('Enter Email address: ')
       #check if account exists, else direct to register
    ##prompt password
    loginPswd = input('Enter Password: ')
       #check pswd, then go to main menu, else retry 5 times
       
    print('\tdebug: login call')
    return

'''*******************************************
* Register
*******************************************'''
def register():
    #prompt email
    emailTaken = True
    regEmail = input('Enter Email address: ')
       #check if email is free, else retry or prompt for cancel
    while emailTaken:
        if regEmail.lower() == 'cancel':
            main()  #debug for reiteration problems
        elif emailTaken:
            regEmail = input("That Email address is taken. Enter a different one or enter 'Cancel' to cancel login: ")
        #prompt: name, phone, password
    if (regEmail.lower != cancel):
        regName = input('Enter Full Name: ')
        regPhone = input('Enter Phone Number: ')
        regPswd = getpass.getpass('Enter Password (input is hidden): ')
        #decide if:
        print('Account has been created') 
        #GOTO main menu
        
    print('\tdebug: register call')
    return

'''*******************************************
* Main Menu
*******************************************'''
def mainMenu():
    #list all options:
    print('This is your Main Menu.')
    #   1. offer a ride
    print('\t1. Offer a Ride')
    #   2. search for rides
    print('\t2. Search for Rides')
    #   3. manage bookings
    print('\t3. Manage Bookings')
    #   4. post ride request
    print('\t4. Post a Ride Request')
    #   5. search ride requests
    print('\t5. Search for Ride Requests')
    #   6. view/delete current ride requests
    print('\t6. View current Ride Requests')
    #prompt for option
    mmOpt = input('Please enter option number and press Enter: ')
    
    print('\tdebug: mainmenu call')
    return

'''*******************************************
* Offer a Ride
*******************************************'''
def offerRide():
    
    print('\tdebug: offerride call')
    return

'''*******************************************
* Search for Rides
*******************************************'''
def searchRides():
    
    print('\tdebug: searchride call')
    return

'''*******************************************
* Manage Bookings
*******************************************'''
def manageBookings():
    
    print('\tdebug: bookings call')
    return

'''*******************************************
* Post Ride Request
*******************************************'''
def postRideReq():
    
    print('\tdebug: postreq call')
    return

'''*******************************************
* Search for Ride Requests
*******************************************'''
def searchRideReq():
    
    print('\tdebug: searchreq call')
    return

'''*******************************************
* View/Delete current Ride Requests
*******************************************'''
def viewRideReq():
    
    print('\tdebug: viewreqs call')
    return

main()