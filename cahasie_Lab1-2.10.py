#Cal Hasie
#9/10/12
#Lab 1- 2.10

#This program will show the stock information Joe has computed.
def stock():
    #Basic math print calculation
    print("This program will show Joe's stock payments and commissions.\n")
    stock_1 = float(32.87*1000)
    print("The amount of money Joe initially spent on stocks is:",stock_1)
    com_1 = float(32.87*1000*.02)
    print("He paid his broker 2% of this initial amount:",com_1)
    stock_2 = float(33.92*1000)
    print("\nJoe sold all the shares two weeks later for:",stock_2)
    com_2 = float(33.92*1000*.02)
    print("Again Joe paid his broker 2% of the amount sold:",com_2)
    mon_left = float(-stock_1 - com_1 + stock_2 - com_2)
    print("\nTotal money after exchange:",format(mon_left,".2f"))
    print("\nJoe lost money.")
    
stock()

