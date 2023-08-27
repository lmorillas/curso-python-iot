---
title: "Clases"

weight: 25
#isFolder: true

---

{{% pageinfo color="primary" %}}
## Documentación
* https://docs.python.org/3/tutorial/classes.html

## Notebook Base
* <a target="_blank" href="https://colab.research.google.com/github/lmorillas/Introduccion-Python-3/blob/curso-py-iot/notebooks/beginner/notebooks/intro-clases.ipynb">
  <img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"/>
</a>

* <a target="_blank" href="https://colab.research.google.com/github/lmorillas/Introduccion-Python-3/blob/curso-py-iot/notebooks/beginner/notebooks/11_classes.ipynb">
  <img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"/>
</a>

{{% /pageinfo %}}


## Ejercicios

* <a target="_blank" href="https://colab.research.google.com/github/lmorillas/Introduccion-Python-3/blob/curso-py-iot/notebooks/beginner/exercises/11_classes_exercise.ipynb">
  <img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"/>
</a>


### Ejercicio 1: Clase Persona

Crea una clase llamada `Persona` que tenga un atributo `nombre` y un método `saludar` que imprima "Hola, soy [nombre]".

### Ejercicio 2: Clase Librería

#### Descripción:

La clase `Libreria` tendrá un conjunto de libros disponibles y permitirá realizar ciertas operaciones como añadir libros, quitar libros y listar los libros disponibles.

#### Código:

```python
class Libreria:
    def __init__(self):
        self.libros = []
        
    def agregar_libro(self, titulo):
        self.libros.append(titulo)
        print(f"Se ha agregado el libro '{titulo}'.")
        
    def quitar_libro(self, titulo):
        if titulo in self.libros:
            self.libros.remove(titulo)
            print(f"Se ha quitado el libro '{titulo}'.")
        else:
            print(f"El libro '{titulo}' no está en la librería.")
            
    def listar_libros(self):
        if self.libros:
            print("Libros disponibles en la librería:")
            for libro in self.libros:
                print(f"- {libro}")
        else:
            print("La librería está vacía.")

# Instanciamos la libreria
mi_libreria = Libreria()

# Añadimos algunos libros
mi_libreria.agregar_libro("1984")
mi_libreria.agregar_libro("Cien años de soledad")

# Listamos los libros
mi_libreria.listar_libros()

# Quitamos un libro
mi_libreria.quitar_libro("1984")

# Listamos de nuevo los libros
mi_libreria.listar_libros()
```

### Tareas:

#### Tarea 1: Método para buscar un libro

Añade un método llamado `buscar_libro` que tome un título como parámetro y diga si el libro está o no en la librería.

#### Tarea 2: Contador de libros

Añade un método llamado `contar_libros` que devuelva el número total de libros en la librería.

