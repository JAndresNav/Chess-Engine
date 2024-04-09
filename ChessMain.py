"""
Archivo principal, aquí el usuario interactúa con el programa y obtiene el siguiente movimiento
"""

import pygame as p
from Chess import ChessEngine

WIDTH = HEIGTH = 512
DIMENSION = 8 #8x8 la dimension del tablero
SQ_SIZE = HEIGTH // DIMENSION
MAX_FPS = 15
IMAGES = {}

"""
Creamos un dicccionario global de imagenes para no hacer tan pesado y lento el codigo
"""
def loadImages():
    pieces = ['wp',"wR","wN","wB","wQ","wK",'bp',"bR","bN","bB","bQ","bK"]
    for piece in  pieces:
        IMAGES[piece] = p.transform.scale(p.image.load("images/"+ piece +".png"), (SQ_SIZE, SQ_SIZE))
    # Ahora podemos llamar una imagen usando el diccionario, ej = 'IMAGES['wp']'

"""
Aqui empieza lo principal del codigo, el input del usuario
"""
def main():
    p.init()
    screen = p.display.set_mode((WIDTH,HEIGTH))
    clock = p.time.Clock()
    screen.fill("white")
    gs = ChessEngine.Gamestate()
    validMoves = gs.getValidMoves()
    moveMade = False

    loadImages() # solo se usa una vez para cargar las imágenes
    running = True
    sqSelected = ()
    playerClicks = [] #Saber de donde a donde movió el jugador el mouse

    while running:
        for e in p.event.get():
            if e.type == p.QUIT:
                running = False
            #uso del mouse
            elif e.type == p.MOUSEBUTTONDOWN:
                location = p.mouse.get_pos() # Posición del ratón
                col = location[0]//SQ_SIZE
                row = location[1]//SQ_SIZE
                if sqSelected == (row,col): # Si el usuario selecciona la misma casilla
                    sqSelected = ()
                    playerClicks = []
                else:
                    sqSelected = (row,col)
                    playerClicks.append(sqSelected) #agrega ambob movimientos
                if len(playerClicks) == 2: # si es el segundo click
                    move = ChessEngine.Move(playerClicks[0],playerClicks[1],gs.board)
                    print(move.getChessNotation())

                    gs.makeMove(move)
                    sqSelected = ()
                    playerClicks = []
            elif e.type == p.KEYDOWN:
                if e.key == p.K_z:
                    gs.undoMove()


            drawGameState(screen,gs)
            clock.tick(MAX_FPS)
            p.display.flip()

"""
parte gráfica del codigo
"""

def drawGameState(screen,gs):
    drawBoard(screen)
    #Aquí se puede agregar cosas extra, como movimientos sugeridos etc
    drawPieces(screen,gs.board)

def drawBoard(screen): #Agrega los cuadrados en el tablero, la parte superior izquierda siempre es blanca
    colors = [p.Color("white"),p.Color("gray")]
    for r in range(DIMENSION):
        for c in range (DIMENSION):
            color = colors[((r+c)% 2)]
            p.draw.rect(screen, color, (c * SQ_SIZE, r * SQ_SIZE, SQ_SIZE, SQ_SIZE))



def drawPieces(screen,board): # Agrega las piezas con repsecto al estado actual del tablero
    for r in range(DIMENSION):
        for c in range(DIMENSION):
            piece = board[r][c]
            if piece != "--":
                screen.blit(IMAGES[piece], p.Rect(c*SQ_SIZE,r*SQ_SIZE, SQ_SIZE, SQ_SIZE))

if __name__ == '__main__':
    main()
