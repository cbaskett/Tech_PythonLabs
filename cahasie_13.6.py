#Cal Hasie
#11/12/12
#Lab 13- 13.6




#Takes the number up to 100 that he/she wants the sum of
def main():

    #Takes in the number
    number=int(input('Enter a positive number: '))
    #Sums the numbers from 0-the users number.
    sum=total(number)
    print('\nThe sum of all numbers from 1 until', number, 'is', sum)

#Returns the sum of all numbers added up to the user number
def total(num):
    if num==0:
        return 0
    else:
        return num +total(num-1)


main()
