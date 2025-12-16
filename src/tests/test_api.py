import json
from app.app import app
from app.PointSet import PointSet

class TestApi:
    
    def setup_method(self):
        self.app = app.test_client()
        self.app.testing = True
        from app.app import manager
        manager.__init__()  # Reset manager storage
    
    def test_add_pointset_success(self):
        data = {
            'nb': 3,
            'list': [0, 0, 1, 0, 0, 1]
        }
        response = self.app.post('/api/manager/add', 
                               data=json.dumps(data),
                               content_type='application/json')
        
        assert response.status_code == 200
        response_data = json.loads(response.data)
        assert response_data['message'] == "Added new PointSet"
        assert response_data['id'] == 0
    
    def test_add_pointset_missing_nb(self):
        data = {
            'list': [0, 0, 1, 0, 0, 1]
        }
        response = self.app.post('/api/manager/add', 
                               data=json.dumps(data),
                               content_type='application/json')
        
        assert response.status_code == 200
        response_data = json.loads(response.data)
        assert response_data['message'] == "nbPoint is missing"
    
    def test_add_pointset_insufficient_points(self):
        data = {
            'nb': 2,
            'list': [0, 0, 1, 0]
        }
        response = self.app.post('/api/manager/add', 
                               data=json.dumps(data),
                               content_type='application/json')
        
        assert response.status_code == 200
        response_data = json.loads(response.data)
        assert response_data['message'] == "nbPoint has to be at least 3"
    
    def test_add_pointset_wrong_list_length(self):
        data = {
            'nb': 3,
            'list': [0, 0, 1, 0]
        }
        response = self.app.post('/api/manager/add', 
                               data=json.dumps(data),
                               content_type='application/json')
        
        assert response.status_code == 200
        response_data = json.loads(response.data)
        assert response_data['message'] == "list has to be of length nbPoint * 2"
    
    def test_add_pointset_invalid_json_list(self):
        data = {
            'nb': 3,
            'list': 'invalid_json'
        }
        response = self.app.post('/api/manager/add', 
                               data=json.dumps(data),
                               content_type='application/json')
        
        assert response.status_code == 200
        response_data = json.loads(response.data)
        assert response_data['message'] == "list has to be of length nbPoint * 2"
    
    def test_get_pointset_success(self):
        data = {
            'nb': 3,
            'list': [0, 0, 1, 0, 0, 1]
        }
        self.app.post('/api/manager/add', 
                      data=json.dumps(data),
                      content_type='application/json')
        
        response = self.app.get('/api/manager/get/0')
        
        assert response.status_code == 200
        response_data = json.loads(response.data)
        assert response_data['message'] == 'Succeeded in getting PointSet'
        assert 'binary' in response_data
        assert response_data['binary'] is not None
    
    def test_get_pointset_invalid_id(self):
        response = self.app.get('/api/manager/get/999')
        
        assert response.status_code == 200
        response_data = json.loads(response.data)
        assert response_data['message'] == "Invalid identifier"
    
    def test_get_pointset_none_binary(self):
        from app.app import manager
        pointSet = PointSet()
        pointSet.binary = None
        manager.storage.append(pointSet)
        
        response = self.app.get('/api/manager/get/0')
        
        assert response.status_code == 200
        response_data = json.loads(response.data)
        assert response_data['message'] == "Invalid binary"
    
    def test_triangulate_success(self):
        data = {
            'nb': 3,
            'list': [0, 0, 1, 0, 0, 1]
        }
        self.app.post('/api/manager/add', 
                      data=json.dumps(data),
                      content_type='application/json')
        
        response = self.app.get('/api/triangulate/0')
        
        assert response.status_code == 200
        response_data = json.loads(response.data)
        assert response_data['message'] == 'Triangulation successful'
        assert 'result' in response_data
        assert response_data['result'] is not None
    
    def test_triangulate_insufficient_points(self):
        from app.app import manager
        pointSet = PointSet()
        pointSet.encode(2, [0, 0, 1, 0])
        manager.storage.append(pointSet)
        
        response = self.app.get('/api/triangulate/0')
        
        assert response.status_code == 200
        response_data = json.loads(response.data)
        assert response_data['message'] == 'Not enough points for triangulation'
        assert response_data['result'] is None
    
    def test_triangulate_invalid_id(self):
        response = self.app.get('/api/triangulate/999')
        
        assert response.status_code == 200
        response_data = json.loads(response.data)
        assert 'Triangulation error' in response_data['message']
        assert response_data['result'] is None
    
    def test_triangulate_collinear_points(self):
        data = {
            'nb': 3,
            'list': [0, 0, 1, 0, 2, 0]
        }
        self.app.post('/api/manager/add', 
                      data=json.dumps(data),
                      content_type='application/json')
        
        response = self.app.get('/api/triangulate/0')
        
        assert response.status_code == 200
        response_data = json.loads(response.data)
        assert response_data['message'] == 'Triangulation successful'
        assert response_data['result'] is not None
    
    def test_homepage_endpoint(self):
        response = self.app.get('/')
        
        assert response.status_code == 200
        assert b'<!DOCTYPE html>' in response.data
        assert b'Ajouter' in response.data
        assert b'Voir' in response.data
        assert b'Trianguler' in response.data