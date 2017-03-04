#CalHasie
#10-8-12
#Lab 6- 6.4


#Enters mathematical terms and calculations
import math

#Global constant for equation
GRAVITY=9.8

#Defines main function
def main():

    #Using for loop have the range run so that all time intervals are included
    for time in range(1,11,1):
        dist = show_distance(time)
        print(dist)

#Displays the calculation output
def show_distance(time):
    distance= format(((GRAVITY *(time)**2)/2),'.2f')
    return distance


main()
