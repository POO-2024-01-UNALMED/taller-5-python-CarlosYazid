class Animal:
    
    # Atributos de Clase
    
    __Total_Animales : int = 0
    
    # Constructor
    
    def __init__(self, nombre : str | None = None, edad : int | None = None, habitat : str | None = None, genero : str | None = None, zona = None):
        self._nombre = nombre
        self._edad = edad
        self._habitat = habitat
        self._genero = genero
        self._zona = zona
        Animal.__Total_Animales += 1
    
    # String representation
    
    def __str__(self) -> str:
        return f"Mi nombre es {self.nombre} , tengo una edad {self.edad}, habito en {self.habitat} y mi genero es {self.genero}"
    
    # Metodos de Instancia
    
    def movimiento(self) -> str:
        return "desplazarse"
    
    # Getters y Setters
    
    @property
    def nombre(self) -> str:
        return self._nombre
    
    @nombre.setter
    def nombre(self, nombre : str):
        self._nombre = nombre
    
    @nombre.deleter
    def nombre(self):
        del self._nombre
    
    @property
    def edad(self) -> int:
        return self._edad
    
    @edad.setter
    def edad(self, edad : int):
        self._edad = edad
    
    @edad.deleter
    def edad(self):
        del self._edad
    
    @property
    def habitat(self) -> str:
        return self._habitat
    
    @habitat.setter
    def habitat(self, habitat : str):
        self._habitat = habitat
    
    @habitat.deleter
    def habitat(self):
        del self._habitat
    
    @property
    def genero(self) -> str:
        return self._genero
    
    @genero.setter
    def genero(self, genero : str):
        self._genero = genero
    
    @genero.deleter
    def genero(self):
        del self._genero
    
    @property
    def zona(self):
        return self._zona
    
    @zona.setter
    def zona(self, zona):
        self._zona = zona
    
    @zona.deleter
    def zona(self):
        del self._zona
        
    @classmethod
    def Total_Animales(cls) -> int:
        return cls.__Total_Animales
    
    @classmethod
    def SetTotal_Animales(cls, total : int):
        cls.__Total_Animales = total
    
    pass