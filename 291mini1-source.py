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
    
    mainMenu()
       
    print('\tdebug: login call')
    return

'''*******************************************
* Register
*******************************************'''
def register():
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
        mainMenu()
        
    print('\tdebug: register call')
    return

'''*******************************************
* Main Menu
*******************************************'''
def mainMenu():
    divider()
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
            offerRide()
        elif mmOpt == '2':
            invalidInput = False
            searchRides()
        elif mmOpt == '3':
            invalidInput = False
            manageBookings()
        elif mmOpt == '4':
            invalidInput = False
            postRideReq()
        elif mmOpt == '5':
            invalidInput = False
            searchRideReq()
        elif mmOpt == '6':
            invalidInput = False
            viewRideReq()
        else:
            mmOpt = input("Invalid input. Try again: ")
    
    print('\tdebug: mainmenu call')
    return

'''*******************************************
* Offer a Ride - 1
*******************************************'''
def offerRide():
    divider()

    ## Input check
    opt = input('Offer a ride? (Y/N): ')
    invalidOpt = True
    
    while invalidOpt:
        if opt.lower() == "n":
            invalidOpt = False
            print("Redirecting to Main Menu.")
            mainMenu()
        elif opt.lower() == "y":
            invalidOpt = False
            newOffer = True
        else:
            opt = input('Invalid option. Try again: ')
            
    if newOffer:
        #create new ride offer  ##consider input check
        newDate =  input("Date (YYYY-MM-DD): ")
        newSeats = input("Number of seats offered: ")
        newPrice = input("Price per seat: ")
        newLugg =  input("Luggage description: ")
        #keyword check
        newSrc =   input("Source location: ")
        newDst =   input("Destination location: ")
        # optional enroute
        # optional car no; check if owned by driver
        # auto set driver and unique rno
        
        # post ride here
        # success check
        
        #newOffer = False
        print("Redirecting to Main Menu.")
        mainMenu()
            
    print('\tdebug: offerride call')
    return

'''*******************************************
* Search for Rides - 2
*******************************************'''
def searchRides():
    divider()
    
    opt = input("Enter option number or 'Main Menu': ")
    invalidOpt = True
    
    while invalidOpt:
        if opt.lower() == "main menu":
            invalidOpt = False
            mainMenu()
        else:
            opt = input('Invalid option. Try again: ')
            
    print('\tdebug: searchride call')
    return

'''*******************************************
* Manage Bookings - 3
*******************************************'''
def manageBookings():
    divider()
    
    opt = input("Enter option number or 'Main Menu': ")
    invalidOpt = True
    
    while invalidOpt:
        if opt.lower() == "main menu":
            invalidOpt = False
            mainMenu()
        else:
            opt = input('Invalid option. Try again: ')
            
    print('\tdebug: bookings call')
    return

'''*******************************************
* Post Ride Request - 4
*******************************************'''
def postRideReq():
    divider()
    
    opt = input("Enter option number or 'Main Menu': ")
    invalidOpt = True
    
    while invalidOpt:
        if opt.lower() == "main menu":
            invalidOpt = False
            mainMenu()
        else:
            opt = input('Invalid option. Try again: ')
            
    print('\tdebug: postreq call')
    return

'''*******************************************
* Search for Ride Requests - 5
*******************************************'''
def searchRideReq():
    divider()
    
    opt = input("Enter option number or 'Main Menu': ")
    invalidOpt = True
    
    while invalidOpt:
        if opt.lower() == "main menu":
            invalidOpt = False
            mainMenu()
        else:
            opt = input('Invalid option. Try again: ')
            
    print('\tdebug: searchreq call')
    return

'''*******************************************
* View/Delete current Ride Requests - 6
*******************************************'''
def viewRideReq():
    divider()
    
    opt = input("Enter option number or 'Main Menu': ")
    invalidOpt = True
    
    while invalidOpt:
        if opt.lower() == "main menu":
            invalidOpt = False
            mainMenu()
        else:
            opt = input('Invalid option. Try again: ')
            
    print('\tdebug: viewreqs call')
    return

'''** print simple divider for UI **'''
def divider():
    print('--------------------------------------')

main()