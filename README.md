Para testear:
-   crear carpeta management
-   dentro de management crear carpeta commands
-   dentro de commands crear archivos que se quieren usar
-   escribir:
-   archivo para pruebas es pruebas.py:
    -   from django.core.management.base import BaseCommand
    -   from registro_cursos_app.services import *  (nombre_aplicacion.services)
    -   crea clase Command:
                            class Command(BaseCommand):
                                def handle(self, *args, **kwargs):
                                    pass

    -   bajo este se empiezan a crear las funciones
-   para correrlo en terminal:
    -   py manage.py pruebas