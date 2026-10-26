#TP3 Tomás Andino, Micaela Consiglio, Marian Soria, Luciano Villavicencio

import os
import pickle
import os.path
from datetime import datetime
from datetime import date
import datetime
from getpass import getpass

def clear():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")

class USUARIOS:
    def __init__(self):
        self.cod = 0
        self.usu = ' '.ljust(100,' ')
        self.clave = " ".ljust(8," ")
        self.tipo = " ".ljust(15," ")

class LOCALES:
    def __init__(self):
        self.codL = 0
        self.nomb = " ".ljust(50," ")
        self.ubi = " ".ljust(50," ")
        self.rub = " ".ljust(50," ")
        self.codu = 0
        self.act = "A".ljust(1," ")

class RUBROS:
    def __init__(self):
        self.rubro = " ".ljust(20," ")
        self.cantidad = 0
    
class PROMOCIONES:
    def __init__(self):
        self.codPromo = 0
        self.textP = " ".ljust(200, " ")
        self.fechaDP = date
        self.fechaHP = date
        self.semana = [0]*7
        self.estado = " ".ljust(10, " ")
        self.codLocal = 0

class USOPROMOCIONES:
    def __init__(self):
        self.codCliente = 0
        self.codPromo = 0
        self.fechaUP = date

class NOVEDADES:
    def __init__(self):
        self.codNovedad = 0
        self.textoN = " ".ljust(200, " ")
        self.fechaDN = date
        self.fechaHN = date
        self.tipoUsu = " ".ljust(20, " ")
        self.estado = " ".ljust(1," ")

MPrincipal = """
|================================================================|
| MENU PRINCIPAL                                                 |
| 1 - INGRESAR CON USUARIO REGISTRADO                            |
| 2 - REGISTRARSE COMO CLIENTE                                   |
| 3 - SALIR                                                      |
|================================================================|
"""

MAdministrador = """
|================================================================|
| MENU ADMINISTRADOR                                             |
| 1 - Gestion de locales                                         |
| 2 - Crear cuenta de dueños locales                             |
| 3 - Aprobar/Denegar solicitudes de descuentos                  |
| 4 - Gestion de novedades                                       |
| 5 - Reporte de utilizacion de descuentos                       |
| 0 - Salir                                                      |
|================================================================|
"""

MGestionLocales = """
|================================================================|
| MENU GESTION DE LOCALES                                        |
| a - Crear locales                                              |
| b - Modificar locales                                          |
| c - Eliminar locales                                           |
| d - Mapa locales                                               |
| e - Volver                                                     |
|================================================================|
"""

MDueñoLocal = """
|================================================================|
| MENU DUEÑO DE LOCAL                                            |
| 1 - Crear descuento                                            |
| 2 - Reporte de uso de descuentos                               |
| 3 - Ver novedades                                              |
| 0 - Salir                                                      |
|================================================================|
"""

MCliente = """
|================================================================|
| MENU CLIENTE                                                   |
| 1 - Buscar descuentos en locales                               |
| 2 - Solicitar descuentos                                       |
| 3 - Ver novedades                                              |
| 0 - Salir                                                      |
|================================================================|
"""

def ConteoRubros(rub):
    for i in range (3):
        rub = rub.strip()           #para borrarle los espacios en blanco y que compare correctamente
        if rub == (Rubros[i].rub).strip():
            Rubros[i].cant = Rubros[i].cant + 1

def RestaRubros(rub):
    for i in range (3):
        rub = rub.strip()           #para borrarle los espacios en blanco y que compare correctamente
        if rub == (Rubros[i].rub).strip():
            Rubros[i].cant = Rubros[i].cant - 1

def INICIALIZAR():
    global U
    global L
    global P
    global UP
    global Usuario_ARL
    global Usuario_ARF
    global Locales_ARF
    global Locales_ARL
    global Promociones_ARF
    global Promociones_ARL
    global UsoPromociones_ARF
    global UsoPromociones_ARL
    global Rubros

    U = USUARIOS()
    L = LOCALES()
    P = PROMOCIONES()
    UP = USOPROMOCIONES()

    Usuario_ARF = "./Usuarios.dat"
    if os.path.exists(Usuario_ARF):
        Usuario_ARL = open (Usuario_ARF, "r+b")
    else:
        Usuario_ARL = open (Usuario_ARF, "w+b")
        U.cod = 1
        U.usu = "admin@shopping.com"
        U.usu = U.usu.ljust(100," ")
        U.clave = "12345"
        U.clave = U.clave.ljust(8," ")
        U.tipo = "administrador"
        U.tipo = U.tipo.ljust(15," ")
        Usuario_ARL.seek(0,0)
        pickle.dump(U,Usuario_ARL)        
    
    Locales_ARF = "./Locales.dat"
    if os.path.exists(Locales_ARF):
        Locales_ARL = open (Locales_ARF, "r+b")
    else:
        Locales_ARL = open (Locales_ARF, "w+b")

    Promociones_ARF = "./Promociones.dat"
    if os.path.exists(Promociones_ARF):
        Promociones_ARL = open (Promociones_ARF, "r+b")
    else:
        Promociones_ARL = open (Promociones_ARF, "w+b")

    UsoPromociones_ARF = "./UsoPromociones.dat"
    if os.path.exists(UsoPromociones_ARF):
        UsoPromociones_ARL = open(UsoPromociones_ARF, "r+b")
    else:
        UsoPromociones_ARL = open(UsoPromociones_ARF, "w+b")

    Rubros = [None]*3                             #definicion de arreglo de registros     
    for i in range(3):             
        Rubros[i] = RUBROS()
        
    Rubros[0].rub = "indumentaria"
    Rubros[1].rub = "perfumeria"
    Rubros[2].rub = "comida"
    Rubros[0].cant = 0
    Rubros[1].cant = 0
    Rubros[2].cant = 0    
   
    t = os.path.getsize(Locales_ARF)
    if t != 0:
        Locales_ARL.seek(0)
        L = pickle.load(Locales_ARL)
        while Locales_ARL.tell() < t:
            if L.act == "A":
                ConteoRubros(L.rub)
            L = pickle.load(Locales_ARL)
        if L.act == "A":
            ConteoRubros(L.rub)
    
    # Muestra del contenido total de todos los archivos, por si se necesita
    """
    for i in range (3):
        print("RUBRO: ",Rubros[i].rub,"CANTIDAD: ",Rubros[i].cant)        

    print("--------------------------------------------------------------------------------------------------------------------------------------------")    

    tam = os.path.getsize(Usuario_ARF)
    Usuario_ARL.seek(0)
    U=pickle.load(Usuario_ARL)
    print(U.cod,U.usu,U.clave,U.tipo)
    while Usuario_ARL.tell()<tam:
        U=pickle.load(Usuario_ARL)
        print(U.cod,U.usu,U.clave,U.tipo)

    print("--------------------------------------------------------------------------------------------------------------------------------------------")    

    tam = os.path.getsize(Locales_ARF)
    if tam != 0:
        Locales_ARL.seek(0)
        L = pickle.load(Locales_ARL)
        print(L.codL,L.nomb,L.ubi,L.rub,L.codu,L.act)
        while Locales_ARL.tell() < tam:
            L = pickle.load(Locales_ARL)
            print(L.codL,L.nomb,L.ubi,L.rub,L.codu,L.act)

    print("--------------------------------------------------------------------------------------------------------------------------------------------")

    tam = os.path.getsize(Promociones_ARF)
    if tam != 0:
        Promociones_ARL.seek(0)
        P = pickle.load(Promociones_ARL)
        print(P.codPromo,P.codLocal,P.textP,P.fechaDP,P.fechaHP)
        while Promociones_ARL.tell() < tam:
            P = pickle.load(Promociones_ARL)
            print(P.codPromo,P.codLocal,P.textP,P.fechaDP,P.fechaHP)

    print("--------------------------------------------------------------------------------------------------------------------------------------------")

    tam = os.path.getsize(UsoPromociones_ARF)
    if tam != 0:
        UsoPromociones_ARL.seek(0)
        UP = pickle.load(UsoPromociones_ARL)
        print(UP.codPromo,UP.codCliente,UP.fechaUP)
        while UsoPromociones_ARL.tell() < tam:
            UP = pickle.load(UsoPromociones_ARL)
            print(UP.codPromo,UP.codCliente,UP.fechaUP)

    print("--------------------------------------------------------------------------------------------------------------------------------------------")       
    """
    
