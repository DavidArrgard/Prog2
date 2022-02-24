
from shutil import move


class Game():
    def __init__(self):
        self.board =[
            ["bR","bN","bB","bQ","bK","bB","bN","bR"],
            ["bp","bp","bp","bp","bp","bp","bp","bp"],
            ["--","--","--","--","--","--","--","--"],
            ["--","--","--","--","--","--","--","--"],
            ["--","--","--","--","--","--","--","--"],
            ["--","--","--","--","--","--","--","--"],
            ["wp","wp","wp","wp","wp","wp","wp","wp"],
            ["wR","wN","wB","wQ","wK","wB","wN","wR"]]
        self.moveFunc = {'p': self.getPmoves, 'R': self.getRmoves, 'N': self.getNmoves, 'B': self.getBmoves,
                         'Q': self.getQmoves, 'K': self.getKmoves}
        self.whiteToMove = True
        self.moveList = []
        self.whiteKPos = (7, 4)
        self.blackKPos = (0, 4)


    def makeMove(self, move):
        self.board[move.startRow][move.startCol] = '--'
        self.board[move.endRow][move.endCol] = move.movePiece
        self.moveList.append(move)
        self.whiteToMove = not self.whiteToMove
        if move.movePiece == 'wK':
            self.whiteKPos = (move.endRow, move.endCol)
        if move.movePiece == 'bK':
            self.whiteKPos = (move.endRow, move.endCol)

    def undoMove(self):
        if len(self.moveList) != 0:
            move = self.moveList.pop()
            self.board[move.startRow][move.startCol] = move.movePiece
            self.board[move.endRow][move.endCol] = move.capuredPiece
            self.whiteToMove = not self.whiteToMove
            if move.movePiece == 'wK':
                self.whiteKPos = (move.endRow, move.endCol)
            if move.movePiece == 'bK':
                self.whiteKPos = (move.endRow, move.endCol)

    def vMoves(self):
        moves = self.possibleMoves()
        for i in range(len(moves)-1, -1, -1):
            self.makeMove(moves[i])
            self.whiteToMove = not self.whiteToMove
            if self.inC():
                moves.remove[moves[i]]
            self.whiteToMove = not self.whiteToMove
            self.undoMove()
        return moves

    def inC(self):
        if self.whiteToMove:
            return self.underAttack(self.whiteKPos[0], self.whiteKPos[1])
        else:
            return self.underAttack(self.blackKPos[0], self.blackKPos[1])

    def underAttack(self, r, c):
        self.whiteToMove = not self.whiteToMove
        oppMove = self.vMoves()
        self.whiteToMove = not self.whiteToMove
        for move in oppMove:
            if move.endRow == r and move.endCol == c:
                self.whiteToMove = not self.whiteToMove
                return True
        return False

    def possibleMoves(self):
        m = []
        for r in range(len(self.board)):
            for c in range(len(self.board[r])):
                turn = self.board[r][c][0]
                if (turn == 'w' and self.whiteToMove) or (turn == 'b' and not self.whiteToMove):
                    p = self.board[r][c][1]
                    self.moveFunc[p](r, c, m)
        return m
    
    def getPmoves(self, r, c, m):
        if self.whiteToMove:
            if self.board[r-1][c] == "--":
                m.append(Move((r,c), (r-1,c), self.board))
                if r == 6 and self.board[r-2][c] == "--":
                    m.append(Move((r, c), (r-2, c), self.board))
            if c-1 >= 0:
                if self.board[r-1][c-1][0] == 'b':
                    m.append(Move((r, c), (r-1, c-1), self.board))
            if c+1 <= 7:
                if self.board[r-1][c+1][0] == 'b':
                    m.append(Move((r, c), (r-1, c+1), self.board))
        else:
            if self.board[r + 1][c] == "--":
                m.append(Move((r, c),(r + 1, c), self.board))
                if r == 1 and self.board[r + 2][c] == "--":
                    m.append(Move((r, c), (r + 2, c), self.board))

            if c - 1 >= 0:
                if self.board[r + 1][c - 1][0] == "w":
                    m.append(Move((r, c), (r + 1, c - 1), self.board))
            if c + 1 <= 7:
                if self.board[r + 1][c + 1][0] == "w":
                    m.append(Move((r, c), (r + 1, c + 1), self.board))

    def getRmoves(self, r, c, m):
        dirrect = ((-1,0), (0, -1), (1, 0), (0, 1))
        eColor = "b" if self.whiteToMove else "w"
        for d in dirrect:
            for i in range(1,8):
                endRow = r + d[0] * i
                endCol = c + d[1] * i
                if 0 <= endRow < 8  and 0 <= endCol < 8:
                    endP = self.board[endRow][endCol]
                    if endP == "--":
                        m.append(Move((r, c), (endRow, endCol), self.board))
                    elif endP[0] == eColor:
                        m.append(Move((r, c), (endRow, endCol), self.board))
                        break
                    else:
                        break
                else:
                    break

    def getNmoves(self, r, c, m):
        kM = ((-2, -1), (-2, 1), (-1, -2), (-1, 2), (1, -2), (1, 2), (2, -1), (2, 1))
        aColor = "w" if self.whiteToMove else "b"
        for i in kM:
            endRow = r + i[0]
            endCol = c + i[1]
            if 0 <= endRow < 8 and 0 <= endCol < 8:
                endP = self.board[endRow][endCol]
                if endP[0] != aColor:
                    m.append(Move((r, c), (endRow, endCol), self.board))

    def getBmoves(self, r, c, m):
        dirrect = ((-1, -1), (-1, 1), (1, -1), (1, 1))
        eColor = "b" if self.whiteToMove else "b"
        for d in dirrect:
            for i in range(1, 8):
                endRow = r + d[0] * i
                endCol = c + d[1] * i
                if 0 <= endRow < 8 and 0 <= endCol < 8:
                    endP = self.board[endRow][endCol]
                    if endP == "--":
                        m.append(Move((r, c), (endRow, endCol), self.board))
                    elif endP[0] == eColor:
                        m.append(Move((r, c), (endRow, endCol), self.board))
                        break
                    else:
                        break
                else:
                    break

    def getQmoves(self, r, c, m):
        self.getRmoves(r, c, m)
        self.getBmoves(r, c, m)

    def getKmoves(self, r, c, m):
        kM = ((-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1))
        aColor = "w" if self.whiteToMove else "b"
        for i in range(8):
            endRow = r + kM[i][0]
            endCol = c + kM[i][1]
            if 0 <= endRow < 8 and 0 <= endRow < 8:
                endP = self.board[endRow][endCol]
                if endP[0] != aColor:
                    m.append(Move((r, c), (endRow, endCol), self.board))
    
class Move():

    rowRanks = {1: '7', 2 :'6', 3: '5', 4: '4', 5: '3', 6: '2', 7: '1', 0: '8'}

    rankRows = {v: k for k, v in rowRanks.items()}
    filesCols = {'a': 0,'b': 1,'c': 2,'d': 3,'e': 4,'f': 5,'g': 6,'h': 7}

    colsFiles = {v: k for k, v in filesCols.items()}

    def __init__(self, startSq, endSq, board):
        self.startRow = startSq[0]
        self.startCol = startSq[1]
        self.endRow = endSq[0]
        self.endCol = endSq[1]
        self.movePiece = board[self.startRow][self.startCol]
        self.capuredPiece = board[self.endRow][self.endCol]
        self.moveID = self.startRow * 1000 + self.startCol * 100 + self.endRow * 10 + self.endCol

    def __eq__(self, other):
        if isinstance(other, Move):
            return self.moveID == other.moveID
        return False

    def getNotation(self):
        return self.getFile(self.startRow, self.startCol) + self.getFile(self.endRow, self.endCol)

    def getFile(self, r, c):
        return self.colsFiles[c] + self.rowRanks[int(r)]
        