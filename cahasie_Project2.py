#Cal Hasie
#10-1-12
#Project 1



#Reads the data for each planet and stores it in a global variable.
merc = open('Mercury.txt', 'r')
mercury = merc.read()
merc.close()

ven = open('Venus.txt', 'r')
venus = ven.read()
ven.close()

ear = open('Earth.txt', 'r')
earth = ear.read()
ear.close()

mar = open('Mars.txt', 'r')
mars = mar.read()
mar.close()

#This Program lets you select a planet and return info about that planet
#and then stores it to files. 
def main():

    #Shows the user the choices he can select for planet info return.
    print("\n     Select a Planet")
    print("1. Mercury")
    print("2. Venus")
    print("3. Earth")
    print("4. Mars")
    print("5. Exit the program")

    #Calls the second function
    convert()

#It converts the mesurement of meters to the unit that is selected.
def convert():

    try:
        #Makes the function continuous or loop.
        num = float(input("\nEnter your selection: "))
        #If they choose five it will give the choice to end the program.
        if num == 5:
            print("\nThanks for using the program! Goodbye!")          

        #Makes the function continuous or loop.
        if num != 5:
            if num == 1:
                print('\n', mercury)
                main()
            elif num == 2:
                print('\n', venus)
                main()
            elif num == 3:
                print('\n', earth)
                main()
            elif num == 4:
                print('\n', mars)
                main()
            else:
                print("\nYou entered a wrong value!!!")
                main()

    #In cases that the user enter an invalid input it will return an error.
    except ValueError:
        print("\nPlease enter a number!!!")
        main()
    except:
        print("\nAn error occured!!!")
        main()

        
main()

