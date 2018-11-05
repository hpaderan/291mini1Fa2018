import time
import getpass
import sqlite3
import datetime

connection = None
cursor = None
g_email = None

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
    print("\t3. Exit program.")
    startOpt = input('>>> ')
    
    while (startOpt != '3'):     
        if startOpt == '1':
            LogIn()
        elif startOpt == '2':
            Register()
        elif startOpt == '3':
            continue
        else:
            print("Invalid input.")
        Divider()
        print('Please enter option number and press Enter.')
        print('\t1. Log In with existing account.')
        print('\t2. Register a new account.')
        print("\t3. Exit program.")
        startOpt = input(">>> ")
        
    print('\tdebug: main call')
    return

'''*******************************************
* Log In
*******************************************'''
def LogIn():
    Divider()
    global connection, cursor,g_email
    #user have total 6 times of input email and psw
    loginSuccess = False
    maxTry = False
    i = 0
    while (loginSuccess == False and i < 5):
        ##prompt email
        loginEmail = change_type(input('Enter Email address: '))
        if (loginEmail[0].lower() == "cancel"):
            break
        ##prompt password
        loginPswd = change_type(input('Enter Password: '))
        #check if account exists
        cursor.execute("SELECT pwd FROM members WHERE email = ?;",loginEmail)
        real_psw = cursor.fetchone()
        if real_psw == None:
            print("Email address not exit, please try again, or 'Cancel'")
        else:
            real_psw = real_psw[0]
            #check pswd, then go to main menu, else retry 5 times
            if real_psw == loginPswd[0]:
                g_email = loginEmail
                loginSuccess = True
            else:
                i += 1
                print("Incorrect password please try again")
                if (i < 5):
                    maxTry = True
        
    if loginSuccess:
        cursor.execute("SELECT name FROM members WHERE email = ?;", loginEmail)
        print("Hello, %s." % cursor.fetchone())
        MainMenu()
    elif maxTry:
        print("Reached max number of tries")
        time.sleep(0.7)
    
       
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
    g_email = (regEmail,)
    MainMenu()
        
    print('\tdebug: register call')
    return

'''*******************************************
* Main Menu
*******************************************'''
def MainMenu():
    global connection, cursor, g_email
    Divider()
    
    ##display messages
    cursor.execute("SELECT * FROM inbox WHERE email = ?;", g_email)
    inboxAll = cursor.fetchall()
    cursor.execute("UPDATE inbox SET seen = 'y' WHERE email = ?;", g_email)
    connection.commit()
    
    print("Inbox: ")
    if (len(inboxAll) < 1):
        print("You have no new messages.")
    for newMssg in inboxAll:
        print(newMssg[5])
        if (newMssg[5] == 'n'):
            print("%s Rno %s \n%s: %s\n" % (newMssg[1], newMssg[4], newMssg[2], newMssg[3]))
        
    Divider()
    time.sleep(1)
    
    ##list all options:
    print('This is your Main Menu.')
    print('\t1. Offer a Ride')
    print('\t2. Search for Rides')
    print('\t3. Manage Bookings')
    print('\t4. Post a Ride Request')
    print('\t5. Search for Ride Requests')
    print('\t6. View current Ride Requests')
    mmOpt = input("Please enter option number or 'Log Out': ")
    invalidInput = True
    
    while invalidInput:
        if mmOpt.lower() == 'log out':
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
    #print(g_email)
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
        newSrc_add_success = False
        while newSrc_add_success == False:
            newSrc =  change_type( input("Source location: "))
            cursor.execute("SELECT * FROM locations WHERE lcode = ?;",newSrc)
            key_word_search = cursor.fetchone()
            if key_word_search == None:
                print("Invalid keyword plese chooes and enter one of the following lcode")
                keyword_search(newSrc[0])
                continue
            else:
                newSrc_add_success = True        
        
        
        newDst_add_success = False
        while newDst_add_success == False:
            newDst =  change_type( input("Destination location: "))
            cursor.execute("SELECT * FROM locations WHERE lcode = ?;",newDst)
            key_word_search = cursor.fetchone()
            if key_word_search == None:
                print("Invalid keyword plese chooes and enter one of the following lcode")
                keyword_search(newDst[0])
                continue
            else:
                newDst_add_success = True            
        
        print('Please enter option and press Enter.')
        
        # optional car no; check if owned by driver
        car_add_succes = False
        while car_add_succes == False:
            opt = input('Adding a car ? (Y/N): ')
            car_add_opt = YesOrNo(opt)
            if car_add_opt:
                cno = change_type(input("Please enter your cno : "))
                cursor.execute("SELECT owner FROM cars WHERE cno = ?;",cno)
                car_search_result = cursor.fetchone()
                #print(car_search_result[0])
                if car_search_result == None:
                    print("Can not find this car, please try again")
                    continue;
                if car_search_result[0] != g_email[0]:
                    print("This car does not belong to you,please try again")
                
                else:
                    print("Car add successed")
                    car_add_succes = True
                    insert_cno = cno[0]
            else:
                insert_cno = None
                car_add_succes = True
            
        # optional enroute
        enroute_add_success = False
        while enroute_add_success == False:
            opt = input('Adding set of enroute location ? (Y/N): ')
            add_enroute_opt = YesOrNo(opt)
            if insert_cno == None:
                print("Can not createnroute without a cno")
                break
            if add_enroute_opt:
                keyword = change_type(input("Please enter the keyword (lcode)"))
                cursor.execute("SELECT * FROM locations WHERE lcode = ?;",keyword)
                key_word_search = cursor.fetchone()
                if key_word_search == None:
                    keyword_search(keyword[0])
                    continue
                enroute_info = (new_rno,keyword[0])
                cursor.execute('INSERT INTO enroute(rno, lcode) VALUES (?,?);', enroute_info)
                connection.commit() 
                enroute_add_success = True
            else:
                enroute_add_success = True
            

        # auto set driver and unique rno
        info = (new_rno,inputprice,inputDate,inputSeats,inputLugg.lower(),newSrc[0],newDst[0],g_email[0],insert_cno)
        cursor.execute('INSERT INTO rides(rno, price, rdate,seats,lugDesc, src, dst, driver, cno) VALUES (?,?,?,?,?,?,?,?,?);', info)
        connection.commit()
        # post ride here
        print("offer rides successed")
        # success check
        
        ## return to main menu on success/fail
        #newOffer = False
        
    ToMainMenu()
            
    print('\tdebug: offerride call')
    return


