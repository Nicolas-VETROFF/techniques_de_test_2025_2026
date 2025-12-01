import pytest
from app.Point import Point
from app.PointSetManager import PointSetManager
from app.PointSet import PointSet


class TestPointSetManager:

    def test_register_points_returns_id(self):
        psm = PointSetManager()
        ps = PointSet(3, [Point(1, 1), Point(2, 2), Point(3, 3)])

        ps_id = psm.add(ps)

        assert isinstance(ps_id, int)
        assert ps_id == 1  # premier ID attendu
        assert psm.storage[ps_id] == ps.getBinary()

    def test_load_existing_pointset(self):
        psm = PointSetManager()
        ps = PointSet(3, [Point(1, 0), Point(2, 0), Point(0, 2)])
        ps_id = psm.add(ps)

        result = psm.get(ps_id)
        assert result == ps.getBinary()

    def test_load_unknown_pointset(self):
        psm = PointSetManager()
        with pytest.raises(KeyError):
            psm.get(1)