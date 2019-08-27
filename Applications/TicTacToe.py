import random

# values = []
# for i in range(1,10):
#     values.append(i)

# List Comprehension
values = [i for i in range(1,10)]

def gameBoard():
    print("""
        {}   |   {}   |   {}
     -----------------------
        {}   |   {}   |   {}
     -----------------------
        {}   |   {}   |   {}
    """.format(values[0],values[1],values[2],values[3],values[4],values[5],values[6],
               values[7],values[8]))

def checkWinner(pos_1,pos_2,pos_3,player):
    if values[pos_1] == player and values[pos_2] == player and values[pos_3] == player:
        return True

def checkConditions(player):
    # if values[0] == 'X' and values[1] == 'X' and values[2] == 'X':
    #     pass
    # elif values[0] == 'X' and values[3] == 'X' and values[6] == 'X':
    #     pass
    if checkWinner(0,1,2,player):
        pass
    elif checkWinner(1,3,6,player):
        pass


def main():
    gameBoard()
    posOccupied = []
    ch = input("Enter your choice : ")
    pos = int(input("Enter your position : "))

    # Check if position is occupied or not
    # if position is occupied then enter position again (Use while loop until user pick the right position)
    values[pos-1] = ch
    gameBoard()

    # Now cpu will randomly pick a number b/w 0-9
    # Check if position is occupied or not
    # if position is occupied then enter position again (Use while loop until user pick the right position)
    cpu_pos = random.randint(1,10)
    values[cpu_pos-1] = '0'
    print("CPU Picked",cpu_pos)

    gameBoard()

main()