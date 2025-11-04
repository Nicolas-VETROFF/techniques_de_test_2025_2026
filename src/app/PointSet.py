class PointSet:
    binary: bool

    # list[Point] plutot ?
    def __init__(self, nbPoints: int, pointList: list[list[int]]):
        raise NotImplementedError
        
    # list[Point] plutot ?
    def encode(self, nbPoints: int, pointList: list[list[int]]) -> None:
        raise NotImplementedError
    
    def decode(self) -> None: # return better type
        raise NotImplementedError
    
    def getBinary(self) -> str:
        raise NotImplementedError