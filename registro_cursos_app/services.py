from .models import *


def crear_curso(codigo:str, nombre:str, version:int):
    curso = Curso(
        codigo = codigo,
        nombre = nombre,
        version = version
    )
    curso.save()
    return curso

def crear_profesor(rut:str, nombre:str, apellido:str, activo:bool, creado_por:str):
    profesor = Profesor(
        rut = rut,
        nombre = nombre,
        apellido = apellido,
        activo = activo,
        creado_por = creado_por
    )
    profesor.save()
    return profesor
    
    

def crear_estudiante(rut:str, nombre:str, apellido:str, fecha_nac:str, activo:bool, creado_por:str):
    estudiante = Estudiante(
        rut = rut,
        nombre = nombre,
        apellido = apellido,
        fecha_nac = fecha_nac,
        activo = activo,
        creado_por = creado_por
    )
    estudiante.save()
    return estudiante

def crear_direccion(calle:str, numero:str, comuna:str, region:str, estudiante_rut:str):
    estudiante = obtiene_estudiante(estudiante_rut)
    direccion = Direccion(
        calle = calle,
        numero = numero,
        comuna = comuna,
        region = region,
        estudiante = estudiante
    )
    direccion.save()
    return direccion

def obtiene_estudiante(estudiante_rut:str):
    estudiante = Estudiante.objects.get(rut=estudiante_rut)
    return estudiante

def obtiene_profesor(profesor_rut:str):
    profesor = Profesor.objects.get(rut=profesor_rut)
    return profesor

def obtiene_curso(codigo_curso):
    curso = Curso.objects.get(codigo=codigo_curso)
    return curso

def agrega_profesor_a_curso(profesor_rut, codigo_curso):
    profesor = obtiene_profesor(profesor_rut)
    curso = obtiene_curso(codigo_curso)
    curso.profesor.rut = profesor
    curso.profesor.add(profesor)
    curso.save()

def agrega_cursos_a_estudiante(curso_codigo, estudiante_rut):
    curso = obtiene_curso(curso_codigo)
    estudiante = obtiene_estudiante(estudiante_rut)

    if curso is not None and estudiante is not None:
        curso.estudiante = estudiante  # Asignar el estudiante al curso
        curso.save()
    # else:
    #     if curso is None:
    #         print(f"No se encontró un curso con el código: {codigo_curso}")
    #     if estudiante is None:
    #         print(f"No se encontró un estudiante con el RUT: {estudiante_rut}")

def imprime_estudiante_cursos(estudiante_rut:str):
    estudiante=obtiene_estudiante(estudiante_rut)
    cursos=estudiante.cursos.all()
    print(f'Estudiante: {estudiante.nombre} {estudiante.apellido}')
    print(f'Cursos tomados: ')
    for curso in cursos:
        print(f'{curso.nombre} {curso.codigo}')
    