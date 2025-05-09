# Triangle Calculator

A web application that computes triangle properties and visualizes triangles based on user input.

## Features

- Input three side lengths to determine if they form a triangle
- Visual representation of the triangle
- Calculation of triangle properties:
  - Type (Equilateral, Isosceles, Scalene)
  - Angle measurements
  - Area
  - Perimeter
- Data persistence in MySQL database
- Logging of all calculations

## Technology Stack

- Frontend: Streamlit, Matplotlib
- API: Flask, OpenAPI 3.0
- Backend: Python
- Database: MySQL
- Logging: CSV files
- Testing: PyTest
- Deployment: Docker, Docker Compose

## Prerequisites

- Python 3.9 or higher
- Docker and Docker Compose
- MySQL (if running locally)

## Local Development Setup

1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd triangle-calculator
   ```

2. Create a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Set up the database:
   ```bash
   mysql -u root -p
   CREATE DATABASE triangle_db;
   ```

5. Run the application:
   ```bash
   # Terminal 1 - API
   python api/app.py

   # Terminal 2 - Frontend
   streamlit run frontend/app.py
   ```

## Docker Deployment

1. Build and start the containers:
   ```bash
   docker-compose up --build
   ```

2. Access the application:
   - Frontend: http://localhost:8501
   - API: http://localhost:5000
   - API Documentation: http://localhost:5000/api/v1

## Project Structure

```
.
├── api/
│   ├── app.py
│   └── requirements.txt
├── backend/
│   ├── models/
│   │   └── triangle_model.py
│   └── services/
│       └── triangle_service.py
├── frontend/
│   ├── app.py
│   └── requirements.txt
├── tests/
│   ├── unit/
│   └── integration/
├── config/
│   └── config.yaml
├── logs/
├── Dockerfile
├── docker-compose.yml
└── requirements.txt
```

## Configuration

The application can be configured through `config/config.yaml`. Key settings include:

- Server host and port
- Database connection details
- Logging configuration
- Frontend settings

## Testing

Run the test suite:
```bash
pytest tests/
```

## Logging

Logs are stored in the `logs` directory and include:
- Timestamp (UTC)
- Username
- Input values
- Calculation results

## Contributing

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push to the branch
5. Create a Pull Request

## License

This project is licensed under the MIT License - see the LICENSE file for details. 