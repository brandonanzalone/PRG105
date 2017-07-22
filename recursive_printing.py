#main
def main():
    global getnum 
    getnum = int(input('Please enter a number greater than 0. '))

    addnumber(1)
#recursive function to print number
def printnum(startnum):
    if startnum > getnum : 
        return
    print(startnum)
    printnum(startnum + 1)

main()
