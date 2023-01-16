from Piece import Piece

class Player:
    def __init__(self, playerType: int):
        self.pieceTypes = {1: "O", 2: "X"}
        self.positions: list[Piece] = []
        self.playerType: str = self.pieceTypes[playerType]

    def addPosition(self, xCoor: int, yCoor: int) -> None:
        self.positions.append(Piece(self.playerType, xCoor, yCoor))

