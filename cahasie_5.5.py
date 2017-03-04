#Cal Hasie
#10-1-12
#Lab 5- 5.5



# This program averages rainfall per month.
def rain_fall():
    tot_years = int(input('Enter the amount of years: '))

# Get the amount of rainfall for each month of each year.
    for years in range(tot_years):
        total = 0.0
        print('Year', years + 1)

        #Allows the user to enter the average rainfall for each month
        #in that year.
        for month in ('January- ', 'February- ', 'March- ', 'April- ',\
            'May- ', 'June- ', 'July- ', 'August- ', 'September- ',\
            'October- ', 'November- ', 'December- '):
            #
            inches = float(input(month))
            total += inches

    #Helps calculate the variables together to get the output
    tot_month = tot_years * 12
    tot_inches = total
    average_inches = total / tot_month
    print('The number of months is:', tot_month)
    print('The total inches of rainfall over-all is:', tot_inches)
    print('The average rainfall per month for the your input',\
    'is:', average_inches)

rain_fall()
