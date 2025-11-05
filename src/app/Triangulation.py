# Encode float : f"{struct.unpack('!L', struct.pack('!L', nbPoints))[0]:032b}"
# Decode to float :  f"{struct.unpack('!L', struct.pack('!f', point[0]))[0]:032b}" + f"{struct.unpack('!L', struct.pack('!f', point[1]))[0]:032b}"

class Triangulation:
    binary: str

    def __init__(self):
        raise NotImplementedError
        
    def encode(self, pointSetBinary: str) -> None:
        raise NotImplementedError
    
    def decode(self) -> object:
        raise NotImplementedError
    
    def decodeNbTriangle(self) -> int:
        raise NotImplementedError
    
    def decodePointCoordinates(self) -> object:
        raise NotImplementedError
    
    def triangulation(self, pointSetID: int) -> None:
        raise NotImplementedError
    
    def getBinary(self) -> str:
        raise NotImplementedError
    
    # Call API
    def getPointsBinary(self) -> str:
        raise NotImplementedError