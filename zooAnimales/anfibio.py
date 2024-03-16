import zooAnimales.animal as animal

class Anfibio(animal.Animal):
    
    # Atributos de clase
    
    __Ranas : int = 0
    __Salamandras : int = 0
    __Listado : list = []
    
    # Constructor
    
    def __init__(self, nombre: str | None = None, edad: int | None = None, habitat: str | None = None, genero: str | None = None, color_piel : str | None = None, venenoso : bool | None = None) -> None:
        super().__init__(nombre, edad, habitat, genero)
        self._color_piel = color_piel
        self._venenoso = venenoso
        Anfibio.__Listado.append(self)
    
    # Metodos de Instancia
    
    def movimiento(self) -> str:
        return "saltar"
    
    # Metodos de clase
    
    @classmethod
    def crearRana(cls, nombre : str, edad : int, genero : str):
        cls.__Ranas += 1
        nueva_Rana = Anfibio(nombre, edad, "selva",genero,"rojo",True)
        return nueva_Rana
    
    @classmethod
    def crearSalamandra(cls, nombre : str, edad : int, genero : str):
        cls.__Salamandras += 1
        nueva_Salamandra = Anfibio(nombre, edad, "selva",genero,"negro y amarillo",False)
        return nueva_Salamandra

    # Getters y Setters
    
    @property
    def color_piel(self) -> str:
        return self._color_piel
    
    @color_piel.setter
    def color_piel(self, color_piel: str) -> None:
        self._color_piel = color_piel
    
    @color_piel.deleter
    def color_piel(self) -> None:
        del self._color_piel
    
    @property
    def venenoso(self) -> int:
        return self._venenoso
    
    @venenoso.setter
    def venenoso(self, venenoso: bool) -> None:
        self._venenoso = venenoso

    
    @classmethod
    def get_total_rana(cls) -> int:
        return cls.__Ranas
    
    @classmethod
    def get_total_salamandra(cls) -> int:
        return cls.__Salamandras
    
    @classmethod
    def get_total_animales(cls) -> int:
        return len(cls.__Listado)
    
    pass
