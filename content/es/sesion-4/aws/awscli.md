---
title: "AWS CLI"

description: >
  Instalación del cliente de AWS

weight: 10
---

{{% pageinfo %}}
## Documentación
* hhttps://docs.aws.amazon.com/cli/latest/userguide/cli-chap-welcome.html

{{% /pageinfo %}}

## Qué es
El AWS CLI es una herramienta unificada para administrar sus servicios de AWS. Con él, puede controlar múltiples servicios de AWS desde la línea de comandos y automatizarlos a través de scripts.

## Instalación
Sigue las instrucciones de tu sistema operativo https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html

También puedes instalarlo con pip
```bash
$ pip install awscli --upgrade --user
```


## Configuración
Ejecuta el comando `aws configure` y sigue las instrucciones o crea el archivo de configuración manualmente.

Copia las credenciales que te da el lab (`AWS Deails > AWS CLI > Show`) en 
* Linus y Max: `~/.aws/credentials`
* Windows: `C:\Users\USERNAME\.aws\credentials`

## Ejemplos de Uso Comunes

#### EC2
- **Listar todas las instancias EC2 en una región**
    ```bash
    aws ec2 describe-instances
    ```
  
- **Iniciar una instancia EC2**
    ```bash
    aws ec2 start-instances --instance-ids i-1234567890abcdef0
    ```
  
- **Detener una instancia EC2**
    ```bash
    aws ec2 stop-instances --instance-ids i-1234567890abcdef0
    ```

#### S3
- **Listar todos los buckets**
    ```bash
    aws s3 ls
    ```
  
- **Copiar un archivo al bucket**
    ```bash
    aws s3 cp myfile.txt s3://my-bucket/
    ```
  
- **Sincronizar un directorio local con un bucket S3**
    ```bash
    aws s3 sync my-folder/ s3://my-bucket/
    ```

#### Lambda
- **Invocar una función Lambda**
    ```bash
    aws lambda invoke --function-name my-function --payload '{"key": "value"}' outputfile.txt
    ```

#### CloudFormation
- **Crear una pila**
    ```bash
    aws cloudformation create-stack --stack-name my-new-stack --template-body file://my-cloudformation-template.yaml
    ```
