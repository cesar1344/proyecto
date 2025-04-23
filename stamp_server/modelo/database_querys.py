import psycopg2
from dotenv import load_dotenv
import os
load_dotenv()


class ConexionBaseDeDatos:
    def __init__(self):
        self.password = os.environ.get("DB_PASSWORD")
        self.dbname = os.environ.get("DB_NAME")
        self.user = os.environ.get("DB_USER")
        self.host = os.environ.get("DB_HOST")
        self.port = os.environ.get("DB_PORT")
    def sql_querys(self, query, params=None):
        connection = None
        try:
            # Establecer la conexión
            connection = psycopg2.connect(dbname=self.dbname, user=self.user, password=self.password, host=self.host, port=self.port)
            # Crear un cursor para realizar operaciones en la base de datos
            with connection.cursor() as cursor:
                # Ejecutar la consulta con parámetros si los hay
                if params:
                    cursor.execute(query, params)
                else:
                    cursor.execute(query)
                # Manejo específico para diferentes tipos de consultas
                query_upper = query.strip().upper()
                if query_upper.startswith("SELECT"):
                    # Para consultas SELECT
                    query_data = cursor.fetchall()
                    print("Datos de la consulta:", query_data)
                    return query_data
                elif query_upper.startswith("INSERT"):
                    # Para consultas INSERT, especialmente con RETURNING
                    connection.commit()
                    # Verificar si hay una cláusula RETURNING
                    if "RETURNING" in query.upper():
                        return cursor.fetchone()
                    return None
                elif query_upper.startswith("UPDATE"):
                    # Para consultas INSERT, especialmente con RETURNING
                    connection.commit()
                    # Verificar si hay una cláusula RETURNING
                    if "RETURNING" in query.upper():
                        return cursor.fetchone()
                    return None
                elif query_upper.startswith("DELETE"):
                    # Para consultas INSERT, especialmente con RETURNING
                    connection.commit()
                    # Verificar si hay una cláusula RETURNING
                    if "RETURNING" in query.upper():
                        return cursor.fetchone()
                    return None
                else:
                    # Para otros tipos de consultas (UPDATE, DELETE, etc.)
                    connection.commit()
                    return None
        except psycopg2.Error as error:
            # Manejo más detallado de errores de PostgreSQL
            print(f"Error de PostgreSQL: {error}")
            if connection:
                connection.rollback()
            return None
        except Exception as error:
            # Captura de errores generales
            print(f"Error general: {error}")
            if connection:
                connection.rollback()
            return None
        finally:
            # Asegurar cierre de la conexión
            if connection:
                connection.close()
                print("Conexión cerrada.")





