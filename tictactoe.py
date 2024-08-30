class TicTacToe:
    def __init__(self):
        self._board = [" "]*9
        self._move = 0
        self._winner = None

    def show(self):
        visual = ""
        minnum = 0
        maxnum = 3
        for loop in range(3):
            if loop == 1:
                minnum = 3
                maxnum = 6
            elif loop == 2:
                minnum = 6
                maxnum = 9
            visual += "\n+---+---+---+\n"
            for i in range(minnum, maxnum):
                visual += f"| {self._board[i]} "
            visual += "|"
        visual += "\n+---+---+---+"
        return visual

    def move(self):
        self._move += 1
        while True:
            if self._move % 2 == 0:
                thing = "O"
            else:
                thing = "X"
            userinput = input("Enter your move: ")
            try:
                if int(userinput) in range(0, 10) and self._board[int(userinput)-1] != "X" and self._board[int(userinput)-1] != "O":
                    print(self._board[int(userinput)-1])
                    self._board[int(userinput)-1] = thing
                    break
                else:
                    print("Invalid input")
            except ValueError:
                print("Invalid, try again")

    def winner(self):
        lines = [
            self._board[0:3], self._board[3:6], self._board[6:9],
            self._board[0:7:3], self._board[1:8:3], self._board[2:9:3],
            self._board[0:9:4], self._board[2:7:2]
        ]
        #print(lines)
        for line in lines:
            if line[0] == line[1] == line[2] != " ":
                self._winner = line[0]
                return
        if " " not in self._board:
            self._winner = "Draw"


def main():
    game = TicTacToe()
    print(game.show())
    while True:
        game.move()
        print(game.show())
        game.winner()
        if game._winner:
            if game._winner == "Draw":
                print("It's a Draw!")
                break
            else:
                print(f"{game._winner} won!")
                break


if __name__ == '__main__':
    main()
