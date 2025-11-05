from app.Triangulation import Triangulation
from unittest.mock import MagicMock

class TestTriangulator:

    def test_triangulation_func_call(self):
        binary = ""
        "00000000000000000000000000000011" # nbPoints
        "00111111000000000000000000000000" # x1
        "00000000000000000000000000000000" # y1
        "00111111100000000000000000000000" # x2
        "00000000000000000000000000000000" # y2
        "00000000000000000000000000000000" # x3
        "00111111100000000000000000000000" # y3

        triangulation = Triangulation()
        triangulation.encode = MagicMock()
        triangulation.getPointsBinary = MagicMock() # Mock API Call
        triangulation.getPointsBinary.return_value = binary

        triangulation.triangulation(1)

        # Testing if func called when correct binary
        assert triangulation.encode.assert_called_once()
        assert triangulation.getPointsBinary.assert_called_once()

    # Ex: Only 2 points
    def test_triangulation_with_not_enough_points(self):
        binary = ""
        "00000000000000000000000000000010" # nbPoints
        "00111111000000000000000000000000" # x1
        "00000000000000000000000000000000" # y1
        "00111111100000000000000000000000" # x2
        "00000000000000000000000000000000" # y2

        triangulation = Triangulation()
        triangulation.encode = MagicMock()
        triangulation.getPointsBinary = MagicMock() # Mock API Call
        triangulation.getPointsBinary.return_value = binary

        triangulation.triangulation(1)

        # Testing if correct binary
        assert triangulation.encode.assert_not_called()
    
    # Ex: 3 points but 4 coordinates
    def test_triangulation_with_wrong_nb_of_points(self):
        pass

    def test_idempotence(self) -> None:
        binary: str = ""
        "00000000000000000000000000000011" # nbPoints
        "00111111000000000000000000000000" # x1
        "00000000000000000000000000000000" # y1
        "00111111100000000000000000000000" # x2
        "00000000000000000000000000000000" # y2
        "00000000000000000000000000000000" # x3
        "00111111100000000000000000000000" # y3

        triangulation = Triangulation()
        triangulation.encode(binary)
        # varTest = triangulation.decode()
        
        assert False

        