'''*******************************************
* Search for Rides - Holden
*******************************************'''
def SearchRides():
    Divider()
    global connection, cursor, g_email
    
    ## Command check
    keywords = input("Enter 1-3 Location keywords or 'Main Menu': ")

    if keywords.lower()== 'main menu':
        ToMainMenu()

    else:
        keywords = keywords.split()
        location = []
        for keys in keywords:
            cursor.execute('''SELECT DISTINCT lcode
                              FROM locations
                              WHERE lcode = ?
                              OR city LIKE ?
                              OR prov LIKE ?
                              OR address LIKE ? ;''',keys)
            Ref = cursor.fetchall()
            for Re in Ref: 
                locations = location.append(Re)
                locations = location(set(ids))

    if len(locations)>2:
        print("Please enter less or equal to 3 keywords!")
        ToMainMenu()

    else:
        results = []
        for lcode in locations:
            cursor.execute('''SELECT *
                              FROM rides r, enroute e, cars c
                              WHERE e.rno = r.rno AND e.lcode = ?
                              OR r.src = ?
                              OR r.dst = ?
                              GROUP BY r.rno
                              HAVING r.rno = e.rno AND r.cno = c.cno;''', lcode)
        results = result.append(cursor.fetchall())

        #process keywords here
        #split into single words
        # search database; input check
        i = 0
        
        # if result success:
        while (i < len(results) and i < 5):
            print(result[i])
            #display results here
            i += 1

        opt = True
        while (i < len(results)and opt):
            r = i
            opt = input('Display 5 more? (Y/N): ')
            display = YesOrNo(opt)
            if display:
                while (i < len(results)and i < r+5 ):
                    print(result[i])
                    i += 1
            else:
                opt = False
                pass

        #on success, option to request booking on a ride
        optRno = input("Enter rno of ride to be booked, or 'Cancel': ")
        if optRno.lower() == 'cancel':
            return
        else:
            numSeats = input("How many seats to book?: ")
            for ride in results:
                if optRno == ride:
                    RefRid = ride
                    pass
            email = RefRid[7]
            t = datetime.datetime.now()
            content = 'Number of seats requested: '+str(numSeats)
            rno = RefRid[0]
            info = (email, time, g_mail, content, rno, 'n')
            cursor.execute('INSERT INTO inbox(email, msgTimestamp, sender, content, rno, seen) VALUES (?,?,?,?,?);', info)
            connection.commit()
        # book seats here!!!!
        #on success:
            print("Booking request sent: ",str(numSeats),"seats in ride", str(optRno))
        
        # if search fail:
        
    #redirect main menu
    ToMainMenu()
            
    print('\tdebug: searchride call')
    return

