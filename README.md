# Pure-FTPd & FileZilla Client Dockerfiles
Este proyecto consiste en la creación de dockerfiles para Pure-FTPd server y FileZilla Client, los cuales se asocian al protocolo FTP, para que ambos puedan generar tráfico entre sí.
## Instalación
Como prerrequisitos, se encuentran la necesidad de tener instalados Docker y Git:

-Docker: https://docs.docker.com/engine/install/

-Git:  https://git-scm.com/book/en/v2/Getting-Started-Installing-Git

**Server:**
```
$ docker build . -t pure-ftpd:final
```
**Client:**
```
$ docker build . -t filezilla:final
```
Para el cliente, el host es ftp://localhost

## Video 1 - (Montaje dockerfiles y conexión server-client):
https://www.youtube.com/watch?v=7y6xFn3h1KI

[![Video para tarea2!](https://s3-us-west-2.amazonaws.com/devcodepro/media/tutorials/instalar-filezilla-para-conectarse-a-un-servidor-ftp-t1.png)](https://youtu.be/7y6xFn3h1KI)

## Polymorph
Luego de la conexión entre Pure-FTPd server y FileZilla Client, se puede utilizar el framework Polymorph para interceptar, capturar y modificar tráfico entre estos, a continuación se deja enlace a esta herramienta y demostración de uso:

-Polymorph: https://github.com/shramos/polymorph

## Video 2 - (Utilizando Polymorph):
https://www.youtube.com/watch?v=UEybiL0i-uM

[![Video para tarea3!](https://1.bp.blogspot.com/-vn5etah3lqU/WuIBtO62BhI/AAAAAAAAr3U/x5C0B9gWX_cL2WMEBH09k3Hb5xiZo0G0QCLcBGAs/s1600/Poly00.jpg)](https://youtu.be/UEybiL0i-uM)
