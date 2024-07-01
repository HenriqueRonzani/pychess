import movement

movingPieces = ['R','N','B','K','Q']

columns = ['a','b','c','d','e','f','g','h']

rows = ['1','2','3','4','5','6','7','8']

acceptedLetters = movingPieces + columns + rows + ['x', '-', 'O']

white = ['R','N','B','K','Q','P']

# T d 4
# T d d 4
# T 1 d 4
# T 1 x d 4
# T d x d 4
# T d 1 x d 4
# T d 1 d 4
# T x d 4
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
   
    if len(move) > 6 or len(move) < 2:
        validMove = False
    
    if len(move) == 2 and (move[0] not in columns or move[1] not in rows):
        validMove = False
        
    for letter in move:
        if letter not in acceptedLetters:
            validMove = False
                             
    return validMove

def makeMove(moveData, board, inCheck):
  [ piece, position, whereTo ] = moveData

  piecesMoving = []
  pos = ''
  
  if isinstance(position, int):
      if board[position] != piece:
          return 'Invalid move 1'
      
  elif position != '':
      
      if position in rows:
          piecesMoving = []
              
          for i in range(8):
              tempPosition = (int(position) - 1) * 8 + i 
              
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
      return 'Invalid move 2'
  
  if whereTo not in piecesMoving[0]:
      return 'Invalid move 3'
  
  tempBoard = list(board)

  tempBoard[pos] = '0'
  
  tempBoard[whereTo] = piece
  
  finalBoard = ''.join(tempBoard)
  
  newInCheck = {'White': not checkIfCheck(finalBoard, 'K', [finalBoard.index('K')]), 'Black': not checkIfCheck(finalBoard, 'k', [finalBoard.index('k')])}	
  
  if inCheck['White'] and newInCheck['White']:
    return 'Invalid move 4'
  if inCheck['Black'] and newInCheck['Black']:
    return 'Invalid move 5'
  
  return [finalBoard, newInCheck]

def checkMoveType(move):  
    position = ''
    piece = move[0]
    
    if move in ['O-O', 'O-O-O']:
        return "Castle"
    
    if len(move) == 6:
      if move[5] in rows:
        position = (move[2] - 1) * 8 + collumnNumbers[move[1]]
        column = move[4]
        row = move[5]
        return [piece, position, collumnNumbers[column] + 8 * (int(row) - 1)]  
      
    if len(move) == 5:   
      if move[4] in rows:
        position = move[1]
        column = move[3]
        row = move[4]
        return [piece, position, collumnNumbers[column] + 8 * (int(row) - 1)]
        # T 1 x d 4 format
        # T d x d 4 format
        
    if len(move) == 4:
      if move[3] in rows and move[0] in movingPieces:
        position = move[1]
        column = move[2]
        row = move[3]
        return [piece, position, collumnNumbers[column] + 8 * (int(row) - 1)]
        # T d d 4 format
        # T 1 d 4 format
    
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
    
    return 'Invalid move 4'
    
def handleCastle(move, board, piece, moveHistory):
    rows = {
        'K': [0, 1, 2, 3, 4, 5, 6, 7],
        'k': [56, 57, 58, 59, 60, 61, 62, 63]
    }
    
    rookForKing = {
        'k': 'r',
        'K': 'R'
    }
    
    if move == 'O-O':
        positions = rows[piece][4:]
        piecesInPositionArray = [board[i] for i in positions]
        piecesInPositionString = ''.join(piecesInPositionArray)
        
        rook = rookForKing[piece]
        
        if piecesInPositionString == piece+'00'+rook:
            for moveData in moveHistory:
                if moveData[0] == rook and moveData[1] == positions[3]: return 'Cannot castle'
                if moveData[0] == piece: return 'Cannot castle'
            
            if not checkIfCheck(board, piece, positions): return 'Cannot castle'
            
            tempBoard = list(board)
            tempBoard[positions[0]] = '0'
            tempBoard[positions[1]] = rook
            tempBoard[positions[2]] = piece
            tempBoard[positions[3]] = '0'
            
            finalBoard = ''.join(tempBoard)
            return finalBoard
    
    if move == 'O-O-O':
        positions = rows[piece][:5]
        piecesInPositionArray = [board[i] for i in positions]
        piecesInPositionString = ''.join(piecesInPositionArray)
        
        rook = rookForKing[piece]
        
        if piecesInPositionString == rook+'000'+piece:
            for moveData in moveHistory:
                if moveData[0] == rook and moveData[1] == positions[0]: return 'Cannot castle'
                if moveData[0] == piece: return 'Cannot castle'
            
            safeToCastle = checkIfCheck(board, piece, positions)
            print(safeToCastle)
            
            if not safeToCastle: return 'Cannot castle'
        
            tempBoard = list(board)
            tempBoard[positions[0]] = '0'
            tempBoard[positions[1]] = '0'
            tempBoard[positions[2]] = piece
            tempBoard[positions[3]] = rook
            tempBoard[positions[4]] = '0'
            
            finalBoard = ''.join(tempBoard)
        
            return finalBoard
            
    return 'Invalid move 5'

def checkIfCheck(board, piece, positions):
    enemies = {
        'K': ['r', 'n', 'b', 'q', 'p'],
        'k': ['R', 'N', 'B', 'Q', 'P']
    }
    
    attackingMoves = set()

    for i, pieces in enumerate(board):
        if pieces in enemies[piece]:
            movesOfPiece = movement.movePiece(i, board)
            if movesOfPiece != None:
                attackingMoves |= set(movesOfPiece)

    attackingMoves = list(attackingMoves)
    print(attackingMoves)
    for position in positions:
        print(position)
        if position in attackingMoves:
            return False
          
    return True        


def interpreter(data):
    [ move, moveCount, moveHistory, board, inCheck ] = data
    
    if not firstCheck(move): return "Move with invalid characters"
    
    try: 
        moveData = checkMoveType(move)
    except Exception as e: 
        print (e)
        return 'Invalid move format 6'
    
    if isinstance(moveData, str): return moveData
    
    if moveData == "Castle":
        try:
          piece = 'k' if moveCount % 2 == 0 else 'K'
          finalBoard = handleCastle(move, board, piece, moveHistory)
          return [finalBoard, "O-O", inCheck]
        except Exception as e:
          return 'Invalid move 9'
    else:
     #   try:
            if moveCount % 2 == 0: moveData[0] = moveData[0].lower()
            
            returnData = makeMove(moveData, board, inCheck)
            if isinstance(returnData, str): return returnData
            
            [finalBoard, inCheck] = returnData
            data = [finalBoard, moveData, inCheck]
            print(data)
            return data
      
      #  except Exception as e:
            return f"invalid move 10, {e}"