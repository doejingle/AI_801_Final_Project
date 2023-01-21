import numpy as np
from Player import Player
from GameIntro import game_intro

class GameEngine:
    def __init__(self):
        self.player1 = Player(1, 12345)
        self.player2 = Player(2, 56789)
        self.__GameBoard = np.empty((5, 5), dtype=str)

    def playGame(self):
        running = True

        print(game_intro)
    
        game_mode = int(input("********************Enter Game Mode********************\n"+
        "Enter '0': Both Players Manual Input...\n" +
        "Enter '1': Player 1 Manual, Player 2 Random Input...\n" + 
        "Enter '2': Both Players Random Input...\n"))

        while running:
            
            correctAnswer: bool = False
            while(not correctAnswer):
                x1: int = np.NAN
                y1: int = np.NAN
                
                # Player 1 Manual Input
                if game_mode==0 or game_mode==1:
                    try:
                        x1, y1 = [int(x) for x in input("Type in coordinate for player 1 'O': ").split(', ')]
                    except:
                        print("Invalid input, try again")

                # Player 1 Random Input
                else:
                    x1, y1 = self.player1.randomMove()

                if x1 >= self.__GameBoard.shape[0] or y1 >= self.__GameBoard.shape[1]:
                    print("Input numbers smaller than 5")
                elif self.__GameBoard[x1, y1]:
                    pass
                    # print(f"{x1}, {y1} Space already taken (player 1)")
                else:
                    correctAnswer = True

            correctAnswer = False
            self.player1.addPosition(x1, y1)
            self.__GameBoard[x1, y1] = self.player1.playerType
            print('\n-----------------------------------\n')

            while(not correctAnswer):
                x2: int = np.NAN
                y2: int = np.NAN
                
                # Player 2 Manual Input
                if game_mode==0:
                    try:
                        x2, y2 = [int(x) for x in input("Type in coordinate for player 2 'X': ").split(', ')]
                    except:
                        print("Invalid input, try again")
                # Player 2 Random Input
                else:
                    x2, y2 = self.player2.randomMove()

                if x2 >= self.__GameBoard.shape[0] or y2 >= self.__GameBoard.shape[1]:
                    print("Input numbers smaller than 5")
                elif self.__GameBoard[x2, y2]:
                    pass
                    # print(f"{x2}, {y2} Space already taken (player 2)")
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





