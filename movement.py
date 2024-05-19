from kingMovement import kingLegalMoves

def checkEnemies(piece):
    white = ['K','Q','B','N','R','P']
    black = ['k','q','b','n','r','p']
    
    if piece in white:
        return black
    else:
        return white   
#end checkEnemies

def movePiece(position, board):
    
    if board[position] in ['r','R']:
        return rookLegalMoves(position,board)
        
    elif board[position] in ['n','N']:
        return knightLegalMoves(position,board)
    
    elif board[position] in ['b','B']:
        return bishopLegalMoves(position,board)
        
    elif board[position] in ['q','Q']:
        return queenLegalMoves(position,board)
    
    elif board[position] in ['k','K']:
        return kingLegalMoves(position,board)   
    
    elif board[position] in ['p','P']:
        return pawnLegalMoves(position,board)
    
    return list()
#end movePiece

def rookLegalMoves(position, board):
    piece = board[position]
    enemies = checkEnemies(piece)
    
    moves = []
    
    for i in range(position+8, 64, 8):
        if i > 63:
            break
        
        if board[i] == '0':
            moves.append(i)
            
        elif board[i] in enemies:
            moves.append(i)
            break
        
        else: 
            break
        
    for i in range(position-8, -1, -8):
        if i < 0:
            break
        
        if board[i] == '0':
            moves.append(i)
            
        elif board[i] in enemies:
            moves.append(i)
            break
        
        else: 
            break
    
    i = position
    while (i+1) % 8 !=0:
        if i+1 > 63:
            break
        
        if board[i+1] == '0':
            moves.append(i+1)
                
        elif board[i+1] in enemies:
            moves.append(i+1)
            break
        
        else: 
            break
        
        i += 1
    
        
    i = position
    while i % 8 != 0:
        if i < 0:
            break
        
        if board[i-1] == '0':
            moves.append(i-1)
                
        elif board[i-1] in enemies:
            moves.append(i-1)
            break
            
        else: 
            break
        
        i -= 1
    
    return moves
#end rook moves

def bishopLegalMoves(position, board):
    piece = board[position]
    enemies = checkEnemies(piece)
    
    moves = []
    
    i = position
    while (i + 1) % 8 != 0 and i+9 < 64:
        if board[i+9] == '0':
            moves.append(i+9)
            
        elif board[i+9] in enemies:
            moves.append(i+9)
            break
        
        else: 
            break
        
        i += 9
        
    i = position
    while i % 8 != 0 and i+7 < 64:
        if board[i+7] == '0':
            moves.append(i+7)
            
        elif board[i+7] in enemies:
            moves.append(i+7)
            break
        
        else: 
            break
        
        i += 7
        
    i = position
    while (i + 1) % 8 != 0 and i-7 > 0:
        if board[i-7] == '0':
            moves.append(i-7)
            
        elif board[i-7] in enemies:
            moves.append(i-7)
            break
        
        else: 
            break
        
        i -= 7
        
        
    i = position
    while i % 8 != 0 and i-9 >= 0:
        if board[i-9] == '0':
            moves.append(i-9)
            
        elif board[i-9] in enemies:
            moves.append(i-9)
            break
        
        else: 
            break
        
        i -= 9
        
    return moves
#end bishop moves

def queenLegalMoves(position, board):
    piece = board[position]
    enemies = checkEnemies(piece)
    
    moves = []
    
    for i in range(position+8, 64, 8):
        
        if board[i] == '0':
            moves.append(i)
            
        elif board[i] in enemies:
            moves.append(i)
            break
        
        else: 
            break
        
    for i in range(position-8, -1, -8):
        
        if board[i] == '0':
            moves.append(i)
            
        elif board[i] in enemies:
            moves.append(i)
            break
        
        else: 
            break
    
    i = position
    while (i+1) % 8 !=0:
        
        if board[i+1] == '0':
            moves.append(i+1)
                
        elif board[i+1] in enemies:
            moves.append(i+1)
            break
            
        else: 
            break
        
        i += 1
    
        
    i = position
    while i % 8 != 0:
        
        if board[i-1] == '0':
            moves.append(i-1)
                
        elif board[i-1] in enemies:
            moves.append(i-1)
            break
            
        else: 
            break
        
        i -= 1
        
        
    #end rooklike moves
    
    i = position
    while (i + 1) % 8 != 0 and i+9 < 64:
        if board[i+9] == '0':
            moves.append(i+9)
            
        elif board[i+9] in enemies:
            moves.append(i+9)
            break
        
        else: 
            break
        
        i += 9
        
    i = position
    while i % 8 != 0 and i+7 < 64:
        if board[i+7] == '0':
            moves.append(i+7)
            
        elif board[i+7] in enemies:
            moves.append(i+7)
            break
        
        else: 
            break
        
        i += 7
        
    i = position
    while (i + 1) % 8 != 0 and i-7 > 0:
        if board[i-7] == '0':
            moves.append(i-7)
            
        elif board[i-7] in enemies:
            moves.append(i-7)
            break
        
        else: 
            break
        
        i -= 7
        
        
    i = position
    while i % 8 != 0 and i-9 >= 0:
        if board[i-9] == '0':
            moves.append(i-9)
            
        elif board[i-9] in enemies:
            moves.append(i-9)
            break
        
        else: 
            break
        
        i -= 9
        
    #end bishoplike moves

    return moves
