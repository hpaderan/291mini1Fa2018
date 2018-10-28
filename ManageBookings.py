'''*******************************************
* Manage Bookings
*******************************************'''
def ManageBookings():
    Divider()
    
    # list all bookings
    print("Here are all of your bookings.")
    
    #submenu
    print("Options Menu")
    print('\t1. Cancel a booking')
    print('\t2. Book a member')
    print('\t3. Return to Main Menu')
    print('')
    
    
    print("input('enter booking number to cancel booking')")
    print("input('Cancel booking? (Y/N): ')")
    # YesOrNo(whatevs)
    
    opt = input("Enter option number: ")
    invalidOpt = True
    
    while invalidOpt:
        if opt.lower() == "main menu":
            invalidOpt = False
            MainMenu()
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
        #cancel existing booking here
        print("input('enter booking number to cancel booking')")
        print("input('Cancel booking? (Y/N): ')")
        #send message to booked member
        
    ToMainMenu()
      
    print('\tdebug: bookings call')
    return
