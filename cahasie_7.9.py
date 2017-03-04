#Cal Hasie
#10-15-12
#Lab7- 7.9


import math

#Defines a program that takes the average of numbers from a text.
def main():

    #Helps varify statements and give solutions for error results.
    try:

        #Defines global variables
        total = 0.0
        count = 0.0
        print("This program will compute the average of numbers in a file.\n\n")
        
        #Open file created in numbers.txt with a reading option
        content = open('numbers.txt', 'r')

        #Using for loop, add total of each line and divide by count
        for line in content:
            count = count + 1
            total += int(line)

        #Computes the average
        average = total / count
        print("The total sum of the number(s) in the file is", total,"\n")
        print("The amount of number(s) in the text is/are", count,"\n")
        print("The average of the number(s) is", format(average, '.2f'))

        #Closes the file
        content.close()
        

    #Except in case of a wrong 'r','w' file
    except IOError:
        print('An error occurred trying to read the file!!!')

    #Except in case of the numbers.txt file having numbers as strings
    except ValueError:
        print('Error: Numbers must be in numeric values!!!')
    except:
        print('Error!!!')


main()
