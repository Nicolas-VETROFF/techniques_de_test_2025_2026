import pytest
from app.PointSetManager import PointSetManager
from app.PointSet import PointSet


class TestPointSetManager:

    def test_register_points_returns_id(self):
        pointSetManager = PointSetManager()
        pointSet = PointSet()
        pointSet.encode(3, [1, 1, 2, 2, 3, 3]) # PAS UNITAIRE

        pointSet_id = pointSetManager.add(pointSet)

        assert isinstance(pointSet_id, int)
        assert pointSet_id == 0
        assert pointSetManager.storage[pointSet_id].binary == pointSet.getBinary()

    def test_load_existing_pointset(self):
        pointSetManager = PointSetManager()
        pointSet = PointSet()
        pointSet.encode(3, [1, 0, 2, 0, 0, 2]) # PAS UNITAIRE
        
        pointSet_id = pointSetManager.add(pointSet)

        result = pointSetManager.get(pointSet_id)
        assert result == pointSet.getBinary()

    def test_load_unknown_pointset(self):
        pointSetManager = PointSetManager()
        with pytest.raises(KeyError):
            pointSetManager.get(1)