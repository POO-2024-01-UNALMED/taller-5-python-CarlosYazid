import sys
import os

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))

from zooAnimales.animal import Animal

class Zona:
    
    def __init__(self, nombre : str | None = None, animales : list[Animal] = [], zoologico : any = None):
        self._nombre = nombre
        self._animales = animales
        self._zoologico = zoologico
    
    def agregarAnimales(self, animal : Animal):
        self._animales.append(animal)
        animal.SetTotal_Animales(animal.Total_Animales()+1)
    
    def cantidadAnimales(self):
        return len(self._animales)
    
    @property
    def nombre(self) -> str:
        return self._nombre
    
    @nombre.setter
    def nombre(self, nombre : str) -> None:
        self._nombre = nombre
    
    @nombre.deleter
    def nombre(self) -> None:
        del self._nombre
    
    @property
    def animales(self) -> list:
        return self._animales
    
    @animales.setter
    def animales(self, animales : list) -> None:
        self._animales = animales
    
    @animales.deleter
    def animales(self) -> None:
        del self._animales
    
    @property
    def zoologico(self) -> any:
        return self._zoologico
    pass