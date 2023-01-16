import numpy as np
from Player import Player

class GameEngine:
    def __init__(self):
        self.player1 = Player(1)
        self.player2 = Player(2)
        self.__GameBoard = np.empty((5, 5), dtype=str)

    def playGame(self):
        running = True

        while running:

            correctAnswer: bool = False
            while(not correctAnswer):
                x1: int = np.NAN
                y1: int = np.NAN
                try:
                    x1, y1 = [int(x) for x in input("Type in coordinate for player: 1 ").split(', ')]
                except:
                    print("Invalid input, try again")

                if x1 >= self.__GameBoard.shape[0] or y1 >= self.__GameBoard.shape[1]:
                    print("Input numbers smaller than 5")
                elif self.__GameBoard[x1, y1]:
                    print("Space already taken")
                else:
                    correctAnswer = True

            correctAnswer = False
            self.player1.addPosition(x1, y1)
            self.__GameBoard[x1, y1] = self.player1.playerType

            while(not correctAnswer):
                x2: int = np.NAN
                y2: int = np.NAN
                try:
                    x2, y2 = [int(x) for x in input("Type in coordinate for player: 2 ").split(', ')]
                except:
                    print("Invalid input, try again")

                if x2 >= self.__GameBoard.shape[0] or y2 >= self.__GameBoard.shape[1]:
                    print("Input numbers smaller than 5")
                elif self.__GameBoard[x2, y2]:
                    print("Space already taken")
                else:
                    correctAnswer = True

            self.player2.addPosition(x2, y2)
            self.__GameBoard[x2, y2] = self.player2.playerType

            print(self.__GameBoard)
            running = self.__CheckWin()

    def __CheckWin(self) -> bool:
        player1Win = np.empty((1, 5), dtype=str)
        player1Win[:] = self.player1.playerType

        player2Win = np.empty((1, 5), dtype=str)
        player2Win[:] = self.player2.playerType

        for i in range(self.__GameBoard.shape[0]):
            if np.array_equal(player1Win, self.__GameBoard[:i]):
                print("Player 1 Wins")
                return False
            elif np.array_equal(player2Win, self.__GameBoard[:i]):
                print("Player 2 Wins")
                return False

        for i in range(self.__GameBoard.shape[1]):
            if np.array_equal(player1Win, self.__GameBoard[i:]):
                print("Player 1 Wins")
                return False
            elif np.array_equal(player2Win, self.__GameBoard[i:]):
                print("Player 2 Wins")
                return False

        diag1 = np.reshape(self.__GameBoard.diagonal(), (1, 5))
        diag2 = np.reshape(np.fliplr(self.__GameBoard).diagonal(), (1, 5))

        if np.array_equal(diag1, player1Win):
            print("Player 1 Wins")
            return False
        elif np.array_equal(diag1, player2Win):
            print("Player 2 Wins")
            return False
        if np.array_equal(diag2, player1Win):
            print("Player 1 Wins")
            return False
        elif np.array_equal(diag2, player2Win):
            print("Player 2 Wins")
            return False

        return True





