from flask import Flask, jsonify, request
from controlador import eventos

class ServerPages(eventos.UsuariosEventos):
    def __init__(self, app):
        super().__init__()
        self.app = app
        self.register_routes()
    # paginas de la API
    def register_routes(self):
        # register eser routes
        self.app.add_url_rule('/registro', 'registrar_usuario', self.registrar_usuario, methods=['POST'])
        self.app.add_url_rule('/login', 'login', self.login, methods=['POST'])
        self.app.add_url_rule('/cuenta', 'datos_de_la_cuenta', self.datos_de_la_cuenta, methods=['POST'])
        self.app.add_url_rule('/modificar', 'modificar_cuenta', self.modificar_cuenta, methods=['PUT'])
        self.app.add_url_rule('/eliminar', 'eliminar_cuenta', self.eliminar_cuenta, methods=['DELETE'])
        self.app.add_url_rule('/crear_camiseta', 'ruta_crear_camiseta', self.ruta_crear_camiseta, methods=['POST'])
        self.app.add_url_rule('/modificar_camiseta', 'ruta_modificar_camiseta', self.ruta_modificar_camiseta, methods=['PUT'])
        self.app.add_url_rule('/crear_un_pedido', 'ruta_crear_pedido', self.ruta_crear_pedido, methods=['POST'])
        self.app.add_url_rule('/consultar_transaccion', 'ruta_consultar_transaccion', self.ruta_consultar_transaccion, methods=['POST'])
        self.app.add_url_rule('/consultar_camiseta', 'ruta_consultar_camiseta', self.ruta_consultar_camiseta, methods=['POST'])
        self.app.add_url_rule('/modificar_producto', 'ruta_modificar_producto', self.ruta_modificar_producto, methods=['PUT'])
        self.app.add_url_rule('/eliminar_camiseta', 'ruta_eliminar_camiseta', self.ruta_eliminar_camiseta, methods=['DELETE'])







    def registrar_usuario(self):
        return self.eventos_resgistro()

    def login(self):
        return self.evento_login()

    def datos_de_la_cuenta(self):
        return self.consultar_cuenta()

    def modificar_cuenta(self):
        return self.cambiar_datos_cuenta()

    def eliminar_cuenta(self):
        return self.borrar_cuenta()
    
    def ruta_crear_camiseta(self):
        return self.crear_camiseta()
    
    def ruta_modificar_camiseta(self):
        return self.modificar_camiseta()

    def ruta_consultar_transaccion(self):
        return self.consultar_transaccion()
    
    def ruta_crear_pedido(self):
        return self.crear_pedido()
    

    def ruta_consultar_camiseta(self):
        return self.consultar_camisetas()


    def ruta_modificar_producto(self):
        return self.modificar_productos() 
    

    def ruta_eliminar_camiseta(self):
        return self.eliminar_camiseta()