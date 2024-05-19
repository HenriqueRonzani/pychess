                     
def handleCastle(move, moveHistory, moveCount, board):
    aColumn = [56, 48, 40, 32, 24, 16, 8, 0]
    hColumn = [63, 55, 47, 39, 31, 23, 15, 7]
    firstRow = [0, 1, 2, 3, 4, 5, 6, 7]
    eightRow = [56, 57, 58, 59, 60, 61, 62, 63]

    
    print (move)
    
    if move == 'O-O':
        if moveCount % 2 == 0:
            piece = 'k'
            
            if board[63] == 'r':
                for moveData in moveHistory:
                    if moveData[0] == 'r' and (moveData[2] in hColumn or moveData[2] in eightRow):
                        return 'Cannot castle'
                
                if board[61] == '0' and board[62] == '0':
                    return 'can castle'
                
                else: return 'Cannot castle'
                
            else: return 'Cannot castle'
                     
        else:
            piece = 'K'
        
            if board[7] == 'R':
                print(moveHistory)
                for moveData in moveHistory:
                    print(moveData[0])
                    if moveData[0] == 'R' and (moveData[2] in hColumn or moveData[2] in firstRow):
                        return 'Cannot castle'
                
                if board[5] == '0' and board[6] == '0':
                    return 'can castle'
                
                else: return 'Cannot castle'    
                
            else: return 'Cannot castle'
        
    elif move == 'O-O-O':
        piece = 'k' if moveCount % 2 == 0 else 'K'
        
    return 'move'

def test():                    
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
    return 'cyka blyat'