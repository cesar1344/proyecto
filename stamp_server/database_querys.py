import psycopg2
from dotenv import load_dotenv
import os

def sql_lista_de_comandos(password, database_name, user, host, port, query, params=None):
    connection = None
    try:
        # Establecer la conexión 
        connection = psycopg2.connect
        dbname=database_name,
        user=user,
        password=password,
        host=host,
        port=port

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
                connection.comit()

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

