class Vehiculo():    
    def __init__(self,color, marca, velocidad_maxima):
        self.color = color
        self.marca = marca
        self.velocidad_maxima = velocidad_maxima
        self.carga_actual = 0
        self.velocidad_actual = 0
        self.encendido = False

    def encender_auto(self):
        self.encendido = True
        print('Auto encendido')
    def apagar_auto(self):
        self.encendido = False
        print('Auto apagado')
    def mostrar_velocimetro(self):
        print('La velocidad es de ' + str(self.velocidad_actual)+'  de '+str(self.velocidad_maxima))
    def acelerar(self,velocidad):
        if (self.encendido == True):
            if self.velocidad_actual + velocidad > self.velocidad_maxima:
                self.velocidad_actual = self.velocidad_maxima
            else:
                self.velocidad_actual = self.velocidad_actual + velocidad
            self.mostrar_velocimetro()
        else:
            print('Para acelerar hay que encender el auto ')
    def frenar(self, velocidad):
        if self.velocidad_actual - velocidad <= 0:
            self.velocidad_actual = 0
        else:
            self.velocidad_actual = self.velocidad_actual - velocidad
        self.mostrar_velocimetro()

class Camion(Vehiculo):
    def __init__(self,carga_maxima,color,marca,velocidad_maxima):
        self.carga_maxima = carga_maxima
        Vehiculo.__init__(self,color,marca,velocidad_maxima)
        self.carga_actual = 0
    def cargar(self,cantidad):
        self.carga_actual = self.carga_actual+cantidad
    def mostrar_velocimetro(self):
        print('La velocidad es de ' + str(self.velocidad_actual)+'  de '+str(self.velocidad_maxima)+ ' con una carga actual ' + str(self.carga_actual))


class Automovil(Vehiculo):
    def __init__(self,puertas, color, marca, velocidad_maxima):
        self.puertas = puertas
        Vehiculo.__init__(self,color,marca,velocidad_maxima)
    def abrir_puertas(self,nro_puertas):
        print('Abrir las puertas')
    
    
mi_auto = Automovil(4,'Naranja','FIAT',200)
mi_auto.encender_auto()
mi_auto.acelerar(100)
# print(mi_auto.color)
# print(mi_auto.marca)

# mi_auto.acelerar(20)
# mi_auto.acelerar(170)
# mi_auto.frenar(5050)

# mi_auto.encender_auto()

mi_camion = Camion('zapote','elfo',200, 200000)
mi_camion.encender_auto
mi_camion.acelerar(80)
mi_camion.mostrar_velocimetro()

# print(mi_camion.carga_actual)