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

[Video1](https://youtu.be/7y6xFn3h1KI)

<a href="https://youtu.be/7y6xFn3h1KI" target="_blank"><img src="https://img.youtube.com/vi/7y6xFn3h1KI/maxresdefault.jpg" 
alt="IMAGE ALT TEXT HERE" width="400" height="225"/></a>

## Polymorph
Luego de la conexión entre Pure-FTPd server y FileZilla Client, se puede utilizar el framework Polymorph para interceptar, capturar y modificar tráfico entre estos, a continuación se deja enlace a esta herramienta y demostración de uso:

-Polymorph: https://github.com/shramos/polymorph

## Video 2 - (Utilizando Polymorph):

[Video2](https://youtu.be/UEybiL0i-uM)

<a href="https://youtu.be/UEybiL0i-uM" target="_blank"><img src="https://img.youtube.com/vi/UEybiL0i-uM/maxresdefault.jpg" 
alt="IMAGE ALT TEXT HERE" width="400" height="225"/></a>

## Video 3 - (IDS para protocolo FTP):

[Video3](https://youtu.be/5yof-fv6nYE)

<a href="https://youtu.be/5yof-fv6nYE" target="_blank"><img src="https://img.youtube.com/vi/5yof-fv6nYE/maxresdefault.jpg" 
alt="IMAGE ALT TEXT HERE" width="400" height="225"/></a>
