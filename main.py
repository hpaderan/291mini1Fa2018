import time
import getpass
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

'''*******************************************
* Offer a Ride
*******************************************'''
def OfferRide():
    Divider()

    ## Input check
    opt = input('Offer a ride? (Y/N): ')
    newOffer = YesOrNo(opt)
            
    ## everything that comes with offering a new ride       
    if newOffer:
        #create new ride offer  ##consider input check
        newDate =  input("Date (YYYY-MM-DD): ")
        newSeats = input("Number of seats offered: ")
        newPrice = input("Price per seat ($): ")
        newLugg =  input("Luggage description: ")
        #keyword check
        newSrc =   input("Source location: ")
        newDst =   input("Destination location: ")
        # optional enroute
        # optional car no; check if owned by driver
        # auto set driver and unique rno
        
        # post ride here
        # success check
        
        ## return to main menu on success/fail
        #newOffer = False
        
    ToMainMenu()
            
    print('\tdebug: offerride call')
    return

'''*******************************************
* Search for Rides
*******************************************'''
def SearchRides():
    Divider()
    
    ## Command check
    keywords = input("Enter Location keywords or 'Main Menu': ")

    if keywords.lower() == "main menu":
        ToMainMenu()
    else:
        #process keywords here
        #split into single words
        # search database; input check
        results = ['poop', 'poo', 'po']
        i = 0
        
        # if result success:
        while (i < len(results) and i < 5):
            #display results here
            i += 1
            print("printing", str(6 - i), "search results")
        #on success, option to request booking on a ride
        optRno = input("Enter rno of ride to be booked, or 'Cancel': ")
        if optRno.lower() == 'cancel':
            return
        else:
            numSeats = input("How many seats to book?: ")
            
        # book seats here!!!!
        
        #on success:
        print("Booking request sent: ",str(numSeats),"seats in ride", str(optRno))
        #on fail
        print("Booking failed.")
        
        # if search fail:
        
    #redirect main menu
    ToMainMenu()
            
    print('\tdebug: searchride call')
    return

'''*******************************************
* Manage Bookings
*******************************************'''
def ManageBookings():
    Divider()
    
    # list all bookings
    print("Here are all of your bookings.")
    print('')
    
    #submenu
    print("Options Menu")
    print('\t1. Cancel a booking')
    print('\t2. Book a member')
    print('\t3. Return to Main Menu')
    print('')

    opt = input("Enter option number, or 'Main Menu': ")
    invalidOpt = True
    newBooking = False
    cancelBooking = False
    
    while invalidOpt:
        if opt.lower() == "main menu":
            invalidOpt = False
            ToMainMenu()
        elif opt.lower() == '3':
            invalidOpt = False
            MainMenu()
        elif opt.lower() == '2':
            invalidOpt = False
            newBooking = True
        elif opt.lower() == '1':
            invalidOpt = False
            cancelBooking = True
        else:
            opt = input('Invalid option. Try again: ')
    
    if newBooking:
        #create new booking here
        print('')
        #send message to booked member
        
    elif cancelBooking:
        targetBno = input('Enter booking number to cancel booking: ')
        confirm = input('Cancel booking? (Y/N): ')
        cancelBno = YesOrNo(confirm)
        #cancel booking here
        #send message to booked member
        
    ToMainMenu()
      
    print('\tdebug: bookings call')
    return

'''*******************************************
* Post Ride Request
*******************************************'''
def PostRideReq():
    Divider()
    
    opt = input('Offer a ride? (Y/N): ')
    newRideReq = YesOrNo(opt)    
    
    if newRideReq:
        #prompts 
        #create new ride req  ##consider input check
        newDate =  input("Date (YYYY-MM-DD): ")
        # keyword check
        newPickup = input("Pickup location: ")
        newDropoff = input("Drop-off location: ")
        newPrice =  input("Price per seat ($): ")
        #generate request id
        #newEmail is the request poster
        #finish create ridereq
        #success message
        
    ToMainMenu()
            
    print('\tdebug: postreq call')
    return

'''*******************************************
* Search for Ride Requests
*******************************************'''
def SearchRideReq():
    Divider()
    
    ## Command check
    keywords = input("Enter Location keywords or 'Main Menu': ")

    if keywords.lower() == "main menu":
        ToMainMenu()
    else:
        #process keywords here
        #split into single words
        # search database; input check
        results = ['poop', 'poo', 'po']
        i = 0
        
        # if result success:
        while (i < len(results) and i < 5):
            #display results here
            i += 1
            print("printing", str(6 - i), "search results")
            
    #on success, option to request booking on a ride
        optRid = input("Enter Request ID to message requester, or 'Cancel': ")
        if optRid.lower() == 'cancel':
            ToMainMenu()
        else:
            message = input("Message to requester: ")
            email = "get email of request"
            
            # book seats here!!!!
        
            #on success:
            print("Message sent to ", email)
            #on fail
            print("Do we need a fail case here?")
        
        # if search fail:
        
            #redirect main menu
            ToMainMenu()        
            
    print('\tdebug: searchreq call')
    return

'''*******************************************
* View/Delete current Ride Requests
*******************************************'''
def ViewRideReq():
    Divider()
    
    cancelRid = input('Enter Request ID to cancel request: ')
    confirm = input("Cancel request? (Y/N): ")
    cancel = YesOrNo(confirm)
    
    if cancel:
        print("Booking canceled.")
        #cancel the booking here
        
    ToMainMenu()
            
    print('\tdebug: viewreqs call')
    return

'''***************************************************
* Helper functions
***************************************************'''

'''** print simple divider **'''
def Divider():
    print('--------------------------------------')
    
'''** redirect to main menu **'''
def ToMainMenu():
    print("\nRedirecting to Main Menu.")
    time.sleep(0.8)
    MainMenu()

'''** Handle yes or no input **'''
def YesOrNo(strParam):
    invalidOpt = True
    while invalidOpt:
        if strParam.lower() == 'y':
            result = True
            invalidOpt = False
        elif strParam.lower() == 'n':
            result = False
            invalidOpt = False
        else:
            strParam = input("Invalid option, try again (Y/N): ")
    return result

Main()