Hermes Sanchez - 27150619
EL proyecto consta de 4 capaz,

La capa Views
    Esta se encarga para monstrar la informacion en el sistema e interactuar con el usuario.
La capa Controllers
    Esta se encarga de recibir los eventos de entrada, y permite gestionar los servicios a utilizar
La capa de Services
    Esta se encarga de interactuar con el modelo de la informacion, lo gestiona y organiza para mandarselo al controlador la data ya estructurada.
La capa de Models
    Esta es la capa mas pura del sistema, y es la representate de las cosas en el mundo real en el sistema, como es en este proyecto, de los usuarios.


Manejo de excepciones
    Existen 2 principales posibilidades en el sitema:
        Las excepciones del modelos
            Estas ocurren al no tener informacion cargada en el sistema, se generan en el modelo y se transmiten por las distintas capaz del proyecto.
        Las excepciones de las vistas:
            Estas ocurren al seleccionar mal un valor, como por ejemplos, cuando se pide un numero, y se ingresa una letra.

Todas las funciones tienen solo un metodo publico y un nombre autoexplicativo, facilitando la legibilidad del codigo al cumplir la S de los principios SOLID.
