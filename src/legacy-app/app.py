from flask import Flask
import psycopg2
import os

app = Flask(__name__)

def get_db_connection():
    """conectando a postgresql"""
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
def obtener_datos():
    try:
        conexion = get_db_connection()
        cursor = conexion.cursor()
        cursor.execute('SELECT nombre FROM usuarios LIMIT 1')
        usuario = cursor.fetchone()
        cursor.close()
        conexion.close()
        return {'estado': 'ok', 'usuario': usuario[0] if usuario else 'ninguno'}
    except Exception as error:
        return {'error': str(error)}, 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
