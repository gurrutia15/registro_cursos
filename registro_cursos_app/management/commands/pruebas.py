from django.core.management.base import BaseCommand
from registro_cursos_app.services import *

class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        imprime_estudiante_cursos('2-3')
        print('Prueba lograda')






# crear_curso('JA02', 'Full Stack Java', 1)
# crear_profesor('1-3', 'Bernardita', 'Retamal', True, 'Fernando')
# crear_estudiante('2-4', 'Felipe', 'Arenas', '1997-05-29', True, 'Fernando')
# crear_direccion('Los Leones', '999', 'Providencia', 'Metropolitana', '2-4')
# obtiene_estudiante('2-2')
# obtiene_profesor('1-2')
# obtiene_curso('JS02')
# agrega_profesor_a_curso('1-3', 'JS02')
# agrega_cursos_a_estudiante('JA02', '2-3')