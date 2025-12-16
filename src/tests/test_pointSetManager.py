"""Test module for PointSetManager class functionality."""

import pytest

from app.PointSet import PointSet
from app.PointSetManager import PointSetManager


class TestPointSetManager:
    """Test cases for PointSetManager class."""

    def test_register_points_returns_id(self):
        """Test that registering points returns a valid ID."""
        pointSetManager = PointSetManager()
        pointSet = PointSet()
        pointSet.encode(3, [1, 1, 2, 2, 3, 3])  # PAS UNITAIRE

        pointSet_id = pointSetManager.add(pointSet)

        assert isinstance(pointSet_id, int)
        assert pointSet_id == 0
        assert pointSetManager.storage[pointSet_id].binary == pointSet.getBinary()

    def test_load_existing_pointset(self):
        """Test loading an existing point set by ID."""
        pointSetManager = PointSetManager()
        pointSet = PointSet()
        pointSet.encode(3, [1, 0, 2, 0, 0, 2])  # PAS UNITAIRE
        
        pointSet_id = pointSetManager.add(pointSet)

        result = pointSetManager.get(pointSet_id)
        assert result == pointSet.getBinary()

    def test_load_unknown_pointset(self):
        """Test that loading unknown point set raises KeyError."""
        pointSetManager = PointSetManager()
        with pytest.raises(KeyError):
            pointSetManager.get(1)