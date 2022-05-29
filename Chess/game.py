from email.mime import image
import pygame as p
from engine import Game, Move


width = height = 512
dimensions = 8
SQ_size = height/8
MAX_FPS = 15
images = {}


def loadImages():   
    pieces = ['wp','wR','wN','wQ','wK','wB','bp','bR','bN','bQ','bK','bB']
    for piece in pieces:
        images[piece] = p.transform.scale(p.image.load("Bilder/" + piece + ".png"), (SQ_size, SQ_size))


def main():
    p.init()
    screen = p.display.set_mode((width,height))
    clock = p.time.Clock()
    screen.fill(p.Color("white"))
    gs = Game()
    vMoves = gs.vMoves()
    moveMade = False
    loadImages()
    sqSelected = ()
    playerClick = []
    running = True
    while running:
        for e in p.event.get():
            if e.type == p.QUIT:
                running = False
            elif e.type == p.MOUSEBUTTONDOWN:
                pos = p.mouse.get_pos()
                col = pos[0]//SQ_size
                row = pos[1]//SQ_size
                if sqSelected == (row, col):
                    sqSelected = []
                    playerClick = []
                else:
                    sqSelected = (int(row), int(col))
                    playerClick.append(sqSelected)
                if len(playerClick) == 2:
                    move = Move(playerClick[0],playerClick[1], gs.board)
                    print(move.getNotation())
                    if move in vMoves:
                        gs.makeMove(move)
                        moveMade = True
                        sqSelected =  {}
                        playerClick = []
                    else:
                        playerClick[sqSelected]

            elif e.type == p.KEYDOWN:
                if e.key == p.K_z:
                    gs.undoMove()
                    moveMade = True

        if moveMade:
            vMoves = gs.possibleMoves()
            moveMade = False    

        GameState(screen, gs)
        clock.tick(MAX_FPS)
        p.display.flip()


def GameState(screen, gs):
    drawBoard(screen)

    drawPieces(screen, gs.board)

def drawBoard(screen):
    colors = [p.Color('white'), p.Color('grey')]
    for x in range(dimensions):
        for y in range(dimensions):
            color = colors[((y+x) % 2)]
            p.draw.rect(screen, color, p.Rect(y*SQ_size,x*SQ_size,SQ_size,SQ_size))


def drawPieces(screen, board):
    for r in range(dimensions):
        for c in range(dimensions):
            piece = board[r][c]
            if piece != "--":
                screen.blit(images[piece], p.Rect(c*SQ_size,r*SQ_size, SQ_size, SQ_size))

if __name__ == "__main__":
    main()
