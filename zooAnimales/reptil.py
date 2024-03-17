import zooAnimales.animal as animal

class Reptil(animal.Animal):
    
    # Atributos de clase
    
    iguanas : int = 0
    serpientes : int = 0
    listado : list = []
    
    # Constructor
    
    def __init__(self, nombre: str | None = None, edad: int | None = None, habitat: str | None = None, genero: str | None = None, color_escamas : str | None = None, largo_cola : int | None = None) -> None:
        super().__init__(nombre, edad, habitat, genero)
        self._color_escams = color_escamas
        self._largo_cola = largo_cola
        Reptil.listado.append(self)
    
    # Metodos de Instancia
    
    def movimiento(self) -> str:
        return "reptar"
    
    # Metodos de clase
    
    @classmethod
    def crearIguana(cls, nombre : str, edad : int, genero : str):
        cls.iguanas += 1
        nueva_Iguana = Reptil(nombre, edad, "humedal",genero,"verde",3)
        return nueva_Iguana
    
    @classmethod
    def crearSerpiente(cls, nombre : str, edad : int, genero : str):
        cls.serpientes += 1
        nueva_Serpiente = Reptil(nombre, edad, "jungla",genero,"blanco",1)
        return nueva_Serpiente

    # Getters y Setters
    
    def getColorEscamas(self) -> str:
        return self._color_escams
    
    def setColorEscamas(self, color_escams: str) -> None:
        self._color_escams = color_escams
    
    def getLargoCola(self) -> int:
        return self._largo_cola
    
    def setLargoCola(self, largo_cola: int) -> None:
        self._largo_cola = largo_cola
    
    @classmethod
    def get_total_iguanas(cls) -> int:
        return cls.iguanas
    
    @classmethod
    def get_total_serpientes(cls) -> int:
        return cls.serpientes
    
    @classmethod
    def get_total_animales(cls) -> int:
        return len(cls.listado)
    
    pass

# Anti - copy : Carlos Yazid Padilla