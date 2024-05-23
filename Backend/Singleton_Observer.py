
from Observer import Observer

class SingletonMeta(type):
	
	_instances = {}

	def __call__( cls , *args , **kwargs ):

		if cls not in cls._instances:
			instance = super().__call__(*args, **kwargs)
			cls._instances[cls] = instance
		return cls._instances[cls]

class Singleton_Observer( metaclass=SingletonMeta ):

	

	def __init__( self ):
		self.instance = None

	def get_instance( self ):
		pass
		if self.instance == None:
			self.instance = Observer

		return self.instance

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

	obj_oserver.notificando_cambios_a_clientes()
