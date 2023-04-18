import sys
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QMainWindow, QPushButton, QLineEdit, QGridLayout, QApplication, QWidget, QVBoxLayout, QHBoxLayout

class Calculadora(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Calculadora")
        ##ELEMENTOS
        #Botones numericos
        #Lista con botones numericos
        self.botones = []
        #Bucle que añade 10 botones a la lista
        for i in range(10):
            self.botones.append(QPushButton(f"{i}"))
        #conectar acciones botones numericos
        self.botones[0].clicked.connect(lambda: self.numeros("0"))
        self.botones[1].clicked.connect(lambda: self.numeros("1"))
        self.botones[2].clicked.connect(lambda: self.numeros("2"))
        self.botones[3].clicked.connect(lambda: self.numeros("3"))
        self.botones[4].clicked.connect(lambda: self.numeros("4"))
        self.botones[5].clicked.connect(lambda: self.numeros("5"))
        self.botones[6].clicked.connect(lambda: self.numeros("6"))
        self.botones[7].clicked.connect(lambda: self.numeros("7"))
        self.botones[8].clicked.connect(lambda: self.numeros("8"))
        self.botones[9].clicked.connect(lambda: self.numeros("9"))

        #Visor
        #Editor en modo solo lectura para crear un string
        self.visor = QLineEdit()
        #Alineo el texto a la derecha para que se vea mejor
        self.visor.setAlignment(Qt.AlignmentFlag.AlignRight)
        #Solo lectura para que funcione a modo de "Pantalla"
        self.visor.setReadOnly(True)

        #Operaciones
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

        #Boton reset
        self.b_reset = QPushButton("AC")
        self.b_reset.clicked.connect(lambda: self.reset())

        #Contenedores
        caja_principal = QVBoxLayout()
        caja_principal.addWidget(self.visor)

        caja_interfaz = QHBoxLayout()

        caja_operaciones = QVBoxLayout()
        caja_operaciones.addWidget(self.b_multiplicar)
        caja_operaciones.addWidget(self.b_dividir)
        caja_operaciones.addWidget(self.b_restar)
        caja_operaciones.addWidget(self.b_sumar)
        caja_operaciones.addWidget(self.b_resultado)

        caja_numeros = QGridLayout()
        #boton 0 en fila 3
        caja_numeros.addWidget(self.botones[0],3,1)
        #boton reset en fila 3
        caja_numeros.addWidget(self.b_reset,3,3)
        #fila 2
        columna = 0
        for i in range(1,4):
            columna += 1
            caja_numeros.addWidget(self.botones[i],2,columna)
        #fila 1
        columna = 0
        for i in range(4,7):
            columna += 1
            caja_numeros.addWidget(self.botones[i],1,columna)
        #fila 0
        columna = 0
        for i in range(7,10):
            columna += 1
            caja_numeros.addWidget(self.botones[i],0,columna)

        #Añado caja con numeros y caja con operaciones a la interfaz con layout horizontal
        caja_interfaz.addLayout(caja_numeros)
        caja_interfaz.addLayout(caja_operaciones)

        #Añado caja interfaz (con caja de numeros y operaciones) a la caja principal
        caja_principal.addLayout(caja_interfaz)

        #Coloco el layout final (caja_principal) en la ventana principal
        ventana_principal = QWidget()
        ventana_principal.setLayout(caja_principal)

        self.setCentralWidget(ventana_principal)
    
    #Funcion que añade numeros al string del visor
    def numeros(self, argumento):
        #Inserto numeros al visor
        self.visor.insert(argumento)

    #Funcion que añade el operador al string en el visor
    def creador_operacion(self, argumento):
        #Añado al visor la operacion
        self.visor.insert(argumento)
        #Inhabilita los botones para que no se pueda modificar la operacion
        self.b_multiplicar.setEnabled(False)
        self.b_dividir.setEnabled(False)
        self.b_sumar.setEnabled(False)
        self.b_restar.setEnabled(False)

    #Funcion que lee el texto del visor y entrega el resultado en el mismo
    def resultado(self, operacion):
        #Recibe el string del visor y lo convierte en lista
        operacion = list(operacion)
        #Multiplicacion
        if operacion.count("*")>0:
            aux = operacion.index("*")
            valor1 = ""
            valor2 = ""
            for i in range(0,aux):
                valor1 += operacion[i]
            for i in range(aux+1,len(operacion)):
                valor2 += operacion[i]
            self.visor.setText(f"{int(valor1)*int(valor2)}")

        #Division
        elif operacion.count("/")>0:
            aux = operacion.index("/")
            valor1 = ""
            valor2 = ""
            for i in range(0,aux):
                valor1 += operacion[i]
            for i in range(aux+1,len(operacion)):
                valor2 += operacion[i]
            self.visor.setText(f"{int(valor1)/int(valor2)}")

        #Suma
        elif operacion.count("+")>0:
            aux = operacion.index("+")
            valor1 = ""
            valor2 = ""
            for i in range(0,aux):
                valor1 += operacion[i]
            for i in range(aux+1,len(operacion)):
                valor2 += operacion[i]
            self.visor.setText(f"{int(valor1)+int(valor2)}")

        #Resta
        elif operacion.count("-")>0:
            aux = operacion.index("-")
            valor1 = ""
            valor2 = ""
            for i in range(0,aux):
                valor1 += operacion[i]
            for i in range(aux+1,len(operacion)):
                valor2 += operacion[i]
            self.visor.setText(f"{int(valor1)-int(valor2)}")
        #Inhabilita los botones para que no pueda modificarse el resultado del visor
        self.botones[0].setEnabled(False)
        self.botones[1].setEnabled(False)
        self.botones[2].setEnabled(False)
        self.botones[3].setEnabled(False)
        self.botones[4].setEnabled(False)
        self.botones[5].setEnabled(False)
        self.botones[6].setEnabled(False)
        self.botones[7].setEnabled(False)
        self.botones[8].setEnabled(False)
        self.botones[9].setEnabled(False)
        self.b_resultado.setEnabled(False)
    
    #Funcion que reinicializa la calculadora
    def reset(self):
        #Actua solo si el visor no esta vacio
        if self.visor.text() != "":
            #Habilita los botones nuevamente y limpia el visor
            self.visor.setText("")
            self.b_multiplicar.setEnabled(True)
            self.b_dividir.setEnabled(True)
            self.b_sumar.setEnabled(True)
            self.b_restar.setEnabled(True)
            self.botones[0].setEnabled(True)
            self.botones[1].setEnabled(True)
            self.botones[2].setEnabled(True)
            self.botones[3].setEnabled(True)
            self.botones[4].setEnabled(True)
            self.botones[5].setEnabled(True)
            self.botones[6].setEnabled(True)
            self.botones[7].setEnabled(True)
            self.botones[8].setEnabled(True)
            self.botones[9].setEnabled(True)
            self.b_resultado.setEnabled(True)
        else:
            self.visor.setText(":)")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ventana = Calculadora()
    ventana.show()
    
    app.exec()