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