def OrdenarRubros():
    for i in range(2):
        for j in range(i+1,3):
            if Rubros[i].cant < Rubros[j].cant:
                aux1 = Rubros[i].cant
                Rubros[i].cant = Rubros[j].cant 
                Rubros[j].cant = aux1
                aux1 = Rubros[i].rub
                Rubros[i].rub = Rubros[j].rub 
                Rubros[j].rub = aux1
    print("--------------------------------------------------------------------------------------------------------------------------------------------")
    print("RUBRO".ljust(20," "),"CANTIDAD DE LOCALES")
    for i in range (3):
        print((Rubros[i].rub).ljust(20," "),Rubros[i].cant)
    print("--------------------------------------------------------------------------------------------------------------------------------------------")

def ValidarExistencia(usua):
    global U
    T = os.path.getsize(Usuario_ARF)
    Usuario_ARL.seek(0,0)
    Lugar = Usuario_ARL.tell()
    U = pickle.load(Usuario_ARL)    
    while (Usuario_ARL.tell() < T) and (U.usu.strip() != usua ):
        Lugar = Usuario_ARL.tell()
        U = pickle.load(Usuario_ARL)
    if U.usu.strip() == usua:
        return Lugar
    else:
        return -1
    
def ValidarNombre(nomb):
    global L
    T = os.path.getsize(Locales_ARF)
    if T != 0:
        Locales_ARL.seek(0,0)
        Lugar = Locales_ARL.tell()
        L = pickle.load(Locales_ARL)  
        tamR = Locales_ARL.tell()
        cantR = round(T/tamR)
        pri = 0
        ult = cantR - 1
        medio = (pri + ult)//2
        Locales_ARL.seek(medio * tamR,0)
        L = pickle.load(Locales_ARL)
        while pri < ult and (L.nomb).strip() != nomb:
            if nomb < L.nomb:
                ult = medio - 1
            else:
                pri = medio + 1
            medio = (pri + ult)//2
            Locales_ARL.seek(medio * tamR,0)
            L = pickle.load(Locales_ARL)
        if (L.nomb).strip() == nomb:
            return medio*tamR
        else:
            return -1
        return 0

def ValidarDueño(cod):
    global U
    T = os.path.getsize(Usuario_ARF)
    Usuario_ARL.seek(0,0)
    Lugar = Usuario_ARL.tell()
    U = pickle.load(Usuario_ARL)    
    while (Usuario_ARL.tell() < T) and (U.cod != cod ):
        Lugar = Usuario_ARL.tell()
        U = pickle.load(Usuario_ARL)
    if U.cod == cod:
        return Lugar
    else:
        return -1

def ValidarLocal(l):
    global L
    T = os.path.getsize(Locales_ARF)
    Locales_ARL.seek(0,0)
    Lugar = Locales_ARL.tell()
    L = pickle.load(Locales_ARL)    
    while (Locales_ARL.tell() < T) and (L.codL != int(l) ):
        Lugar = Locales_ARL.tell()
        L = pickle.load(Locales_ARL)
    if L.codL == int(l):
        return Lugar
    else:
        return -1        

def ValidarDescuento(des):
    global P
    T = os.path.getsize(Promociones_ARF)
    Promociones_ARL.seek(0)
    Lugar = Promociones_ARL.tell()
    P = pickle.load(Promociones_ARL)
    while (Promociones_ARL.tell() < T) and (P.codPromo != int(des)):
        Lugar = Promociones_ARL.tell()
        P = pickle.load(Promociones_ARL)
    if P.codPromo == int(des):
        return Lugar
    else:
        return -1
       
def IngresarCodu():
    global codu
    ban = 0
    codu = int(input("Ingrese codigo de usuario del dueño de local o 0 para cancelar la carga de local : "))
    if codu != 0:
        pos = ValidarDueño(codu)
        if pos == -1:
            print("El código ingresado es inválido")
        else:
            if U.tipo.strip() != "dueñoLocal":
                print("El código ingresado no pertenece a un dueño de local ")
            else:
                ban = 1
    else:
        ban = 2
    return ban

