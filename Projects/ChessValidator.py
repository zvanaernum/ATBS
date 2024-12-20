validBoard = {
    '1a': 'brook', '1b': 'bknight', '1c': 'bbishop', '1d': 'bqueen', 
    '1e': 'bking', '1f': 'bbishop', '1g': 'bknight', '1h': 'brook',
    '2a': 'bpawn', '2b': 'bpawn', '2c': 'bpawn', '2d': 'bpawn', 
    '2e': 'bpawn', '2f': 'bpawn', '2g': 'bpawn', '2h': 'bpawn',
    '8a': 'wrook', '8b': 'wknight', '8c': 'wbishop', '8d': 'wqueen', 
    '8e': 'wking', '8f': 'wbishop', '8g': 'wknight', '8h': 'wrook',
    '7a': 'wpawn', '7b': 'wpawn', '7c': 'wpawn', '7d': 'wpawn', 
    '7e': 'wpawn', '7f': 'wpawn', '7g': 'wpawn', '7h': 'wpawn'
}

tooManyWhite = {
    '1h': 'wking', '6c': 'wqueen', '2g': 'wbishop', '5h': 'wqueen', 
    '3e': 'wbishop', '1a': 'wrook', '1b': 'wrook', '1c': 'wrook', 
    '2a': 'wpawn', '2b': 'wpawn', '2c': 'wpawn', '2d': 'wpawn', 
    '2e': 'wpawn', '2f': 'wpawn', '2h': 'wpawn', '3a': 'wpawn',
    '3b': 'wpawn'  # This extra pawn makes it more than the allowed 16 white pieces..
}

tooManyBlack = {
    '1h': 'bking', '6c': 'bqueen', '2g': 'bbishop', '5h': 'bqueen', 
    '3e': 'bbishop', '8a': 'brook', '8b': 'brook', '8c': 'brook', 
    '7a': 'bpawn', '7b': 'bpawn', '7c': 'bpawn', '7d': 'bpawn', 
    '7e': 'bpawn', '7f': 'bpawn', '7g': 'bpawn', '7h': 'bpawn',
    '6a': 'bpawn'  # This extra pawn makes it more than the allowed 16 black pieces.
}

invalidPosition = {
    '1a': 'brook', '1b': 'bknight', '1c': 'bbishop', '1d': 'bqueen', 
    '1e': 'bking', '1f': 'bbishop', '1g': 'bknight', '1h': 'brook',
    '2a': 'bpawn', '2b': 'bpawn', '2c': 'bpawn', '2d': 'bpawn', 
    '2e': 'bpawn', '2f': 'bpawn', '2g': 'bpawn', '2h': 'bpawn',
    '9a': 'wpawn'  # Invalid position '9a'
}

invalidWhiteKings = {
    '1a': 'brook', '1b': 'bknight', '1c': 'bbishop', '1d': 'bqueen', 
    '1e': 'bking', '1f': 'bbishop', '1g': 'bknight', '1h': 'brook',
    '2a': 'bpawn', '2b': 'bpawn', '2c': 'bpawn', '2d': 'bpawn', 
    '2e': 'bpawn', '2f': 'bpawn', '2g': 'bpawn', '2h': 'bpawn',
    '8e': 'wking', '8d': 'wking'  # Two white kings
}

invalidPieceType = {
    '1a': 'brook', '1b': 'bknight', '1c': 'bbishop', '1d': 'bqueen', 
    '1e': 'bking', '1f': 'bbishop', '1g': 'bknight', '1h': 'brook',
    '2a': 'bpawn', '2b': 'bpawn', '2c': 'bpawn', '2d': 'bpawn', 
    '2e': 'bpawn', '2f': 'bpawn', '2g': 'bpawn', '2h': 'bpawn',
    '7a': 'wpawn', '8b': 'wprince'  # 'wprince' is an invalid piece type
}

invalidWhitePawns = {
    '1a': 'brook', '1b': 'bknight', '1c': 'bbishop', '1d': 'bqueen', 
    '1e': 'bking', '1f': 'bbishop', '1g': 'bknight', '1h': 'brook',
    '2a': 'bpawn', '2b': 'bpawn', '2c': 'bpawn', '2d': 'bpawn', 
    '2e': 'bpawn', '2f': 'bpawn', '2g': 'bpawn', '2h': 'bpawn',
    '7a': 'wpawn', '7b': 'wpawn', '7c': 'wpawn', '7d': 'wpawn', 
    '7e': 'wpawn', '7f': 'wpawn', '7g': 'wpawn', '7h': 'wpawn',
    '6a': 'wpawn'  # This extra pawn makes it 9 white pawns
}


