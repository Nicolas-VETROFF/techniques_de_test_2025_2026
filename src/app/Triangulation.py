# Encode float : f"{struct.unpack('!L', struct.pack('!L', nbPoints))[0]:032b}"
# Decode to float :  f"{struct.unpack('!L', struct.pack('!f', point[0]))[0]:032b}" + f"{struct.unpack('!L', struct.pack('!f', point[1]))[0]:032b}"

class Triangulation:
    binary: str

    def __init__(self):
        pass
        
    def encode(self, pointSetBinary: str):
        pass
    
    def decode(self):
        pass
    
    def decodeNbTriangle(self):
        pass
    
    def decodePointCoordinates(self):
        pass
    
    def triangulation(self, pointSetID: int) -> str:
        return ''
    
    def getBinary(self):
        pass
    
    # Call API
    def getPointsBinary(self):
        pass