import movement

acceptedLetters = ['R','N','B','K','Q','a','b','c','d','e','f','g','h','x','1','2','3','4','5','6','7','8']

movingPieces = ['R','N','B','K','Q']

columns = ['a','b','c','d','e','f','g','h']

rows = ['1','2','3','4','5','6','7','8']

# Td4
# Tdd4
# Txd4
# Tdxd4

# e4
# dxe4

collumnNumbers = {
  "a": 0,
  "b": 1,
  "c": 2,
  "d": 3,
  "e": 4,
  "f": 5,
  "g": 6,
  "h": 7
}
#value = row-1 + collumnNumbers[letter]+

def firstCheck(move):
    exception = 'none'
    if (len(move) > 5) | (len(move) < 2):
        exception = 'Lance inválido'
        
    for letter in move:
        if letter not in acceptedLetters:
            exception = 'Lance inválido'
                   
    return exception

def makeMove(piece, whereto, position, moveNumber, board):
    if moveNumber % 2 == 1: piece = piece.lower()
    piecesMoving = []
    pos = ''
    
    for i in range(0, 64, 1):
        if board[i] == piece:
            moves = movement.movePiece(i, board)
            if moves is not None:
                piecesMoving[i] = moves
                
    for i, piecesMoving in enumerate(piecesMoving):
        if whereto in piecesMoving:
            if pos != '' and position == 'none':
                return 'ilegal move'
            else: 
                pos = i
    
    if position != 'none':
        if pos != position: return 'ilegal move'
    
    finalBoard = board
    finalBoard[pos] = '0'
    finalBoard[whereto] = piece
    
    return finalBoard
        
                
#end checkforChecks

def interpreter(move, moveNumber, board):
    color = 'Black' if moveNumber % 2 == 0 else 'White'
    
    ambigous = False
    attacking = False
    position = 'none'

    exception = firstCheck(move)
    if exception != 'none': return exception

    if move[0] in movingPieces:
        if move[1] in columns and move[2] in rows:
            piece = move[0]
            whereto = (int(move[2])-1) * 8 + collumnNumbers[move[1]]
        
        elif move[1] in columns and move[2] in columns and move[3] in rows:
            piece = move[0]
            position = move[1]
            whereto = (int(move[2])-1) * 8 + collumnNumbers[move[1]]
        
        elif move [1] == 'x' and move[2] in columns and move[3] in rows:
            piece = move[0]
            whereto = (int(move[3])-1) * 8 + collumnNumbers[move[2]]
        
        elif move[1] in columns and move[2] == 'x' and move[3] in columns and move[4] in rows:
            piece = move[0]
            position = move[1]
            whereto = (int(move[4])-1) * 8 + collumnNumbers[move[3]]
        
        else: 
            exception = 'invalid move'
    
    elif move[0] in columns:
        if move[1] in rows:
            piece = 'P'
            whereto = (int(move[1])-1) * 8 + collumnNumbers[move[0]]
        
        elif move[1] == 'x' and move[2] in columns and move[3] in rows:
            piece = 'P'
            position = move[0]
            whereto = (int(move[3])-1) * 8 + collumnNumbers[move[2]]
        
        else: 
            exception = 'invalid move'
            
    else: 
        exception = 'invalid move'
    
    if exception == 'none':
        finalBoard = makeMove(piece, whereto, position, moveNumber, board)
        return finalBoard
    else: print(exception)
        