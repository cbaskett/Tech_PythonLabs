#Cal Hasie
#9-17-12
#Lab 2- 3.4


#This program will take in the users monthly payments for their car.
def main():
    loan = int(input("How much is your loan payment monthly?: "))
    insurance = int(input("How much is your insurance monthly?: "))
    gas = int(input("How much do you spend on gas monthly?: "))
    oil = int(input("How much do you spend on oil monthly?: "))
    tires = int(input("How much do your tires cost monthly?: "))
    maint = int(input("How much do you spend on maintanance monthly?: "))
    #Total_month adds each monthly cost together
    total_month = (loan + insurance + gas + oil + tires + maint)
    print("\nYour total monthly automobile cost is",\
        format(total_month,".2f"), sep=' $')
    print("\nYour total annual automobile costs are",\
        format(total_month * 12,".2f"), sep=' $')
    

main()
