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