def OrdenarLocales():  
    tamarch = os.path.getsize(Locales_ARF)
    Locales_ARL.seek(0)
    L1 = pickle.load(Locales_ARL)
    tamreg = Locales_ARL.tell()
    cantreg = round(tamarch / tamreg)        
    for i in range (cantreg - 1):
        for j in range(i+1 , cantreg):
            P1 = i * tamreg
            Locales_ARL.seek(P1,0)
            L1 = pickle.load(Locales_ARL)
            P2 = j * tamreg
            Locales_ARL.seek(P2,0)
            L2 = pickle.load(Locales_ARL)
            if L1.nomb > L2.nomb:
                Locales_ARL.seek(P1,0)
                pickle.dump(L2, Locales_ARL)
                Locales_ARL.seek(P2, 0)
                pickle.dump(L1, Locales_ARL)
                Locales_ARL.flush()

def CrearLocales():
    L = LOCALES()
    respuesta = input("¿Desea crear un nuevo local? (S/N): ").upper()
    while respuesta != "S" and respuesta != "N":
        respuesta = input("¿Desea crear un nuevo local? (S/N): ").upper()
    while respuesta == "S":
        tam = os.path.getsize(Locales_ARF)
        if tam == 0:
            ultcod = 0
        else:
            Locales_ARL.seek(0)
            L = pickle.load(Locales_ARL)
            t = Locales_ARL.tell()
            ultcod = round(tam/t)
        L.codL = ultcod + 1 
        L.nomb = input("Ingrese el nombre del nuevo local: ")
        pos = ValidarNombre(L.nomb)
        while pos != -1: 
            print("Nombre no disponible. ")
            L.nomb = input("Ingrese el nombre del nuevo local: ")
            pos = ValidarNombre(L.nomb)
        L.nomb = L.nomb.ljust(50, " ")     # ajuste de los campos
        L.ubi = input("Ingrese la ubicacion del nuevo local: ")
        L.ubi = L.ubi.ljust(50, " ")
        L.rub = input("Ingrese rubro: (indumentaria/perfumeria/comida): ")
        while L.rub != "indumentaria" and L.rub != "perfumeria" and L.rub != "comida":
            L.rub = input("Rubro incorrecto. Ingrese el rubro (indumentaria/perfumeria/comida): ")
        L.rub = L.rub.ljust(50, " ")
        b = IngresarCodu()
        while b == 0:
            b = IngresarCodu()
        if b == 1:          
            L.codu = codu 
            L.act = "A"
            L.act = L.act.ljust(1, " ")
            ConteoRubros(L.rub)
            Locales_ARL.seek(0,2)
            pickle.dump(L,Locales_ARL)
            Locales_ARL.flush()
            clear()
            print( "Su local fue creado con exito!")
        respuesta = input("¿Desea crear un nuevo local? (S/N): ").upper()
        while respuesta != "S" and respuesta != "N":
            respuesta = input("¿Desea crear un nuevo local? (S/N): ").upper()
    OrdenarRubros()
    OrdenarLocales()  

def cargarArchivoL(p):
    Locales_ARL.seek(p,0)
    pickle.dump(L,Locales_ARL)   
    Locales_ARL.flush()
    print("Local modificado con exito!")

def ModificarLocal():
    global L
    mod = 1
    resp = input("¿Desea modificar un local? (S/N): ").upper()
    while resp != "S" and resp != "N":
        resp = input("Respuesta inválida. ¿Desea modificar un local? (S/N): ").upper()
    while resp == "S":    
        local = input("Ingrese el código de local que desea modificar: ")
        pos = ValidarLocal(local)
        while pos == -1:
            local = input("Código inválido ingrese el código de local que desea modificar: ")
            pos = ValidarLocal(local)
        Locales_ARL.seek(pos,0)    
        L = pickle.load(Locales_ARL) 
        if L.act == "B":
            print("El local \"",L.nomb.strip(),"\" esta inactivo, desea activarlo para poder modificarlo? (S/N): ")
            act = input().upper()
            while act != "S" and act != "N":
                print("El local \"",L.nomb.strip(),"\" esta inactivo, desea activarlo para poder modificarlo? (S/N): ")
                act = input().upper()
            if act == "N":
                mod = 0
        if mod == 1:
            atributo = input("Ingrese el atributo que desea modificar (nombre/ubicacion/rubro/dueño) o x para finalizar modificacion: ").lower()
            while atributo != "nombre" and atributo != "ubicacion" and atributo != "rubro" and atributo != "dueño" and atributo != "x":
                atributo = input("Atributo inválido. Ingrese el atributo que desea modificar (nombre/ubicacion/rubro/dueño) o x para finalizar modificacion: ").lower()
            while atributo != "x":
                if atributo == "nombre":
                    nomb = input("Ingrese el nombre del nuevo local: ")
                    posn = ValidarNombre(nomb)
                    while posn != -1: 
                        print("Nombre no disponible. ")
                        nomb = input("Ingrese el nuevo nombre del local: ")
                        posn = ValidarNombre(nomb)
                    Locales_ARL.seek(pos,0)
                    L = pickle.load(Locales_ARL)
                    L.nomb = nomb
                    L.nomb = L.nomb.ljust(50, " ")   
                    cargarArchivoL(pos)             
                elif atributo == "ubicacion":
                    L.ubi = input("Ingrese la nueva ubicacion del local: ")
                    L.ubi = L.ubi.ljust(50, " ")
                    cargarArchivoL(pos)
                elif atributo == "rubro":
                    rubant = L.rub
                    L.rub = input("Ingrese el nuevo rubro: (indumentaria/perfumeria/comida): ")
                    while L.rub != "indumentaria" and L.rub != "perfumeria" and L.rub != "comida":
                        L.rub = input("Rubro incorrecto. Ingrese el nuevo rubro (indumentaria/perfumeria/comida): ")                
                    RestaRubros(rubant)         #restar uno a rubro anterior
                    ConteoRubros(L.rub)         #agregar uno al nuevo rubro
                    L.rub = L.rub.ljust(50, " ")
                    cargarArchivoL(pos)
                else:
                    b = IngresarCodu()
                    while b == 0:
                        b = IngresarCodu()
                    if b == 1:          
                        L.codu = codu                
                        cargarArchivoL(pos)
                atributo = input("Ingrese el atributo que desea modificar (nombre/ubicacion/rubro/dueño) o x para finalizar modificacion: ").lower()
                while atributo != "nombre" and atributo != "ubicacion" and atributo != "rubro" and atributo != "dueño" and atributo != "x":
                    atributo = input("Atributo inválido. Ingrese el atributo que desea modificar (nombre/ubicacion/rubro/dueño) o x para finalizar modificacion: ").lower()   
        resp = input("¿Desea modificar un nuevo local? (S/N): ").upper()
        while resp != "S" and resp != "N":
            resp = input("Respuesta inválida. ¿Desea modificar un nuevo local? (S/N): ").upper()

