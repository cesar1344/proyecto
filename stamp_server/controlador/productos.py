from modelo import database_querys
from modelo import productos_querys

class DatosProductos(productos_querys.ProductosConsultas, database_querys.ConexionBaseDeDatos):
    def __init__(self):
        super().__init__()


    def generar_producto(self, nombredisenyo, descripcion, usuarioid):
        return self.sql_querys(self.creacion_disenyos, params=(nombredisenyo, descripcion, usuarioid))
    
    def modificar_producto(self, nombredisenyo, descripcion, disenyoid):
        return self.sql_querys(self.modificar_disenyos, params=(nombredisenyo, descripcion,disenyoid))


    def generar_pedido(self, fechaPedido, estadoPedido, usuarioid):
        return self.sql_querys(self.nuevo_pedido, params=(fechaPedido, estadoPedido, usuarioid))
    

    def consultar_pedido(self,idpedido):
        return self.sql_querys(self.datos_pedidos, params=(idpedido,))

    def consultar_producto(self,idproducto):
        return self.sql_querys(self.mostrar_datos_productos, params=(idproducto,))
    
    def modificar_datos_de_un_producto(self,nombre, precio, imagen, id):
        return self.sql_querys(self.modificar_productos, params=(nombre, precio, imagen, id))

    def eliminar_producto(self, id):
        return self.sql_querys(self.eliminando_producto, params=(id,))



