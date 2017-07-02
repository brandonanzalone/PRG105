#main
def main():
    try:
        boysnames = readfile('BoyNames.txt')
        girlsnames = readfile('GirlNames.txt')
        type = input('If you want to enter a boys name type B, if you want to enter a girls name type G, if you would like both type A. ')
        if not type:
            raise ValueError('Please enter B, G, or A. ')
        if (type != 'B') and (type != 'G') and (type != 'A'):
            raise ValueError('Please enter B, G, or A. ')
        if type == 'B' or type == 'A':
            nameofboy = input('Please enter a boys name. ')
            if not nameofboy:
                raise ValueError('Please enter a boys name. ')
            if searchlist(nameofboy, boysnames):
                print(nameofboy, "Is amongst the most popular names list. ")
        if type == 'G' or type == 'A':
            nameofgirl = input('Please enter a girls name. ')
            if not nameofgirl:
                raise ValueError('Please enter a girls name. ')
            if searchlist(nameofgirl, girlsnames):
                print(nameofgirl, "Is amongst the most popular names list. ")
    except IOError as e:
        print(e)
    except ValueError as z:
        print(z)
#reading file names
def readfile(filename):
    names = []
    f = open(filename, "r")
    for line in f:
        names.append(line.strip('\n'))
    return names
#searchlist for name
def searchlist(nameyourlookingfor, listofnames):
    for name in listofnames:
        if name == nameyourlookingfor:
            return True
main()
