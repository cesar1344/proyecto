from modelo import database_querys
from modelo import usuarios_querys 

class DatosUsarios(usuarios_querys.UsuariosConsultas, database_querys.ConexionBaseDeDatos):
    def __init__(self):
        super().__init__()

    # crear un nuevo usuario
     
    def nuevo_usuario(self, nombre, correo, contrasenya):
        # verifacion de suario existente
        usuario_existe = True
        usuario_existe = self.verificar_usuario_por_correo_o_nombre(nombre, correo)
        # insertar un nuevo usuario
        if usuario_existe == False:
            params = (nombre, correo, contrasenya)
            return self.sql_querys(self.insertar_usuarios, params)
        else:
            return "El usuario ya existe"

    def usuario_login(self,user_name, password):
        return self.sql_querys(self.buscar_usuario, params=(user_name, password))
        
    def consultar_datos_de_usuario(self, idusuario):
        if idusuario != None:
            return self.sql_querys(self.usuario_ya_encontrado, params=(idusuario,))
        
    def modificar_datos_usuarios(self, usuarioid, nombre, email, password):
        return self.sql_querys(self.modificar_datos_cuenta, params=(nombre, email, password, usuarioid))
    
    def eliminar_datos_usuario(self, user_id):
        # verificar que el usuario exista
        user_exist = False
        user_exist = self.verificar_usuario_por_id(user_id)
        # elminar datos de usuario
        if user_exist == True:
            return self.sql_querys(self.eliminar_usuario, params=(user_id,))
        
