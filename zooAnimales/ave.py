import zooAnimales.animal as animal

class Ave(animal.Animal):
    
    # Atributos de clase
    
    __Halcones : int = 0
    __Aguilas : int = 0
    __Listado : list = []
    
    # Constructor
    
    def __init__(self, nombre: str | None = None, edad: int | None = None, habitat: str | None = None, genero: str | None = None, color_pluma : str | None = None) -> None:
        super().__init__(nombre, edad, habitat, genero)
        self._color_pluma = color_pluma
        Ave.__Listado.append(self)
    
    # Metodos de Instancia
    
    def movimiento(self) -> str:
        return "volar"
    
    # Metodos de clase
    
    @classmethod
    def crearHalcon(cls, nombre : str, edad : int, genero : str):
        cls.__Halcones += 1
        nuevo_Halcon = Ave(nombre, edad, "montanas",genero,"cafe glorioso")
        return nuevo_Halcon
    
    @classmethod
    def crearAguila(cls, nombre : str, edad : int, genero : str):
        cls.__Aguilas += 1
        nueva_Aguila = Ave(nombre, edad, "montanas",genero,"blanco y amarillo")
        return nueva_Aguila

    # Getters y Setters
    
    @property
    def color_pluma(self) -> str:
        return self._color_pluma
    
    @color_pluma.setter
    def color_pluma(self, color_pluma: str) -> None:
        self._color_pluma = color_pluma
    
    @color_pluma.deleter
    def color_pluma(self) -> None:
        del self._color_pluma
    
    @classmethod
    def get_total_halcones(cls) -> int:
        return cls.__Halcones
    
    @classmethod
    def get_total_aguilas(cls) -> int:
        return cls.__Aguilas
    
    @classmethod
    def get_total_animales(cls) -> int:
        return len(cls.__Listado)
    
    pass
