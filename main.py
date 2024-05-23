from Backend.Mediador import Mediador
from Backend.Observer import Observer
from Backend.Lista_Elementos import Lista_Elementos

from Frontend.Mediador_UI_Cliente import Mediador_UI_Cliente
from Frontend.UI import run_app , MainWindow

from PyQt6.QtWidgets import QApplication
import sys

if __name__ == "__main__":
	
	# Backend --------------<<<<<<<>>>>>>>>>>>>
	obj_observer = Observer()
	obj_lista_elementos = Lista_Elementos()
	obj_Mediador = Mediador( obj_observer , obj_lista_elementos )
	# ----------------------<<<<<<>>>>>>>>>>>>>
	
	# Frontend --------------<<<<<<<>>>>>>>>>>>>
	
	app = QApplication(sys.argv)
	
	obj_mediador_ui_cliente = Mediador_UI_Cliente( obj_Mediador )
	obj_main_window = MainWindow( obj_mediador_ui_cliente )
	obj_mediador_ui_cliente.add_window_ui( obj_main_window )
	# ----------------------<<<<<<>>>>>>>>>>>>>
	
	# Lista_Observador -----<<<<<<<>>>>>>>>>>>
	obj_observer.agregar_cliente_observador( obj_mediador_ui_cliente )
	# ----------------------<<<<<<>>>>>>>>>>>>>
	
	obj_main_window.show()
	sys.exit(app.exec())