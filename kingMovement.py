def checkEnemies(piece):
    white = ['K','Q','B','N','R','P']
    black = ['k','q','b','n','r','p']
    
    if piece in white:
        return black
    else:
        return white   
#end checkEnemies

def findThreats(position, board):
    if board[position] in ['r','R']:
        return rookAttack(position,board)
        
    elif board[position] in ['n','N']:
        return knightAttack(position,board)
    
    elif board[position] in ['b','B']:
        return bishopAttack(position,board)
    
    elif board[position] in ['q','Q']:
        return queenAttack(position,board)
    
    elif board[position] in ['k','K']:
        return kingPossibleMoves(position,board)
    
    elif board[position] in ['p','P']:
        return pawnAttack(position,board)
    
    return list()
#end findThreats

def checkEnemieMoves(board, enemies):
    enemieMoves = set()
    for i in range(0, 64, 1):
        if board[i] in enemies:
            threats = findThreats(i, board)
            if threats is not None:
                enemieMoves |= set(threats)
    return enemieMoves
#end checkforChecks

def kingLegalMoves(position, board): 
    piece = board[position]
    enemies = checkEnemies(piece)
      
    enemiesMoves = checkEnemieMoves(board, enemies)
    kingMoves = set(kingPossibleMoves(position, board))
    
    kingLegal = kingMoves - enemiesMoves
    
    return list(kingLegal)
#end king legal moves

def kingPossibleMoves(position, board):
    
    moves = []
    
    if (position +1) % 8 != 0:
        #check 1
        moves.append(position+1) 
        
        #check 9
        if (position + 9) < 64:
            moves.append(position+9)
        
        #check -7
        if (position -7) > 0:
            moves.append(position-7)
            
    if position % 8 != 0:
        #check -1
        moves.append(position-1)

        #check 7
        if (position + 7) < 64:
            moves.append(position+7)
        
        #check -9
        if (position -9) >= 0:
            moves.append(position -9)
            
    #check 8
    if position + 8 < 64:
        moves.append(position+8)
    
    #check -8
    if position -8 >= 0:
        moves.append(position-8)
        
    return moves
#end king moves

def blackPawnAttack(position, board):
    moves = []
    
    if (position + 1 % 8) != 0 and position - 7 >= 0:
        moves.append(position-7)
        
    if position % 8 != 0 and position - 9 >= 0:
        moves.append(position-9)
    
    return moves
#end black pawn attack

def whitePawnAttack(position, board):
    moves = []
    
    if position % 8 != 0 and position + 7 < 64:
        moves.append(position+7)
        
    if (position + 1) % 8 != 0 and position + 9 < 64:
        moves.append(position+9)
            
    return moves
#end white pawn attack

def pawnAttack(position, board):
    piece = board[position]
    
    moves = []    
    if piece == 'p': 
        moves = blackPawnAttack(position, board)
    elif piece == 'p': 
        moves = whitePawnAttack(position, board)
    
    return moves
#end pawnAttacks

def rookAttack(position, board):
    moves = []
    
    for i in range(position+8, 64, 8):
        if i > 63:
            break
        
        if board[i] == '0':
            moves.append(i)
            
        else:
            moves.append(i)
            break
        
    for i in range(position-8, -1, -8):
        if i < 0:
            break
        
        if board[i] == '0':
            moves.append(i)
        
        else: 
            moves.append(i)
            break
    
    i = position
    while (i+1) % 8 !=0:
        if i+1 > 63:
            break
        
        if board[i+1] == '0':
            moves.append(i+1)
        
        else: 
            moves.append(i+1)
            break
        
        i += 1
    
        
    i = position
    while i % 8 != 0:
        if i < 0:
            break
        
        if board[i-1] == '0':
            moves.append(i-1)
            
        else: 
            moves.append(i-1)
            break
        
        i -= 1
    
    return moves
#end rook moves

def bishopAttack(position, board):
    
    moves = []
    
    i = position
    while (i + 1) % 8 != 0 and i+9 < 64:
        if board[i+9] == '0':
            moves.append(i+9)
            
        else:
            moves.append(i+9) 
            break
        
        i += 9
        
    i = position
    while i % 8 != 0 and i+7 < 64:
        if board[i+7] == '0':
            moves.append(i+7)
        
        else: 
            moves.append(i+7)
            break
        
        i += 7
        
    i = position
    while (i + 1) % 8 != 0 and i-7 > 0:
        if board[i-7] == '0':
            moves.append(i-7)
        
        else:
            moves.append(i-7)
            break
        
        i -= 7
        
        
    i = position
    while i % 8 != 0 and i-9 >= 0:
        if board[i-9] == '0':
            moves.append(i-9)
            
        else:
            moves.append(i-9)
            break
        
        i -= 9
        
    return moves
#end bishop moves

def queenAttack(position, board):
    moves = []
    
    for i in range(position+8, 64, 8):
        
        if board[i] == '0':
            moves.append(i)
            
        else:
            moves.append(i) 
            break
        
    for i in range(position-8, -1, -8):
        
        if board[i] == '0':
            moves.append(i)
    
        else: 
            moves.append(i)
            break
    
    i = position
    while (i+1) % 8 !=0:
        
        if board[i+1] == '0':
            moves.append(i+1)
                
        else: 
            moves.append(i+1)
            break
        
        i += 1
    
        
    i = position
    while i % 8 != 0:
        
        if board[i-1] == '0':
            moves.append(i-1)            
            
        else: 
            moves.append(i-1)
            break
        
        i -= 1
        
        
    #end rooklike moves
    
    i = position
    while (i + 1) % 8 != 0 and i+9 < 64:
        if board[i+9] == '0':
            moves.append(i+9)
            
        else:
            moves.append(i+9) 
            break
        
        i += 9
        
    i = position
    while i % 8 != 0 and i+7 < 64:
        if board[i+7] == '0':
            moves.append(i+7)
        
        else:
            moves.append(i+7) 
            break
        
        i += 7
        
    i = position
    while (i + 1) % 8 != 0 and i-7 > 0:
        if board[i-7] == '0':
            moves.append(i-7)
           
        else:
            moves.append(i-7)
            break
        
        i -= 7
        
        
    i = position
    while i % 8 != 0 and i-9 >= 0:
        if board[i-9] == '0':
            moves.append(i-9)
            
        else:
            moves.append(i-9)
            break
        
        i -= 9
        
    #end bishoplike moves

    return moves
#end queen moves

def knightAttack(position, board):
    moves = []
  
    if position % 8 != 0:
        if position + 15 < 64:
            moves.append(position+15)
        if position -17 >= 0:
            moves.append(position-17)

        if (position -1) % 8 != 0:
            if position + 6 < 64:
                moves.append(position+6)
            if position -10 >= 0:
                moves.append(position-10)
    
    if (position+1) % 8 != 0:
        if position + 17 < 64:
            moves.append(position+17)
        if position -15 >= 0:
            moves.append(position-15)
        
        if (position + 2) % 8 != 0:
            if position + 10 < 64:
                moves.append(position+10)
            if position -6 >= 0:
                moves.append(position-6)
                
    return moves
#end knight moves