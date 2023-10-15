from persona import Persona
from deportista import Deportista

class Futbolista(Persona, Deportista):
    _listaFutbolistas = []
    def __init__(self, nombre, edad, altura, sexo, añosParticipando, golesMarcados, tarjetasRojas, piernaHabil):
        self._golesMarcados = golesMarcados
        self._tarjetasRojas = tarjetasRojas
        self._piernaHabil = piernaHabil
        Persona.__init__(self,nombre,edad,altura,sexo)
        Deportista.__init__(self,"Futbol", añosParticipando)
        Futbolista._listaFutbolistas.append(self)

    def getGolesMarcados(self):
        return self._golesMarcados
        
    def getTarjetasRojas(self):
        return self._tarjetasRojas
        
    def getPiernaHabil(self):
        return self._piernaHabil
        
    def setGolesMarcados(self, golesMarcados):
        self._golesMarcados = golesMarcados

    def setTarjetasRojas(self, tarjetasRojas):
        self._tarjetasRojas = tarjetasRojas
        
    def setPiernaHabil(self, piernaHabil):
        self._piernaHabil = piernaHabil

    def __str__(self):
        return f"Mi nombre es {super().nombre} soy profesional en el deporte {super().deporte} Tengo {super().edad} años de edad y llevo {super().añosParticipando} años en el deporte"