from typing import Any
from zooAnimales.animal import Animal
from gestion.zoologico import Zoologico


"""
    Taller 5 Python

    Realizado el 16 de marzo del 2024
    Desarrollado por Carlos Yazid Padilla
    Topico: Herencia

    Dependencias: 
    
        - gestion > zona
        - gestion > zoologico
        - zooAnimales > Anfibio
        - zooAnimales > Animal
        - zooAnimales > Ave
        - zooAnimales > Mamifero
        - zooAnimales > Pez
        - zooAnimales > Reptil
 """   

class Zona:
    
  def __init__(self, nombre : str | None = None,zoologico : Zoologico | None = None,animales : list | None = None):
    self._nombre = nombre
    self._animales = animales if animales is not None else []
    self._zoologico = zoologico
    
  def agregarAnimales(self, animal : Animal):
    self._animales.append(animal)
    
  def cantidadAnimales(self):
    return len(self._animales)
    
  def getNombre(self) -> str | None:
    return self._nombre
    
  def setNombre(self, nombre : str) -> None:
    self._nombre = nombre
    
  def getAnimales(self) -> list:
    return self._animales
    
  def setAnimales(self, animales : list) -> None:
    self._animales = animales
    
  def getZoo(self):
    return self._zoologico
  
  pass

# Anti - copy : Carlos Yazid Padilla