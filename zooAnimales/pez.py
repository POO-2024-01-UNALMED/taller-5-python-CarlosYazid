import zooAnimales.animal as animal

class Pez(animal.Animal):
    
    # Atributos de clase
    
    __Salmones : int = 0
    __Bacalaos : int = 0
    __Listado : list = []
    
    # Constructor
    
    def __init__(self, nombre: str | None = None, edad: int | None = None, habitat: str | None = None, genero: str | None = None, color_escamas : str | None = None, cantidad_aletas : int | None = None) -> None:
        super().__init__(nombre, edad, habitat, genero)
        self._color_escamas = color_escamas
        self._cantidad_aletas = cantidad_aletas
        Pez.__Listado.append(self)
    
    # Metodos de Instancia
    
    def movimiento(self) -> str:
        return "nadar"
    
    # Metodos de clase
    
    @classmethod
    def crearSalmon(cls, nombre : str, edad : int, genero : str):
        cls.__Salmones += 1
        nuevo_Salmon = Pez(nombre, edad, "oceano",genero,"rojo",6)
        return nuevo_Salmon
    
    @classmethod
    def crearBacalao(cls, nombre : str, edad : int, genero : str):
        cls.__Bacalaos += 1
        nuevo_Bacalao = Pez(nombre, edad, "oceano",genero,"gris",6)
        return nuevo_Bacalao

    # Getters y Setters
    
    @property
    def color_escamas(self) -> str:
        return self._color_escams
    
    @color_escamas.setter
    def color_escamas(self, color_escams: str) -> None:
        self._color_escams = color_escams
    
    @color_escamas.deleter
    def color_escamas(self) -> None:
        del self._color_escams
    
    @property
    def cantidad_aletas(self) -> int:
        return self._cantidad_aletas
    
    @cantidad_aletas.setter
    def cantidad_aletas(self, cantidad_aletas: int) -> None:
        self._cantidad_aletas = cantidad_aletas
    
    @cantidad_aletas.deleter
    def cantidad_aletas(self) -> None:
        del self._cantidad_aletas
    
    @classmethod
    def get_total_salmon(cls) -> int:
        return cls.__Salmones
    
    @classmethod
    def get_total_bacalao(cls) -> int:
        return cls.__Bacalaos
    
    @classmethod
    def get_total_animales(cls) -> int:
        return len(cls.__Listado)
    
    pass