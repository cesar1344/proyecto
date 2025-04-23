from  controlador import productos
from controlador import usuarios
from flask import Flask, jsonify, request
class UsuariosEventos(productos.DatosProductos, usuarios.DatosUsarios):
    def __init__(self):
        super().__init__()

    def eventos_resgistro(self):
        datos_usuarios = request.get_json() 
        nombre = datos_usuarios.get('nombre') 
        correo = datos_usuarios.get('correo') 
        contrasenya = datos_usuarios.get('contrasenya') 
        if nombre != None and contrasenya != None and correo != None:
            return self.nuevo_usuario(nombre, correo, contrasenya)
        

    def evento_login(self):
        datos_usuarios = request.get_json() 
        nombre = datos_usuarios.get('nombre') 
        contrasenya = datos_usuarios.get('contrasenya') 
        if nombre != None and contrasenya != None:
            return jsonify(self.usuario_login(nombre, contrasenya))


    def consultar_cuenta(self):
        idusuario = request.args.get('idusuario')
        return jsonify(self.consultar_datos_de_usuario(idusuario))        
    
    def cambiar_datos_cuenta(self):
        datos_usuarios = request.get_json() 
        nombre = datos_usuarios.get('nombre') 
        idusuario= datos_usuarios.get('idusuario') 
        email= datos_usuarios.get('email') 
        contrasenya = datos_usuarios.get('contrasenya') 
        if nombre != None and contrasenya != None and email != None and idusuario != None:
            print('mod',self.modificar_datos_usuarios(idusuario, nombre, email, contrasenya))
            return jsonify(self.modificar_datos_usuarios(idusuario, nombre, email, contrasenya))

    def borrar_cuenta(self):
        dato = request.get_json() 
        idusuario = dato.get('idusuario') 
        return jsonify(self.eliminar_datos_usuario(idusuario))
    
    def crear_camiseta(self):
        datos_camiseta = request.get_json() 
        nombre = datos_camiseta.get('nombre') 
        descripcion= datos_camiseta.get('descripcion') 
        usuarioid = datos_camiseta.get('usuarioid')
        return jsonify(self.generar_producto(nombre, descripcion, usuarioid))
      

    def modificar_camiseta(self):
        datos_camiseta = request.get_json() 
        nombre = datos_camiseta.get('nombre') 
        precio = datos_camiseta.get('precio')
        imagen = datos_camiseta.get('imagen') 
        usuarioid= datos_camiseta.get('usuarioid')
        return jsonify(self.modificar_datos_de_un_producto(nombre, precio, imagen, usuarioid))
      

    def crear_pedido(self):
        datos_pedido = request.get_json() 
        fecha= datos_pedido.get('fecha') 
        estado_pedido= datos_pedido.get('estado_pedido') 
        usuarioid= datos_pedido.get('usuarioid')
        return jsonify(self.generar_pedido(fecha, estado_pedido, usuarioid))
      

    def consultar_transaccion(self):
        datos_pedido = request.get_json() 
        usuarioid= datos_pedido.get('usuarioid')
        return jsonify(self.consultar_pedido(usuarioid))
      

    
    def consultar_camisetas(self):
        datos_pedido = request.get_json() 
        productosid= datos_pedido.get('productoid')
        return jsonify(self.consultar_producto(productosid))
      

    def modificar_un_producto(self):
        datos_productos = request.get_json() 
        nombre= datos_productos.get('nombre') 
        precio= datos_productos.get('precio') 
        imagen= datos_productos.get('imagen')
        id = datos_productos.get('id')
        return jsonify(self.modificar_producto(nombre, precio, imagen,id))
    

    def eliminar_camiseta(self):
        datos_pedido = request.get_json() 
        productosid= datos_pedido.get('productoid')
        return jsonify(self.eliminando_producto(productosid))
      
 
      
