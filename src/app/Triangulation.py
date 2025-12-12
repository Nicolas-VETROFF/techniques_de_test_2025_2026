from typing import List, Tuple, Optional

class Triangulation:
    def encode(self, pointSetBinary: str, triangulatedPoints: List[List[int]]) -> str:
        """Encode triangulation result back to binary format"""
        if not triangulatedPoints:
            return pointSetBinary
        
        # Add number of triangles as 32-bit binary
        nb_triangles = len(triangulatedPoints)
        nb_triangles_bin = f"{nb_triangles:032b}"
        
        # Add triangle data (each triangle has 3 point indices)
        triangles_bin = ""
        for triangle in triangulatedPoints:
            for point_index in triangle:
                triangles_bin += f"{point_index:032b}"
        
        return pointSetBinary + nb_triangles_bin + triangles_bin
    
    def triangulation(self, pointSetID: int) -> Optional[str]:
        """Main triangulation method using Delaunay algorithm"""
        binary = self.getPointsBinary(pointSetID)
        
        if binary is None:
            raise Exception("Unknown pointset")
        
        if len(binary) < 32:
            raise Exception("Corrupted binary")
        
        # Parse number of points from first 32 bits
        nb_points_bits = binary[:32]
        nb_points = int(nb_points_bits, 2)
        
        # Check if binary length matches expected format
        expected_length = 32 + nb_points * 64
        if len(binary) < expected_length:
            raise Exception("Corrupted binary")
        elif len(binary) != expected_length:
            raise Exception("Wrong number of points")
        
        # Check if we have enough points for triangulation
        if nb_points < 3:
            return None
        
        # Extract points from binary
        points = self._extract_points_from_binary(binary, nb_points)
        
        # Check if points are collinear
        if self._are_points_collinear(points):
            triangles = []
        else:
            # Use Delaunay triangulation
            triangles = self._delaunay_triangulation(points)
        
        return self.encode(binary, triangles)
    
    def getPointsBinary(self, id: int) -> Optional[str]:
        """API call to get binary data - will be mocked in endpoint"""
        return ''
    
    def _extract_points_from_binary(self, binary: str, nb_points: int) -> List[Tuple[int, int]]:
        """Extract points from binary string"""
        points = []
        for i in range(nb_points):
            # Each point has 2 coordinates, each 32 bits
            start = 32 + i * 64
            x_bits = binary[start:start+32]
            y_bits = binary[start+32:start+64]
            
            x = int(x_bits, 2)
            y = int(y_bits, 2)
            points.append((x, y))
        
        return points
    
    def _are_points_collinear(self, points: List[Tuple[int, int]]) -> bool:
        """Check if all points are collinear"""
        if len(points) < 3:
            return True
        
        # Calculate area of triangle formed by first 3 points
        (x1, y1), (x2, y2), (x3, y3) = points[0], points[1], points[2]
        area = x1 * (y2 - y3) + x2 * (y3 - y1) + x3 * (y1 - y2)
        
        if area != 0:
            return False
        
        # Check remaining points
        for i in range(3, len(points)):
            xi, yi = points[i]
            # Check if point lies on the line formed by first two points
            if (yi - y1) * (x2 - x1) != (y2 - y1) * (xi - x1):
                return False
        
        return True
    
    def _delaunay_triangulation(self, points: List[Tuple[int, int]]) -> List[List[int]]:
        """Delaunay triangulation using Bowyer-Watson algorithm"""
        if len(points) < 3:
            return []
        
        if len(points) == 3:
            return [[0, 1, 2]]
        
        # Create super-triangle
        super_triangle = self._create_super_triangle(points)
        triangles = [(len(points), len(points) + 1, len(points) + 2)]
        
        # Add super-triangle vertices to points list
        extended_points = points + [super_triangle[0], super_triangle[1], super_triangle[2]]
        
        # Add points one by one
        for i, point in enumerate(points):
            bad_triangles = []
            
            # Find triangles whose circumcircle contains the point
            for triangle in triangles:
                if self._point_in_circumcircle(point, triangle, extended_points):
                    bad_triangles.append(triangle)
            
            # Find boundary of bad triangles
            polygon = []
            for triangle in bad_triangles:
                for edge in self._triangle_edges(triangle):
                    if not self._edge_shared_by_triangles(edge, bad_triangles):
                        polygon.append(edge)
            
            # Remove bad triangles
            for triangle in bad_triangles:
                triangles.remove(triangle)
            
            # Create new triangles from polygon edges and current point
            for edge in polygon:
                new_triangle = (edge[0], edge[1], i)
                triangles.append(new_triangle)
        
        # Remove triangles that contain super-triangle vertices
        final_triangles = []
        for triangle in triangles:
            if not any(vertex >= len(points) for vertex in triangle):
                final_triangles.append(list(triangle))
        
        return final_triangles
    
    def _create_super_triangle(self, points: List[Tuple[int, int]]) -> List[Tuple[int, int]]:
        """Create a super-triangle that contains all points"""
        if not points:
            return []
        
        # Find bounding box
        min_x = min(p[0] for p in points)
        max_x = max(p[0] for p in points)
        min_y = min(p[1] for p in points)
        max_y = max(p[1] for p in points)
        
        # Create large triangle
        dx = max_x - min_x
        dy = max_y - min_y
        max_dim = max(dx, dy)
        
        mid_x = (min_x + max_x) / 2
        mid_y = (min_y + max_y) / 2
        
        # Super-triangle vertices
        p1 = (mid_x - 2 * max_dim, mid_y - max_dim)
        p2 = (mid_x, mid_y + 2 * max_dim)
        p3 = (mid_x + 2 * max_dim, mid_y - max_dim)
        
        return [p1, p2, p3]
    
    def _point_in_circumcircle(self, point: Tuple[int, int], triangle: Tuple[int, int, int], 
                              points: List[Tuple[int, int]]) -> bool:
        """Check if point is inside circumcircle of triangle"""
        try:
            p1 = points[triangle[0]]
            p2 = points[triangle[1]]
            p3 = points[triangle[2]]
        except IndexError:
            return False
        
        # Calculate circumcircle
        ax, ay = p1
        bx, by = p2
        cx, cy = p3
        
        # Calculate circumcenter using perpendicular bisectors
        d = 2 * (ax * (by - cy) + bx * (cy - ay) + cx * (ay - by))
        if abs(d) < 1e-10:
            return False  # Degenerate triangle
        
        ux = ((ax**2 + ay**2) * (by - cy) + (bx**2 + by**2) * (cy - ay) + (cx**2 + cy**2) * (ay - by)) / d
        uy = ((ax**2 + ay**2) * (cx - bx) + (bx**2 + by**2) * (ax - cx) + (cx**2 + cy**2) * (bx - ax)) / d
        
        # Check if point is inside circumcircle
        px, py = point
        dist_sq = (px - ux)**2 + (py - uy)**2
        r_sq = (ax - ux)**2 + (ay - uy)**2
        
        return dist_sq < r_sq - 1e-10  # Small epsilon for numerical stability
    
    def _triangle_edges(self, triangle: Tuple[int, int, int]) -> List[Tuple[int, int]]:
        """Get all edges of a triangle"""
        return [(triangle[0], triangle[1]), (triangle[1], triangle[2]), (triangle[2], triangle[0])]
    
    def _edge_shared_by_triangles(self, edge: Tuple[int, int], triangles: List[Tuple[int, int, int]]) -> bool:
        """Check if edge is shared by multiple triangles in the list"""
        count = 0
        for triangle in triangles:
            edges = self._triangle_edges(triangle)
            if edge in edges or (edge[1], edge[0]) in edges:
                count += 1
                if count > 1:
                    return True
        return False