
from .Observer import Observer
from .Lista_Elementos import Lista_Elementos

class Mediador():
	
	obj_observer = None
	obj_lista_elementos = None

	def __init__( self , obj_observer , obj_lista_elementos ):
		self.obj_observer = obj_observer
		self.obj_lista_elementos = obj_lista_elementos

	def notificar_cambios( self ):
		try:
			self.obj_observer.notificando_cambios_a_clientes()
		except Exception as error:
			print( error )

	def get_lista_elementos( self ):
		lista_elementos = []
		try:
			lista_elementos = self.obj_lista_elementos.get_lista_elementos()
		except Exception as error:
			print( error )
		return lista_elementos

	def agregar_elemento( self , nombre , path_imagen ):
		dicc_elemento = {}
		try:
			dicc_elemento = self.obj_lista_elementos.agregar_elemento( nombre , path_imagen )
			self.notificar_cambios()
		except Exception as error:
			print( error )
		return dicc_elemento

	def borrar_elemento( self , pos ):
		dicc_elemento = {}
		try:
			dicc_elemento = self.obj_lista_elementos.borrar_elemento( pos )
			self.notificar_cambios()
		except Exception as error:
			print( error )
		return dicc_elemento

	def cambiar_posicion_elemento( self , pos_actual , nueva_pos ):
		try:	
			self.obj_lista_elementos.cambiar_posicion_elemento( pos_actual , nueva_pos )
			self.notificar_cambios()
		except Exception as error :
			print( error )

	def mescla_random( self ):
		try:
			self.obj_lista_elementos.mescla_random()
			self.notificar_cambios()
		except Exception as error:
			print( error )


if __name__ == "__main__":
	obj_observador = Observer()
	obj_lista_elementos = Lista_Elementos()
	obj_mediador = Mediador( obj_observador , obj_lista_elementos )

	obj_mediador.agregar_elemento( "elemento_001" , "path_imagen 001" )
	obj_mediador.agregar_elemento( "elemento_002" , "path_imagen 002" )
	obj_mediador.agregar_elemento( "elemento_003" , "path_imagen 003" )
	obj_mediador.agregar_elemento( "elemento_004" , "path_imagen 004" )

	print( obj_mediador.get_lista_elementos() )
	
	obj_mediador.mescla_random( )

	print( obj_mediador.get_lista_elementos() )