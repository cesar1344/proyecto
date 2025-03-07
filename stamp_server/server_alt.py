#import psycopg2
from flask import Flask, jsonify, request
from dotenv import load_dotenv
import os
from database_querys import sql_lista_de_comandos


load_dotenv()
# Parametros de conexión 
password = os.environ.get("PASS")
user = "postgres"
dbname =  "stamp_art_db"
host = "localhost" # la dirección IP de mi servidor
port = "5432" # puerto por defecto del postgreSQL
query = "SELECT * FROM usuario;"
#db_test = sql_lista_de_comandos(password, dbname, user, host, port, query)
#print(db_test)

app = Flask(__name__)
port = 5000

@app.route('/')
def hello():
    return ''' 
        el rey barbaro esta enojado 
        '''

@app.route('/info')
def page_data():
    return '''    
        Stamp Arts 
        '''

# GET/Users - obtención de todos los usuarios.
@app.route('/users', methods=['GET'])
def ver_usuarios():
    query = "SELECT * FROM usuario;"
    usuarios = sql_lista_de_comandos(password, dbname, user, host, port, query)
    if usuarios is None:
        return jsonify({"message": "No users found"}), 404
    # Convertir los resultados a un formato JSON amigable
    usuarios_list = []
    for usuario in usuarios:
        usuarios_list.append({
            "idusuario": usuarios[0],
            "nombre": usuarios[1],
            "correo": usuarios[2],
            "contrasenya": usuarios[3]  
        })
    return jsonify(usuarios), 200

#main
if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True, port=port)