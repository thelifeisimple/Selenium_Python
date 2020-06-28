nombreCompleto = input("Ingrese su nombre y un apellido: ")
notaMatematica = int(input("Ingrese nota de matematicas: "))
notaLiteratura = int(input("Ingrese nota de literatura: "))
notaFisica = int(input("Ingrese nota de fisica: "))

promedio =float((notaMatematica + notaFisica + notaLiteratura)/3)


if promedio > 6:
    print("Aprobado")
    if promedio > 9:
        print("Alumno destacado")
if promedio < 4:
    print("Insuficiente")
if promedio > 4 and promedio < 5.9999999:
    print ("Recuperatorio")

