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

    
