#Cal Hasie
#9-17-12
#Lab 2- 3.7

#This program will calculate the amount of calories taken from fats and carbs
def main():
    fat_grams = int(input("How many grams of fat did you consume today?: "))
    carb_grams = int(input("How many grams of carbs did you consume today?: "))
    #Prints the calories in fat
    print("\nThe amount of calories that result from fat are..",\
          format(fat_grams*9, ".2f"), "calories")
    #Prints the calories in carbs
    print("\nThe amount of calories that result from carbs are..",\
          format(carb_grams*4, ".2f"), "calories")
    #Prints the total calories by adding carbs and fat
    print("\nThe total amount of calories consumed for the day are..",\
          format(fat_grams*9+carb_grams*4, ".2f"), "calories")



main()
