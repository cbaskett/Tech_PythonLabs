#Cal Hasie
#10-29-12
#Lab 8- 8.5



#This function determines if a users account number is valid or not
def main():

    #Trys a first process and if not correct uses the except validation
    try:
        #Infile goes into the file and reads the data
        infile = open('charge_accounts.txt' ,'r')
        numbers = infile.readlines()
        infile.close()
    
        #Intakes the users input value 
        account = input('Enter an account number that is seven digits long: ')
        index = 0

        #Loops the index of numbers and strips it to a correct order
        while index < len(numbers):
            numbers[index] = numbers[index].rstrip('\n')
            index += 1
        
        #Decides if the number is in the account or not
        if account in numbers:
            print('This number is valid')
        else:
            print('This number is not valid')

    #If an incorrect value is entered except returns an error reasoning
    except IOError:
        print('An error occurred when reading file')
    except ValueError:
        print('Please enter a number')
    except:
        print('An error occurred')
    
main()
