from zooAnimales.animal import Animal

class Zoologico:

  def __init__(self,
               nombre: str | None = None,
               ubicacion: str | None = None,
               zonas: list = []):
    self._nombre = nombre
    self._ubicacion = ubicacion
    self._zonas = zonas

  def agregarZonas(self, zona):
    if zona != None:
      self._zonas.append(zona)

  def cantidadTotalAnimales(self):
    return sum(z.cantidadAnimales() for z in self.getZona())

  def getNombre(self) -> str | None:
    return self._nombre

  def setNombre(self, nombre: str) -> None:
    self._nombre = nombre

  def getUbicacion(self) -> str | None:
    return self._ubicacion

  def setUbicacion(self, ubicacion: str) -> None:
    self._ubicacion = ubicacion

  def getZona(self) -> list:
    return self._zonas

  def setZona(self, zonas: list) -> None:
    self._zonas = zonas

  pass

# Anti - copy : Carlos Yazid Padilla Royero