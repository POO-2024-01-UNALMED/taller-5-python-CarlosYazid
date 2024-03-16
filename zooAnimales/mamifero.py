import zooAnimales.animal as animal

class Mamifero(animal.Animal):
    
    # Atributos de clase
    
    Caballos : int = 0
    Leones : int = 0
    Listado : list = []
    
    # Constructor
    
    def __init__(self, nombre: str | None = None, edad: int | None = None, habitat: str | None = None, genero: str | None = None, pelaje : bool = False,patas : int | None = None) -> None:
        super().__init__(nombre, edad, habitat, genero)
        self._pelaje = pelaje
        self._patas = patas
        Mamifero.Listado.append(self)
    
    # Metodos de clase
    
    @classmethod
    def crearCaballo(cls, nombre : str, edad : int, genero : str):
        cls.Caballos += 1
        nuevo_Caballo = Mamifero(nombre, edad, "pradera",genero,True,4)
        return nuevo_Caballo
    
    @classmethod
    def crearLeon(cls, nombre : str, edad : int, genero : str):
        cls.Leones += 1
        nuevo_Leon = Mamifero(nombre, edad, "selva",genero,True,4)
        return nuevo_Leon

    # Getters y Setters
    
    @property
    def pelaje(self) -> bool:
        return self._pelaje
    
    @pelaje.setter
    def pelaje(self, pelaje: bool) -> None:
        self._pelaje = pelaje
    
    @pelaje.deleter
    def pelaje(self) -> None:
        del self._pelaje
    
    @property
    def patas(self) -> int:
        return self._patas
    
    @patas.setter
    def patas(self, patas: int) -> None:
        self._patas = patas
    
    @patas.deleter
    def patas(self) -> None:
        del self._patas
    
    @classmethod
    def get_total_caballo(cls) -> int:
        return cls._Caballos
    
    @classmethod
    def get_total_leon(cls) -> int:
        return cls._Leones
    
    @classmethod
    def get_total_animales(cls) -> int:
        return len(cls._Listado)
    
    pass