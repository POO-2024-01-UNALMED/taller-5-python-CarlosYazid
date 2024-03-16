import sys
import os

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))

from gestion.zona import Zona
from zooAnimales.animal import Animal

class Zoologico:
    
    def __init__(self, nombre : str | None = None, ubicacion : str | None = None, zonas : list[Zona] = []):
        self._nombre = nombre
        self._ubicacion = ubicacion
        self._zonas = zonas
        
    def agregarZonas(self,zona : Zona | None = None):
        if zona!= None:
            self._zonas.append(zona)
    
    @classmethod
    def cantidad_total_animales(cls) -> int:
        return Animal.Total_Animales()
    
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
    def ubicacion(self) -> str:
        return self._ubicacion
    
    @ubicacion.setter
    def ubicacion(self, ubicacion : str) -> None:
        self._ubicacion = ubicacion
    
    @ubicacion.deleter
    def ubicacion(self) -> None:
        del self._ubicacion
    
    @property
    def zonas(self) -> list[Zona]:
        return self._zonas
    
    @zonas.setter
    def zonas(self, zonas : list[Zona]) -> None:
        self._zonas = zonas
    
    @zonas.deleter
    def zonas(self) -> None:
        del self._zonas
    
    pass