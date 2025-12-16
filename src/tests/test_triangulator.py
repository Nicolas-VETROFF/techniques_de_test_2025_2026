"""Test module for Triangulation class functionality."""

from unittest.mock import MagicMock

import pytest
from bitstring import BitArray

from app.Triangulation import Triangulation


class TestTriangulator:
    """Test cases for Triangulation class."""

    def test_triangulation_calls_encode_and_get_points(self):
        """Test that triangulation calls encode and get_points methods."""
        binary = ("" +
        BitArray(uint=3, length=32).bin +
        BitArray(uint=0, length=32).bin +
        BitArray(uint=0, length=32).bin +
        BitArray(uint=1, length=32).bin +
        BitArray(uint=0, length=32).bin +
        BitArray(uint=0, length=32).bin +
        BitArray(uint=1, length=32).bin)

        triang = Triangulation()
        triang.encode = MagicMock()
        triang.getPointsBinary = MagicMock(return_value=binary)

        triang.triangulation(1)

        triang.getPointsBinary.assert_called_once()
        triang.encode.assert_called_once()

    def test_triangulation_not_enough_points(self):
        """Test triangulation with insufficient points."""
        binary = ("" +
        BitArray(uint=2, length=32).bin +
        BitArray(uint=0, length=32).bin +
        BitArray(uint=0, length=32).bin +
        BitArray(uint=1, length=32).bin +
        BitArray(uint=1, length=32).bin)

        triang = Triangulation()
        triang.encode = MagicMock()
        triang.getPointsBinary = MagicMock(return_value=binary)

        result = triang.triangulation(1)

        # encode() ne doit PAS être appelé
        triang.encode.assert_not_called()
        assert result is None

    def test_triangulation_wrong_number_of_points(self):
        """Test triangulation with wrong number of points."""
        binary = ("" +
        BitArray(uint=4, length=32).bin +
        BitArray(uint=1, length=32).bin +
        BitArray(uint=0, length=32).bin +
        BitArray(uint=0, length=32).bin +
        BitArray(uint=0, length=32).bin +
        BitArray(uint=0, length=32).bin +
        BitArray(uint=1, length=32).bin)

        triang = Triangulation()
        triang.getPointsBinary = MagicMock(return_value=binary)

        with pytest.raises(Exception, match="Wrong number of points"):
            triang.triangulation(1)

    def test_idempotence(self):
        """Test that triangulation is idempotent."""
        binary = ("" +
        BitArray(uint=3, length=32).bin +
        BitArray(uint=1, length=32).bin +
        BitArray(uint=0, length=32).bin +
        BitArray(uint=1, length=32).bin +
        BitArray(uint=1, length=32).bin +
        BitArray(uint=0, length=32).bin +
        BitArray(uint=1, length=32).bin)

        triang = Triangulation()
        triang.getPointsBinary = MagicMock(return_value=binary)

        result = triang.triangulation(1)
        
        expected_triangles = [[0, 1, 2]]
        expected_result = triang.encode(binary, expected_triangles)
        
        assert result == expected_result

    def test_good_triangle_for_3_points(self):
        """Test triangulation of 3 valid points."""
        binary = ("" +
        BitArray(uint=3, length=32).bin +
        BitArray(uint=1, length=32).bin +
        BitArray(uint=0, length=32).bin +
        BitArray(uint=2, length=32).bin +
        BitArray(uint=0, length=32).bin +
        BitArray(uint=0, length=32).bin +
        BitArray(uint=2, length=32).bin)

        triang = Triangulation()
        triang.getPointsBinary = MagicMock(return_value=binary)

        result = triang.triangulation(1)

        assert result.startswith(binary)

        nb_triangles = int(result[len(binary):len(binary)+32], 2)
        assert nb_triangles == 1

        triangles_bin = result[len(binary)+32:]
        assert len(triangles_bin) == 96

    def test_colinear_points_give_zero_triangles(self):
        """Test that collinear points produce zero triangles."""
        # Trois points alignés
        binary = ("" +
        BitArray(uint=3, length=32).bin +
        BitArray(uint=0, length=32).bin +
        BitArray(uint=0, length=32).bin +
        BitArray(uint=1, length=32).bin +
        BitArray(uint=0, length=32).bin +
        BitArray(uint=2, length=32).bin +
        BitArray(uint=0, length=32).bin)
    
        triang = Triangulation()
        triang.getPointsBinary = MagicMock(return_value=binary)
    
        result = triang.triangulation(1)
    
        assert result.startswith(binary)
        
        if len(result) == len(binary):
            assert True
        else:
            nb_triangles_bin = result[len(binary):len(binary)+32]
            nb_triangles = int(nb_triangles_bin, 2)
            assert nb_triangles == 0

    def test_square_has_two_triangles(self):
        """Test that a square produces two triangles."""
        binary = ("" +
        BitArray(uint=4, length=32).bin +
        BitArray(uint=0, length=32).bin +
        BitArray(uint=0, length=32).bin +
        BitArray(uint=1, length=32).bin +
        BitArray(uint=0, length=32).bin +
        BitArray(uint=0, length=32).bin +
        BitArray(uint=1, length=32).bin +
        BitArray(uint=1, length=32).bin +
        BitArray(uint=1, length=32).bin)

        triang = Triangulation()
        triang.getPointsBinary = MagicMock(return_value=binary)

        result = triang.triangulation(1)

        assert result.startswith(binary)

        nb_tri = int(result[len(binary):len(binary)+32], 2)
        assert nb_tri == 2

        triangles_data = result[len(binary)+32:]
        assert len(triangles_data) == 2 * 96

    def test_unknown_pointset_should_raise(self):
        """Test that unknown point set raises appropriate exception."""
        triang = Triangulation()
        triang.getPointsBinary = MagicMock(return_value=None)

        with pytest.raises(Exception, match="Unknown pointset"):
            triang.triangulation(1)

    def test_corrupted_binary_should_raise(self):
        """Test that corrupted binary raises appropriate exception."""
        binary = BitArray(uint=1, length=32).bin + "01"  # tronqué

        triang = Triangulation()
        triang.getPointsBinary = MagicMock(return_value=binary)

        with pytest.raises(Exception, match="Corrupted binary"):
            triang.triangulation(1)