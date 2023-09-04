---
title: "Jupyter en EC2"

description: >
  Lanzar Jupyter desde EC2

weight: 35

---

{{% pageinfo %}}
## Documentación
* https://jupyter.org/
* https://towardsdatascience.com/setting-up-and-using-jupyter-notebooks-on-aws-61a9648db6c5
* https://saturncloud.io/blog/how-to-autoconfigure-jupyter-password-from-command-line/
{{% /pageinfo %}}

## Pasos

* Crear una instancia EC2 con AWS AMI Linux
* Añadir regla de entrada en el grupo de seguridad para permitir el acceso al puerto 8888 desde cualquier IP
* Conectarse por SSH a la instancia
* Crear carpeta, preparar entorno e instalar jupyter
```bash
$ mkdir jupyter
$ cd jupyter
$ python3 -m venv env
$ source env/bin/activate
$ pip install jupyter
```
* Generar contraseña para jupyter
```bash
$ jupyter notebook password
```
* Lanzar jupyter
```bash
$ jupyter notebook --ip=0.0.0.0 --port=8888 --no-browser
```
* Acceder a la instancia desde el navegador con la IP pública de la instancia y el puerto 8888
* Para parar jupyter, pulsar Ctrl+C

