import zooAnimales.animal as animal

class Pez(animal.Animal):
    
    # Atributos de clase
    
    salmones : int = 0
    bacalaos : int = 0
    listado : list = []
    
    # Constructor
    
    def __init__(self, nombre: str | None = None, edad: int | None = None, habitat: str | None = None, genero: str | None = None, color_escamas : str | None = None, cantidad_aletas : int | None = None) -> None:
        super().__init__(nombre, edad, habitat, genero)
        self._color_escamas = color_escamas
        self._cantidad_aletas = cantidad_aletas
        Pez.listado.append(self)
    
    # Metodos de Instancia
    
    def movimiento(self) -> str:
        return "nadar"
    
    # Metodos de clase
    
    @classmethod
    def crearSalmon(cls, nombre : str, edad : int, genero : str):
        cls.salmones += 1
        nuevo_Salmon = Pez(nombre, edad, "oceano",genero,"rojo",6)
        return nuevo_Salmon
    
    @classmethod
    def crearBacalao(cls, nombre : str, edad : int, genero : str):
        cls.bacalaos += 1
        nuevo_Bacalao = Pez(nombre, edad, "oceano",genero,"gris",6)
        return nuevo_Bacalao

    # Getters y Setters
    

    def getColorEscamas(self) -> str:
        return self._color_escamas
    
    def setColorEscamas(self, color_escams: str) -> None:
        self._color_escams = color_escams
    
    def getCantidadAletas(self) -> int:
        return self._cantidad_aletas
    
    def setCantidadAletas(self, cantidad_aletas: int) -> None:
        self._cantidad_aletas = cantidad_aletas
    
    @classmethod
    def get_total_salmon(cls) -> int:
        return cls.salmones
    
    @classmethod
    def get_total_bacalao(cls) -> int:
        return cls.bacalaos
    
    @classmethod
    def get_total_animales(cls) -> int:
        return len(cls.listado)
    
    pass

# Anti - copy : Carlos Yazid Padilla