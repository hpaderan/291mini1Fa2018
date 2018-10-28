'''*******************************************
* Search for Ride Requests
*******************************************'''
def SearchRideReq():
    Divider()
    
    opt = input("Enter option number or 'Main Menu': ")
    invalidOpt = True
    
    while invalidOpt:
        if opt.lower() == "main menu":
            invalidOpt = False
            MainMenu()
        else:
            opt = input('Invalid option. Try again: ')
            
    print('\tdebug: searchreq call')
    return