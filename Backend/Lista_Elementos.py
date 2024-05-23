import random
import copy

class Lista_Elementos():
	
	lista_elementos = []

	def __init__( self ):
		self.lista_elementos = []

	def get_lista_elementos( self ):
		return self.copy_deep_lista_elementos()

	def agregar_elemento( self , nombre , path_img ):
		dicc_elemento = { "nombre":str(nombre) , "imagen":str(path_img) }
		self.lista_elementos.append( dicc_elemento )
		return dicc_elemento

	def borrar_elemento( self , pos ):
		dicc_elemento = self.lista_elementos.pop( pos )
		return dicc_elemento

	def cambiar_posicion_elemento( self , pos_actual , nueva_pos ):
		if len( self.lista_elementos ) > 0 and pos_actual>0 and nueva_pos>=0:
			
			# Validamos que las posiciones sean validas sino Error por Pos--->>>
			self.lista_elementos[pos_actual]
			self.lista_elementos[nueva_pos]
			# --------------------------------------------------------------->>>
			
			new_lista = []
			dicc_elemento = self.lista_elementos.pop( pos_actual )
			dicc_ingresado = False
			for pos , elemento in enumerate( self.lista_elementos ):
				if pos == nueva_pos:
					new_lista.append( dicc_elemento )
					dicc_ingresado = True
				new_lista.append( elemento )
			if dicc_ingresado == False:
				new_lista.append( dicc_elemento )

			self.lista_elementos = new_lista

	def mescla_random( self ):
		for pos , dicc_elemento in enumerate(self.lista_elementos):
			nueva_pos = random.randint( 0 , len(self.lista_elementos)-1 )
			self.cambiar_posicion_elemento( pos , nueva_pos )

	def copy_deep_lista_elementos( self ):
		list_dicc_elementos = []
		for dicc_element in self.lista_elementos:
			list_dicc_elementos.append( copy.deepcopy(dicc_element) )
		
		return list_dicc_elementos


if __name__ == "__main__":

	obj_lista_elementos = Lista_Elementos()

	obj_lista_elementos.agregar_elemento( "nombre" , "path_img" )

	print( obj_lista_elementos.agregar_elemento( "item1" , "path_img1" ) )

	print( obj_lista_elementos.agregar_elemento( "item2" , "path_img2" ) )

	print( obj_lista_elementos.get_lista_elementos() )

	#obj_lista_elementos.borrar_elemento( 1 )

	#print( obj_lista_elementos.get_lista_elementos() )

	#obj_lista_elementos.cambiar_posicion_elemento( 0 , 2 )

	#for x in range(20):
	#	obj_lista_elementos.mescla_random()
	
	#lista_elementos_copia = obj_lista_elementos.copy_deep_lista_elementos()

	print( obj_lista_elementos.get_lista_elementos() )