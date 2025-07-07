import requests
from flask import Flask
import os

app = Flask(__name__)

LEGACY_API_URL = os.getenv('LEGACY_API_URL', 'http://legacy-app:5000')

@app.route('/health')
def health():
    return {'status': 'ok', 'service': 'microservice'}

@app.route('/api/status')
def get_status():
    """obtener estado del microservicio"""
    try:
        response = requests.get(f'{LEGACY_API_URL}/api/data', timeout=5)
        legacy_data = response.json()
        return {
            'microservice_status': 'running',
            'legacy_connection': 'ok',
            'legacy_data': legacy_data
        }
    except Exception as e:
        return {
            'microservice_status': 'running',
            'legacy_connection': 'error',
            'error': str(e)
        }, 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)
