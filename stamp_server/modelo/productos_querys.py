from modelo import database_querys

class ProductosConsultas(database_querys.ConexionBaseDeDatos):
    def __init__(self):
        super().__init__()
        # cosultar los productos
        self.creacion_disenyos = "INSERT INTO disenyo(nombredisenyo, descripcion, usuarioid) VALUES (%s, %s, %s);"
        self.modificar_disenyos = "UPDATE disenyo SET nombredisenyo=%s, descripcion=%s, WHERE iddisenyo=%s RETURNING *;"
        self.nuevo_pedido = "INSERT INTO pedido(fechaPedido, estadoPedido, usuarioid VALUES (%s, %s, %s);"
        self.datos_pedidos = "SELECT fechapedido, estadopedido FROM pedido WHERE idpedido = %s;"
        self.mostrar_datos_productos = "SELECT nombreproducto, precio, imagen FROM idproducto = %s;"
        self.modificar_productos = "UPDATE producto SET  nombreproducto=%s, precio=%s, imagen=%s WHERE idproducto = %s RETURNING *;"
        self.eliminando_producto = "DELETE FROM producto WHERE idproducto=%s RETURNING *;"