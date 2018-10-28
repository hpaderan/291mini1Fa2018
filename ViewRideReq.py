'''*******************************************
* View/Delete current Ride Requests
*******************************************'''
def ViewRideReq():
    divider()
    
    opt = input("Enter option number or 'Main Menu': ")
    invalidOpt = True
    
    while invalidOpt:
        if opt.lower() == "main menu":
            invalidOpt = False
            MainMenu()
        else:
            opt = input('Invalid option. Try again: ')
            
    print('\tdebug: viewreqs call')
    return