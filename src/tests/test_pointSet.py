from app import PointSet

class TestPointSet:
    def test_idempotence(self) -> bool:
        # nbPoints = 3
        # points = [[0.5, 0], [1, 0], [0, 1]]

        return False
    
    def test_binary_convertion(self) _> bool:
        nbPoints = 3
        points: list[list[float]] = [[0.5, 0], [1, 0], [0, 1]]

        encoding = PointSet(nbPoints, points) # Find error

        assert encoding.getBinary() == "00000000000000000000000000000011001111110000000000000000000000000000000000000000000000000000000000111111100000000000000000000000000000000000000000000000000000000000000000000000000000000000000000111111100000000000000000000000"

