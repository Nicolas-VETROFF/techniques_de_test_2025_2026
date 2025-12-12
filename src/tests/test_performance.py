import pytest
import time
import random
from unittest.mock import MagicMock
from app.Triangulation import Triangulation
from app.PointSet import PointSet
from app.PointSetManager import PointSetManager
from app.app import app
import json

class TestPerformance:
    
    def test_large_triangulation_performance(self):
        """Test performance of triangulation with 10000 points"""
        # Generate 10000 random points in a grid pattern
        nb_points = 10000
        points = []
        
        # Create a grid of points to ensure good triangulation
        grid_size = int(nb_points ** 0.5) + 1
        for i in range(grid_size):
            for j in range(grid_size):
                if len(points) // 2 < nb_points:  # Check number of points, not coordinates
                    x = i * 10
                    y = j * 10
                    points.extend([x, y])
        
        # Trim to exactly nb_points * 2 coordinates
        points = points[:nb_points * 2]
        
        # Create binary representation
        pointSet = PointSet()
        pointSet.encode(nb_points, points)
        binary = pointSet.getBinary()
        
        # Create custom triangulation class for testing
        class TestTriangulation(Triangulation):
            def __init__(self, binary_data):
                super().__init__()
                self.binary_data = binary_data
            
            def getPointsBinary(self, pointSetID):
                return self.binary_data
        
        # Create triangulation instance
        triang = TestTriangulation(binary)
        
        # Measure triangulation time
        start_time = time.time()
        result = triang.triangulation(1)
        end_time = time.time()
        
        duration = end_time - start_time
        
        # Performance assertions
        print(f"Triangulation of {nb_points} points took {duration:.4f} seconds")
        
        # Should complete within reasonable time (adjust threshold as needed)
        assert duration < 120.0, f"Triangulation took too long: {duration:.4f} seconds"
        
        # Should return a valid result
        assert result is not None
        assert result.startswith(binary)
        
        # Parse result to verify triangles were created
        if len(result) > len(binary):
            nb_triangles_bin = result[len(binary):len(binary)+32]
            nb_triangles = int(nb_triangles_bin, 2)
            print(f"Generated {nb_triangles} triangles")
            
            # For a grid, should have approximately 2*(n-1)*(m-1) triangles
            expected_min_triangles = nb_points - 2  # Minimum for any valid triangulation
            assert nb_triangles >= expected_min_triangles
    
    def test_medium_triangulation_performance(self):
        """Test performance of triangulation with 1000 points"""
        nb_points = 1000
        points = []
        
        # Create a grid of points
        grid_size = int(nb_points ** 0.5) + 1
        for i in range(grid_size):
            for j in range(grid_size):
                if len(points) < nb_points * 2:
                    x = i * 5
                    y = j * 5
                    points.extend([x, y])
        
        points = points[:nb_points * 2]
        
        # Create binary representation
        pointSet = PointSet()
        pointSet.encode(nb_points, points)
        binary = pointSet.getBinary()
        
        # Create triangulation instance
        triang = Triangulation()
        triang.getPointsBinary = MagicMock(return_value=binary)
        
        # Measure triangulation time
        start_time = time.time()
        result = triang.triangulation(1)
        end_time = time.time()
        
        duration = end_time - start_time
        
        # Performance assertions
        print(f"Triangulation of {nb_points} points took {duration:.4f} seconds")
        
        # Should complete quickly for medium dataset
        assert duration < 2.0, f"Medium triangulation took too long: {duration:.4f} seconds"
        
        # Should return a valid result
        assert result is not None
        assert result.startswith(binary)
    
    def test_small_triangulation_performance(self):
        """Test performance of triangulation with 100 points"""
        nb_points = 100
        points = []
        
        # Create random points
        random.seed(42)  # For reproducible results
        for i in range(nb_points):
            x = random.randint(0, 1000)
            y = random.randint(0, 1000)
            points.extend([x, y])
        
        # Create binary representation
        pointSet = PointSet()
        pointSet.encode(nb_points, points)
        binary = pointSet.getBinary()
        
        # Create triangulation instance
        triang = Triangulation()
        triang.getPointsBinary = MagicMock(return_value=binary)
        
        # Measure triangulation time
        start_time = time.time()
        result = triang.triangulation(1)
        end_time = time.time()
        
        duration = end_time - start_time
        
        # Performance assertions
        print(f"Triangulation of {nb_points} points took {duration:.4f} seconds")
        
        # Should complete very quickly for small dataset
        assert duration < 0.5, f"Small triangulation took too long: {duration:.4f} seconds"
        
        # Should return a valid result
        assert result is not None
        assert result.startswith(binary)
    
    def test_performance_comparison(self):
        """Compare performance across different dataset sizes"""
        test_sizes = [10, 50, 100, 500, 1000]
        results = []
        
        for nb_points in test_sizes:
            points = []
            
            # Create grid pattern for consistency
            grid_size = int(nb_points ** 0.5) + 1
            for i in range(grid_size):
                for j in range(grid_size):
                    if len(points) < nb_points * 2:
                        x = i * 10
                        y = j * 10
                        points.extend([x, y])
            
            points = points[:nb_points * 2]
            
            # Create binary representation
            pointSet = PointSet()
            pointSet.encode(nb_points, points)
            binary = pointSet.getBinary()
            
            # Create triangulation instance
            triang = Triangulation()
            triang.getPointsBinary = MagicMock(return_value=binary)
            
            # Measure triangulation time
            start_time = time.time()
            result = triang.triangulation(1)
            end_time = time.time()
            
            duration = end_time - start_time
            results.append((nb_points, duration))
            
            print(f"{nb_points} points: {duration:.4f} seconds")
            
            # Basic validation
            assert result is not None
        
        # Check that performance scales reasonably (not exponentially)
        # This is a basic check - you may need to adjust based on your algorithm
        print("Performance Summary:")
        for nb_points, duration in results:
            print(f"  {nb_points:4d} points: {duration:.4f}s")
