from productionworker import productionworker
#main
def main():
    try:
        worker = UserInput()
        print('Employee name:',worker.get_name())
        print('Employee number:',worker.get_number())
        if worker.get_shiftnumber() == 1:
            print('Shift: Day')
        else:
            print('Shift: Night')
        print('Employee hourly rate: $',format(worker.get_hourly(), '.2f'))
    except ValueError as e:
        print(e)
#userinput
def UserInput():
    employeename = input('Enter Employee Name: ')
    if not employeename:
        raise ValueError('Please Enter Employee Name: ')
    employeenumber = input('Please Enter Employee Number: ')
    if not employeenumber:
        raise ValueError('Please Enter Employee Number: ')
    employeshift = int(input('Please Enter Employees Shift: 1 For Day Shift, and 2 For Night Shift: '))
    if not employeshift and (employeshift != 1 and employeshift != 2):
        raise ValueError('Please Enter Employee Shift 1 For Day Shift and 2 For Night Shift: ')
    hourlyrate = float(input('Please Enter an hourly rate: '))
    if not hourlyrate :
        raise ValueError('Please Enter an hourly rate: ')
    prodworker = productionworker(employeename,employeenumber,employeshift, hourlyrate)
#    e = employee(employeename,employeenumber)
    return prodworker

main()
