#Cal Hasie
#9-24-12
#Lab 3- 4.7

#This function will tell the user how any points have been earned from books.
def main():
    points = float(input("How many books have you purchased this month?: "))
    #The if statement computes the number of books bought to points.
    if points == 0:
        print("You have earned 0 points this month.")
    elif points == 1:
        print("You have earned 5 points this month.")
    elif points == 2:
        print("You have earned 15 points this month.")
    elif points == 3:
        print("You have earned 30 points this month.")
    elif points >= 4:
        print("You have earned 60 points this month.")
    else:
        print("You entered an invalid number.")


main()
