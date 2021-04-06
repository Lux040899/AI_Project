class Token:

    def __init__(this, coordinate, tokenID):
        this.coordinate = coordinate
        this.tokenID = tokenID
        this.player = "Upper" if tokenID.upper() else "Lower"

    def getCoordinate(this):
        return this.coordinate
    
    def getTokenID(this):
        return this.tokenID
    
    def getPlayer(this):
        return this.player

     def possibleMoves(this, blocked):
        """
        implement movement logic here?
        board logic for part 1...  will need to update for later
        need to implement swing functionality
        need to implement a token neighbour function 
            -> token keeps track of neighbouring tokens and can flee or attack
        remember to delete the curent coordinate if it is back in possibleMoves bcoz of swingmove
        """
        possible_moves = moveGenerator(this.getCoordinate)
        possible_moves = boundaryChecker(possible_moves)
        possible_moves = blockChecker(possible_moves, blocked)
    


    def moveGenerator(coordinates):
        """
        creates moves, ignores boundaries/ other tokens...
        """
        r = coordinates[0]
        q = coordinates[1]

        possible_moves = []
        possible_moves.append((r+1,q-1), (r+1,q), (r,q+1), (r-1,q+1), (r-1,q), (r,q-1))

        return possible_moves

    def boundaryChecker(coordinatesList):
        """
        checks if token goes beyond limits
        """
        result_list = []
        for coordinates in coordinatesList:
            if boundaryCheck(coordinates):
                result_list.append(coordinates)
        return result_list
    

    def boundaryCheck(coordinates):
        """
        helper func for boundaryChecker
        """
        r, q = coordinates[0], coordinates[1]

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

    def blockChecker(boundaryCheckedMoves, blocked):
        
        result_list = []
        
        for coordinate in boundaryCheckedMoves:
            if coordinates not in blocked:
                result_list.append(coordinates) 
        
        return result_list