def EliminarLocal():
    global L
    resp = input("¿Desea eliminar un local? (S/N): ").upper()
    while resp != "S" and resp != "N":
        resp = input("Respuesta inválida. ¿Desea eliminar un local? (S/N): ").upper()
    while resp == "S":    
        local = input("Ingrese el código de local que desea eliminar: ")
        pos = ValidarLocal(local)
        while pos == -1:
            local = input("Código inválido ingrese el código de local que desea eliminar: ")
            pos = ValidarLocal(local)
        Locales_ARL.seek(pos,0)    
        L = pickle.load(Locales_ARL)
        if L.act == "B":
            print("El local ya esta dado de baja.")
        else:
            print("¿Esta seguro que desea dar de baja el local \"",L.nomb.strip(),"\"? (S/N): ")
            rta = input().upper()
            while rta != "S" and rta != "N":
                print("¿Esta seguro que desea dar de baja el local ",L.nomb.strip(),"? (S/N): ")
                rta = input().upper()
            if rta == "S":
                L.act = "B"
                Locales_ARL.seek(pos,0)
                pickle.dump(L,Locales_ARL)
                Locales_ARL.flush()
                RestaRubros(L.rub)
                print("Local eliminado con exito")
        resp = input("¿Desea eliminar un nuevo local? (S/N): ").upper()
        while resp != "S" and resp != "N":
            resp = input("Respuesta inválida. ¿Desea eliminar un  nuevo local? (S/N): ").upper()

