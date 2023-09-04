---
title: "EC2"

description: >
  Creación y accesos a instancias EC2

weight: 30
---

{{% pageinfo %}}
## Documentación
* https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/EC2_GetStarted.html
{{% /pageinfo %}}

## Qué es EC2
EC2 es un servicio de computación en la nube de Amazon Web Services. Permite crear instancias de máquinas virtuales en la nube. Las instancias se organizan en regiones.

## Acceso a una instancia EC2

```python
import boto3

ec2 = boto3.resource('ec2')

# Describe instances
instances = ec2.instances.filter(
    Filters=[{'Name': 'instance-state-name', 'Values': ['running']}])

for instance in instances:
    print(instance.id, instance.instance_type)

# stop instance
ec2.instances.filter(InstanceIds=['i-1234567890abcdef0']).stop()

# start instance
ec2.instances.filter(InstanceIds=['i-1234567890abcdef0']).start()

# terminate instance
ec2.instances.filter(InstanceIds=['i-1234567890abcdef0']).terminate()
```
