from app.Point import Point

class PointSet:
    binary: str

    # list[Point] plutot ?
    def __init__(self, nbPoints: int, pointList: list[Point]):
        raise NotImplementedError
        
    # list[Point] plutot ?
    def encode(self, nbPoints: int|None = None, pointList: list[(Point)]|None = None) -> None:
        raise NotImplementedError

    def getBinary(self) -> str:
        raise NotImplementedError