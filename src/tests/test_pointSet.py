"""Test module for PointSet class functionality."""

from app.PointSet import PointSet

"""Test cases for PointSet class."""


class TestPointSet:
    """Test cases for PointSet class."""
    
    def test_binary_not_null(self) -> None:
        """Test that binary representation is not None after encoding."""
        pointSet = PointSet()
        pointSet.encode(3, [0, 0, 1, 0, 0, 1])

        assert pointSet.getBinary() is not None

    def test_binary_convertion(self) -> None:
        """Test binary conversion accuracy."""
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