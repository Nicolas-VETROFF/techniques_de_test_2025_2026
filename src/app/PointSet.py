from app.Point import Point

class PointSet:
    binary: str

    # list[Point] plutot ?
    def __init__(self):
        raise NotImplementedError
        
    # list[Point] plutot ?
    def encode(self, nbPoints: int, pointList: list[Point]) -> None:
        raise NotImplementedError

    def getBinary(self) -> str:
        raise NotImplementedError