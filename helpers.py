'''***************************************************
* Helper functions
***************************************************'''

'''** print simple divider **'''
def Divider():
    print('--------------------------------------')
    
'''** redirect to main menu **'''
def ToMainMenu():
    print("\nRedirecting to Main Menu.")
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