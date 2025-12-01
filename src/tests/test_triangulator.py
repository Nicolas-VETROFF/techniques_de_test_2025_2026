import pytest
from unittest.mock import MagicMock
from app.Triangulation import Triangulation
from bitstring import BitArray

class TestTriangulator:

    def test_triangulation_calls_encode_and_get_points(self):
        binary = ""
        BitArray(uint=3, length=32).bin
        BitArray(uint=0, length=32).bin
        BitArray(uint=0, length=32).bin
        BitArray(uint=1, length=32).bin
        BitArray(uint=0, length=32).bin
        BitArray(uint=0, length=32).bin
        BitArray(uint=1, length=32).bin

        triang = Triangulation()
        triang.encode = MagicMock()
        triang.getPointsBinary = MagicMock(return_value=binary)

        triang.triangulation(1)

        triang.getPointsBinary.assert_called_once()
        triang.encode.assert_called_once()

    def test_triangulation_not_enough_points(self):
        binary = ""
        BitArray(uint=2, length=32).bin
        BitArray(uint=0, length=32).bin
        BitArray(uint=0, length=32).bin
        BitArray(uint=1, length=32).bin
        BitArray(uint=1, length=32).bin

        triang = Triangulation()
        triang.encode = MagicMock()
        triang.getPointsBinary = MagicMock(return_value=binary)

        result = triang.triangulation(1)

        # encode() ne doit PAS être appelé
        triang.encode.assert_not_called()
        assert result is None

    def test_triangulation_wrong_number_of_points(self):
        binary = ""
        BitArray(uint=4, length=32).bin
        BitArray(uint=1, length=32).bin
        BitArray(uint=0, length=32).bin
        BitArray(uint=0, length=32).bin
        BitArray(uint=0, length=32).bin
        BitArray(uint=0, length=32).bin
        BitArray(uint=1, length=32).bin

        triang = Triangulation()
        triang.getPointsBinary = MagicMock(return_value=binary)

        with pytest.raises(Exception):
            triang.triangulation(1)

    def test_idempotence(self):
        binary = ""
        BitArray(uint=3, length=32).bin
        BitArray(uint=1, length=32).bin
        BitArray(uint=0, length=32).bin
        BitArray(uint=1, length=32).bin
        BitArray(uint=1, length=32).bin
        BitArray(uint=0, length=32).bin
        BitArray(uint=1, length=32).bin

        triang = Triangulation()
        triang.getPointsBinary = MagicMock(return_value=binary)

        triang.encode(binary)
        result = triang.decode()

        assert result == binary

    def test_good_triangle_for_3_points(self):
        binary = ""
        BitArray(uint=3, length=32).bin
        BitArray(uint=1, length=32).bin
        BitArray(uint=0, length=32).bin
        BitArray(uint=2, length=32).bin
        BitArray(uint=0, length=32).bin
        BitArray(uint=0, length=32).bin
        BitArray(uint=2, length=32).bin

        triang = Triangulation()
        triang.getPointsBinary = MagicMock(return_value=binary)

        result = triang.triangulation(1)

        assert result.startswith(binary)

        nb_triangles = int(result[len(binary):len(binary)+32], 2)
        assert nb_triangles == 1

        triangles_bin = result[len(binary)+32:]
        assert len(triangles_bin) == 96

    def test_colinear_points_give_zero_triangles(self):
        # Trois points alignés
        binary = ""
        BitArray(uint=3, length=32).bin
        BitArray(uint=0, length=32).bin
        BitArray(uint=0, length=32).bin
        BitArray(uint=1, length=32).bin
        BitArray(uint=0, length=32).bin
        BitArray(uint=2, length=32).bin
        BitArray(uint=0, length=32).bin

        triang = Triangulation()
        triang.getPointsBinary = MagicMock(return_value=binary)

        result = triang.triangulation(1)

        assert result.startswith(binary)

        nb_triangles = int(result[len(binary):len(binary)+32], 2)
        assert nb_triangles == 0

    def test_square_has_two_triangles(self):

        binary = ""
        BitArray(uint=4, length=32).bin
        BitArray(uint=0, length=32).bin
        BitArray(uint=0, length=32).bin
        BitArray(uint=1, length=32).bin
        BitArray(uint=0, length=32).bin
        BitArray(uint=0, length=32).bin
        BitArray(uint=1, length=32).bin
        BitArray(uint=1, length=32).bin
        BitArray(uint=1, length=32).bin

        triang = Triangulation()
        triang.getPointsBinary = MagicMock(return_value=binary)

        result = triang.triangulation(1)

        assert result.startswith(binary)

        nb_tri = int(result[len(binary):len(binary)+32], 2)
        assert nb_tri == 2

        triangles_data = result[len(binary)+32:]
        assert len(triangles_data) == 2 * 96

    def test_unknown_pointset_should_raise(self):
        triang = Triangulation()
        triang.getPointsBinary = MagicMock(return_value=None)

        with pytest.raises(Exception):
            triang.triangulation(1)

    def test_corrupted_binary_should_raise(self):
        binary = BitArray(uint=1, length=32).bin + "01" # tronqué

        triang = Triangulation()
        triang.getPointsBinary = MagicMock(return_value=binary)

        with pytest.raises(Exception):
            triang.triangulation(1)