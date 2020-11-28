from datetime import date


class Actividad:
    def __init__(self, nombre, dia, mes, estado):
        self.nombre = nombre
        self.dia = dia
        self.mes = mes
        self.estado = estado
        
def fecha_actual():
    #Día actual
    hoy = date.today()
    dia = format(hoy.day)
    mes = format(hoy.month)
    return dia, mes

def fecha_a_consultar():
    dia_a_consultar = input("Ingrese la fecha a averiguar: ")
    mes_a_consultar = input("Ingrese el mes a consultar: ")
    return dia_a_consultar, mes_a_consultar

def comparacion_dias(dia, dia_a_consultar, mes, mes_a_consultar):
    if ((dia == dia_a_consultar) and (mes == mes_a_consultar)):
        pass

def nueva_actividad(vec_act):
    print("Registro de Actividades...")
    print("Ingrese los valores con numeros...")
    nom_act = input("Titulo: ")
    dia_act = input("Dia: ")
    mes_act = input("Mes: ")
    est_act = input("Estado: ")
    vec_act.append(Actividad(nom_act, dia_act, mes_act, est_act))
    
def to_string(vec_act): #RETOCAR
    for i in range(len(vec_act)):
        print(vec_act[i].nombre)
        print(vec_act[i].dia)
        print(vec_act[i].mes)
        print(vec_act[i].estado)

def crear_vector():
    vec_act = []
    return vec_act

def grabar_archivo(vec_act):
    archivo = open('C:\Users\kelop\Desktop\to_do_list.txt', 'wb')
    archivo.write(vec_act)





nueva_actividad(vec_act)
to_string(vec_act)
    
 






