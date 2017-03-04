#Cal Hasie
#9/10/12
#Lab 1- 2.6

#This program will calculate the amount of sales tax.
def tax():
    print("This program will calculate the amount of sale tax.\n")
    spent = float(input("How much did you spend on purchase?: "))
    state = float(spent*.04)
    county = float(spent*.02)
    tot_sale = float(spent + state + county)
    print("\nAmount of purchase:",spent)
    print("Amount of state tax:",state)
    print("Amount of county tax:",county)
    print("\nAmount of total sale:",tot_sale)
    
tax()
