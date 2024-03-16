import zooAnimales.animal as animal

class Reptil(animal.Animal):
    
    # Atributos de clase
    
    __Iguanas : int = 0
    __Serpientes : int = 0
    __Listado : list = []
    
    # Constructor
    
    def __init__(self, nombre: str | None = None, edad: int | None = None, habitat: str | None = None, genero: str | None = None, color_escamas : str | None = None, largo_cola : int | None = None) -> None:
        super().__init__(nombre, edad, habitat, genero)
        self._color_escams = color_escamas
        self._largo_cola = largo_cola
        Reptil.__Listado.append(self)
    
    # Metodos de Instancia
    
    def movimiento(self) -> str:
        return "reptar"
    
    # Metodos de clase
    
    @classmethod
    def crearIguana(cls, nombre : str, edad : int, genero : str):
        cls.__Iguanas += 1
        nueva_Iguana = Reptil(nombre, edad, "humedal",genero,"verde",3)
        return nueva_Iguana
    
    @classmethod
    def crearSerpiente(cls, nombre : str, edad : int, genero : str):
        cls.__Serpientes += 1
        nueva_Serpiente = Reptil(nombre, edad, "jungla",genero,"blanco",1)
        return nueva_Serpiente

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
    def largo_cola(self) -> int:
        return self._largo_cola
    
    @largo_cola.setter
    def largo_cola(self, largo_cola: int) -> None:
        self._largo_cola = largo_cola
    
    @largo_cola.deleter
    def largo_cola(self) -> None:
        del self._largo_cola
    
    @classmethod
    def get_total_iguanas(cls) -> int:
        return cls.__Iguanas
    
    @classmethod
    def get_total_serpientes(cls) -> int:
        return cls.__Serpientes
    
    @classmethod
    def get_total_animales(cls) -> int:
        return len(cls.__Listados)
    
    pass