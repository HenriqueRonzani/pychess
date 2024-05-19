import movement

movingPieces = ['R','N','B','K','Q']

columns = ['a','b','c','d','e','f','g','h']

rows = ['1','2','3','4','5','6','7','8']

acceptedLetters = movingPieces + columns + rows + ['x', '-', 'O']

# T d 4

# T d d 4 -

# T 1 d 4 -

# T 1 x d 4 - 

# T d x d 4 -

# T d 1 x d 4

# T d 1 d 4 - 

# T x d 4 -

# 0 1 2 3 4 5

# e 4
# d x e 4

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
# value = (row-1) * 8 + collumnNumbers[letter]

def firstCheck(move):
    validMove = True
   
    if len(move) > 5 or len(move) < 2:
        validMove = False
    
    if len(move) == 2 and (move[0] not in columns or move[1] not in rows):
        validMove = False
        
    for letter in move:
        if letter not in acceptedLetters:
            validMove = False
                             
    return validMove

def makeMove(moveData, board):
    piece = moveData[0]
    position = moveData[1]
    whereTo = moveData[2]
    
    piecesMoving = []
    pos = ''
    
    if isinstance(position, int):
        if board[position] != piece:
            return 'Invalid move 2'
        
    elif position != '':
        
        if position in rows:
            piecesMoving = []
                
            for i in range(8):
                tempPosition = (position - 1) * 8 + i 
                
                if board[tempPosition] == piece:
                    tempMove = movement.movePiece(tempPosition, board)
                
                    if tempMove != None:
                        if whereTo in tempMove:
                            piecesMoving.append(tempMove)
                            pos = tempPosition
        
        if position in columns:
            piecesMoving = []
            
            for i in range(8):
                tempPosition =  i * 8 + collumnNumbers[position]
                
                if board[tempPosition] == piece:
                    tempMove = movement.movePiece(tempPosition, board)
                    
                    if tempMove != None:
                        if whereTo in tempMove:
                            piecesMoving.append(tempMove)
                            pos = tempPosition

    else:
        
        for tempPosition in range(64):
            
            if board[tempPosition] == piece:
                tempMove = movement.movePiece(tempPosition, board)
                
                if tempMove != None:
                    if whereTo in tempMove:
                        piecesMoving.append(tempMove)
                        pos = tempPosition
                        
    
    if len(piecesMoving) != 1:
        return 'Invalid move'
    
    if whereTo not in piecesMoving[0]:
        return 'Invalid move 1'
    
    tempBoard = list(board)

    tempBoard[pos] = '0'
    
    tempBoard[whereTo] = piece
    
    finalBoard = ''.join(tempBoard)
    
    return finalBoard

def checkMoveType(move):
    position = ''
    piece = move[0]
    
    if move in ['O-O', 'O-O-O']:
        return "Castle"
    
    if move[1] == "x" and move[0] in movingPieces:
        column = move[2]
        row = move[3]
        return [piece, position, collumnNumbers[column] + 8 * (int(row) - 1)]
        # T x d 4 format
    
    if move[0] in movingPieces:
        column = move[1]
        row = move[2]
        return [piece, position, collumnNumbers[column] + 8 * (int(row) - 1)]
        # T d 4 format
                    
    if move[0] in columns:
        piece = "P"
        position = move[0]
        
        if move[1] == "x":
            column = move[2]
            row = move[3]
            return [piece, position, collumnNumbers[column] + 8 * (int(row) - 1)]
            # e x d 4 format
        
        column = move[0]
        row = move[1]
        return [piece, position, collumnNumbers[column] + 8 * (int(row) - 1)]
        # e 4 format
        
    if move[3] in rows and move[0] in movingPieces:
        position = move[1]
        column = move[2]
        row = move[3]
        return [piece, position, collumnNumbers[column] + 8 * (int(row) - 1)]
        # T d d 4 format
        # T 1 d 4 format
        
    if move[4] in rows:
        position = move[1]
        column = move[3]
        row = move[4]
        return [piece, position, collumnNumbers[column] + 8 * (int(row) - 1)]
        # T 1 x d 4 format
        # T d x d 4 format
        
    if move[5] in rows:
        position = (move[2] - 1) * 8 + collumnNumbers[move[1]]
        column = move[4]
        row = move[5]
        return [piece, position, collumnNumbers[column] + 8 * (int(row) - 1)]
    
    return 'Invalid move format'
    

def interpreter(data):
    exception = 'none'
    
    move = data[0]
    moveCount = data[1]
    moveHistory = data[2]
    board = data[3]
    
    if not firstCheck(move): return "Move with invalid characters"

    # if move in ['O-O', 'O-O-O']:
    #     exception = handleCastle(move, moveHistory, moveCount, board)
    
    #     print(exception) 
    #     return [exception, moveCount, board]
    
    try: 
        moveData = checkMoveType(move)
    except: 
        return 'Invalid move format'
    
    if moveData == 'Invalid move format': 
        return 'Invalid move format'
    
    if moveData == "Castle":
        return 'Castle'
        # go to handleCastle
    if moveCount % 2 == 0:
        moveData[0] = moveData[0].lower()
                
    finalBoard = makeMove(moveData, board)

    data = [finalBoard, moveData]
    return data