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

<iframe width="900" height="506" src="https://www.youtube.com/embed/7y6xFn3h1KI" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

## Polymorph
Luego de la conexión entre Pure-FTPd server y FileZilla Client, se puede utilizar el framework Polymorph para interceptar, capturar y modificar tráfico entre estos, a continuación se deja enlace a esta herramienta y demostración de uso:

-Polymorph: https://github.com/shramos/polymorph

## Video 2 - (Utilizando Polymorph):
https://www.youtube.com/watch?v=UEybiL0i-uM
