import time
import random
from unittest.mock import MagicMock
from app.Triangulation import Triangulation
from app.PointSet import PointSet

class TestPerformance:
    
    def test_large_triangulation_performance(self):
        nb_points = 10000
        points = []
        
        grid_size = int(nb_points ** 0.5) + 1
        for i in range(grid_size):
            for j in range(grid_size):
                if len(points) // 2 < nb_points:
                    x = i * 10
                    y = j * 10
                    points.extend([x, y])
        
        points = points[:nb_points * 2]
        
        pointSet = PointSet()
        pointSet.encode(nb_points, points)
        binary = pointSet.getBinary()
        
        class TestTriangulation(Triangulation):
            def __init__(self, binary_data):
                super().__init__()
                self.binary_data = binary_data
            
            def getPointsBinary(self, pointSetID):
                return self.binary_data
        
        triang = TestTriangulation(binary)
        
        start_time = time.time()
        result = triang.triangulation(1)
        end_time = time.time()
        
        duration = end_time - start_time
        
        print(f"Triangulation of {nb_points} points took {duration:.4f} seconds")
        
        assert duration < 180.0, f"Triangulation took too long: {duration:.4f} seconds"
        
        assert result is not None
        assert result.startswith(binary)
        
        if len(result) > len(binary):
            nb_triangles_bin = result[len(binary):len(binary)+32]
            nb_triangles = int(nb_triangles_bin, 2)
            print(f"Generated {nb_triangles} triangles")
            
            expected_min_triangles = nb_points - 2
            assert nb_triangles >= expected_min_triangles
    
    def test_medium_triangulation_performance(self):
        nb_points = 1000
        points = []
        
        grid_size = int(nb_points ** 0.5) + 1
        for i in range(grid_size):
            for j in range(grid_size):
                if len(points) < nb_points * 2:
                    x = i * 5
                    y = j * 5
                    points.extend([x, y])
        
        points = points[:nb_points * 2]
        
        pointSet = PointSet()
        pointSet.encode(nb_points, points)
        binary = pointSet.getBinary()
        
        triang = Triangulation()
        triang.getPointsBinary = MagicMock(return_value=binary)
        
        start_time = time.time()
        result = triang.triangulation(1)
        end_time = time.time()
        
        duration = end_time - start_time
        
        print(f"Triangulation of {nb_points} points took {duration:.4f} seconds")
        
        assert duration < 3.0, f"Medium triangulation took too long: {duration:.4f} seconds"
        
        assert result is not None
        assert result.startswith(binary)
    
    def test_small_triangulation_performance(self):
        nb_points = 100
        points = []
        
        random.seed(42)  # For reproducible results
        for i in range(nb_points):
            x = random.randint(0, 1000)
            y = random.randint(0, 1000)
            points.extend([x, y])
        
        pointSet = PointSet()
        pointSet.encode(nb_points, points)
        binary = pointSet.getBinary()
        
        triang = Triangulation()
        triang.getPointsBinary = MagicMock(return_value=binary)
        
        start_time = time.time()
        result = triang.triangulation(1)
        end_time = time.time()
        
        duration = end_time - start_time
        
        print(f"Triangulation of {nb_points} points took {duration:.4f} seconds")
        
        assert duration < 0.5, f"Small triangulation took too long: {duration:.4f} seconds"
        
        assert result is not None
        assert result.startswith(binary)
    
    def test_performance_comparison(self):
        test_sizes = [10, 50, 100, 500, 1000]
        results = []
        
        for nb_points in test_sizes:
            points = []
            
            grid_size = int(nb_points ** 0.5) + 1
            for i in range(grid_size):
                for j in range(grid_size):
                    if len(points) < nb_points * 2:
                        x = i * 10
                        y = j * 10
                        points.extend([x, y])
            
            points = points[:nb_points * 2]
            
            pointSet = PointSet()
            pointSet.encode(nb_points, points)
            binary = pointSet.getBinary()
            
            triang = Triangulation()
            triang.getPointsBinary = MagicMock(return_value=binary)
            
            start_time = time.time()
            result = triang.triangulation(1)
            end_time = time.time()
            
            duration = end_time - start_time
            results.append((nb_points, duration))
            
            print(f"{nb_points} points: {duration:.4f} seconds")
            
            assert result is not None
        
        print("Performance Summary:")
        for nb_points, duration in results:
            print(f"  {nb_points:4d} points: {duration:.4f}s")
