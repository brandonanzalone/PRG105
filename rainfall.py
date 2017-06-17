total = 0.0
years = int(input('How many years of data do you have? '))
for x in range(years):
    for y in range(12):
        question = "Number of inches in month "+format(y + 1, '>2')+" of year "+format(x + 1, '>2')+": "
        total += int(input(question))
print("Over",years * 12, "months there was", format(total, '.2f'), "inches of rain.")
print("The average monthly rainfall was ",format(total /(years * 12), '.2f'), "inch(es) per month.")
