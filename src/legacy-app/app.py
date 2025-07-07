from flask import Flask
import psycopg2
import os

app = Flask(__name__)

def get_db_connection():
    """Conexion a postgresql"""
    return psycopg2.connect(
        host=os.getenv('DB_HOST', 'localhost'),
        database=os.getenv('DB_NAME', 'legacy_db'),
        user=os.getenv('DB_USER', 'postgres'),
        password=os.getenv('DB_PASSWORD', 'password')
    )

@app.route('/health')
def health():
    return {'status': 'ok'}

@app.route('/api/data')
def get_data():
    """Endpoint para obtener datos"""
    try:
        conn = get_db_connection()
        cur = conn.cursor()
        cur.execute('SELECT 1')
        result = cur.fetchone()
        cur.close()
        conn.close()
        return {'data': 'legacy app running', 'db_status': 'connected'}
    except Exception as e:
        return {'error': str(e)}, 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
