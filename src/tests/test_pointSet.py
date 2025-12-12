from app.PointSet import PointSet

class TestPointSet:
    def test_binary_not_null(self) -> None:
        pointSet = PointSet()
        pointSet.encode(3, [0, 0, 1, 0, 0, 1])

        assert pointSet.getBinary() != None

    def test_binary_convertion(self) -> None:
        pointSet = PointSet()
        pointSet.encode(3, [0, 0, 1, 0, 0, 1])

        assert pointSet.getBinary() == (
        "00000000000000000000000000000011" +
        "00000000000000000000000000000000" +
        "00000000000000000000000000000000" +
        "00000000000000000000000000000001" +
        "00000000000000000000000000000000" +
        "00000000000000000000000000000000" +
        "00000000000000000000000000000001")