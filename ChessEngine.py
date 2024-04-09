"""
Este archivo es el responsable de manejar toda la información con respecto a una partida de ajedrez.
También evaluará los movimientos
"""

class Gamestate():
    def __init__(self):
        #Este es el tablero, hace una lista 2d de las piezas representandolos con caracteres
        # 'b' son las piezas negras y 'w' las blancas
        # -- es un espacio vacío
        self.board = [
            ["bR","bN","bB","bQ","bK","bB","bN","bR"],
            ["bp","bp","bp","bp","bp","bp","bp","bp"],
            ["--","--","--","--","--","--","--","--"],
            ["--","--","--","--","--","--","--","--"],
            ["--","--","--","--","--","--","--","--"],
            ["--","--","--","--","--","--","--","--"],
            ["wp","wp","wp","wp","wp","wp","wp","wp"],
            ["wR","wN","wB","wQ","wK","wB","wN","wR"]]
        self.whiteTomove = True
        self.movelog = []

    def makeMove(self,move):
        self.board[move.startRow][move.startCol] = "--"
        self.board[move.endRow][move.endCol] = move.pieceMoved
        self.movelog.append(move)
        self.whiteTomove = not self.whiteTomove

    def undoMove(self):
        if len(self.movelog) != 0:
            move = self.movelog.pop()
            self.board[move.startRow][move.startCol] = move.pieceMoved
            self.board[move.endRow][move.endCol] = move.piecescaptured
            self.whiteTomove = not self.whiteTomove

    """
    Movimientos considerando el jaque
    """
    def getValidMoves(self):
        return self.getAllPossibleMoves()

    """
    Movimientos sin considerar el jaque
    """
    def getAllPossibleMoves(self):
        moves = []
        for r in range(len(self.board)): # lineas
            for c in range(len(self.board[r])): #Columnas
                turn = self.board[r][c][0]
                if (turn == 'w' and self.whiteTomove) and (turn == 'b' and not self.whiteTomove):
                    piece = self.board[r][c][1]
                    if piece == 'p':
                        self.getPawnMoves(r,c,moves)
                    elif piece == 'R':
                        self.getRookMoves(r,c,moves)
        return moves

    """
    Se obtienen los movimientos del peon para el peon localizado en col y row y agrega esos movimientos a la lista
    """
    def getPawnMoves(self,r,c,moves):
        pass

    """
    Se obtienen los movimientos de la torre para la torre localizada en col y row y agrega esos movimientos a la lista
    """
    def getRookMoves(self,r,c,moves):
        pass

class Move():
        # maps keys to values
        # key : value
        ranksToRows = {"1":7,"2":6,"3":5,"4":4,
                       "5":3,"6":2,"7":1,"8":0}
        rowstoRanks = {v:k for k, v in ranksToRows.items()}
        filesToCols = {"a":0,"b":1,"c":2,"d":3,
                       "e":4,"f":5,"g":6,"h":7}
        colsToFiles = {v: k for k,v in filesToCols.items()}


        def __init__(self, startSq, endSq, board):
            self.startRow = startSq[0]
            self.startCol = startSq[1]
            self.endRow = endSq[0]
            self.endCol = endSq[1]
            self.pieceMoved = board[self.startRow][self.startCol]
            self.piecescaptured = board[self.endRow][self.endCol]

        def getChessNotation(self):
            return self.getRankFile(self.startRow,self.startCol) + self.getRankFile(self.endRow,self.endCol)

        def getRankFile(self,r,c):
            return self.colsToFiles[c] + self.rowstoRanks[r]
