from search.util import tokenOwner

class Token:
    """
    Token Class: helpful for creating tokens with specific and changeable attributes
    Token(Coordinate, tokenID, Player(derived), isActive(derived**))
    """
    def __init__(this, coordinate, tokenID, neighbour):
        this.coordinate = coordinate
        this.tokenID = tokenID
        this.player = tokenOwner(this)
        this.neighbour = []

    
    def getCoordinate(this):
        return this.coordinate
    
    def getTokenID(this):
        return this.tokenID
    
    def getPlayer(this):
        return this.player
    
    def getNeighbour(this):
        return this.neighbour
    
    def setCoordinate(this, coordinate):
        this.coordinate = coordinate
    
    def setTokenID(this, tokenID):
        this.tokenID = tokenID
    
    def setNeighbour(this, token):
        this.neighbour.append(token)
    
    def deleteNeighbour(this, token):
        this.neighbour.remove(token)

    


