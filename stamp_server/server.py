from flask import Flask
from flask_cors import CORS
from rutas import las_rutas


app = Flask(__name__)
CORS(app)
port = 8888
server_pages = las_rutas.ServerPages(app)


#main
if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True, port=port)
