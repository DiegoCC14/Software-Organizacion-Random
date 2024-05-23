class Singleton_Meta_Observer(type):
	_instances = {}
	def __call__( cls , *args , **kwargs ):
		if cls not in cls._instances:
			instance = super().__call__(*args, **kwargs)
			cls._instances[cls] = instance
		return cls._instances[cls]

class Observer( metaclass=Singleton_Meta_Observer ):

	lista_clientes = []

	def __init__( self ):
		self.lista_clientes = []

	def notificando_cambios_a_clientes( self ):
		for obj_cliente in self.lista_clientes:
			try:
				obj_cliente.notificado_cambios_en_modelo()
			except:
				pass

	def agregar_cliente_observador( self , obj_cliente ):
		self.lista_clientes.append( obj_cliente )

	def eliminar_cliente_observador( self , obj_cliente ):
		for pos , obj_cliente_almacenado in self.lista_clientes:
			if obj_cliente_almacenado == obj_cliente:
				self.lista_clientes.pop( pos )

class Cliente_Prueba():

	def __init__( self ):
		pass

	def notificado_cambios_en_modelo( self ):
		print("Cliente Notificado")

if __name__ == "__main__":
	obj_oserver = Observer()

	obj_cliente = Cliente_Prueba()
	obj_cliente1 = Cliente_Prueba()
	obj_cliente2 = Cliente_Prueba()
	obj_cliente3 = Cliente_Prueba()
	
	obj_oserver.agregar_cliente_observador( obj_cliente )
	obj_oserver.agregar_cliente_observador( obj_cliente1 )
	obj_oserver.agregar_cliente_observador( obj_cliente2 )
	obj_oserver.agregar_cliente_observador( obj_cliente3 )

	obj_oserver = Observer()
	obj_oserver = Observer()
	print( obj_oserver.lista_clientes )

	#obj_oserver.notificando_cambios_a_clientes()
	