import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QListWidgetItem, QWidget, QVBoxLayout, QLabel, QPushButton, QHBoxLayout, QFileDialog
from PyQt6.QtGui import QPixmap
from PyQt6 import uic

from Frontend.Mediador_UI_Cliente import Mediador_UI_Cliente


class ListItemWidget(QWidget):
	
	def __init__(self, name, dir_file , posicion , obj_mediador_ui_cliente ):
		super(ListItemWidget, self).__init__()

		layout = QVBoxLayout()
		self.setLayout(layout)
		
		self.posicion = posicion
		self.obj_mediador_ui_cliente = obj_mediador_ui_cliente

		self.name_label = QLabel(name)
		layout.addWidget(self.name_label)

		self.dir_file_label = QLabel(dir_file)
		layout.addWidget(self.dir_file_label)
		
		buttons_layout = QHBoxLayout()

		self.button1 = QPushButton("Borrar")
		self.button2 = QPushButton("Subir")
		self.button3 = QPushButton("Bajar")

		buttons_layout.addWidget(self.button1)
		buttons_layout.addWidget(self.button2)
		buttons_layout.addWidget(self.button3)

		layout.addLayout(buttons_layout)

		self.button1.clicked.connect( self.borrar_elemento )
		self.button2.clicked.connect( self.subir_item )
		self.button3.clicked.connect( self.bajar_item )

	def borrar_elemento( self ):
		self.obj_mediador_ui_cliente.borrar_elemento( self.posicion )

	def subir_item( self ):
		self.obj_mediador_ui_cliente.cambiar_posicion_elemento( self.posicion , self.posicion-1 )

	def bajar_item(self):
		self.obj_mediador_ui_cliente.cambiar_posicion_elemento( self.posicion , self.posicion+1 )

class MainWindow(QMainWindow):
	
	lista_elementosUI = []

	def __init__( self , obj_mediador_ui_cliente ):
		super(MainWindow, self).__init__()

		uic.loadUi(r"R:\\Proyecto_Un_Sistema_por_Semana\\Dia 0\\Sistema\\Frontend\\UI\\UI.ui", self)  

		#Referencia Mediador --->>>>>>>>>>>>
		self.obj_mediador_ui_cliente = obj_mediador_ui_cliente
		# ---------------------->>>>>>>>>>>>

		#Actions --------------->>>>>>>>>>>>
		self.button_agregar_item.clicked.connect( self.agregar_elemento )
		
		self.button_cargar_imagen.clicked.connect( self.open_file_dialog )
		
		self.button_mescla_random.clicked.connect( self.mescla_random )
		# ---------------------->>>>>>>>>>>>


	def agregar_elemento( self ):
		name = self.input_name_item.text() #Texto Name
		dir_file = self.label_path_imagen.text() #Texto Dir Path
		
		self.obj_mediador_ui_cliente.agregar_elemento( name , dir_file )


	def actualizar_data_UI( self , lista_elementosCliente ):
		
		self.lista_items.clear()

		for pos,data_item in enumerate(lista_elementosCliente):
			list_item_widget = ListItemWidget( data_item["nombre"] , data_item["imagen"] , pos , self.obj_mediador_ui_cliente )
			list_item = QListWidgetItem(self.lista_items)
			list_item.setSizeHint(list_item_widget.sizeHint())
			self.lista_items.addItem(list_item)
			self.lista_items.setItemWidget(list_item, list_item_widget)

	def mescla_random( self ):
		self.obj_mediador_ui_cliente.mescla_random()


	def subir_posicion_item( self ):
		pass

	def bajar_posicion_item( self ):
		pass

	def open_file_dialog(self):
		
		file_dialog = QFileDialog()
		file_path, _ = file_dialog.getOpenFileName(self, "Seleccionar archivo", "", "Todos los archivos (*.*)")
		
		# Mostrar la ruta del archivo seleccionado en el QLineEdit
		if file_path:
			self.label_path_imagen.setText(file_path)

def run_app( obj_main_window ):
	
	app = QApplication(sys.argv)
	obj_main_window.show()
	sys.exit(app.exec())