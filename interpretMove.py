import movement

acceptedLetters = ['R','N','B','K','Q','a','b','c','d','e','f','g','h','x','1','2','3','4','5','6','7','8']

movingPieces = ['R','N','B','K','Q']

columns = ['a','b','c','d','e','f','g','h']

rows = ['1','2','3','4','5','6','7','8']

# T d 4

# T d d4

# T 1 d4

# T 1 xd4

# T d xd4

# T x d4

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
# value = (row-1) * 8 + collumnNumbers[letter]

def firstCheck(move):
    exception = 'none'
    if len(move) > 5 or len(move) < 2:
        exception = 'Invalid move format'
    
    if len(move) == 2 and (move[0] not in columns or move[1] not in rows):
        exception = 'Invalid move format'
        
    for letter in move:
        if letter not in acceptedLetters:
            exception = 'Invalid move format'
                   
    return exception

def makeMove(piece, position, whereTo, moveNumber, board):
    
    if moveNumber % 2 == 0: piece = piece.lower()
    
    piecesMoving = []
    
    if position != 'none':
        if position in rows:
            piecesThere = []
            
            #position - 1 * 8 + i 
            for i in range(8):
                tempPosition = (position - 1) * 8 + i 
                
                if board[tempPosition] == piece:
                    piecesThere.append[tempPosition]
                    position = tempPosition
                    
            if len(piecesThere) != 1:
                return 'invalid algebraic notation'
            
            pieceMoves = movement.movePiece(position, board)
        
        elif position in columns:
            piecesThere = []
            
            #position + 8 * i
            for i in range(8):
                tempPosition = collumnNumbers[position] + 8 * i
                
                if board[tempPosition] == piece:
                    piecesThere.append(tempPosition)
                    position = tempPosition
                    break
              
            if len(piecesThere) == 0:
                return 'Invalid move'
            elif len(piecesThere) > 1:
                return 'Ambigous move'
            
            pieceMoves = movement.movePiece(position, board)
        
        if whereTo not in pieceMoves:
            return 'Illegal move'
        #check if pieceMoves in whereto     
        
    else:        
        piecesMoving = []
        pos = ''
        
        for i in range(64):
            
            if board[i] == piece:
                moves = movement.movePiece(i, board)
                kingPos = i
                
                if moves != None:
                    if whereTo in moves:
                        if len(piecesMoving) != 0:
                            return 'Ambigous move, try specifing piece collumn/row'
                        piecesMoving.append(moves)
                        pos = i         
            
        if len(piecesMoving) != 1: 
            if piece in ['K','k']:
                if whereTo not in moves and whereTo in movement.kingPossibleMoves(kingPos, board):
                    return 'This move is dangerous for the King'
                else:
                    return 'Invalid move 2'
    
        if position != 'none':
            if pos != position: return 'illegal move'
        else:
            position = pos
    
    
    
    tempBoard =  list(board)
    
    tempBoard[position] = '0'
    
    tempBoard[whereTo] = piece
    
    finalBoard = ''.join(tempBoard)
    
    return finalBoard
                    
#end checkforChecks

def checkMoveType(move):
    position = 'none'
    if move[0] in movingPieces: 
        piece = move[0]
        
        if move[1] == "x":
            
            #check if is valid
            if move[2] not in columns or move[3] not in rows:
                exception = "invalid move 4"
                return exception
            column = move[2]
            row = move[3]
            
            #handle Txd4 format
            
        elif move[1] in columns:
            column = move[1]
            
            if move[2] in rows:
                row = move[2]
                
                #handle Td4 format
                
            elif move[2] in columns or move[2] in rows:
                 
                #check if is valid
                if move[3] not in rows:
                    exception = "invalid move 5"
                    return exception
                
                position = move[1]
                column = move[2]
                row = move[3]
                
                #handle Tdd4 format
                
            elif move[2] == "x":

                #check if is valid
                if (move[3] not in columns and move[3] not in rows) or move[4] not in rows:
                    exception = "invalid move 6"
                    return exception
                
                position = move[1]
                column = move[3]
                row = move[4]
                
                #handle Tdxd4 format
            
            else: 
                exception = "invalid move 7"
                return exception
                
        else: 
            exception = "invalid move 8"
            return exception
            
    elif move[0] in columns:
        piece = 'P'
        
        if move[1] in rows:
            column = move[0]
            row = move[1]
            position = move[0]
            #handle e4 format
            
        elif move[1] == "x":
            
            #check if is valid
            if move[2] not in columns or move[3] not in rows:
                exception = "invalid move 9"
                return exception
            
            position = move[0]
            column = move[2]
            row = move[3]

        else: 
            exception = "Invalid move"
            return exception
        
    else: 
        exception = "invalid move 11"
        return exception
    
    whereTo = collumnNumbers[column] + 8 * ( int(row) - 1) 
    
    moveData = [piece, position, whereTo]
    
    return moveData
    

def interpreter(move, moveNumber, board):
    exception = 'none'

    exception = firstCheck(move)
    
    if exception != 'none': return exception

    moveData = checkMoveType(move)
    
    if not isinstance(moveData, list):
        return moveData 
    
    piece = moveData[0]

    position = moveData[1]
    
    whereto = moveData[2]
    
    if exception == 'none':
        finalBoard = makeMove(piece, position, whereto, moveNumber, board)
        return finalBoard
    else: print(exception)
        