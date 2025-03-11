import psycopg2
from dotenv import load_dotenv
import os


load_dotenv()
def sql_lista_de_comandos(password, db_name, user, host, port, query, params=None):
    connection = None
    try:
        # Establecer la conexión 
        connection = psycopg2.connect(
        dbname=dbname,
        user=user,
        password=password,
        host=host,
        port=port) 

        # crear un curso para realizar operaciones en la base de datos 
        with connection.cursor() as cursor:
            # Ejecutar la consulta con parametros si los hay 
            if params:
                cursor.execute(query,params)
            else:
                cursor.execute(query)
            # Manejo especifico para diferentes tipos de consultas 
            query_upper = query.strip().upper()
            
            if query_upper.startswith("SELECT"):
                # Para consultas SELECT
                query_data = cursor.fetchall()
                print("Datos de la consulta", query_data)
                return query_data
            
            elif query_upper.startwith("INSERT"):
                # Para consultas INSERT, especialmente con RETURING
                connection.commit()

                # Verficar si hay una clausula RETURING
                if "RETURNING" in query.upper():
                    return cursor.fetchone()
                return None
            
            else:
                # Para otros tipos de consultas (UPDATE, DELETE, etc.)
                connection.commit()
                return None
            
    except psycopg2.Error as error:
        # Manejo mas detallado de errores de PostgreSQL
        print(f"Error de postrgreSQL: {error}")
        if connection:
            connection.rollback()
        return None
    
    except Exception as error:
        # Captura de errores generales
        print(f"Error general:{error}")
        if connection:
            connection.rollback()
        return None    
                
    finally:
        #Asegurar cierre la conexión
        if connection:
            connection.close()
            print("Conexión cerrada")


# Parametros de conexión 
password = os.environ.get("PASS")
user = "postgres"
dbname =  "stamp_art_db"
host = "localhost" # o la dirección IP del servidor
port = "5432" # puerto por defecto de postgreSQL
query_simple = "SELECT * FROM usuario WHERE idusuario = 4;"
# Llamar a la función con user_id especifico
user_id = 8
#result = sql_lista_de_comandos(password, dbname, user, host, port, query_simple)


# Imprimir el resultado de la consulta 
#print("resultado de la consulta", result, "tipo:", type,(result))




