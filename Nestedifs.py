package = input('Please enter which package you have, A, B, or C.')
minutes = int(input('Please enter number of minutes used.'))
total = 0.0
billableminutes = 0

if package == "A":
    if minutes <= 450:
       total = 39.99
    else:
        billableminutes = minutes - 450
        total = 39.99 + (billableminutes * .45)
    print("Your bill is $", format(total, '.2f'))
else:
    if package == "B":
        if minutes <= 900:
            total = 59.99
        else:
             billableminutes = minutes - 900
             total = 59.99 + (billableminutes * .40)
        print("Your bill is $", format(total, '.2f'))
    else:
        if package == "C":
            total = 69.99
            print("Your bill is $", format(total, '.2f'))
        else:
            print("Invalid package please choose A, B, or C.")
