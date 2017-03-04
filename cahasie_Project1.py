#Cal Hasie
#10-1-12
#Project 1



#Program that asks the user to enter a distance in meters.
#The program will then present its metric conversion.
def main():

    #Inputs the users metric meter amount.
    meter = float(input("\nEnter a distance in meters: "))
    if meter < 0:
        print("\nYou can't use a negative value!!!")
        main()

    #Shows the user the choices he can convert the meters to.
    print("\n1. Convert to kilometers")
    print("2. Convert to inches")
    print("3. Convert to feet")
    print("4. Convert to miles")
    print("5. Quit the program")
    convert(meter)

#It converts the mesurement of meters to the unit that is selected.
def convert(meter):

    #Makes the function continuous or loop.
    num = float(input("\nWhat would you like to do?(Choose a number 1-5): "))

    #If they choose five it will give the choice to end the program.
    if num == 5:
        print("\nThanks for using the program! Goodbye!")

    #Makes the function continuous or loop.
    if num != 5:
        if num == 1:
            print("\nThere are", \
            format(meter * .001, '.5f'), "kilometers in",meter,"meter(s).")
            main()
        elif num == 2:
            print("\nThere are", \
            format(meter * 39.37, '.5f'), "inches in",meter,"meter(s).")
            main()
        elif num == 3:
            print("\nThere are", \
            format(meter * 3.281, '.5f'), "feet in",meter,"meter(s).")
            main()
        elif num == 4:
            print("\nThere are", \
            format(meter * .000621, '.5f'), "miles in",meter,"meter(s).")
            main()
        else:
            print("\nYou entered a wrong value!!!")
            main()

main()
