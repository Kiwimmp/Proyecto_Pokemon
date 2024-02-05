import sys, os
from images import *
from PySide6 import QtWidgets
from PySide6.QtUiTools import QUiLoader

class MainWindow(QtWidgets.QMainWindow):

    def __init__(self):

        super(MainWindow, self).__init__()
        loader = QUiLoader()
        
        self.main_screen = loader.load(os.path.join(os.path.dirname(__file__), "NovaLogin.ui"), self)
        self.screen_login = loader.load(os.path.join(os.path.dirname(__file__), "pantalla_registro.ui"), self)
        self.screen_game = loader.load(os.path.join(os.path.dirname(__file__), "seleccion_partida.ui"), self)
        self.battle_screen = loader.load(os.path.join(os.path.dirname(__file__), "pantalla_lucha_definitiva.ui"), self)
        self.battle_screen_team = loader.load(os.path.join(os.path.dirname(__file__), "pantalla_cambiar_pokemon.ui"), self)
        self.team_edit = loader.load(os.path.join(os.path.dirname(__file__), "Edicion_equipo.ui"), self)
        self.team_choose = loader.load(os.path.join(os.path.dirname(__file__), "Eleccion_equipo.ui"), self)

        self.stack = QtWidgets.QStackedWidget(self)
        self.stack.addWidget(self.main_screen)
        self.stack.addWidget(self.screen_login)
        self.stack.addWidget(self.screen_game)
        self.stack.addWidget(self.battle_screen)
        self.stack.addWidget(self.battle_screen_team)
        self.stack.addWidget(self.team_edit)
        self.stack.addWidget(self.team_choose)

        self.setCentralWidget(self.stack)

        self.main_screen.Acceder.clicked.connect(self.cambio_pantalla_partida)
        self.main_screen.Registrarse.clicked.connect(self.cambio_pantalla_registro)

        self.screen_login.AccederLogin.clicked.connect(self.registrarse_login)
        self.screen_login.Cancelar.clicked.connect(self.cancelar_registro)

        self.screen_game.partidaRapida.clicked.connect(self.partida_rapida)
        self.screen_game.team.clicked.connect(self.team_edit_screen)
        self.screen_game.ladder.clicked.connect(self.ir_ladder)
        self.screen_game.cerrarSesion.clicked.connect(self.cerrar_sesion)

        self.team_edit.volverLobby.clicked.connect(self.volver_lobby)

        self.team_choose.cambiarEquipo.clicked.connect(self.camb_equipo)
        self.team_choose.empezarJugar.clicked.connect(self.ir_jugar)
        self.team_choose.volverInicio.clicked.connect(self.volver_inicio)
        


        self.battle_screen.Mochila.clicked.connect(self.cambio_equipo_batalla)
        self.battle_screen.abandonar.clicked.connect(self.abandonar)

        self.battle_screen_team.Mochila2.clicked.connect(self.volver_cambio_equipo)
        self.battle_screen_team.abandonar2.clicked.connect(self.abandonar2)

    def abandonar2(self):
        self.stack.setCurrentIndex(2)
        
    def abandonar(self):
        self.stack.setCurrentIndex(2)

    def cerrar_sesion(self):
        self.stack.setCurrentIndex(0)

    def volver_inicio(self):
        self.stack.setCurrentIndex(2)

    def ir_jugar(self):
        self.stack.setCurrentIndex(3)

    def camb_equipo(self):
        self.stack.setCurrentIndex(5)

    def cambio_pantalla_partida(self):
        self.stack.setCurrentIndex(2)
    
    def cambio_pantalla_registro(self):
        self.stack.setCurrentIndex(1)
    
    def registrarse_login(self):
        self.stack.setCurrentIndex(0)
    
    def cancelar_registro(self):
        self.stack.setCurrentIndex(0)
    
    def partida_rapida(self):
        self.stack.setCurrentIndex(3)
    
    def cambio_equipo_batalla(self):
        self.stack.setCurrentIndex(4)
    
    def team_edit_screen(self):
        self.stack.setCurrentIndex(5)
    
    def volver_cambio_equipo(self):
        self.stack.setCurrentIndex(3)
    
    def volver_lobby(self):
        self.stack.setCurrentIndex(2)

    def ir_ladder(self):
        self.stack.setCurrentIndex(6)


def main():

    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()