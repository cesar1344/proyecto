import psycopg2
from flask import Flask, jsonify, request
from dotenv import load_dotenv
import os
from database_querys import sql_lista_de_comandos

load_dotenv()
# Parametros de conexión 
password_sql = os.environ.get("PASS")
user_sql = "postgres"
dbname_sql =  "stamp_art_db"
host_sql = "localhost" # la dirección IP de mi servidor
port_sql = "5432" # puerto por defecto del postgreSQL
query = "SELECT * FROM usuario;"
#db_test = sql_lista_de_comandos(password_sql, dbname, user_sql, host_sql, port_sql, query)
#print(db_test)

app = Flask(__name__)
port = 8888

@app.route('/')
def hello():
    return '''    
    el rey barbaro esta enojado 
    '''

@app.route('/info')
def info():
    return '''    
    Stamp Arts 
    '''

# GET/Users - obtención de todos los usuarios.
@app.route('/users', methods=['GET'])
def get_users():
    query = "SELECT * FROM usuario;"
    usuario = sql_lista_de_comandos(password_sql, dbname_sql, user_sql, host_sql, port_sql, query)
    if usuario is None:
        return jsonify({"message": "No users found"}), 404
    '''
    <h1>Lista de usuarios</h1>
        <table>
            <tr>
                <th>ID</th>
                <th>Nombres de usuario</th>
                <th>Email></th>
                <th>Contraseña</th>
            </tr>
            {% for user in usuario %}
            <tr>
                <td>{{ user[0] }}</td>
                <td>{{ user[1] }}</td>
                <td>{{ user[2] }}</td>
                <td>{{ user[4] }}</td>
            </tr>
                {% endfor %}
        </table>
    '''
    return jsonify(usuario), 200

# GET/Users - obtención de todos los usuarios.
@app.route('/users/<int:usuario_id>', methods=['GET'])
def get_one_user(usuario_id):
    query = "SELECT * FROM usuario WHERE idusuario = %s;"
    usuario = sql_lista_de_comandos(password_sql, dbname_sql, user_sql, host_sql, port_sql, (usuario_id,))
    if usuario is None or len(usuario):
        return jsonify({"message": "No users found"}), 404
    '''
    <h1>Lista de usuarios</h1>
        <table>
            <tr>
                <th>ID</th>
                <th>Nombres de usuario</th>
                <th>Email></th>
                <th>Contraseña</th>
            </tr>
            {% for user in usuario %}
            <tr>
                <td>{{ user[0] }}</td>
                <td>{{ user[1] }}</td>
                <td>{{ user[2] }}</td>
                <td>{{ user[4] }}</td>
            </tr>
                {% endfor %}
        </table>
    '''
    return jsonify(usuario), 200


#main
if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True, port=port)
