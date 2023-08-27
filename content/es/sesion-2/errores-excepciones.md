---
title: "Errores y Excepciones"

weight: 30
#isFolder: true

---

{{% pageinfo color="primary" %}}
## Documentación
* https://docs.python.org/3/tutorial/errors.html
* https://docs.python.org/3/library/exceptions.html

## Notebook Base
* <a target="_blank" href="https://colab.research.google.com/github/lmorillas/Introduccion-Python-3/blob/curso-py-iot/notebooks/beginner/notebooks/12_exceptions.ipynb">
  <img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"/>
</a>

* <a target="_blank" href="https://colab.research.google.com/github/lmorillas/Introduccion-Python-3/blob/curso-py-iot/notebooks/beginner/exercises/12_exceptions_exercise.ipynb">
  <img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"/>
</a>

{{% /pageinfo %}}


## The try-except block
When you think an error may occur, you can write a `try-except` block to handle the exception that might be raised.
The try block tells Python to try running some code, and the except block tells Python what to do if the code results in a particular kind of error.

### Ejemplo: Handling the ZeroDivisionError exception
```python
try:
    print(5/0)
except ZeroDivisionError:
    print("You can't divide by zero!")
``` 

### Ejemplo: Handling the FileNotFoundError exception

```python
from pathlib import Path
path = Path("siddhartha.txt")
try:
    contents = path.read_text()
except FileNotFoundError:
    msg = f"Can’t find file: {path.name}."
    print(msg)
```

### ```else``` block
```python
prompt = "How many tickets do you need? "
num_tickets = input(prompt)
try:
    num_tickets = int(num_tickets)
except ValueError:
    print("Please try again.")
else:
    print("Your tickets are printing.")
```

## Knowing which exception to handle

It can be hard to know what kind of exception to handle when writing code. Try writing your code without a try block, and make it generate an error. The traceback will tell you
what kind of exception your program needs to handle. 

