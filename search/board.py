

class Board:
    
    def __init__(this, upper, lower, blocked):
        this.upper = upper
        this.lower = lower
        this.blocked = blocked

    def getCoordinateList(this, tkns):
        crdnt_list = []
        for tkn in tkns:
            crdnt_list.append(tkn.getCoordinate())                

        return crdnt_list

    def startGame(this):
        queue = []
        visited = []
        predecessor = []

        lower_coordinates = this.getCoordinateList(this.lower)

        visited.append(this.upper[0].getCoordinate())
        queue.append(this.upper[0].getCoordinate())
        predecessor.append((-100,-100))

        while queue:
            s = queue.pop(0) 

            for neighbour in this.possibleMoves(s): #s.getmoves gives us the possible moves from a coordinate 
                if neighbour not in visited:
                    visited.append(neighbour)
                    queue.append(neighbour)
                    predecessor.append(s)
                
                
                if neighbour in lower_coordinates:
                    #delete that coordinate from lower.
                    print(visited)
                    print(predecessor)

                    lower_coordinates.remove(neighbour)
                    #if lower length == 0 break             
                    if len(lower_coordinates) == 0:
                        this.printPath(visited, predecessor)
                        return 0;      

    def printPath(this, visited, predecessor):

        path = [visited[-1]]
        prdscr = predecessor[-1]
        while(prdscr != (-100,-100)):
            path.insert(0, prdscr)
            #find index of prdscr in visited
            i = visited.index(prdscr)
            prdscr = predecessor[i]

        this.printOutput(path)
        
        return 0
                
    def printOutput(this, path):
        for i in range(len(path)-1):
            print(f"Turn {i+1}: SLIDE from {path[i]} to {path[i+1]}")

    def possibleMoves(this, s):
        
        """
        implement movement logic here?
        board logic for part 1...  will need to update for later
        need to implement swing functionality
        need to implement a token neighbour function 
            -> token keeps track of neighbouring tokens and can flee or attack
        remember to delete the curent coordinate if it is back in possibleMoves bcoz of swingmove
        """

        possible_moves = this.moveGenerator(s)
        possible_moves = this.boundaryChecker(possible_moves)
        possible_moves = this.blockChecker(possible_moves)

        return possible_moves
    


    def moveGenerator(this, coordinates):
        """
        creates moves, ignores boundaries/ other tokens...
        """
        r = coordinates[0]
        q = coordinates[1]
        
        possible_moves = [(r+1,q-1), (r+1,q), (r,q+1), (r-1,q+1), (r-1,q), (r,q-1)]
        return possible_moves

    def boundaryChecker(this, coordinatesList):
        """
        checks if token goes beyond limits
        """
        result_list = []
        for coordinates in coordinatesList:
            if this.boundaryCheck(coordinates):
                result_list.append(coordinates)
        return result_list
    

    def boundaryCheck(this, coordinates):
        """
        helper func for boundaryChecker
        """
        r, q = coordinates[0], coordinates[1]

        if (r > 4 or r < -4 or q > 4 or q < -4):
            return 0

        elif (r == 4) :
            return 1 if (q >= -4 and q <= 0) else 0
        elif (r == 3) :
            return 1 if (q >= -4 and q <= 1) else 0
        elif (r == 2) :
            return 1 if (q >= -4 and q <= 2) else 0
        elif (r == 1) :
            return 1 if (q >= -4 and q <= 3) else 0    
        elif (r == 0) :
            return 1 if (q >= -4 and q <= 4) else 0
        elif (r == -1) :
            return 1 if (q >= -3 and q <= 4) else 0
        elif (r == -2) :
            return 1 if (q >= -2 and q <= 4) else 0
        elif (r == -3) :
            return 1 if (q >= -1 and q <= 4) else 0
        elif (r == -4) :
            return 1 if (q >=  0 and q <= 4) else 0

    def blockChecker(this, boundaryCheckedMoves):
        
        result_list = []
        
        for coordinates in boundaryCheckedMoves:
            if coordinates not in this.blocked:
                result_list.append(coordinates) 
        
        return result_list
    
