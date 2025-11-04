class TestTriangulator:
    def test_triangulator_with_three_points(self):
        # Encode float : f"{struct.unpack('!L', struct.pack('!L', nbPoints))[0]:032b}"
        # Decode to float :  f"{struct.unpack('!L', struct.pack('!f', point[0]))[0]:032b}" + f"{struct.unpack('!L', struct.pack('!f', point[1]))[0]:032b}"
        
        binary = "00000000000000000000000000000011001111110000000000000000000000000000000000000000000000000000000000111111100000000000000000000000000000000000000000000000000000000000000000000000000000000000000000111111100000000000000000000000"

        triangles = Triangulation()

        # Test
        assert len(triangles) == 1