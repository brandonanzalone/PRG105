total = 0.0
pennies = 0.01
days = int(input('How many days will you work for pennies? '))
print("Days Worked   |  Amount Earned That Day ")
print("-------------------------------------- ")
for x in range(days):
    print("        ",format(x + 1, '>2'),"  |  $", pennies)
    total += pennies
    pennies *= 2
print("Total earned over", days,"days is $", format(total, '.2f'))
