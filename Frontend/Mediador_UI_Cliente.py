
class Mediador_UI_Cliente():
	
	obj_mediador_backend = None
	obj_windows_ui = None
	lista_elementos = []

	def __init__( self , obj_mediador_backend ):
		self.obj_mediador_backend = obj_mediador_backend
		self.obj_windows_ui = None
		self.lista_elementos = []

	def add_window_ui( self , obj_windows_ui ):
		self.obj_windows_ui = obj_windows_ui

	def data_item_es_valido( self , name , dir_path ):
		name = name.replace(" ","")
		return len( name )>0

	def agregar_elemento( self , name , dir_path ):
		if self.data_item_es_valido( name , dir_path ) == True:
			self.obj_mediador_backend.agregar_elemento( name , dir_path )

	def actualizar_data_UI( self ):
		self.lista_elementos = self.obj_mediador_backend.get_lista_elementos()
		self.obj_windows_ui.actualizar_data_UI( self.lista_elementos )

	def notificado_cambios_en_modelo( self ):
		self.actualizar_data_UI()

	def mescla_random( self ):
		self.obj_mediador_backend.mescla_random()

	def borrar_elemento( self , pos ):
		self.obj_mediador_backend.borrar_elemento(pos)

	def cambiar_posicion_elemento( self , pos_actual , nueva_pos ):
		self.obj_mediador_backend.cambiar_posicion_elemento( pos_actual , nueva_pos )

if __name__ == "__main__":
	pass