'''*******************************************
* Manage Bookings - Holden
*******************************************'''
def ManageBookings():
    Divider()
    
    # list all bookings
    cursor.execute('SELECT * FROM bookings WHERE email = ? ;', g_mail)
    Blist = cursor.fetchall()
    print("Here are all of your bookings.")
    for bookings in Blist:
        print(str(bookings))
    
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
        member = input('Enter the EMAIL of the member whose ride you want to book: ')
        cursor.execute('''SELECT * FROM rides WHERE driver = ? ;''', member)
        RidList = cursor.fetchall()

        i = 0
        while (i<len(RidList) and i<5):
            print(RidList[i])
            i += 1

        opt = True
        while (i < len(RidList) and opt):
            r = i
            opt = input('Display 5 more? (Y/N): ')
            display = YesOrNo(opt)
            if display:
                while (i < len(RidList) and i < r+5):
                    print(RidList[i])
                    i += 1
            else:
                opt = False
                pass

        print('')
        

        Brno = input('Please enter the Ride Number that you want to book: ')
        email = input('Please enter the email of the member who offers the ride: ')
        cost = input('Please enter the price you can offer for each seat: ')
        seats = input('Please enter the seat required of your booking: ')
        pickup = input('Please enter the location code of your pick up location: ')
        dropoff = input('Please enter the location code of your drop off location: ')
        cursor.execute('SELECT COUNT(*) FROM bookings ')
        bno = cursor.fetchone()
        bno = 1 + int(bno[0])

        
        cursor.execute('SELECT seats FROM rides WHERE rno = ? ;', Brno)
        rseats = cursor.fetchone()
        if seats > int(rseats[0]):
            print('Warning! This member may not be able to offer all seats for your request! Your booking will still be registed.')

        info = (bno, email, Brno, cost, seats, pickup, fropoff)
        cursor.execute('INSERT INTO bookings(bno, email, rno, cost, seats, pickup, dropoff) VALUE (?,?,?,?,?,?,?);', info)
        connection.commit()
        
        content = 'Someone has offered a Booking!'
        ti = datetime.datetime.now()
        
        mess = (member, ti, g_mail, content, Brno, 'n')
        cursor.execute("INSERT INTO inbox (email, msgTimestamp, sender, content, rno, seen) VALUES (?,?,?,?,?,?)", mess)
        #send message to booked member
        
    elif cancelBooking:
        targetBno = input('Enter booking number to cancel booking: ')
        confirm = input('Cancel booking? (Y/N): ')
        cancelBno = YesOrNo(confirm)
        cursor.execute('SELECT * FROM rides WHERE bookings.bno = ? AND bookings.rno = rides.rno ;', targetBno )
        RefRid = cursor.fetchone()
        email = RefRid[7]
        content = "The Booking has been canceled"
        t = datetime.datetime.now()
        sender = g_mail
        rno = RefRid[0]
        mess = (email, t, sender, content, rno, 'n')
        cursor.execute("INSERT INTO inbox (email, msgTimestamp, sender, content, rno, seen) VALUES (?,?,?,?,?,?)", mess)
        cursor.execute('DELETE FROM bookings WHERE bno = ? ;', targetBno)
        connection.commit()
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
    keyword = input("Enter Location keywords or 'Main Menu': ")

    if keyword.lower() == "main menu":
        ToMainMenu()
    else:
        #process keywords here
        #split into single words    
        while (len(keyword.split()) > 1):
            keyword = input("Please enter a city or a location code: ")

        # search database; input check
        searchRes = []
        fmtTemp = (keyword[0].upper(), keyword[1:].lower())
        fmtKeyword = "%s%s" % fmtTemp
        cursor.execute('''SELECT * 
                          FROM requests 
                          WHERE pickup = ? 
                          OR pickup IN (SELECT lcode FROM locations WHERE city = ?)''', (keyword,fmtKeyword))
        searchRes = cursor.fetchall()
        searchRids = []
                
        
            
    #on success, option to request booking on a ride
        print('')
                
        #input check
        invRid = True
        dispIndex = 0
        while invRid:         
            for i in range(dispIndex, dispIndex+5):
                if (i < len(searchRes)):
                    searchRids.append(searchRes[i][0])
                    
                    reqName = GetFullName(searchRes[i][1])
                    reqPickup = GetAddressFromCode(searchRes[i][3])
                    reqDropoff = GetAddressFromCode(searchRes[i][4])
                    fmtReq = ("%s : %s from %s to %s %s -- $%s") % (searchRes[i][0], reqName, reqPickup, reqDropoff, searchRes[i][2], searchRes[i][5])
                    print(fmtReq)
        
            Divider()
            optRid = input("Enter Request number to message requester, 'Next' to view next 5, or 'Cancel': ")               
            if optRid.lower() == 'cancel':
            # case if user wants to cancel message sending
                invRid = False
                # exit out of loop into Main Menu
                
            elif optRid.lower() == 'next':
                dispIndex += 5
                if dispIndex >= len(searchRes):
                    dispIndex = 0
                
            elif (int(optRid) in searchRids):
            # case if rid is valid and user is sending a message
                invRid = False
                
                # Rno check
                invRno = True
                mssgRno = input("Enter an RNO of associated Ride, or 'Cancel': ")
                cursor.execute("SELECT rno FROM rides WHERE driver = ?;", g_email)
                confirmRnos = []
                allRnos = cursor.fetchall()
                for eachRno in allRnos:
                    confirmRnos.append(str(eachRno[0]))
                while invRno:
                    if (str(mssgRno).lower() == "cancel"):
                        #case if user cancel rno selection
                        invRno = False
                        break
                    elif (mssgRno in confirmRnos):
                        #case if rno selection success
                        invRno = False
                        message = input("Message to requester: ")
                        
                        #get email to
                        for req in searchRes:
                            if req[0] == int(optRid):
                                email = req[1]         
                                
                        #get mssg info
                        timeNow = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
                        mssgInKey = (email, timeNow, g_email[0], message, mssgRno,'n')
                        
                        # send message here
                        cursor.execute("INSERT INTO inbox (email, msgTimestamp, sender, content, rno, seen) VALUES (?,?,?,?,?,?)", mssgInKey)
                        connection.commit()
                        #on success:
                        print("Message sent to ", email)  
                        time.sleep(0.5)
                        
                    else:
                        #case if invalid rno
                        mssgRno = input("You are not the driver of this ride, \n\tPlease enter RNO of a ride you offered: ")
                        
            else:
            # case if input is invalid
                print("Invalid RID. Please try again: ")
        
        #redirect main menu
        ToMainMenu()        
            
    print('\tdebug: searchreq call')
    return

