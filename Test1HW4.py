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

dic_profesores = {'nombre_profesor': ['p1', 'p2', 'p3'], 'materia': ['matematicas', 'lengua', 'geografia']}

ingresar_alumno = '1'
while ingresar_alumno == '1':
    ingresar_alumno = input("seleccione\n 1 - para ingresar un alumno\n 2 - para finalizar\n")
    if ingresar_alumno == '1':
        alumno(dic_profesores)
    else:
        print("Se termino")
    