from modelo import database_querys

db = database_querys.ConexionBaseDeDatos()

print(db.password, db.dbname, db.host, db.port, db.user)
db.sql_querys("SELECT * FROM usuario;")


