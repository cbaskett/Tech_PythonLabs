#Cal Hasie
#9-24-12
#Lab 3- 4.9

#This program will tell how much it costs for the certain weight of product.
def main():
    pound = float(input("How much does your package weigh?: "))
    if pound <= 2:
        print("The shipping charge is",format(pound*1.1, ".2f"),sep=' $')
    elif pound > 2 or pound <= 6:
        print("The shipping charge is",format(pound*2.2, ".2f"),sep=' $')
    elif pound > 6 or pound <= 10:
        print("The shipping charge is",format(pound*3.7, ".2f"),sep=' $')
    elif pound > 10:
        print("The shipping charge is",format(pound*3.8, ".2f"),sep=' $')
    else:
        print("You entered an invalid number.")
    
main()
