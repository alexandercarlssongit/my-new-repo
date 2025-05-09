import os
import sys

def create_directory_structure():
    # Root directories
    directories = [
        'frontend',
        'api',
        'backend',
        'data',
        'tests',
        'config',
        'logs'
    ]
    
    # Create root directories
    for directory in directories:
        os.makedirs(directory, exist_ok=True)
        
    # Create subdirectories and files
    structure = {
        'frontend': {
            'templates': {},
            'static': {
                'css': {},
                'js': {},
                'images': {}
            }
        },
        'api': {
            'routes': {},
            'schemas': {}
        },
        'backend': {
            'models': {},
            'services': {}
        },
        'data': {
            'database': {}
        },
        'tests': {
            'unit': {},
            'integration': {}
        },
        'config': {},
        'logs': {}
    }
    
    # Create the structure
    for root, subdirs in structure.items():
        for subdir, _ in subdirs.items():
            os.makedirs(os.path.join(root, subdir), exist_ok=True)
            
    # Create initial files
    files_to_create = {
        'requirements.txt': '',
        'frontend/requirements.txt': '',
        'api/requirements.txt': '',
        'backend/requirements.txt': '',
        'tests/requirements.txt': '',
        'config/config.yaml': '',
        'docker-compose.yml': '',
        'Dockerfile': '',
        'README.md': '',
        '.gitignore': ''
    }
    
    for file_path, content in files_to_create.items():
        with open(file_path, 'w') as f:
            f.write(content)

if __name__ == '__main__':
    create_directory_structure()
    print("Project structure created successfully!") 