"""PointSet module for encoding and decoding point data."""

from bitstring import BitArray


class PointSet:
    """A class to manage point sets with binary encoding and decoding."""

    binary: str|None = None

    def encode(self, nbPoints: int, pointList: list[int]):
        """Encode points into binary format.
        
        Args:
            nbPoints: Number of points to encode
            pointList: List of coordinates [x1, y1, x2, y2, ...]
            
        Returns:
            str: Error message if encoding fails, None otherwise

        """
        if nbPoints * 2 != len(pointList):
            return "Failed to create PointSet : nbPoints != pointList"
        
        self.binary = BitArray(uint=nbPoints, length=32).bin

        for point in pointList:
            self.binary += BitArray(uint=point, length=32).bin

    def getBinary(self) -> str|None:
        """Get the binary representation of the point set.
        
        Returns:
            str|None: Binary string or None if not encoded

        """
        return self.binary
    
    def decode(self) -> dict:
        """Decode binary data back to point coordinates.
        
        Returns:
            dict: Dictionary with 'nbPoints' and 'points' keys

        """
        if self.binary is None or len(self.binary) < 32:
            return {}
        
        # Extract number of points from first 32 bits
        nb_points_bits = self.binary[:32]
        nb_points = int(nb_points_bits, 2)
        
        # Extract points
        points = []
        for i in range(nb_points):
            start = 32 + i * 64
            x_bits = self.binary[start:start+32]
            y_bits = self.binary[start+32:start+64]
            
            x = int(x_bits, 2)
            y = int(y_bits, 2)
            points.append([x, y])
        
        return {
            'nbPoints': nb_points,
            'points': points
        }
    
    def decode_triangulation(self, binary_with_triangulation: str) -> dict:
        """Decode binary data including triangulation information.
        
        Args:
            binary_with_triangulation: Binary string containing points and triangles
            
        Returns:
            dict: Dictionary with points and triangulation data

        """
        if len(binary_with_triangulation) < 32:
            return {}
        
        # Extract number of points from first 32 bits
        nb_points_bits = binary_with_triangulation[:32]
        nb_points = int(nb_points_bits, 2)
        
        # Calculate expected point data length
        point_data_length = 32 + nb_points * 64
        
        if len(binary_with_triangulation) < point_data_length:
            return {}
        
        # Extract points
        points = []
        for i in range(nb_points):
            start = 32 + i * 64
            x_bits = binary_with_triangulation[start:start+32]
            y_bits = binary_with_triangulation[start+32:start+64]
            
            x = int(x_bits, 2)
            y = int(y_bits, 2)
            points.append([x, y])
        
        result = {
            'nbPoints': nb_points,
            'points': points,
            'nbTriangles': 0,
            'triangles': []
        }
        
        # Extract triangulation data if present
        if len(binary_with_triangulation) > point_data_length:
            # Extract number of triangles (next 32 bits)
            nb_triangles_bits = binary_with_triangulation[
                point_data_length:point_data_length+32
            ]
            nb_triangles = int(nb_triangles_bits, 2)
            
            # Extract triangle indices
            triangles = []
            triangle_data_start = point_data_length + 32
            for i in range(nb_triangles):
                triangle_start = (
                    triangle_data_start + i * 96  # 3 indices * 32 bits each
                )
                p1_bits = binary_with_triangulation[triangle_start:triangle_start+32]
                p2_bits = binary_with_triangulation[triangle_start+32:triangle_start+64]
                p3_bits = binary_with_triangulation[triangle_start+64:triangle_start+96]
                
                p1 = int(p1_bits, 2)
                p2 = int(p2_bits, 2)
                p3 = int(p3_bits, 2)
                triangles.append([p1, p2, p3])
            
            result['nbTriangles'] = nb_triangles
            result['triangles'] = triangles
        
        return result