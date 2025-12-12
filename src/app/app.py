from flask import Flask, abort, jsonify, render_template, request
import json

from app.PointSet import PointSet
from app.PointSetManager import PointSetManager
from app.Triangulation import Triangulation

app = Flask(__name__)

manager = PointSetManager()

@app.route('/')
def hello():
    return render_template('index.html')

@app.route('/api/manager/add', methods=['POST'])
def add_pointset_to_manager():
    data = request.get_json()
    nbPoints = int(data.get('nb')) if data.get('nb') is not None else None
    listString = data.get('list')
    listArray: list[int]

    if (nbPoints is None):
        return jsonify({
            'message': "nbPoint is missing",
        })

    if (nbPoints < 3):
        return jsonify({
            'message': "nbPoint has to be at least 3",
        })

    try:
        listArray = json.loads(str(listString))
    except json.JSONDecodeError:
        listArray = []

    if (len(listArray) != nbPoints * 2):
        return jsonify({
            'message': "list has to be of length nbPoint * 2",
        })

    pointSet = PointSet()
    pointSet.encode(nbPoints, listArray)

    manager.add(pointSet)

    return jsonify({
        'message': "Added new PointSet",
        'id': len(manager.storage) - 1
    })

@app.route('/api/manager/get/<id>')
def get_pointset_from_manager(id: int):    
    try:
        pointSet = manager.get_pointset(int(id))
        if pointSet is None:
            return jsonify({
                'message': "Invalid identifier"
            })
        if pointSet.binary is None:
            return jsonify({
                'message': "Invalid binary"
            })
        return jsonify({
            'message': 'Succeeded in getting PointSet',
            'binary': pointSet.binary
        })
    except KeyError:
        return jsonify({
            'message': "Invalid identifier"
        })

@app.route('/api/manager/readable/<id>')
def get_pointset_readable(id: int):    
    try:
        binary = manager.get(int(id))
        if binary is None:
            return jsonify({
                'message': "Invalid binary"
            })
        
        pointSet = PointSet()
        pointSet.binary = binary
        readable_data = pointSet.decode()
        
        return jsonify({
            'message': 'Succeeded in getting readable PointSet',
            'data': readable_data
        })
    except KeyError:
        return jsonify({
            'message': "Invalid identifier"
        })

@app.route('/api/triangulate/<id>')
def get_triangulation(id: int):    
    triang = Triangulation()
    triang.getPointsBinary = lambda point_id: manager.get(int(point_id))
    
    try:
        result = triang.triangulation(int(id))
        if result is None:
            return jsonify({
                'message': 'Not enough points for triangulation',
                'result': None
            })
        
        # Convert result to readable format
        pointSet = PointSet()
        readable_result = pointSet.decode_triangulation(result)
        
        return jsonify({
            'message': 'Triangulation successful',
            'result': readable_result
        })
    except Exception as e:
        return jsonify({
            'message': f'Triangulation error: {str(e)}',
            'result': None
        })

if __name__ == "__main__":
    app.debug