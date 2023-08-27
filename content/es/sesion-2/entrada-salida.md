---
title: "Entrada y Salida"

weight: 20

#isFolder: true
math: true
---

{{% pageinfo color="primary" %}}
## Documentación
* https://docs.python.org/3/tutorial/inputoutput.html

## Notebook Base
* <a target="_blank" href="https://colab.research.google.com/github/lmorillas/Introduccion-Python-3/blob/curso-py-iot/notebooks/beginner/notebooks/input_print.ipynb">
  <img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"/>
</a>

{{% /pageinfo %}}



## Ejercicio Práctico: Calculadora de Índice de Masa Corporal (IMC)

### Objetivo

El objetivo de este ejercicio es crear un programa en Python que calcule el Índice de Masa Corporal (IMC) de una persona. El programa deberá pedir la altura en metros y el peso en kilogramos, calcular el IMC y mostrar un mensaje con el resultado.

### Fórmula del IMC

El IMC se calcula con la siguiente fórmula: 
```math
\text{IMC} = \frac{\text{Peso en kg}}{( \text{Altura en m} )^2}
```

### Instrucciones

1. Crea un nuevo archivo Python y nómbralo `calculadora_imc.py`.
2. Utiliza la función `input()` para obtener el peso y la altura del usuario. Asegúrate de convertir estas entradas a números flotantes para poder hacer cálculos con ellos.
3. Usa la fórmula del IMC para calcular el índice.
4. Utiliza la función `print()` para mostrar el IMC calculado. Asegúrate de que el resultado se muestre con dos decimales.

{{% details summary="Código de ejemplo"%}}

```python
# Obtener peso del usuario
peso = float(input("Por favor, introduce tu peso en kilogramos: "))

# Obtener altura del usuario
altura = float(input("Por favor, introduce tu altura en metros: "))

# Calcular IMC
imc = peso / (altura ** 2)

# Mostrar el resultado
print(f"Tu Índice de Masa Corporal (IMC) es: {imc:.2f}")
```
{{% /details %}}

#### Ampliación

1. Agrega validaciones para asegurarte de que el usuario no introduzca números negativos o cero.
2. Extiende el programa para que, además de mostrar el IMC, indique si el usuario está bajo de peso, en su peso ideal o tiene sobrepeso, según la escala de IMC.
