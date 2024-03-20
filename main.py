import pygame
import pygame_textinput
from interpretMove import interpreter

# % 2 == 0: Black
# % 2 == 1: White

moves = 1

def startingPosition():
    # White
    # Rook = 1 || Knight = 2 || Bishop = 3
    # Queen = 4 || King = 5 || Pawn = 6

    # Black

    # Rook = 7 || Knight = 8 || Bishop = 9
    #/ Queen = A || King = B || Pawn = C

    #Blank = 0
    #Starting board
    row8 = "rnbqkbnr"
    row7 = "pppppppp"
    row6 = "00000000"
    row5 = "00000000"
    row4 = "00000000"
    row3 = "00000000"
    row2 = "PPPPPPPP"
    row1 = "RNBQKBNR"
    
    startingBoard = row1 + row2 + row3 + row4 + row5 + row6 + row7 + row8
    #end starting board

    return startingBoard

#end startPosition

def screenDefinition():
    screen_width = 1000
    screen_height = 800
    screen = pygame.display.set_mode((screen_width, screen_height))

    return screen

#end screenDefinition  

def defineColor(piece):
    if piece in ['B','N','Q','K','P','R']:
        return 'w'+ piece
    else: 
        return 'b'+ piece.upper()

#end defineColor

def defineInput():
    pygame.display.set_caption("PyChess")
    font = pygame.font.SysFont("Consolas", 20)
    textinput = pygame_textinput.TextInputVisualizer(font_object=font)
    return textinput

#end defineInput

def updateBoard(screen, board):
    i = 25
    j = 725
    k = 0 
    for piece in board:
        if piece != '0':
           imageSrc = 'img/'+ defineColor(piece) + ".svg"
           image = pygame.image.load(imageSrc)
           screen.blit(image, (i, j))
           
        i+= 100
        k+=1
        
        if k == 8:
            j -= 100
            i = 25
            k = 0

#end updateBoard

def plotBoard(screen):
    black = (100, 100, 100)
    white = (200, 200, 200)
    
    for i in range(8):
        for j in range(8):
            color = white if (i + j) % 2 == 0 else black
            pygame.draw.rect(screen, color, (j*100, i*100, 100, 100))
    
    pygame.draw.rect(screen, (255, 255, 255), (800, 0, 800, 1000))
    
    font = pygame.freetype.SysFont("Consolas", 20, True)
    font.render_to(screen, (854, 50), 'Welcome', (20, 20, 20))
    font.render_to(screen, (846, 70), 'To Pychess', (20, 20, 20))
    font = pygame.freetype.SysFont("Consolas", 15, True)
    font.render_to(screen, (845, 120), 'Input your move', (20, 20, 20,))
    
    #textinput = 
    
#end plotBoard

def handleInput(screen, textinput, events):
    textinput.update(events)
    screen.blit(textinput.surface, (845, 200))

#end handleInput

def handleMove(textinput, board):
    newBoard = interpreter(textinput.value, moves, board)
    
    textinput.value = ''
    
    if newBoard != 'ilegal move' and newBoard != 'invalid move':
        return board

def run():
    pygame.init()
    
    textinput = defineInput()

    screen = screenDefinition()
    board = startingPosition()

    clock = pygame.time.Clock()

    running = True
    while running:
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
                board = handleMove(textinput, board)
            
        #Game logic
        plotBoard(screen)
        
        updateBoard(screen, board)
        handleInput(screen, textinput, events)
        
        #end
        pygame.display.flip()
        clock.tick(30)

run()
pygame.quit()