#end queen moves

def knightLegalMoves(position, board):
    piece = board[position]
    enemies = checkEnemies(piece)
    moves = []
    
    if position % 8 != 0:
        if position + 15 < 64:
            if board[position + 15] == "0" or board[position + 15] in enemies:
                moves.append(position+15)
        if position -17 >= 0:
            if board[position - 17] == "0" or board[position - 17] in enemies:
                moves.append(position-17)

        if (position -1) % 8 != 0:
            if position + 6 < 64:
                if board[position + 6] == "0" or board[position + 6] in enemies:
                    moves.append(position+6)
            if position -10 >= 0:
                if board[position - 10] == "0" or board[position - 10] in enemies:
                    moves.append(position-10)
    
    if (position+1) % 8 != 0:
        if position + 17 < 64:
            if board[position + 17] == "0" or board[position + 17] in enemies:
                moves.append(position+17)
        if position -15 >= 0:
            if board[position - 15] == "0" or board[position - 15] in enemies:
                moves.append(position-15)
        
        if (position + 2) % 8 != 0:
            if position + 10 < 64:
                if board[position + 10] == "0" or board[position + 10] in enemies:
                    moves.append(position+10)
            if position -6 >= 0:
                if board[position - 6] == "0" or board[position - 6] in enemies:
                    moves.append(position-6)
    
    return moves
#end knight moves

def kingPossibleMoves(position, board):
    
    piece = board[position]
    enemies = checkEnemies(piece)
    
    moves = []
    
    if (position +1) % 8 != 0:
        #check 1
        if board[position + 1] == '0' or board[position + 1] in enemies: moves.append(position+1) 
        
        #check 9
        if (position + 9) < 64:
            if board[position + 9] == '0' or board[position + 9] in enemies: moves.append(position+9)
        
        #check -7
        if (position -7) > 0:
            if board[position -7] == '0' or board[position -7] in enemies: moves.append(position-7)
            
    if position % 8 != 0:
        #check -1
        if board[position -1] == '0' or board[position -1] in enemies: moves.append(position-1)

        #check 7
        if (position + 7) < 64:
            if board[position + 7] == '0' or board[position + 7] in enemies: moves.append(position+7)
        
        #check -9
        if (position -9) >= 0:
            if board[position -9] == '0' or board[position -9] in enemies: moves.append(position -9)
            
    #check 8
    if position + 8 < 64:
        if board[position + 8] == '0' or board[position + 8] in enemies: moves.append(position+8)
    
    #check -8
    if position -8 >= 0:
        if board[position -8] == '0' or board[position - 8] in enemies: moves.append(position-8)
        
    return moves
#end king moves

def whitePawnLegalMoves(position, board):
    moves = []
    
    if position + 8 < 64:
        
        if board[position+8] == '0':
            moves.append(position+8)
            
            if position + 16 < 64:
                
                if position in range(8,16) and board[position+16] == '0':
                    moves.append(position+16)
    
    return moves
#end white pawn moves

def whitePawnAttack(position, board):
    piece = board[position]
    enemies = checkEnemies(piece)
    
    moves = []
    
    if position % 8 != 0 and position + 7 < 64:
        if board[position+7] in enemies:
            moves.append(position+7)
        
    if (position + 1) % 8 != 0 and position + 9 < 64:
        if board[position+9] in enemies:
            moves.append(position+9)
            
    return moves
#end white pawn attack

def blackPawnLegalMoves(position, board):
    moves = []
    
    if position - 8 >= 0:
        
        if board[position-8] == '0':
            moves.append(position-8)
            
            if position - 16 >= 0:
                if position in range(48,56) and board[position-16] == '0':
                    moves.append(position-16)
                    
    return moves
#end pawn moves

def blackPawnAttack(position, board):
    piece = board[position]
    enemies = checkEnemies(piece)
    
    moves = []
    if (position + 1 % 8) != 0 and position - 7 >= 0:
        if board[position-7] in enemies:
            moves.append(position-7)
        
    if position % 8 != 0 and position - 9 >= 0:
        if board[position-9] in enemies:
            moves.append(position-9)
            
    return moves
#end black pawn attack

def pawnLegalMoves(position, board):
    piece = board[position]
    
    moves = []    
    if piece == 'p': 
        moves = blackPawnLegalMoves(position, board)
        moves += blackPawnAttack(position, board)
    elif piece == 'P': 
        moves = whitePawnLegalMoves(position, board)
        moves += whitePawnAttack(position, board)
    
    return moves
#end pawnLegalMoves

def pawnAttack(position,board):
    piece = board[position]
    
    moves = []    
    if piece == 'p': 
        moves = blackPawnAttack(position, board)
    elif piece == 'p': 
        moves = whitePawnAttack(position, board)
    
    return moves
#end pawnAttacks