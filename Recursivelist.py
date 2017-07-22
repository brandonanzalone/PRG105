def main():
    listofnumbers = [1,2,3,4,5]
    print('Sum of List is ',str(listsum(listofnumbers)))
#recursive sum list of numbers
def listsum(numList):
   if len(numList) == 1:
        return numList[0]
   else:
        return numList[0] + listsum(numList[1:])

main()
