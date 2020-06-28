# Dada una concesionaria de autos, 5 clientes van a pedir un auto, debe preguntarsele:

# *Nombre y apellido del comprador.
# *Marca
# *Puertas
# *Color

# Marcas posibles y sus precios:

# -Ford $100000
# -Chevrolet: $120000
# -Fiat: $80000

# -Por la cantidad de puertas se añade un precio:

# -2: $50000
# -4: $65000
# -5: $78000

# Dependiendo del color, se deben sumar:

# -Blanco: $10000
# -Azul: $20000
# -Negro: $30000

# Deben imprimirse los datos de cada compra y el precio total.


def definir_marca(marca_ar):

    d_marca = marca_ar

    if(d_marca == '1'):
        m_valor = 100000
        return(m_valor)
    if(d_marca == '2'):
        m_valor = 120000
        return(m_valor)
    if(d_marca == '3'):
        m_valor = 80000
        return(m_valor)
    else:
        print("Valor incorrecto marca: " + d_marca)
 
def cantidad_puertas(puertas_ar):

    c_puertas = puertas_ar

    if(c_puertas == '2'):
        p_valor = 50000
        return(p_valor)
    if(c_puertas == '4'):
        p_valor = 65000
        return(p_valor)
    if(c_puertas == '5'):
        p_valor = 78000
        return(p_valor)
    else:
        print("Valor incorrecto puertas: " + c_puertas)

def tipo_color(color_ar):

    t_color = color_ar

    if (t_color == '1'):
        v_color = 10000
        return(v_color)
    if (t_color == '2'):
        v_color = 20000
        return(v_color)
    if (t_color == '3'):
        v_color = 30000
        return(v_color)
    else:
        print("Valor incorrecto marca: " + t_color)

def total_auto(f_name_ar, marca_ar, puertas_ar, color_ar):

    total_autos =[] 

   #f_name = f_name_ar
    print ("Comprador : "+ f_name_ar)

    marca_el = marca_ar
    total_autos.append(marca_el)
    print(f"Total marca $ {marca_ar}")

    puertas_cant = puertas_ar
    total_autos.append(puertas_cant)
    print(f"Total puertas $ {puertas_ar}")

    t_color = int (color_ar)
    total_autos.append(t_color)
    print(f"Total color $ {color_ar}")

    total_compra = sum (total_autos)
    print (f"El total a pagar es $  {total_compra}")
    


saludo = "Buenas tardes, ingrese los datos para saber el valor del auto que quiere comprar "
print(saludo)

for i in range (5):

    full_name = (input("Escriba su nombre completo: "))
    #print (full_name)
    marca = input("Elija una marca:  \n 1 Ford\n 2 Chevrolet\n 3 Fiat\n")
    #print(marca)
    puertas = input("Elija cantidad de puertas: \n 2 \n 4 \n 5 \n")
    #print(puertas)
    color = input("Elija un color: \n1 Blanco \n2 Azul \n3 Negro \n")
    #print(color)

    marca_ar = definir_marca(marca)
    puertas_ar = cantidad_puertas(puertas)
    color_ar = tipo_color(color)
    total_auto(full_name, marca_ar, puertas_ar, color_ar)

    
    i= i + 1    

