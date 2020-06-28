# Dado el problema anterior del concesionario de autos debemos modificarlo, teniendo en cuenta:

# 1-Ya no sabemos cuantos clientes tendremos,
# 2-Si el pedido no es uno de los autos en venta, entonces debe volver a preguntar hasta que si lo sea
# 3-Lo mismo con la cantidad de puertas y los colores.
# 4-Al final se pregunta si hay otro cliente o no, si hay otro cliente, entonces vuelve a preguntar todo.
# 5-Si la cantidad de clientes fue:
# --5.1: 0 a 5 personas no hay descuento
# --5.2: 6 a 10 personas: hay un descuento del 10%
# --5.3: 11 a 50 personas: hay un descuento del 15%
# --5.4: Más de 50 personas: El descuento es del 18%
# 6-Solo se va a mostrar que se vendió al final del programa

def definir_marca(marca_ar):

    d_marca = marca_ar

    if(d_marca == '1'):
        m_valor = 100000
        return(m_valor)
    elif(d_marca == '2'):
        m_valor = 120000
        return(m_valor)
    elif(d_marca == '3'):
        m_valor = 80000
        return(m_valor)   
    else:
        print(" ERROR: Valor incorrecto marca: " + d_marca)
        return 0

 
def cantidad_puertas(puertas_ar):

    c_puertas = puertas_ar

    if(c_puertas == '2'):
        p_valor = 50000
        return(p_valor)
    elif(c_puertas == '4'):
        p_valor = 65000
        return(p_valor)
    elif(c_puertas == '5'):
        p_valor = 78000
        return(p_valor)
    else:
        print(" ERROR:  Valor incorrecto puertas: " + c_puertas)
        return False

def tipo_color(color_ar):

    t_color = color_ar
    
    if (t_color == '1'):
        v_color = 10000
        return(v_color)
    elif (t_color == '2'):
        v_color = 20000
        return(v_color)
    elif (t_color == '3'):
        v_color = 30000
        return(v_color)
    else:
        print(" ERROR: Valor incorrecto marca: " + t_color)
        return False

def total_auto(f_name_ar, marca_ar, puertas_ar, color_ar,cant_clientes_ar):

    total_autos =[] 

    print ("Comprador : "+ f_name_ar)

    marca_el = marca_ar
    total_autos.append(marca_el)
    print(f"Total marca $ {marca_ar}")

    puertas_cant = puertas_ar
    total_autos.append(puertas_cant)
    print(f"Total puertas $ {puertas_ar}")

    t_color = (color_ar)
    total_autos.append(t_color)
    print(f"Total color $ {color_ar}")

    clientes = cant_clientes_ar

    if (clientes < 2):#modifique numero
        total_compra = sum (total_autos)
        print("No tiene descuento ")
        return (f"El total a pagar es $ {total_compra}")

    elif (clientes > 2 and clientes <= 10):#modifique numero
        print("Despuesto del 10%")
        total_compra = sum (total_autos) * 1.1
        return (f"El total a pagar es $ {total_compra}")

    elif (clientes >= 10 and clientes <=50):
        print("Despuesto del 15%")
        total_compra = sum (total_autos) * 1.15
        return (f"El total a pagar es $ {total_compra}")

    elif (clientes >50):
        print("Despuesto del 18%")
        total_compra = sum (total_autos) * 1.18
        return (f"El total a pagar es $ {total_compra}")
    else:
        print("NO HAY DESCUENTO TOTAL_AUTOS")   
    
    # total_compra = sum (total_autos)
    # print(f"El total a pagar es $ {total_compra}") 
    
    

#----------------------------------------------------------------------------------------
def clase_principal():

    print("INICIO")
    agregar_cliente = 1

    while agregar_cliente == 1:

        clientes = []
        full_name = (input("Escriba su nombre completo: "))
        clientes.append(full_name)
        
        while True:
            marca = input("Elija un numero con la marca deseada y enter:  \n 1 - Ford\n 2 - Chevrolet\n 3 - Fiat\n")
            marca_ar = definir_marca(marca)
            if (marca_ar != 0):
                break
        
        while True:
            puertas = input("Elija cantidad de puertas desada y enter: \n 2 \n 4 \n 5 \n")
            puertas_ar = cantidad_puertas(puertas)
            if (puertas_ar != False):
                break

        while True:
            color = input("Elija un numero con el color deseado y enter: \n1 - Blanco \n2 - Azul \n3 - Negro \n")
            color_ar = tipo_color(color)
            if(color_ar != False):
                break

        cant_clientes = len(clientes)
        total_auto(full_name, marca_ar, puertas_ar, color_ar,cant_clientes)

        agregar_cliente = int(input("Ingrese un numero y presione enter:\n 1 - Crear un cliente\n 2 - Finalizar\n"))            
     
#======================main===================

clase_principal()

    