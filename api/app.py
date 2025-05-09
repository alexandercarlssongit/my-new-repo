from flask import Flask, request, jsonify
from flask_restx import Api, Resource, fields
from datetime import datetime
import yaml
import os
import sys

# Add parent directory to path to import backend modules
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from backend.services.triangle_service import TriangleService
from backend.models.triangle_model import TriangleCalculation, init_db

# Load configuration
with open('config/config.yaml', 'r') as f:
    config = yaml.safe_load(f)

# Initialize Flask app
app = Flask(__name__)
api = Api(app, version='1.0', title='Triangle Calculator API',
          description='API for calculating triangle properties')

# Initialize database
db_session = init_db(f"mysql+pymysql://{config['database']['user']}:{config['database']['password']}@"
                    f"{config['database']['host']}:{config['database']['port']}/{config['database']['name']}")

# Define API models
triangle_input = api.model('TriangleInput', {
    'username': fields.String(required=True, description='Name of the user'),
    'side1': fields.Float(required=True, description='Length of first side'),
    'side2': fields.Float(required=True, description='Length of second side'),
    'side3': fields.Float(required=True, description='Length of third side')
})

triangle_output = api.model('TriangleOutput', {
    'is_triangle': fields.Boolean(description='Whether the inputs form a valid triangle'),
    'triangle_type': fields.String(description='Type of triangle'),
    'angles': fields.List(fields.Float, description='Angles of the triangle'),
    'area': fields.Float(description='Area of the triangle'),
    'perimeter': fields.Float(description='Perimeter of the triangle')
})

@api.route('/triangle')
class TriangleCalculator(Resource):
    @api.expect(triangle_input)
    @api.marshal_with(triangle_output)
    def post(self):
        data = request.json
        service = TriangleService()
        result = service.analyze_triangle(data['side1'], data['side2'], data['side3'])
        
        # Save to database
        calculation = TriangleCalculation(
            username=data['username'],
            side1=data['side1'],
            side2=data['side2'],
            side3=data['side3'],
            is_triangle=int(result.is_triangle),
            triangle_type=result.triangle_type,
            angle1=result.angles[0],
            angle2=result.angles[1],
            angle3=result.angles[2],
            area=result.area,
            perimeter=result.perimeter
        )
        db_session.add(calculation)
        db_session.commit()
        
        return {
            'is_triangle': result.is_triangle,
            'triangle_type': result.triangle_type,
            'angles': result.angles,
            'area': result.area,
            'perimeter': result.perimeter
        }

if __name__ == '__main__':
    app.run(host=config['server']['host'], port=config['server']['port']) 