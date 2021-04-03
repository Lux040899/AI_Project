from search.util import tokenOwner

class Token:
    """
    Token Class: helpful for creating tokens with specific and changeable attributes
    Token(Coordinate, tokenID, Player(derived), isActive(derived**))
    """
    def __init__(this, coordinate, tokenID):
        this.coordinate = coordinate
        this.tokenID = tokenID
        this.player = tokenOwner(this)

    
    def getCoordinate(this):
        return this.coordinate
    
    def getTokenID(this):
        return this.tokenID
    
    def getPlayer(this):
        return this.player
    
    def setCoordinate(this, coordinate):
        this.coordinate = coordinate
    
    def setTokenID(this, tokenID):
        this.tokenID = tokenID

    


