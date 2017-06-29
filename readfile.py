
def main():
    counter = 0
    f = open("c:\\names.txt", "r")
    for line in f:
        counter += 1
        print(line)
    print("Total number of names is ", counter)
main()
