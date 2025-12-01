from app.PointSet import PointSet
from app.Point import Point

class TestPointSet:
    def test_binary_not_null(self) -> None:
        pointSet = PointSet(3, [Point(0, 0), Point(1, 0), Point(0, 1)])
        pointSet.encode()

        assert pointSet.getBinary() != None

    def test_binary_convertion(self) -> None:
        pointSet = PointSet(3, [Point(0, 0), Point(1, 0), Point(0, 1)])
        pointSet.encode()

        assert pointSet.getBinary() == ("" +
        "00000000000000000000000000000011" + # nbPoints
        "00111111000000000000000000000000" + # x1
        "00000000000000000000000000000000" + # y1
        "00111111100000000000000000000000" + # x2
        "00000000000000000000000000000000" + # y2
        "00000000000000000000000000000000" + # x3
        "00111111100000000000000000000000") # y3