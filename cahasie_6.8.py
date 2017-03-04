#Cal Hasie
#10-8-12
#Lab 6- 6.8


#Enters mathematical terms and calculations. 
import math

#Function taking user input to see their number.
def main():
    number = int(input('Enter a number '))

    #Calls thes second function
    determ = is_prime(number)
    
    #Tells if it is prime or not
    if is_prime(number):
        print('The number is prime')
    else:
        print('The number is not prime')

#Function determining if the number is prime.
def is_prime(number):

     #Loops the function with users number.   
     for count in range(2, number):
         if number % count == 0:
             return False
     return True


main()
