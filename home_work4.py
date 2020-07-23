# Una escuela tiene alumnos, cuyas características son:

# *Nombre
# *Apellido
# *Nota Matematica
# *Nota Lengua
# *Nota geografía
# *Promedio
# -Los alumnos pueden dar exámenes.

# La escuela también tiene profesores que tienen las siguientes características:

# *Nombre
# *Apellido
# *Materia que enseña

# -Los profesores toman exámenes y le dan al alumno una nota.

# Se deben cargar distintos alumnos y profesores, que los alumnos den exámenes que toman los profesores y que el 
# resultado sea una nota. El alumno siempre debe tener un promedio (al principio las tres notas son 0).


#-------------------------------------------------------------------------------------------------------------

#Se crea una funcion donde se ingresa el nombre del profesor y la materia
def profesor():

    dic_profesores = {}
    i = 1

    for i in range(3):
    #Se crea undiccionario con el profesor y materia

        nombre_profesor = input("Ingrese nombre completo del profesor: ")
        key_nombre = 'nombre_profesor'
        dic_profesores.setdefault(key_nombre,[])
        dic_profesores['nombre_profesor'].append(nombre_profesor)

        materia = input("\nIngrese que materia de las siguientes da:\n matematicas\n lengua\n geografia\n")
        key_materia = 'materia'
        dic_profesores.setdefault(key_materia,[])
        dic_profesores['materia'].append(materia)

    i += 1

    return dic_profesores 

#-----------------------------------------------------------------------------------------
#A la funcion alumno ingresan las listas de los profesores por materia
def alumno(dic_profesores):
    
    print (f"prueba DICCIONARIO PROFESOR: {dic_profesores}")

    dic_alumno = {}
    nombre_alumno = input("Ingrese nombre y apellido del alumno: ")
    #Prueba diccionario
    print(f"Esto es para ver si funciona materio_dic {dic_profesores ['materia']}")

    tomo_examen = int(input("Colocar:\n 1 - Tomo examen\n 0 - No tomo el examen\n"))
    dic_profesores = dic_profesores
    
    nota_matematicas = 0
    nota_lengua = 0
    nota_geografia = 0

    #cant_profesores = len(dic_profesores) 

    if (tomo_examen == 1):
        values_mat_profe = dic_profesores ['materia']

        for item in values_mat_profe :
            
            if ( item == 'matematicas'):
                nota_matematicas = int(input("Ingrese la calificación de matematicas del 1-10\n"))
            if (item == 'lengua'):
                nota_lengua = int(input("Ingrese la calificación de lengua del 1-10\n"))
            if (item == 'geografia'):
                nota_geografia = int(input("Ingrese la calificación de geografia del 1-10\n"))

    #Se suman las notas de las 3 materias y se dividen entre el total para dar el promedio
    promedio_nota = (nota_matematicas + nota_lengua + nota_geografia)/3
    print(promedio_nota)
    
    dic_alumno[nombre_alumno] = promedio_nota
    #Se itera mientras tomo_examen =1 y pregunta dependiendo la materia que ingrese la nota ese profesor y se guarda en una variable
    print(dic_alumno)
 
#=======================MAIN============================================================

ingresar = '1'
while ingresar == '1':
    ingresar = input ("seleccione\n 1 - para ingresar un profesor \n 2 - para finalizar\n")
    if ingresar == '1':
        dic_profesores = profesor()
    else:
        ingresar_alumno = '1'
        while ingresar_alumno == '1':
            ingresar_alumno = input("seleccione\n 1 - para ingresar un alumno\n 2 - para finalizar\n")
            
            if ingresar_alumno == '1':
                alumno(dic_profesores)
            else:
                print("Se termino")
    