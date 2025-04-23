from modelo import database_querys

class UsuariosConsultas(database_querys.ConexionBaseDeDatos):
    def __init__(self):
        super().__init__()
        #  Consultar los datos usuarios
        self.insertar_usuarios = "INSERT INTO usuario(nombre, correo, contrasenya) VALUES (%s, %s, %s) RETURNING *;"
        self.buscar_usuario = "SELECT idusuario, nombre FROM usuario WHERE nombre = %s AND contrasenya = %s;"
        self.usuario_ya_encontrado = "SELECT nombre, correo FROM usuario WHERE idusuario = %s;"
        self.modificar_datos_cuenta = "UPDATE usuario SET  nombre=%s, correo=%s, contrasenya=%s WHERE idusuario=%s;"
        self.eliminar_usuario = "UPDATE usuario SET estado = 'inactive' WHERE idusuario = %s;"
        self.verificar_nuevo_usuario = "SELECT COUNT(*) as existenz FROM usuario  WHERE nombre = %s AND correo = %s;"
        self.verificar_nombre_usuario = "SELECT COUNT(*) as existenz FROM usuario  WHERE nombre = %s;"
        self.verificar_correo_usuario = "SELECT COUNT(*) as existenz FROM usuario  WHERE correo = %s;"
        self.verificar_id_usuario = "SELECT COUNT(*) as existenz FROM usuario  WHERE idusuario = %s;"

    def verificar_usuario_por_correo_o_nombre(self, user_name, email):
        verification_existence = self.sql_querys(self.verificar_nuevo_usuario, params=(user_name, email, ))
        if verification_existence[0][0] == 0:
            return False
        else:
            return True
        
    def verificar_usuario_por_correo(self,  email):
        verification_existence = self.sql_querys(self.verificar_correo_usuario, params=( email,))
        print(verification_existence)
        if verification_existence[0][0] == 0:
            return False
        else:
            return True
        
    def verificar_usuario_por_nombre(self, user_name, ):
        verification_existence = self.sql_querys(self.verificar_nombre_usuario, params=(user_name,))
        if verification_existence[0][0] == 0:
            return False
        else:
            return True
        
    def verificar_usuario_por_id(self, id):
        verification_existence = self.sql_querys(self.verificar_id_usuario , params=(id,))
        if verification_existence[0][0] == 0:
            return False
        else:
            return True

    

    