def main():
   # input = ['1', '2', '3', '4','5','6']
    try:
        months = input('Enter the each month of rainfall seperated by commas. ')
        if not months:
            raise ValueError('Please enter a comma seperated rainfall value.')
        average(months)
    except ValueError as e:
        print(e)

#calculates average, highest and lowest months and total of rainfall also handles errors
def average(months):
    average = 0.0
    total = 0
    highest = 0
    lowest = 0
    lowestrainfall = 100000
    highestrainfall = 0
    month = 0
    try:
        for x in months.split(','):
            month += 1
            rainfall = int(x)
            total += rainfall
            if rainfall < lowestrainfall:
                lowest = month
                lowestrainfall = rainfall
            if rainfall > highestrainfall:
                highest = month
                highestrainfall = rainfall
        print("Total rainfall for",month,"months",total, "inches")
        print("Average rainfall for",month,"months",format(total/month, '.2f'), "inches")
        print("highest month of rainfall = ",highest)
        print("Lowest month of rainfall = ",lowest)
    except ValueError:
        print("Please enter a number for rainfall. not ",x )

main()
