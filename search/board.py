

class Board:
    
    def __init__(this, upper, lower, blocked):
        this.upper = upper
        this.lower = lower
        this.blocked = blocked

    def start_game(this):
        queue = []
        visited = []
        predecssor = []

        visited.append(upper[0].getCoordinate)
        queue.append(upper[0].getCoordinate)
        predecssor.append((-100,-100))

        while queue:
            s = queue.pop(0) 
            print (s, end = " ") 

            for neighbour in s.getMoves(): #s.getmoves gives us the possible moves from a coordinate 
                if neighbour not in visited:
                    visited.append(neighbour)
                    queue.append(neighbour)
                
                
                #if neighbour in lower:
                    #delete that coordinate from lower.
                    #if lower length == 0
                    # brak;                    
                
                

