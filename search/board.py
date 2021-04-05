class Board:
    """
    Board class for controlling token movements and calculating possible movements
    """
    def __init__(this, tokens):
        this.tokens = tokens

    def possible_moves(token):
        """
        implement movement logic here?
        board logic for part 1...  will need to updte for later
        """
        possible_moves = moveGenerator(token.getCoordinate)
        boundaryCheckedMoves = boundaryChecker(possible_moves)


        # r = rows, q = qolumn


    def moveGenerator(coordinate):
        """
        creates moves, ignores boundaries/ other tokens...
        """
        r = coordinate[0]
        q = coordinate[1]

        possible_moves = []
        possible_moves.append((r+1,q-1), (r+1,q), (r,q+1), (r-1,q+1), (r-1,q), (r,q-1))

        return possible_moves
    
    def boundaryChecker(coordinatesList):
        """
        checks if token goes beyond limits
        """
        result_list = []
        for index, coordinate in enumerate(coordinatesList):
            if boundaryCheck(coordinate):
                result_list.append(coordinate)
        return result_list



    def boundaryCheck(coordinate):
        """
        helper func for boundaryChecker
        """
        r, q = coordinate[0], coordinate[1]

        if (r > 4 or r < -4 or q > 4 or q < -4):
            return 0

        elif (r = 4) :
            return 1 if (q >= -4 and q <= 0) else 0
        elif (r = 3) :
            return 1 if (q >= -4 and q <= 1) else 0
        elif (r = 2) :
            return 1 if (q >= -4 and q <= 2) else 0
        elif (r = 1) :
            return 1 if (q >= -4 and q <= 3) else 0    
        elif (r = 0) :
            return 1 if (q >= -4 and q <= 4) else 0
        elif (r = -1) :
            return 1 if (q >= -3 and q <= 4) else 0
        elif (r = -2) :
            return 1 if (q >= -2 and q <= 4) else 0
        elif (r = -3) :
            return 1 if (q >= -1 and q <= 4) else 0
        elif (r = -4) :
            return 1 if (q >=  0 and q <= 4) else 0

    
    def suicidalMoveCheck(coordinate):
        """
        checks if token's possible move lands on opponent's / our killing token
        r->s :: s->p :: p->r
        """
        r, q = coordinate[0], coordinate[1]

        






