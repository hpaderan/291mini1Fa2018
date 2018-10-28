'''*******************************************
* Search for Rides
*******************************************'''
def SearchRides():
    Divider()
    
    ## Command check
    keywords = input("Enter Location keywords or 'Main Menu': ")

    if keywords.lower() == "main menu":
        MainMenu()
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