'''*******************************************
* View/Delete current Ride Requests
*******************************************'''
def ViewRideReq():
    Divider()
    
    #show user reqs here
    global connection, cursor, g_email
    
    cursor.execute("SELECT * FROM requests WHERE email = ?;", g_email)
    reqs = cursor.fetchall()
    for i in range(len(reqs)):
        cursor.execute("SELECT address,city,prov FROM locations WHERE lcode = ?;", (reqs[i][3],))
        newPickup = cursor.fetchone()
        cursor.execute("SELECT address,city,prov FROM locations WHERE lcode = ?;", (reqs[i][4],))
        newDropoff = cursor.fetchone()
        
        print (reqs[i][0],":", newPickup, "to" , newDropoff, reqs[i][2], "$", reqs[i][5])
    
    cancelRid = input('Enter Request ID to cancel request, or "Return": ')

    cancel = False
    if (cancelRid.lower() != 'return'):
        confirm = input("Cancel request? (Y/N): ")
        cancel = YesOrNo(confirm)
        
    
    if cancel:
        intRid = int(cancelRid)
        print("Booking canceled.")
        cursor.execute("DELETE FROM requests WHERE rid = ?", (intRid,))
        connection.commit()
        
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

'''** keyword search print location that related with or similar with (print only)**'''
def keyword_search(keyword):
    global connection, cursor
    keyword = keyword.capitalize()
    similar_address = "%"+keyword + "%"
    keyword = (keyword,keyword,similar_address)
    cursor.execute("select distinct* from locations where city = ? or prov = ? or address like ?; ",keyword)
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
                print("printed all similar locations")
                return
            for i in range(5):
                print(result[count+i])
            opt = input('continue to print? (Y/N): ')
            printing = YesOrNo(opt)
    return

'''** Get member name from email **'''
def GetFullName(email):
    global connection, cursor
    cursor.execute("SELECT name FROM members WHERE email = ?;", (email,))
    return cursor.fetchone()[0]

'''**  Get address from location code **'''
def GetAddressFromCode (lcode):
    global connection, cursor
    cursor.execute("SELECT address,city,prov FROM locations WHERE lcode = ?;", (lcode,))
    return cursor.fetchone()
    
Main()