def validPieceNames(board):
    # Define a list of valid piece names
    validPieces = ['king', 'queen', 'rook', 'bishop', 'knight', 'pawn']

    # Iterate over each piece on the board
    for piece in board.values():
        # Check if the piece starts with 'w' or 'b'
        if piece [0] in ['w', 'b']:
            # Extract the piece type (everything after the first character)
            pieceType = piece[1:]
            # Check if the piece type is in the list of valid pieces
            if pieceType in validPieces:
                continue # Piece name is valid, move to next phase
            else:
                return 'Invalid piece type found: ' + piece
        else:
            return 'Invalid piece type found: ' + piece
    return True # All pieces are valid


def posValid(board):
    for position in board.keys():
        row = position[0] # index 0 in the key represents the numeric row
        column = position[1] # index 1 in the key represents the alphabetical column

        # Check if row is within 1-8 and column is within a-h
        if row in '12345678' and column in 'abcdefgh':
            continue
        else:
            return position + ' Is not a valid position'
    return True


def tooManyPieces(board):
    b = 0
    w = 0
    for piece in board.values():
        if piece[0] == 'b':
            b +=1
        elif piece[0] == 'w':
            w +=1
    if b > 16:
        return 'Too many black pieces on the board'
    if w > 16:
        return 'Too many white pieces on the board' 
    return True   


def tooManyKings(board):
    b = 0
    w = 0
    for piece in board.values():
        if piece[0] =='b' and 'king' in piece:
            b +=1
        elif piece[0] == 'w' and 'king' in piece:
            w += 1
    if b != 1:
        return 'Invalid number of black kings on the board'
    if w != 1:
        return 'Invalid number of white kings on the board'
    return True


def tooManyQueens(board):
    b = 0
    w = 0
    for piece in board.values():
        if piece[0] =='b' and 'queen' in piece:
            b +=1
        elif piece[0] == 'w' and 'queen' in piece:
            w += 1
    if b > 1:
        return 'Too many black queens on the board'
    if w > 1:
        return 'Too many white queens on the board'
    return True


def tooManyRooks(board):
    b = 0
    w = 0
    for piece in board.values():
        if piece[0] =='b' and 'rook' in piece:
            b +=1
        elif piece[0] == 'w' and 'rook' in piece:
            w += 1
    if b > 2:
        return 'Too many black rooks on the board'
    if w > 2:
        return 'Too many white rooks on the board'
    return True


def tooManyBishops(board):
    b = 0
    w = 0
    for piece in board.values():
        if piece[0] =='b' and 'bishop' in piece:
            b +=1
        elif piece[0] == 'w' and 'bishop' in piece:
            w += 1
    if b > 2:
        return 'Too many black bishops on the board'
    if w > 2:
        return 'Too many white bishops on the board'
    return True


def tooManyKnights(board):
    b = 0
    w = 0
    for piece in board.values():
        if piece[0] =='b' and 'knight' in piece:
            b +=1
        elif piece[0] == 'w' and 'knight' in piece:
            w += 1
    if b > 2:
        return 'Too many black knights on the board'
    if w > 2:
        return 'Too many white knights on the board'
    return True

def tooManyPawns(board):
    b = 0
    w = 0
    for piece in board.values():
        if piece[0] =='b' and 'pawn' in piece:
            b +=1
        elif piece[0] == 'w' and 'pawn' in piece:
            w += 1
    if b > 8:
        return 'Too many black pawns on the board'
    if w > 8:
        return 'Too many white pawns on the board'
    return True

def isValidChessBoard(board):
    # Call each validation function and capture the result
    result = validPieceNames(board)
    if result != True:
        return result
    
    result = posValid(board)
    if result != True:
        return result
    
    result = tooManyPieces(board)
    if result != True:
        return result
    
    result = tooManyKings(board)
    if result != True:
        return result
    
    result = tooManyQueens(board)
    if result != True:
        return result
    
    result = tooManyRooks(board)
    if result != True:
        return result
    
    result = tooManyBishops(board)
    if result != True:
        return result
    
    result = tooManyKnights(board)
    if result != True:
        return result
    
    result = tooManyPawns(board)
    if result != True:
        return result
    
    # If all checks pass, the board is valid
    return "The chessboard is valid"

isValidChessBoard(invalidWhitePawns)
