from Piece import Piece
import numpy as np

class Player:
    def __init__(self, playerType: int, randomSeed):
        self.pieceTypes = {1: "O", 2: "X"}
        self.positions: list[Piece] = []
        self.playerType: str = self.pieceTypes[playerType]
        self.randomSeed = np.random.default_rng(randomSeed)

    def addPosition(self, xCoor: int, yCoor: int) -> None:
        self.positions.append(Piece(self.playerType, xCoor, yCoor))

    def randomMove(self):
        randomPlayerRngInt = self.randomSeed.integers(low=0, high=5, size=2)
        x = randomPlayerRngInt[0]
        y = randomPlayerRngInt[1]
        return x, y

