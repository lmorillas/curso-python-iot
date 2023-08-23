---
title: "Ejercicio de depuración"
linkTitle: "Depuración"
weight: 20
description: >
  Introducción a la depuracion de código Python con VS Code
---


## Depurar
* https://code.visualstudio.com/docs/python/debugging


### Objetivo

En este ejercicio, los estudiantes deberán depurar un programa Python que intenta realizar una búsqueda binaria en una lista ordenada de números. El programa tiene varios errores, y los alumnos deberán utilizar las herramientas de debug de VS Code para identificar y corregir estos problemas.

### Instrucciones

1. Crea un nuevo archivo Python (`debug_binsearch.py`) en un nuevo proyecto en VS Code.
2. Pega el siguiente código, que tiene varios errores intencionados:

```python
# debug_binsearch.py
# Este programa tiene errores. Tu tarea es usar el debug de VS Code para encontrarlos y corregirlos.

def binary_search(arr, x):
    low = 0
    high = len(arr)

    while low <= high:
        mid = (low + high) / 2  # Error intencionado
        mid_val = arr[mid]  # Error intencionado

        if mid_val < x:
            low = mid + 1
        elif mid_val > x:
            high = mid - 1
        else:
            return mid  # Encuentra el valor

    return -1  # Valor no encontrado

if __name__ == "__main__":
    arr = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
    x = input("Ingrese un número para buscar en la lista: ")  # Error intencionado

    # Realizar búsqueda binaria
    result = binary_search(arr, x)

    if result != -1:
        print(f"El número {x} está en la posición {result} de la lista.")
    else:
        print(f"El número {x} no se encuentra en la lista.")
```

2. Coloca breakpoints en las líneas que consideres relevantes para encontrar los errores.
3. Inicia el debug (puedes hacerlo presionando F5 o yendo a la barra lateral de "Run and Debug").
4. Observa las variables, la salida y el flujo del programa para identificar los errores.
5. Corrige los errores que encuentres y reinicia el debug para confirmar que el programa funciona correctamente.


{{% details summary="Errores a Corregir"%}}
1. `mid = (low + high) / 2` calcula `mid` como un número de punto flotante. Debe ser un entero para indexar la lista. Puede corregirse como `mid = (low + high) // 2`.
2. `high = len(arr)` debería ser `high = len(arr) - 1` para evitar el acceso fuera de rango.
3. El valor ingresado `x` es una cadena. Debe ser convertido a un entero antes de pasarlo a la función `binary_search`.

{{% /details %}}

## `if __name__ == "__main__"`

Por supuesto, el bloque `if __name__ == "__main__":` es un patrón común en programas Python.

Cuando ejecutas un script en Python, el intérprete asigna un valor especial a la variable `__name__`. Este valor será `"__main__"` si el script se está ejecutando como programa principal. Pero si el script se importa como un módulo en otro script, el valor de `__name__` será el nombre del archivo del script (sin la extensión `.py`).

En otras palabras, `if __name__ == "__main__":` permite diferenciar entre los dos escenarios: ¿se está ejecutando este archivo Python como programa principal o se está importando en otro script como un módulo?

### ¿Para qué se usa?

Este bloque se usa principalmente por dos razones:

1. **Modularidad**: Al poner el código bajo este bloque, te aseguras de que ese código solo se ejecute cuando el script sea el programa principal. Esto permite que otros scripts importen funciones y clases de este script sin ejecutar todo el código inmediatamente al importarlo.

2. **Organización del Código**: Al colocar el "código de arranque" del script bajo este bloque, se separa claramente la definición de funciones y clases del código que realmente inicia la lógica del programa. Esto hace que el código sea más legible y mantenible.

### Un ejemplo

Supongamos que tienes un script llamado `mi_script.py` con el siguiente contenido:

```python
# Definición de una función
def imprimir_saludo(nombre):
    print(f"Hola, {nombre}.")

# Código de arranque
if __name__ == "__main__":
    imprimir_saludo("Alice")
```

Si ejecutas `mi_script.py` directamente (`python mi_script.py`), verás la salida `Hola, Alice.` porque el script se está ejecutando como programa principal y, por lo tanto, `__name__` es igual a `"__main__"`.

Ahora, si importas `mi_script.py` en otro script:

```python
import mi_script

mi_script.imprimir_saludo("Bob")
```

Verás la salida `Hola, Bob.` pero no verás `Hola, Alice.` Esto es porque al importar `mi_script`, la variable `__name__` en `mi_script.py` no es `"__main__"`, por lo que el bloque `if __name__ == "__main__":` no se ejecuta.

