"""
Autor: Oriol López Miret

Descripción: Contiene una classe "Vector". 
    - Multiplicar entre 2 objetos classe Vector.
    - Multiplicar 1 objeto classe Vector con 1 escalar.
    - Multiplica y despues suma los valores de 2 vectores.
    - Valores tagenciales de vector 1 con vector 2
    - Valores normalizados de vector 1 con vector 2
"""

class Vector:
    """
    Permite hacer calculos con vectores.
    """
    vector = []
    def __init__(self, iterable):
        self.vector = [expresion for expresion in iterable]

    def __repr__(self):
        return "Vector(" + repr(self.vector) + ")"

    def __str__(self):
        return str(self.vector)

    def __rmul__(self, other):
        """
        Permite multiplicar entre objetos de la misma classe.
    
        Args:
            self,other(Class): Objetos de la classe "Vector"
    
        Returns:
            list: una lista con los valores multiplicados 
    
        Tests:
            >>> v1 = Vector([1, 2, 3])
            >>> v2 = Vector([4, 5, 6])
            >>> v1 * v2
            Vector([4, 10, 18])
        """
        tmp = [v1*v2 for v1, v2 in zip(self.vector, other.vector)]
        return Vector(tmp)

    def __mul__(self, other):
        """
        Permite multiplicar un escalar o objetos de la misma classe.
    
        Args:
            self,other(Class): Objetos de la classe "Vector"
    
        Returns:
            list: una lista con los valores multiplicados 
    
        Tests:
            >>> v1 = Vector([1, 2, 3])
            >>> v1 * 2
            Vector([2, 4, 6])
        """
        if isinstance(other, (int, float)):
            tmp = [v1*other for v1 in self.vector]
            return Vector(tmp)
        else:
            return self.__rmul__(other)

    def __matmul__(self, other):
        """
        Sobre carga el operador @ dando la suma total de las 2 matrizes una vez multiplicadas.
    
        Args:
            self,other(Class): Objetos de la classe "Vector"
    
        Returns:
            list: el producto escalar de los 2 vectores
    
        Tests:
            >>> v1 = Vector([1, 2, 3])
            >>> v2 = Vector([4, 5, 6])
            >>> v1 @ v2
            32
        """
        return sum(v1 * v2 for v1, v2 in zip(self.vector, other.vector))

    def __rmatmul__(self, other):
        """
        Sobre carga el operador @ dando la suma total de las 2 matrizes una vez multiplicadas.
    
        Args:
            self,other(Class): Objetos de la classe "Vector"
    
        Returns:
            list: el producto escalar de los 2 vectores
        """
        return self.__matmul__(other)

    def __floordiv__(self, other):
        """
        Sobre carga el operador // dando los valores tangenciales
    
        Args:
            self,other(Class): Objetos de la classe "Vector"
    
        Returns:
            list: componentes tangenciales de v1 con v2

        Tests:
        >>> v1 = Vector([2, 1, 2])
        >>> v2 = Vector([0.5, 1, 0.5])
        >>> v1 // v2
        Vector([1.0, 2.0, 1.0])
        """
        sub = sum(a * a for a in other.vector)
        factor = (self @ other) / sub
        return other * factor

    def __rfloordiv__(self, other):
        """
        Sobre carga el operador // dando los valores tangenciales
    
        Args:
            self,other(Class): Objetos de la classe "Vector"
    
        Returns:
            list: componentes tangenciales de v2 con v1
        """
        return self.__floordiv__(other)
        
    def __mod__(self, other):
        """
        Sobre carga el operador % dando los valores normales
    
        Args:
            self,other(Class): Objetos de la classe "Vector"
    
        Returns:
            list: componentes normales entre v1 y v2

        Tests:
        >>> v1 = Vector([2, 1, 2])
        >>> v2 = Vector([0.5, 1, 0.5])
        >>> v1 % v2
        Vector([1.0, -1.0, 1.0])
        """
        temp = []
        for v1, v2 in zip(self.vector, self.__floordiv__(other).vector):
            temp.append(v1 - v2)
        return Vector(temp)
        
    def __rmod__(self, other):
        """
        Sobre carga el operador % dando los valores normales
    
        Args:
            self,other(Class): Objetos de la classe "Vector"
    
        Returns:
            list: componentes normales entre v2 y v1
        """
        return self.__mod__(other)
        
import doctest
doctest.testmod(verbose=True)