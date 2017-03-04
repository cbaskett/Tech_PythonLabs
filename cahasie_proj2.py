#Cal Hasie
#4/22/12
#Project 2

#Gets the users input on which file to open and sets to add.
def user_sets():
    use_select = input("Would you like to get sets from a file?(Y or N): ")
    if use_select == 'Y' or use_select == 'y':
        try:
            user_write = input("\nPlease enter file name?: ")
            user_add = open(user_write,"r")
            user_add.close()
            return set_show(user_write)
        except:
            print("File not found.\n")
            return user_sets()
    elif use_select == 'N' or use_select == 'n':
        done = False
        while done == False:
            user_read = input("\nPlease enter a set one at a time, each element seperated by a comma.: " + '\n')
            file_read = open('sets.txt',"a")
            file_read.write(user_read+'\n')
            more_set = input("\nWould you like to enter another set?(Y or N): ")
            if more_set == 'Y' or more_set == 'y':
                done = False
            else:
                done = True
        file_read.close()
        return set_show(user_write = 'sets.txt')
    else:
        print("\nSorry you entered a wrong answer.\n")
        return user_sets()

#Lists the sets entered by the user into the file and reutrns their input.
def set_show(user_write):
    file = open(user_write,'r')
    fileread = file.readlines()
    place = 1
    for line in fileread:
        line = line.rstrip('\n')
        print('set'+str(place)+" = {"+line+"}")
        place += 1


    

        
    
    
        
    
user_sets()
