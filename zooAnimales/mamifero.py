import zooAnimales.animal as animal

class Mamifero(animal.Animal):
    
    # Atributos de clase
    
    caballos : int = 0
    leones : int = 0
    listado : list = []
    
    # Constructor
    
    def __init__(self, nombre: str | None = None, edad: int | None = None, habitat: str | None = None, genero: str | None = None, pelaje : bool = False,patas : int | None = None) -> None:
        super().__init__(nombre, edad, habitat, genero)
        self._pelaje = pelaje
        self._patas = patas
        Mamifero.listado.append(self)
    
    # Metodos de clase
    
    @classmethod
    def crearCaballo(cls, nombre : str, edad : int, genero : str):
        cls.caballos += 1
        nuevo_Caballo = Mamifero(nombre, edad, "pradera",genero,True,4)
        return nuevo_Caballo
    
    @classmethod
    def crearLeon(cls, nombre : str, edad : int, genero : str):
        cls.leones += 1
        nuevo_Leon = Mamifero(nombre, edad, "selva",genero,True,4)
        return nuevo_Leon

    # Getters y Setters
    
    def isPelaje(self) -> bool:
        return self._pelaje
    
    def setPelaje(self, pelaje: bool) -> None:
        self._pelaje = pelaje
    
    def getPatas(self) -> int:
        return self._patas
    
    def setPatas(self, patas: int) -> None:
        self._patas = patas
    
    @classmethod
    def get_total_caballo(cls) -> int:
        return cls.caballos
    
    @classmethod
    def get_total_leon(cls) -> int:
        return cls.leones
    
    @classmethod
    def get_total_animales(cls) -> int:
        return len(cls.listado)
    
    pass

# Anti - copy : Carlos Yazid Padilla