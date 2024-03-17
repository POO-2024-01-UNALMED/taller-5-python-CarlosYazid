class Animal:

  # Atributos de Clase

  __Total_Animales: int = 0

  # Constructor

  def __init__(self,
               nombre: str | None = None,
               edad: int | None = None,
               habitat: str | None = None,
               genero: str | None = None,
               zona=None):
    self._nombre = nombre
    self._edad = edad
    self._habitat = habitat
    self._genero = genero
    self._zona = zona
    Animal.__Total_Animales += 1

  # String representation

  def __str__(self) -> str:
    return f"Mi nombre es {self._nombre} , tengo una edad de {self._edad}, habito en {self._habitat} y mi genero es {self._genero}"

  def toString(self) -> str:
    return f"Mi nombre es {self._nombre}, tengo una edad de {self._edad}, habito en {self._habitat} y mi genero es {self._genero}"

  @classmethod
  def totalPorTipo(cls) -> str:
    from zooAnimales.mamifero import Mamifero
    from zooAnimales.pez import Pez
    from zooAnimales.reptil import Reptil
    from zooAnimales.ave import Ave
    from zooAnimales.anfibio import Anfibio
    return f"""Mamiferos : {Mamifero.get_total_animales()}\nAves : {Ave.get_total_animales()}\nReptiles : {Reptil.get_total_animales()}\nPeces : {Pez.get_total_animales()}\nAnfibios : {Anfibio.get_total_animales()}"""

  # Metodos de Instancia

  def movimiento(self) -> str:
    return "desplazarse"

  # Getters y Setters

  def getNombre(self) -> str | None:
    return self._nombre

  def setNombre(self, nombre: str):
    self._nombre = nombre

  def getEdad(self) -> int | None:
    return self._edad

  def setEdad(self, edad: int):
    self._edad = edad

  def getHabitat(self) -> str | None:
    return self._habitat

  def setHabitat(self, habitat: str):
    self._habitat = habitat

  def getGenero(self) -> str | None:
    return self._genero

  def setGenero(self, genero: str):
    self._genero = genero

  def getZona(self):
    return self._zona

  def setZona(self, zona):
    self._zona = zona

  @classmethod
  def Total_Animales(cls) -> int:
    return cls.__Total_Animales

  @classmethod
  def SetTotal_Animales(cls, total: int):
    cls.__Total_Animales = total

  pass

# Anti - copy : Carlos Yazid Padilla