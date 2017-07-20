from officefurniture import OfficeFurniture
from desk import Desk 
#main
def main():
    furniture = OfficeFurniture('chair','metal', 12 , 10, 14, 100.00)
    print(furniture)
    print("\n")


    desk = Desk('desk','wood', 60 , 36, 30, 250.00, 'right', 5)
    print(desk)
main()
