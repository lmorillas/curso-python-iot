---
title: "Decoradores"

weight: 28
#isFolder: true

---

{{% pageinfo color="primary" %}}
## Documentación
* https://docs.python.org/3/glossary.html#term-decorator

* <a target="_blank" href="https://colab.research.google.com/github/lmorillas/curso-python-iot/blob/main/notebooks/ejemplo_decoradores.ipynb">
  <img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"/>
</a>
{{% /pageinfo %}}

## ¿Qué es un Decorador en Python?

Un decorador es una función que toma una función como entrada y devuelve una nueva función. Se usan para modificar el comportamiento de las funciones o clases de una manera limpia, reutilizable y legible.

## Sintaxis

La sintaxis básica para usar un decorador es preceder la definición de una función con el símbolo `@` seguido del nombre del decorador.

```python
@decorador
def mi_funcion():
    pass
```

## ¿Cómo Funcionan?

Veamos un ejemplo sencillo de cómo funciona un decorador. Supongamos que deseamos medir el tiempo que toma la ejecución de una función.

```python
import time

def timer_decorator(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"{func.__name__} se ejecutó en {end_time - start_time} segundos")
        return result
    return wrapper

@timer_decorator
def mi_funcion(n):
    suma = 0
    for i in range(n):
        suma += i
    return suma
```

Cuando llamamos a `mi_funcion`, en realidad estamos llamando a `wrapper`, que a su vez llama a `mi_funcion`, permitiéndonos hacer cosas antes y después de que se ejecute `mi_funcion` sin modificar su código.

## Utilidad

1. **Separación de Responsabilidades**: Los decoradores ayudan a seguir el principio de separación de responsabilidades al extraer la lógica que no está directamente relacionada con la tarea de una función.
  
2. **Reusabilidad**: Una vez que tienes un decorador, puedes usarlo en múltiples funciones.

3. **Modificación Dinámica**: Permiten modificar el comportamiento de una función o clase sin tener que modificar su código fuente.

4. **Legibilidad**: Mejoran la legibilidad al etiquetar las funciones con su comportamiento adicional.

## ¿Por Qué se Utilizan Tanto Ahora?

1. **Desarrollo Web**: En frameworks como Flask y Django, los decoradores se usan ampliamente para manejar rutas, permisos, entre otros.

2. **Código Asíncrono**: Con la introducción de `asyncio`, los decoradores se usan para manejar tareas asíncronas.

3. **Analítica y Monitoreo**: En la ciencia de datos y en el aprendizaje automático, los decoradores pueden ser útiles para registrar métricas o manejar recursos.

4. **Decoradores de Clase**: Con la creciente popularidad de la programación orientada a objetos, los decoradores de clases se están utilizando más para extender la funcionalidad de las clases de manera limpia y reutilizable.

5. **Soporte en el Lenguaje**: Python ha añadido varias características de lenguaje (como el uso de `@` para decoradores) que hacen que los decoradores sean más fáciles de escribir y entender.
