board = [[1, 2, 3],
         [4, 5, 6],
         [7, 8, 9]]
rows = len(board[0])
columns = len(board)
av = [1, 2, 3, 4, 5, 6, 7, 8, 9]

def main():
    print("Welcome to tictactoe")#
    show()


def show():
    for i in range(rows):
        print("\n+---+---+---+")
        print("|", end="")
        for x in range(columns):
            print("", board[i][x], end=" |")
    print("\n+---+---+---+")
    play()

def play():
    userinput = input("Enter your move: ")
     

if __name__ == '__main__':
    main()