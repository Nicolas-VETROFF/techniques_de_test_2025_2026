"""PointSetManager module for managing collections of PointSet objects."""

from app.PointSet import PointSet


class PointSetManager:
    """A class to manage storage and retrieval of PointSet objects."""

    storage: list[PointSet]

    def __init__(self) -> None:
        """Initialize the PointSetManager with empty storage."""
        self.storage = list[PointSet]()

    def add(self, pointSet: PointSet) -> int:
        """Add a PointSet to storage.
        
        Args:
            pointSet: The PointSet object to add
            
        Returns:
            int: The ID assigned to the stored PointSet

        """
        self.storage.append(pointSet)

        return len(self.storage) - 1
    
    def get(self, id: int) -> str|None:
        """Get the binary representation of a stored PointSet.
        
        Args:
            id: The ID of the PointSet to retrieve
            
        Returns:
            str|None: Binary representation of the PointSet
            
        Raises:
            KeyError: If the ID is invalid

        """
        if (id < 0 or id > len(self.storage) - 1):
            raise KeyError()

        return self.storage[id].getBinary()
    
    def get_pointset(self, id: int) -> PointSet|None:
        """Get a stored PointSet object.
        
        Args:
            id: The ID of the PointSet to retrieve
            
        Returns:
            PointSet|None: The PointSet object
            
        Raises:
            KeyError: If the ID is invalid

        """
        if (id < 0 or id > len(self.storage) - 1):
            raise KeyError()

        return self.storage[id]