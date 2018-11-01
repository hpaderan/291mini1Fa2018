import time
import getpass
import sqlite3

connection = None
cursor = None
g_email = ' '

def connect(path):
    global connection, cursor

    connection = sqlite3.connect(path)
    cursor = connection.cursor()
    cursor.execute(' PRAGMA forteign_keys=ON; ')
    connection.commit()
    return


'''*******************************************
* Main function
*******************************************'''
def Main():
    global connection, cursor
    path = "./mini1.db"
    connect(path)
    
    
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
    global connection, cursor,g_email
    #user have total 6 times of input email and psw
    for i in range(6):
        ##prompt email
        loginEmail = change_type(input('Enter Email address: '))
        ##prompt password
        loginPswd = change_type(input('Enter Password: '))
        print(loginEmail)
        #check if account exists, else direct to register
        cursor.execute("SELECT pwd FROM members WHERE email = ?;",loginEmail)
        real_psw = cursor.fetchone()
        if real_psw == None:
            print("Email address not exit, please try again")
            continue
        real_psw = real_psw[0]
        #check pswd, then go to main menu, else retry 5 times
        if real_psw == loginPswd[0]:
            g_email = loginEmail
            MainMenu()
        else:
            print("Incorrect password please try again")
    
       
    print('\tdebug: login call')
    return

'''*******************************************
* Register
*******************************************'''
def Register():
    global connection, cursor, g_email
    created = False
    ##prompt email
    emailTaken = False
    regEmail = change_type(input('Enter Email address: '))
    while created == False:
        #check if email is free, else retry or prompt for cancel
        cursor.execute("SELECT * FROM members WHERE email = ?;",regEmail)
        result = cursor.fetchone()
        if regEmail[0] == 'cancel':
            Main()  #debug for reiteration problems
            
        if result != None:
            emailTaken = True   
            
        if emailTaken:
            print("That Email address is taken. Try again or enter 'Cancel'")
            Register()
            
        ##prompt: name, phone, password
        else:
            regName = input('Enter Full Name: ')
            regPhone = input('Enter Phone Number: ')
            regPswd = getpass.getpass('Enter Password (input is hidden): ')
            regEmail = regEmail[0]
            info = (regEmail,regName.lower(),regPhone.lower(),regPswd.lower())
            cursor.execute('INSERT INTO members(email, name, phone, pwd) VALUES (?,?,?,?);', info)
            print('Account has been created') 
            created = True
    connection.commit()            
    ##GOTO main menu
    g_email = regEmail
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
    global connection, cursor, g_email
    ## Input check
    opt = input('Offer a ride? (Y/N): ')
    newOffer = YesOrNo(opt)
            
    ## everything that comes with offering a new ride       
    if newOffer:
        #create a unique rno
        cursor.execute('select max(rides.rno)from rides;')
        current_rno = cursor.fetchone()
        new_rno = current_rno[0] + 1        
        #create new ride offer  ##consider input check
        inputDate = input("Date (YYYY-MM-DD): ")

        inputSeats = input("Number of seats offered: ")

        inputprice = input("Price per seat ($): ")

        inputLugg =  input("Luggage description: ")

        #keyword check
        newSrc =  change_type( input("Source location: "))
        newDst =  change_type( input("Destination location: "))
        print('Please enter option and press Enter.')
        
        
        
        
        # optional car no; check if owned by driver
        opt = input('Adding a car ? (Y/N): ')
        car_add_succes = False
        while car_add_succes == False:
            car_add_opt = YesOrNo(opt)
            if car_add_opt:
                
                cno = change_type(input("Please enter your cno or type cancel:"))
                cursor.execute("SELECT owner FROM cars WHERE cno = ?;",cno)
                car_search_result = cursor.fetchone()
                
                if car_search_result == None:
                    print("Can not find this car, please try again")
                    continue;
                elif car_search_result[0] != g_email:
                    print("This car does not belong to you,please try again")
                
                else:
                    print("Car add successed")
                    car_add_succes = True
            
        # optional enroute    
        opt = input('Adding set of enroute location ? (Y/N): ')
        add_enroute_opt = YesOrNo(opt)
        if add_enroute_opt:
            enroute_keyword = change_type(input("Please enter the keyword"))
            keyword_search(enroute_keyword)
                
            

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
    global connection, cursor,g_email
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
        cursor.execute('SELECT max(requests.rid) from requests;')
        current_rid = cursor.fetchone()
        new_rid = current_rid[0] + 1
        #newEmail is the request poster
        #finish create ridereq
        info = (new_rid,g_email,newDate,newPickup.lower(),newDropoff.lower(),newPrice)
        cursor.execute('INSERT INTO requests(rid, email, rdate, pickup, dropoff,amount) VALUES (?,?,?,?,?,?);', info)
        #success message
        connection.commit()
        print('ride post successed')
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

'''** convert input to sqlite3 readble typr **'''

def change_type(strings):
    output = (strings.lower(),)
    return output

'''** keyword search **'''
def keyword_search(keyword):
    global connection, cursor
    similar_address = "%"+keyword + "%"
    keyword = (keyword,keyword,keyword,similar_address)
    cursor.execute("select distinct* from locations where lcode = ? or city = ? or prov = ? or address like ?; ",keyword)
    result = cursor.fetchall()
    length = len(result)
    if length < 5:
        for r in result:
            print(r)
    else:
        printing = True
        count = 0
        while printing == True:
            count += 5
            length -= 5            
            if length < 5:
                for i in range(length):
                    print(result[count+i])
                print("printed all reavent locations")
                break
        
            for i in range(5):
                print(result[count+i])
            opt = input('continue to print? (Y/N): ')
            printing = YesOrNo(opt)


Main()