def MapaLocales():
    Loc = [str()]*5
    tamarch = os.path.getsize(Locales_ARF)
    Locales_ARL.seek(0)
    L = pickle.load(Locales_ARL)
    tamreg = Locales_ARL.tell()
    cantloc = round(tamarch / tamreg)
    filas = (cantloc // 5)
    extra = cantloc - (filas * 5)
    Locales_ARL.seek(0)
    if cantloc > 50:
        filas = 10
        extra = 0
    for i in range (filas):
        for i in range(5):           
            L = pickle.load(Locales_ARL)
            if L.act == "B":
                Loc [i] = str(-L.codL)
            else:
                Loc [i] = " " + str(L.codL)
        print ("+  -  +  -  +  -  +  -  +  -  +")
        print ("|",(Loc[0]).ljust(3," "),"|",(Loc[1]).ljust(3," "),"|",(Loc[2]).ljust(3," "),"|",(Loc[3]).ljust(3," "),"|",(Loc[4]).ljust(3," "),"|")
    if extra != 0:
        for i in range(extra):           
            L = pickle.load(Locales_ARL)
            if L.act == "B":
                Loc [i] = str(-L.codL)
            else:
                Loc [i] = " " + str(L.codL)
        for i in range(extra,5): 
            Loc[i] = " 0 " 
        filas = filas + 1
        print ("+  -  +  -  +  -  +  -  +  -  +")
        print ("|",(Loc[0]).ljust(3," "),"|",(Loc[1]).ljust(3," "),"|",(Loc[2]).ljust(3," "),"|",(Loc[3]).ljust(3," "),"|",(Loc[4]).ljust(3," "),"|")
    print ("+  -  +  -  +  -  +  -  +  -  +")
    if filas < 10:
        for i in range (10-filas):
            print ("|"," 0 ","|"," 0 ","|"," 0 ","|"," 0 ","|"," 0 ","|")
            print ("+  -  +  -  +  -  +  -  +  -  +")
    if cantloc > 50:
        print("Proximamente se habilitará un mapa con los demas locales...")
    
def MostrarLocales():
    print("=================================================================================================================================================================================")
    print("CODIGO".ljust(7," "),"NOMBRE".ljust(50," "),"UBICACION".ljust(50," "),"RUBRO".ljust(20," "),"CODIGO DUEÑO".ljust(13," "),"ESTADO")
    print("-----------------------------------------------------------------------------------------------------------------------------------------------------------------")
    tam = os.path.getsize(Locales_ARF)
    if tam != 0:
        Locales_ARL.seek(0)
        L = pickle.load(Locales_ARL)
        print(str(L.codL).ljust(7," "),L.nomb,L.ubi,(L.rub).strip().ljust(20," "),str(L.codu).ljust(13," "),L.act)   
        while Locales_ARL.tell() < tam:
            L = pickle.load(Locales_ARL)
            print(str(L.codL).ljust(7," "),L.nomb,L.ubi,(L.rub).strip().ljust(20," "),str(L.codu).ljust(13," "),L.act)
    print("=================================================================================================================================================================================")

def GestionLocales():
    clear()
    print(MGestionLocales)
    opcion = input("Ingrese la opcion: ").lower()
    while opcion != "a" and opcion != "b" and opcion != "c" and opcion != "d" and opcion != "e":
        clear()
        print("Opcion incorrecta. \n",MGestionLocales)
        opcion = input("Ingrese la opcion: ").lower()
    while opcion != "e":
        if opcion == "a":
            print ("LOCALES HASTA EL MOMENTO")
            MostrarLocales()
            print("CREAR LOCALES\n")
            CrearLocales()                                      #<3
        elif opcion == "b":
            tam = os.path.getsize(Locales_ARF)
            if tam != 0:
                print ("LOCALES HASTA EL MOMENTO")
                MostrarLocales()
                print("MODIFICAR LOCAL")
                ModificarLocal()
            else:
                print("No hay locales para modificar por el momento")
            clear()
        elif opcion == "c":
            tam = os.path.getsize(Locales_ARF)
            if tam != 0:
                print ("LOCALES HASTA EL MOMENTO")
                MostrarLocales()
                print("ELIMINAR LOCAL")
                EliminarLocal()
            else:
                print("No hay locales para eliminar por el momento")
            clear()
        elif opcion == "d":
            tam = os.path.getsize(Locales_ARF)
            if tam != 0:
                print ("MAPA DE LOCALES")
                MapaLocales()
            else: 
                print("No hay locales por el momento")
        print(MGestionLocales)
        opcion = input("Ingrese la opcion: ").lower()
        while opcion != "a" and opcion != "b" and opcion != "c" and opcion != "d" and opcion != "e":
            clear()
            print("Opcion incorrecta. \n",MGestionLocales)
            opcion = input("Ingrese la opcion: ").lower()

def Registrarse(tipousu):
    res = input("¿Esta seguro de que desea registrar una cuenta? (S/N): ").upper()
    while res != "S" and res != "N":
        res = input("Respuesta invalida ¿Esta seguro de que desea registrar una cuenta? (S/N): ").upper()
    while res != "N":
        usuario = input("Ingrese su mail: ")
        pos = ValidarExistencia(usuario)
        if pos == -1:
            password = input("Ingrese una contraseña de 8 caracteres: ")
            while len(password) != 8:
                password = input("Debe ingresar una contraseña de 8 caracteres: ")
            tam = os.path.getsize(Usuario_ARF)
            Usuario_ARL.seek(0)
            U = pickle.load(Usuario_ARL)
            t = Usuario_ARL.tell()
            ultcod = round(tam/t)
            U.cod = ultcod + 1 
            U.usu = usuario
            U.usu = U.usu.ljust(100," ")
            U.clave = password
            U.clave = U.clave.ljust(8, " ")
            U.tipo = tipousu
            U.tipo = U.tipo.ljust(15, " ")
            Usuario_ARL.seek(0,2)
            pickle.dump(U,Usuario_ARL)
            Usuario_ARL.flush()
            print("Usuario creado con exito.")
        else:
            print("Usuario ya existente.")
        res = input("¿Esta seguro de que desea registrar una cuenta? (S/N): ").upper()
        while res != "S" and res != "N":
            res = input("Respuesta invalida ¿Esta seguro de que desea registrar una cuenta? (S/N): ").upper()

def MostrarDescuentos():
    print("=================================================================================================================================================================")
    print("COD PROMO".ljust(12," "),"COD LOCAL".ljust(12," "),"NOMBRE ".ljust(20," "),"DESCRIPCION".ljust(40," "),"FECHA DESDE".ljust(15," "),"FECHA HASTA".ljust(15," "),"L","M","M","J","V","S","D","ESTADO".ljust(15," "))
    print("-----------------------------------------------------------------------------------------------------------------------------------------------------------------")
    tam = os.path.getsize(Promociones_ARF)
    if tam != 0:
        Promociones_ARL.seek(0)
        while Promociones_ARL.tell() < tam:
            P = pickle.load(Promociones_ARL)         
            if (P.estado).strip() == "Pendiente":
                pos = ValidarLocal(P.codLocal)
                print(str(P.codPromo).ljust(12," "), str(P.codLocal).ljust(12," "), (L.nomb).strip().ljust(20," "), (P.textP).strip().ljust(40," "), str(P.fechaDP).ljust(15," "), str(P.fechaHP).ljust(15," "), P.semana[0],P.semana[1],P.semana[2],P.semana[3],P.semana[4],P.semana[5],P.semana[6], (P.estado).strip().ljust(15," "))
    print("=================================================================================================================================================================")

def ASolicitudes():              
    clear()
    MostrarDescuentos()
    desc = input("Ingrese el codigo de descuento que desea aprobar o denegar o un 0 para finalizar: ")
    while desc != "0":
        pos = ValidarDescuento(desc)
        if pos == -1:
            print("Codigo de descuento invalido")
        elif (P.estado).strip() != "Pendiente":
            print("El codigo de descuento no se encuentra pendiente de aprobacion")
        elif (P.estado).strip() == "Pendiente":
            res = input("Ingrese la opcion deseada: \nA- Aprobar \nD- Denegar \nS- Salir\n").upper()
            while res != "A" and res != "D" and res != "S":
                res = input("Opcion invalida. Ingrese la opcion deseada: \nA- Aprobar \nD- Denegar \nS- Salir \n").upper()
            if res == "A":
                P.estado = "Aceptada"
                P.estado = P.estado.ljust(10," ")
                Promociones_ARL.seek(pos,0)
                pickle.dump(P,Promociones_ARL)
                Promociones_ARL.flush()
                print("Promocion aceptada con exito.")
            elif res == "D":
                P.estado = "Rechazada"
                P.estado = P.estado.ljust(10," ")
                Promociones_ARL.seek(pos,0)
                pickle.dump(P,Promociones_ARL)
                Promociones_ARL.flush()
                print("Promocion rechazada con exito.")
        desc = input("Ingrese el codigo de descuento que desea aprobar o denegar o un 0 para finalizar: ")
        clear()
        MostrarDescuentos()

def FechaReporte():
    global desde
    global hasta
    flag = True
    while flag:
        try:
            desde = input("Ingrese la fecha del comienzo para el reporte de uso de descuentos en el formato DD/MM/AAAA: ")
            datetime.datetime.strptime(desde, '%d/%m/%Y')
            flag = False
        except ValueError:
            print("Fecha inválida") 
    ban = 0
    while ban == 0:
        flag = True
        while flag:
            try:
                hasta = input("Ingrese la fecha de finalización para el reporte de uso de descuentos en el formato DD/MM/AAAA: ")
                datetime.datetime.strptime(hasta, '%d/%m/%Y')
                flag = False
            except ValueError:
                print("Fecha inválida")
        if hasta >  desde:
            ban = 1
        else:
            print("La fecha de finalización es anterior a la fecha de inicio del reporte. Intente nuevamente.")

def ReporteDescuentos():
    resp = input("¿Desea ver un reporte de uso de descuentos? (S/N): ").upper()
    while resp != "S" and resp != "N":
        resp = input("Opcion incorrecta ¿Desea ver un reporte de uso de descuentos? (S/N): ").upper()
    while resp != "N":
        clear()
        FechaReporte()
        T = os.path.getsize(Promociones_ARF)
        if T != 0:
            print("INFORME \n","Fecha desde: ",desde, "\t Fecha hasta: ",hasta)
            print("=========================================================================================================================================================")
            print("COD PROMO".ljust(11," "),"COD LOCAL".ljust(11," "),"DESCRIPCION".ljust(40," "),"FECHA DESDE".ljust(15," "),"FECHA HASTA".ljust(15," "),"L","M","M","J","V","S","D","CANTIDAD DE USOS ")
            Promociones_ARL.seek(0)
            while Promociones_ARL.tell()< T:
                P = pickle.load(Promociones_ARL)
                if (P.estado).strip() == "Aceptada" and desde <= P.fechaDP and hasta >= P.fechaHP:
                    cont = 0 
                    tam = os.path.getsize(UsoPromociones_ARF)
                    if tam != 0:
                        UsoPromociones_ARL.seek(0)
                        while UsoPromociones_ARL.tell() < tam:       
                            UP = pickle.load(UsoPromociones_ARL)
                            if UP.codPromo == P.codPromo:
                                cont = cont + 1    
                    print((str(P.codPromo)).ljust(11," "), (str(P.codLocal)).ljust(11," "), (P.textP).strip().ljust(40," "), (P.fechaDP).ljust(15," "), (P.fechaHP).ljust(15," "), P.semana[0],P.semana[1],P.semana[2],P.semana[3],P.semana[4],P.semana[5],str(P.semana[6]).ljust(5," "), cont)
            print("=========================================================================================================================================================")
        resp = input("¿Desea ver un reporte de uso de descuentos? (S/N): ").upper()
        while resp != "S" and resp != "N":
            resp = input("Opcion incorrecta ¿Desea ver un reporte de uso de descuentos? (S/N): ").upper()        

def MenuAdministrador():
    print(MAdministrador)
    opcion = input("Ingrese la opcion: ")
    while opcion != "1" and opcion != "2" and opcion != "3" and opcion != "4" and opcion != "5" and opcion != "0":
        clear()
        print("Opcion incorrecta. \n",MAdministrador)
        opcion = input("Ingrese la opcion: ")
    while opcion != "0":
        if opcion == "1":
            clear()
            print("GESTION DE LOCALES\n")           
            GestionLocales()
        elif opcion == "2":
            print("CREAR CUENTAS DE DUEÑOS DE LOCALES")
            Registrarse("dueñoLocal")
        elif opcion == "3":
            print("APROBAR/DENEGAR SOLICITUDES DE DESCUENTO")
            ASolicitudes()
        elif opcion == "4":
            print ("GESTION DE NOVEDADES- Solo chapin <3")
        elif opcion == "5":
            print("REPORTE DE UTILIZACION DE DESCUENTOS")
            ReporteDescuentos()
        print(MAdministrador)
        opcion = input("Ingrese la opcion: ")
        while opcion != "1" and opcion != "2" and opcion != "3" and opcion != "4" and opcion != "5" and opcion != "0":
            clear()
            print("Opcion incorrecta. \n",MAdministrador)
            opcion = input("Ingrese la opcion: ")

def CargaDescuento(local):
    global P
    tam = os.path.getsize(Promociones_ARF)           
    if tam == 0 :
        P.codPromo = 1
    else:
        Promociones_ARL.seek(0)
        P = pickle.load(Promociones_ARL)
        treg = Promociones_ARL.tell()
        P.codPromo = (round(tam/treg))+1         
    P.textP = input("Ingrese la descripción del descuento: ")
    P.textP = P.textP.ljust(200," ")
    ban = 0
    while ban == 0:
        flag = True
        while flag:
            try:
                P.fechaDP = input("Ingrese la fecha del comienzo de la promoción en el formato DD/MM/AAAA: ")
                datetime.datetime.strptime(P.fechaDP, '%d/%m/%Y')
                flag = False
            except ValueError:
                print("Fecha inválida") 
        hoy = str(date.today())
        a,m,d = hoy.split("-")
        hoy = d + "/" + m + "/" + a 
        if P.fechaDP >= hoy:
            ban = 1
        else:
            print("La fecha de inicio de la promoción es anterior a la fecha de hoy. Intente nuevamente.")
    ban = 0
    while ban == 0:
        flag = True
        while flag:
            try:
                P.fechaHP = input("Ingrese la fecha de finalización de la promoción en el formato DD/MM/AAAA: ")
                datetime.datetime.strptime(P.fechaHP, '%d/%m/%Y')
                flag = False
            except ValueError:
                print("Fecha inválida")
        if P.fechaHP >  P.fechaDP:
            ban = 1
        else:
            print("La fecha de finalización es anterior a la fecha de inicio de la promoción. Intente nuevamente.")
    for i in range (7):
        P.semana[i] = 0
    dia = input("Ingrese el número del dia de la semana en que es válida la promoción \n1- Lunes \n2- Martes \n3- Miércoles \n4- Jueves \n5- Viernes \n6- Sabádo \n7- Domingo \n0- Finalizar \n ")
    while dia != "0" and dia != "1" and dia != "2" and dia != "3" and dia != "4" and dia != "5" and dia != "6" and dia != "7":
        dia = input("Opcion incorrecta. Ingrese el número del dia de la semana en que es válida la promoción \n1- Lunes \n2- Martes \n3- Miércoles \n4- Jueves \n5- Viernes \n6- Sabádo \n7- Domingo \n0- Finalizar \n ")
    while dia != "0":                
        P.semana[int(dia)-1] = 1
        dia = input("Ingrese el número del dia de la semana en que es válida la promoción \n1- Lunes \n2- Martes \n3- Miércoles \n4- Jueves \n5- Viernes \n6- Sabádo \n7- Domingo \n0- Finalizar \n ")
        while dia != "0" and dia != "1" and dia != "2" and dia != "3" and dia != "4" and dia != "5" and dia != "6" and dia != "7":
            dia = input("Opcion incorrecta. Ingrese el número del dia de la semana en que es válida la promoción \n1- Lunes \n2- Martes \n3- Miércoles \n4- Jueves \n5- Viernes \n6- Sabádo \n7- Domingo \n0- Finalizar \n ")
    P.codLocal = int(local)
    P.estado = "Pendiente"
    P.estado = P.estado.ljust(10," ")
    Promociones_ARL.seek(0,2)
    pickle.dump(P,Promociones_ARL) 
    Promociones_ARL.flush()

def CrearDescuento():
    global P
    MostrarDescuentosDueño()         
    print("CREAR DESCUENTO")
    rta = input("¿Desea crear un nuevo descuento? (S/N): ").upper()
    while rta != "S" and rta != "N":
        rta = input("Respuesta invalida. ¿Desea crear un nuevo descuento? (S/N): ").upper()
    while rta == "S":
        loc = input("Ingrese le código del local para el que quiere crear un descuento: ")
        pos = ValidarLocal(loc)
        if pos == -1:
            print("Código de local inválido.")
        elif L.codu != codigoUsuario:
            print("No puede crear descuentos de locales que no le pertenecen.")
        elif L.act == "B":
            resp = input("El local no esta activo ¿Desea activarlo? (S/N): ").upper()
            while resp != "S" and resp != "N":
                resp = input("El local no esta activo ¿Desea activarlo? (S/N): ").upper()
            if resp == "S":
                L.act = "A"
                Locales_ARL.seek(pos,0)
                pickle.dump(L, Locales_ARL)
                Locales_ARL.flush()
                CargaDescuento(loc)
        else:
            CargaDescuento(loc)
        clear()
        MostrarDescuentosDueño()         
        print("CREAR DESCUENTO")
        rta = input("¿Desea crear un nuevo descuento? (S/N): ").upper()
        while rta != "S" and rta != "N":
            rta = input("Respuesta invalida. ¿Desea crear un nuevo descuento? (S/N): ").upper()

def MostrarDescuentosDueño():
    print("=================================================================================================================================================================")
    print("CODIGO".ljust(10," "),"LOCAL".ljust(5," "),"DESCRIPCION".ljust(40," "),"FECHA DESDE".ljust(15," "),"FECHA HASTA".ljust(15," "),"L","M","M","J","V","S","D","ESTADO".ljust(15," "))
    print("-----------------------------------------------------------------------------------------------------------------------------------------------------------------")
    tam = os.path.getsize(Promociones_ARF)
    if tam != 0:
        Promociones_ARL.seek(0)
        hoy = str(date.today())
        a,m,d = hoy.split("-")
        hoy = d + "/" + m + "/" + a
        while Promociones_ARL.tell() < tam:
            P = pickle.load(Promociones_ARL)
            pos = ValidarLocal(P.codLocal)
            if L.act == "A" and L.codu == codigoUsuario and P.fechaHP > hoy and P.fechaDP <= hoy:
                print(str(P.codPromo).ljust(10," "),str(P.codLocal).ljust(5," "), P.textP.strip().ljust(40," "), P.fechaDP.ljust(15," "), P.fechaHP.ljust(15," "), P.semana[0],P.semana[1],P.semana[2],P.semana[3],P.semana[4],P.semana[5],P.semana[6], P.estado.ljust(15," ")  )
    print("=================================================================================================================================================================")

def BuscarDescuento():                                              
    loc = input("Ingrese el codigo de local del que quiere ver las promociones o 0 para finalizar: ")   
    while loc != "0":
        pos = ValidarLocal(loc)
        if pos != -1:
            ban = 0
            while ban == 0:
                flag = True
                while flag:
                    try:
                        fecha = input("Ingrese la fecha para la que desea ver las promociones en el formato DD/MM/AAAA: ")
                        datetime.datetime.strptime(fecha, '%d/%m/%Y')
                        flag = False
                    except ValueError:
                        print("Fecha inválida") 
                hoy = str(date.today())
                a,m,d = hoy.split("-")
                hoy = d + "/" + m + "/" + a 
                if fecha >= hoy:
                    ban = 1
                else:
                    print("La fecha ingresada es anterior a la fecha de hoy. Intente nuevamente.")
            print("--------------------------------------------------------------------------------------------------------------------------------------------")
            tam = os.path.getsize(Promociones_ARF)
            if tam != 0:
                Promociones_ARL.seek(0)
                P = pickle.load(Promociones_ARL)
                d,m,a = fecha.split("/")
                fec = datetime.date(int(a),int(m),int(d))
                dia = fec.weekday()
                if P.codLocal == L.codL and fecha >= P.fechaDP and fecha <= P.fechaHP and (P.estado).strip() == "Aceptada" and P.semana[dia] == 1:
                    print(P.codPromo, P.textP, P.fechaDP, P.fechaHP)
                while Promociones_ARL.tell() < tam:
                    P = pickle.load(Promociones_ARL)
                    if P.codLocal == L.codL and fecha >= P.fechaDP and fecha <= P.fechaHP and (P.estado).strip() == "Aceptada" and P.semana[dia] == 1:
                        print(P.codPromo, P.textP, P.fechaDP, P.fechaHP)
            print("--------------------------------------------------------------------------------------------------------------------------------------------")
        else:   
            print("Codigo de local invalido")
        loc = input("Ingrese el codigo de local del que quiere ver las promociones o 0 para finalizar: ")

def SolicitarDescuento():
    desc = input("Ingrese el codigo de promocion que desea utilizar o 0 para salir: ")
    while desc != "0":
        pos = ValidarDescuento(desc)
        if pos != -1:
            hoy = date.today()
            dia = hoy.weekday()
            hoy = str(date.today())
            a,m,d = hoy.split("-")
            hoy = d + "/" + m + "/" + a
            if (P.estado).strip() == "Aceptada" and P.fechaDP <= hoy and P.fechaHP >= hoy and P.semana[dia] == 1:
                UP.codCliente = codigoUsuario
                UP.codPromo = int(desc)
                UP.fechaUP = hoy
                UsoPromociones_ARL.seek(0,2)
                pickle.dump(UP,UsoPromociones_ARL)
                UsoPromociones_ARL.flush()
                print("Promocion utilizada con exito ")
            else:
                print("La promocion no es valida")
        else:
            print("Codigo de promocion invalido")
        desc = input("Ingrese el codigo de promocion que desea utilizar o 0 para salir: ")

def Menucliente():  
    clear()
    print(MCliente,"\n")
    opcion = input("Ingresar opcion: ")
    while opcion != "1" and opcion != "2" and opcion != "3" and opcion != "0":
        clear()
        print("Opcion incorrecta. \n",MCliente)
        opcion = input("Ingresar opcion: ")
    clear()
    while opcion != "0":
        if opcion == "1":
            BuscarDescuento()
        elif opcion == "2":
            SolicitarDescuento()
        elif opcion == "3":
            print("Ver novedades - Solo chapin <3")
        clear()
        print(MCliente,"\n")
        opcion = input("Ingresar opcion: ")
        while opcion != "1" and opcion != "2" and opcion != "3" and opcion != "0":
            clear()
            print("Opcion incorrecta. \n",MCliente)
            opcion = input("Ingresar opcion: ")        

def ReporteDescuentosDueños():
    resp = input("¿Desea ver un reporte de uso de descuentos? (S/N): ").upper()
    while resp != "S" and resp != "N":
        resp = input("Opcion incorrecta ¿Desea ver un reporte de uso de descuentos? (S/N): ").upper()
    while resp != "N":
        FechaReporte()
        TAM = os.path.getsize(Locales_ARF)
        if TAM != 0:
            clear()
            print("INFORME \n","Fecha desde: ",desde, "\t Fecha hasta: ",hasta)
            Locales_ARL.seek(0)
            while Locales_ARL.tell()<TAM:
                L = pickle.load(Locales_ARL)
                if L.codu == codigoUsuario:
                    T = os.path.getsize(Promociones_ARF)
                    if T != 0:
                        Promociones_ARL.seek(0)
                        ban = 0
                        while Promociones_ARL.tell()< T:
                            P = pickle.load(Promociones_ARL)
                            if (P.estado).strip() == "Aceptada" and desde <= P.fechaDP and hasta >= P.fechaHP and P.codLocal == L.codL:
                                cont = 0 
                                tam = os.path.getsize(UsoPromociones_ARF)
                                if tam != 0:
                                    UsoPromociones_ARL.seek(0)
                                    while UsoPromociones_ARL.tell() < tam:       
                                        UP = pickle.load(UsoPromociones_ARL)
                                        if UP.codPromo == P.codPromo:
                                            cont = cont + 1
                                if ban == 0:
                                    print("=========================================================================================================================")
                                    print("CODIGO LOCAL".ljust(15," "),"NOMBRE LOCAL".ljust(20," "))
                                    print(str(L.codL).ljust(15," "),str(L.nomb).ljust(20," "))
                                    print("-------------------------------------------------------------------------------------------------------------------------")
                                    print("Codigo Promo".ljust(13," "),"Texto".ljust(40," "),"Fecha desde".ljust(15," "),"Fecha hasta".ljust(15," "),"Cantidad de usos")    
                                    ban = 1
                                tex = (P.textP).strip()
                                print((str(P.codPromo)).ljust(13," "), tex.ljust(40," "), str(P.fechaDP).ljust(15," "), str(P.fechaHP).ljust(15," "), cont)

        resp = input("¿Desea ver un reporte de uso de descuentos? (S/N): ").upper()
        while resp != "S" and resp != "N":
            resp = input("Opcion incorrecta ¿Desea ver un reporte de uso de descuentos? (S/N): ").upper()

def MenuDueño():
    clear()
    print(MDueñoLocal,"\n")
    opcion = input("Ingrese opcion: ")
    while opcion != "1" and opcion != "2" and opcion != "3" and opcion != "0":
        clear()
        print("Opcion incorrecta. \n",MDueñoLocal)
        opcion = input("Ingrese opcion: ")
    clear()
    while opcion != "0":
        if opcion == "1":   
            CrearDescuento()
        elif opcion == "2":
            print("REPORTE DE USO DE DESCUENTOS")
            ReporteDescuentosDueños()
        elif opcion == "3":
            print("VER NOVEDADES")
        print(MDueñoLocal,"\n")
        opcion = input("Ingrese opcion: ")
        while opcion != "1" and opcion != "2" and opcion != "3" and opcion != "0":
            clear()
            print("Opcion incorrecta. \n",MDueñoLocal)
            opcion = input("Ingrese opcion: ")             

def Ingresar():
    global codigoUsuario
    intentos = 0
    while intentos < 3:
        usuario = str(input("Ingrese usuario: "))
        clave = str(getpass("Ingrese la contraseña: "))
        pos = ValidarExistencia(usuario)
        codigoUsuario = U.cod
        if pos == -1:
            intentos = intentos + 1
            print("Usuario incorrecto")
        else:
            if U.clave.strip() == clave:
                print("Ingreso correctamente")
                intentos = 4
                if U.tipo.strip() == "administrador":
                    clear()         
                    MenuAdministrador()      
                elif U.tipo.strip() == "dueñoLocal":
                    clear()
                    MenuDueño()
                else :
                    Menucliente()
                    print ("Menu Cliente")
            else:
                print("contraseña incorrecta")
                intentos = intentos + 1
        if intentos == 3:
            print ("Se han acabado los intentos")

def MENUPPAL():
    print(MPrincipal,"\n")
    opcion = input("Ingrese opcion: ")
    while opcion != "1" and opcion != "2" and opcion != "3":
         clear()
         print("Opcion incorrecta. \n",MPrincipal,"\n")
         opcion = input("Ingrese opcion: ")
    clear()
    while opcion != "3":
        if opcion == "1":
            Ingresar()
        elif opcion == "2":
            Registrarse("cliente")
        else:
            print("Adiós")
        clear()
        print(MPrincipal,"\n")
        opcion = input("Ingrese opcion: ")        
        while opcion != "1" and opcion != "2" and opcion != "3":
            clear()
            print("Opcion incorrecta. \n",MPrincipal,"\n")
            opcion = input("Ingrese opcion: ")

def FINALIZAR():
    Usuario_ARL.close()
    Locales_ARL.close()
    Promociones_ARL.close()
    UsoPromociones_ARL.close()

#------------------------------------------------------------------------------PROGRAMA PRINCIPAL--------------------------------------------------------------------------------#

INICIALIZAR()
MENUPPAL()
FINALIZAR()








