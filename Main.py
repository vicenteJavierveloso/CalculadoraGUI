import sys
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QMainWindow, QPushButton, QLineEdit, QGridLayout, QApplication, QWidget, QVBoxLayout, QHBoxLayout, QLabel

class Calculadora(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Calculadora")
        #Botones numericos
        #Lista con botones numericos
        botones = []
        for i in range(10):
            botones.append(QPushButton(f"{i}"))
        print(botones)
        #ACciones botones numericos
        botones[0].clicked.connect(lambda: self.numeros("0"))
        botones[1].clicked.connect(lambda: self.numeros("1"))
        botones[2].clicked.connect(lambda: self.numeros("2"))
        botones[3].clicked.connect(lambda: self.numeros("3"))
        botones[4].clicked.connect(lambda: self.numeros("4"))
        botones[5].clicked.connect(lambda: self.numeros("5"))
        botones[6].clicked.connect(lambda: self.numeros("6"))
        botones[7].clicked.connect(lambda: self.numeros("7"))
        botones[8].clicked.connect(lambda: self.numeros("8"))
        botones[9].clicked.connect(lambda: self.numeros("9"))
        #Visor
        #Editor en modo solo lectura para crear un string
        self.visor = QLineEdit()
        #Alineo el texto a la derecha para que se vea mejor
        self.visor.setAlignment(Qt.AlignmentFlag.AlignRight)
        self.visor.setReadOnly(True)
        #operaciones
        self.b_multiplicar = QPushButton("*")
        self.b_dividir = QPushButton("/")
        self.b_sumar = QPushButton("+")
        self.b_restar = QPushButton("-")
        self.b_resultado = QPushButton("=")
        #Acciones botones operaciones
        self.b_multiplicar.clicked.connect(lambda: self.creador_operacion("*"))
        self.b_dividir.clicked.connect(lambda: self.creador_operacion("/"))
        self.b_sumar.clicked.connect(lambda: self.creador_operacion("+"))
        self.b_restar.clicked.connect(lambda: self.creador_operacion("-"))

        self.b_resultado.clicked.connect(lambda: self.resultado(self.visor.text()))
        #Contenedores
        caja_aun_mayor = QVBoxLayout()
        caja_aun_mayor.addWidget(self.visor)

        caja_mayor = QHBoxLayout()

        caja_operaciones = QVBoxLayout()

        caja_operaciones.addWidget(self.b_multiplicar)
        caja_operaciones.addWidget(self.b_dividir)
        caja_operaciones.addWidget(self.b_restar)
        caja_operaciones.addWidget(self.b_sumar)
        caja_operaciones.addWidget(self.b_resultado)

        caja_numeros = QGridLayout()
        #boton 0 en fila 3
        caja_numeros.addWidget(botones[0],3,1)
        #fila 2
        columna = 0
        for i in range(1,4):
            columna += 1
            caja_numeros.addWidget(botones[i],2,columna)
        #fila 1
        columna = 0
        for i in range(4,7):
            columna += 1
            caja_numeros.addWidget(botones[i],1,columna)
        #fila 0
        columna = 0
        for i in range(7,10):
            columna += 1
            caja_numeros.addWidget(botones[i],0,columna)
        caja_mayor.addLayout(caja_numeros)
        caja_mayor.addLayout(caja_operaciones)
        caja_aun_mayor.addLayout(caja_mayor)

        contenedor = QWidget()
        contenedor.setLayout(caja_aun_mayor)
        self.setCentralWidget(contenedor)
    
    def numeros(self, argumento):
        #Inserto numeros al visor
        self.visor.insert(argumento)

    def creador_operacion(self, argumento):
        #Añado al visor la operacion
        self.visor.insert(argumento)
        #Desconecto las acciones de las operaciones para que no pueda cambiarla
        self.b_multiplicar.clicked.disconnect()
        self.b_dividir.clicked.disconnect()
        self.b_sumar.clicked.disconnect()
        self.b_restar.clicked.disconnect()

    def resultado(self, operacion):
        print(operacion)
        print(type(operacion))
        

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ventana = Calculadora()
    ventana.show()
    
    app.exec()