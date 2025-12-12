from app.PointSet import PointSet

class PointSetManager:
    storage: list[PointSet]

    def __init__(self) -> None:
        self.storage = list[PointSet]()

    def add(self, pointSet: PointSet) -> int:
        self.storage.append(pointSet)

        return len(self.storage) - 1
    
    def get(self, id: int) -> str|None:
        if (id < 0 or id > len(self.storage) - 1):
            raise KeyError()

        return self.storage[id].getBinary()
    
    def get_pointset(self, id: int) -> PointSet|None:
        if (id < 0 or id > len(self.storage) - 1):
            raise KeyError()

        return self.storage[id]