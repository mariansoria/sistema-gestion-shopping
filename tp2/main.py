"""Trabajo Práctico nro 2 de AyED - ISI com 05"""

import os

def clear():
	os.system('cls' if os.name == 'nt' else 'clear')

# Variables: 
# int: aux2, aux3, cont, p, q, codUsuario, op1, op2, op3, i, j, m, n, x, y, pos, pri, ult, med, t, c, codigo, numerocodlocal, intentos, intentosrest
# char: opGL, opGN, opGD, rubroLocal, opCrear, opVer, opEliminar, opConfirm, opAct, opMod, opCampo
# str: aux1, aux4, nombreUsuario, claveUsuario, nombreLocal, codUsuario, ubic
# Array: Z = array [0,49][0,3]; M = array [0,49][0,1]; V = array [0,99][0,2]; F = array [0,3]; R1 = array [0,2]; R2 = array [0,2]; T1 = array [0,2]; T2 = array [0,2]



def MENU_DUEÑO():
	print ("   ")
	print (" ========================= Menú - Dueño del Local =========================")
	print ("   ")
	print ("   1. Gestion de Descuentos")
	print ("     a) Crear descuento para mi local")
	print ("     b) Modificar descuento de mi local")
	print ("     c) Eliminar descuento de mi local")
	print ("     d) Volver")
	print ("   2. Aceptar / Rechazar pedido de descuento")
	print ("   3. Reporte de uso de descuentos")
	print ("   0. Salir")
	print ("   ")


def PROCED_DUEÑO():
	global op2
	global opGD

	MENU_DUEÑO()
	op2 = input(" Ingrese la opción deseada (0-3): ")
	while op2 < "0" or op2 > "3":
		op2 = input(" Respuesta inválida. Ingrese la opción deseada (0-3): ")
	while op2 != "0":

		if op2 == "1":
			print ("   ")

			opGD = input(" Ingrese la opción deseada (a-d): ")
			while opGD < "a" or opGD > "d":
				opGD = input(" Respuesta inválida. Ingrese la opción deseada (a-d): ")
			while opGD != "d":
				clear()
				if opGD == "a":
					print (" ========== - ========== - ========== Crear descuento para mi local ========== - ========== - ==========")
					RTA()
				elif opGD == "b":
					print (" ========== - ========== - ========== Modificar descuento de mi local ========== - ========== - ==========")
					RTA()
				else:
					print (" ========== - ========== - ========== Eliminar descuento de mi local ========== - ========== - ==========")
					RTA()	

				MENU_DUEÑO()			
				opGD = input(" Ingrese la opción deseada (a-d): ")
				while opGD < "a" or opGD > "d":
					opGD = input(" Respuesta inválida. Ingrese la opción deseada (a-d): ")
			clear()

		elif op2 == "2":
			clear()
			print (" ---------- - ---------- - ---------- Aceptar / Rechazar pedido de descuento ---------- - ---------- - ----------")
			RTA()
		else:
			clear()
			print (" ---------- - ---------- - ---------- Reporte de uso de descuentos ---------- - ---------- - ----------")
			RTA()
		MENU_DUEÑO()
		op2 = input(" Ingrese la opción deseada (0-3): ")
		while op2 < "0" or op2 > "3":
			op2 = input(" Respuesta inválida. Ingrese la opción deseada (0-3): ")


def MENU_CLIENTE():
	print ("   ")
	print (" ========================= Menú - Cliente =========================")
	print ("   ")
	print ("   1. Registrarme")
	print ("   2. Buscar descuentos en locales")
	print ("   3. Solicitar descuento")
	print ("   4. Ver novedades")
	print ("   0. Volver")
	print ("   ")


def PROCED_CLIENTE():
	global op3

	MENU_CLIENTE()
	op3 = input(" Ingrese la opción deseada (0-4): ")
	while op3 < "0" or op3 > "4":
		op3 = input(" Respuesta inválida. Ingrese la opción deseada (0-4): ")
	while op3 != "0":
		clear()
		if op3 == "1":
			print (" ---------- - ---------- - ---------- Registrarme ---------- - ---------- - ----------")
			RTA()
		elif op3 == "2":
			print (" ---------- - ---------- - ---------- Buscar descuentos en locales ---------- - ---------- - ----------")
			RTA()
		elif op3 == "3":
			print (" ---------- - ---------- - ---------- Solicitar descuento ---------- - ---------- - ----------")
			RTA()
		else:
			print (" ---------- - ---------- - ---------- Ver novedades ---------- - ---------- - ----------")
			RTA()

		MENU_CLIENTE()
		op3 = input(" Ingrese la opción deseada (0-4): ")
		while op3 < "0" or op3 > "4":
			op3 = input(" Respuesta inválida. Ingrese la opción deseada (0-4): ")







def BUSCAR_NOM():
	global nombreLocal
	global Z
	global p
	global contveces

	# Búsqueda dicotómica sobre los locales cargados (ordenados por nombre, ascendente)
	pri = 0
	ult = contveces - 1
	p = -1
	while pri <= ult and p == -1:
		med = (pri+ult)//2
		if Z[med][0] == nombreLocal:
			p = med
		elif nombreLocal < Z[med][0]:
			ult = med - 1
		else:
			pri = med + 1


def ORDENAR_LOCALES():
	global Z
	global M
	global contveces
	
	for m in range (contveces-1):
		for n in range (m+1,contveces):
			if Z[m][0] > Z[n][0]:
				for x in range (0,4):
					aux1 = Z[m][x]
					Z[m][x] = Z[n][x]
					Z[n][x] = aux1
				for y in range (0,2):
					aux2 = M[m][y]
					M[m][y] = M[n][y]
					M[n][y] = aux2


def MOSTRAR_LOCALES():
	global M
	global Z
	global contveces

	print ("   ")
	opVer = input(" Desea ver los locales cargados hasta el momento? (s o n): ")
	while opVer != "s" and opVer != "n":
		opVer = input(" Respuesta inválida. Desea ver los locales cargados hasta el momento? (s o n): ")

	if opVer == "s":
		if contveces == 0:
			print ("   ")
			print ("  ----------------------------------------------------------------------------------------------------------")
			print ("  CódigoLocal:        Nombre           Ubicación           Rubro           Estado           CodUsuario")
			print ("  No se han ingresado detos de momento.")
			print ("  ----------------------------------------------------------------------------------------------------------")
			print ("   ")
		else:
			print ("   ")
			print ("  ----------------------------------------------------------------------------------------------------------")
			print ("  CódigoLocal:        Nombre           Ubicación           Rubro           Estado           CodUsuario")
			for i in range (0,contveces):
				print ("      ",M[i][0],"\t     ",Z[i][0],"\t      ",Z[i][1],"\t\t    ",Z[i][2],"\t\t    ",Z[i][3],"\t\t       ",M[i][1])
			print ("  ----------------------------------------------------------------------------------------------------------")
			print ("   ")
	else:	
		print ("   ")


def VALIDACIÓN_COD(X,cod):
	pos = 0
	while X[pos] != cod and pos < 4:
		pos = pos + 1
	if X[pos] == cod:
		return pos
	else:
		return -1


def CREACION_DE_LOCALES():
	global nombreLocal
	global codUsuario
	global contveces
	global numerocodlocal
	global p
	global Z
	global M
	global R1
	global R2
	global T1
	global T2
	global V
	global F

	print (" ========== - ========== - ========== Creación de Locales ========== - ========== - ==========")

	MOSTRAR_LOCALES()

	opCrear = input(" Desea crear un local? (s o n): ")
	while opCrear != "s" and opCrear != "n":
		opCrear = input(" Respuesta inválida. Desea crear un local? (s o n): ")
	print ("   ")
	
	while opCrear != "n" and contveces < 50:
			
		numerocodlocal = numerocodlocal + 1
		M[contveces][0] = numerocodlocal


		nombreLocal = input(" Ingrese el nombre del local a crear: ")
		BUSCAR_NOM()
		while p != -1:
			print (" El nombre que ha ingresado no se encuentra disponible. Vuelva a intentarlo.")
			nombreLocal = input(" Ingrese el nombre del local a crear: ")
			BUSCAR_NOM()

		Z[contveces][0] = nombreLocal


		Z[contveces][1] = input(" Ingrese la ubicación del local: ")


		Z[contveces][2] = input(" Ingrese el rubro del local [Indumentaria(i)) / Perfumería(p) / Comida(c)]: ")
		while Z[contveces][2] != "i" and Z[contveces][2] != "p" and Z[contveces][2] != "c":
			Z[contveces][2] = input(" Respuesta inválida. Ingrese el rubro del local [Indumentaria(i)) / Perfumería(p) / Comida(c)]: ")

		if Z[contveces][2] == "i":
			R1[0] = R1[0] + 1
		elif Z[contveces][2] == "p":
			R1[1] = R1[1] + 1
		else: 
			R1[2] = R1[2] + 1

		for i in range (0,3):
			R2[i] = R1[i]
			T2[i] = T1[i]

		for i in range (0,2):
			for j in range (1,3):
				if R2[i] < R2[j]:
					aux3 = R2[i]
					R2[i] = R2[j]
					R2[j] = aux3

					aux4 = T2[i]
					T2[i] = T2[j]
					T2[j] = aux4


		codUsuario = int(input(" Ingrese el código de Usuario: "))
		g = VALIDACIÓN_COD(F,codUsuario)

		if g != -1:
			if V[g][2] == "dueñoLocal":
				M[contveces][1] = codUsuario
			else:
				print (" El usuario no es de tipo DueñoLocal. Vuelva a intentarlo.")
		else:
			print (" Usuario no existente. Vuelva a intentarlo.")

		while V[g][2] != "dueñoLocal" :

			codUsuario = int(input(" Ingrese el código de Usuario: "))
			g = VALIDACIÓN_COD(F,codUsuario)

			if g != -1:
				if V[g][2] == "dueñoLocal":
					M[contveces][1] = codUsuario
				else:
					print (" El usuario no es de tipo DueñoLocal. Vuelva a intentarlo.")
			else:
				print (" Usuario no existente. Vuelva a intentarlo.")


		Z[contveces][3] = "A"

		contveces = contveces + 1
		ORDENAR_LOCALES()

		print ("   ")
		opCrear = input(" Desea crear otro local? (s o n): ")
		while opCrear != "s" and opCrear != "n":
			opCrear = input(" Respuesta inválida. Desea crear otro local? (s o n): ")
		print ("   ")


	if contveces == 50:
		print ("Ha alcanzado el número máximo de locales a cargar.")

	if opCrear == "n":
		for i in range (0,3):
				R2[i] = R1[i]
				T2[i] = T1[i]

		for i in range (0,2):
			for j in range (1,3):
				if R2[i] < R2[j]:
					auxrub = R2[i]
					R2[i] = R2[j]
					R2[j] = auxrub

					auxrubtexto = T2[i]
					T2[i] = T2[j]
					T2[j] = auxrubtexto

	print ("   ")
	print ("       Rubro \t      Cantidad  ")
	for k in range (0,3):
		print ("   ",T2[k],":\t",R2[k])
	print ("   ")

	ORDENAR_LOCALES()


def MENU_MOD():
	print ("   ")
	print (" --------------- Opciones a modificar: ---------------")
	print ("   ")
	print ("   1. Modificar Nombre")
	print ("   2. Modificar Ubicación")
	print ("   3. Modificar Rubro")
	print ("   4. Modificar CodUsuario")
	print ("   0. Volver")
	print ("   ")


def NOM():
	global nombreLocal
	global p
	global contveces
	global Z
	global t

	nombreLocal = input(" Ingrese el nuevo nombre del local: ")
	BUSCAR_NOM()
	while p != -1:
		print (" El nombre que ha ingresado no se encuentra disponible. Vuelva a intentarlo.")
		nombreLocal = input(" Ingrese el nuevo nombre del local: ")
		BUSCAR_NOM()
	
	Z[t][0] = nombreLocal
	ORDENAR_LOCALES()
	BUSCAR_NOM()
	t = p

def UBIC():
	global t
	global Z

	Z[t][1] = input(" Ingrese la nueva ubicación: ")

def PROCED_ELIMINAR_RUB():
	global t
	global Z
	global R1

	if Z[t][2] == "i":
		R1[0] = R1[0] - 1
	elif Z[t][2] == "p":
		R1[1] = R1[1] - 1
	else:
		R1[2] = R1[2] - 1

def RUB():
	global rubro
	global R1
	global t

	PROCED_ELIMINAR_RUB()
	rubro = input(" Ingrese el nuevo rubro del local [Indumentaria(i)) / Perfumería(p) / Comida(c)]: ")
	while rubro != "i" and rubro != "p" and rubro != "c":
		rubro = input(" Respuesta inválida. Ingrese el nuevo rubro del local [Indumentaria(i)) / Perfumería(p) / Comida(c)]: ")
	if rubro == "i":
		R1[0] = R1[0] + 1
	elif rubro == "p":
		R1[1] = R1[1] + 1
	else:
		R1[2] = R1[2] + 1

	Z[t][2] = rubro

def COD_DL():
	global codUsuario
	global p
	global V
	global t

	codUsuario = int(input(" Ingrese el nuevo código de Usuario: "))
	g = VALIDACIÓN_COD(F,codUsuario)
	if g != -1:
		if V[g][2] == "dueñoLocal":
			M[t][1] = codUsuario
		else:
			print (" El usuario no es de tipo DueñoLocal. Vuelva a intentarlo.")
	else:
		print (" Usuario no existente. Vuelva a intentarlo.")
	while V[g][2] != "dueñoLocal" :
		codUsuario = int(input(" Ingrese el nuevo código de Usuario: "))
		g = VALIDACIÓN_COD(F,codUsuario)
		if g != -1:
			if V[g][2] == "dueñoLocal":
				M[t][1] = codUsuario
			else:
				print (" El usuario no es de tipo DueñoLocal. Vuelva a intentarlo.")
		else:
			print (" Usuario no existente. Vuelva a intentarlo.")


def PROCED_MODIFICAR():
	global t
	global M
	global Z
	global modCampo

	print ("   ")
	print ("  -----------------------------------------------------------------------------------------")
	print ("  CódigoLocal:        Nombre           Ubicación           Rubro           CodUsuario")
	print ("      ",M[t][0],"\t     ",Z[t][0],"\t      ",Z[t][1],"\t\t    ",Z[t][2],"\t\t      ",M[t][1])
	print ("  -----------------------------------------------------------------------------------------")

	MENU_MOD()
	modCampo = int(input(" Seleccione la opción a ejecutar: "))
	while modCampo < 0 or modCampo > 4:
		modCampo = int(input(" Respuesta inválida. Seleccione la opción a ejecutar: "))
	while modCampo != 0:
		if modCampo == 1:
			NOM()
		elif modCampo == 2:
			UBIC()
		elif modCampo == 3:
			RUB()
		else:
			COD_DL()

		MENU_MOD()
		modCampo = int(input(" Seleccione la opción a ejecutar: "))
		while modCampo < 0 or modCampo > 4:
			modCampo = int(input(" Respuesta inválida. Seleccione la opción a ejecutar: "))


def MODIFICAR_LOCALES():
	global Z
	global M
	global opCampo
	global opMod
	global posicion
	global t
	global contveces
	global R1

	opCampo = 5
	opMod = "s"
	modCampo = 1

	print (" ========== - ========== - ========== Modificación de Locales ========== - ========== - ==========")

	while opCampo != 0 and opMod != "n" and modCampo != 0:

		MOSTRAR_LOCALES()
		if contveces != 0:

			codigo = int(input(" Ingrese el código del local a modificar: "))

			posicion = 0
			while M[posicion][0] != codigo and posicion <= contveces:
				posicion = posicion + 1
			if M[posicion][0] == codigo:
				t = posicion
			else:
				t = -1

			while t == -1:
				print (" El codigo ingresado no corresponde a ningún local registrado. Vuelva a intentarlo.")
				codigo = int(input(" Ingrese el código del local a modificar: "))
				posicion = 0
				while M[posicion][0] != codigo and posicion <= contveces:
					posicion = posicion + 1
				if M[posicion][0] == codigo:
					t = posicion
				else:
					t = -1

			if t != -1:
				if Z[t][3] == "A":
					PROCED_MODIFICAR()
				else:
					opAct = input(" Este local se encuntra dado de baja, desea activar el local? (s o n): ")
					while opAct != "s" and opAct != "n":
						opAct = input(" Respuesta inválida. Desea activar el local? (s o n): ")
					if opAct == "s":
						Z[t][3] = "A"
						if Z[t][2] == "i":
							R1[0] = R1[0] + 1
						elif Z[t][2] == "p":
							R1[1] = R1[1] + 1
						elif Z[t][2] == "c": 
							R1[2] = R1[2] + 1
						PROCED_MODIFICAR()

					else:
						print ("   ")
						opMod = input(" Desea modificar otro local? (s o n): ")
						while opMod != "s" and opMod != "n":
							opMod = input(" Respuesta inválida. Desea modificar otro local? (s o n): ")
						if opMod == "n":
							clear()
						else:
							clear()
							print (" ========== - ========== - ========== Modificación de Locales ========== - ========== - ==========")

			ORDENAR_LOCALES()

			print ("   ")
			opMod = input(" Desea modificar otro local? (s o n): ")
			while opMod != "s" and opMod != "n":
				opMod = input(" Respuesta inválida. Desea modificar otro local? (s o n): ")
			if opMod == "n":
				clear()
			else:
				clear()
				print (" ========== - ========== - ========== Modificación de Locales ========== - ========== - ==========")
		else:
			opMod = "n"


def ELIMINAR_LOCALES():
	global Z
	global M
	global t
	global contveces

	print (" ========== - ========== - ========== Eliminación de Locales ========== - ========== - ==========")

	opEliminar = "s"

	while opEliminar != "n":
		MOSTRAR_LOCALES()
		if contveces != 0:
			codigo = int(input(" Ingresar el código del local a eliminar: "))

			posicion = 0
			while M[posicion][0] != codigo and posicion <= contveces:
				posicion = posicion + 1
			if M[posicion][0] == codigo:
				t = posicion
			else:
				t = -1

			if t != -1:
				print ("   ")
				print ("  -----------------------------------------------------------------------------------------")
				print ("  CódigoLocal:        Nombre           Ubicación           Rubro           CodUsuario")
				print ("      ",M[t][0],"\t     ",Z[t][0],"\t      ",Z[t][1],"\t\t    ",Z[t][2],"\t\t      ",M[t][1])
				print ("  -----------------------------------------------------------------------------------------")
				if Z[t][3] == "A":
					opConfirm = input(" Está seguro que desea eliminar este local? (s o n): ")
					while opConfirm != "s" and opConfirm != "n":
						opConfirm = input(" Respuesta inválida. Está seguro que desea eliminar este local? (s o n): ")
					if opConfirm == "s":
						Z[t][3] = "B"
						PROCED_ELIMINAR_RUB()
					else:
						print ("   ")
				else:
					print (" El local ya se encuentra dado de baja.")
			else:
				print (" El local a eliminar no existe.")

			print ("   ")
			opEliminar = input(" Desea eliminar otro local? (s o n): ")
			while opEliminar != "s" and opEliminar != "n":
				opEliminar = input(" Respuesta inválida. Desea eliminar otro local? (s o n): ")
			if opEliminar == "n":
				clear()
			else:
				clear()
				print (" ========== - ========== - ========== Eliminación de Locales ========== - ========== - ==========")
		else:
			opEliminar = "n"


def MAPA_DE_LOCALES():
	global M

	print (" ========== - ========== - ========== Mapa de Locales ========== - ========== - ==========")

	i = 0

	print ("   ")
	for k in range (0,10):
		print ("        +---+---+---+---+---+     ")
		print ("        |",M[i][0],"|",M[i+1][0],"|",M[i+2][0],"|",M[i+3][0],"|",M[i+4][0],"|")
		i = i + 5
	print ("        +---+---+---+---+---+     ")


def MENU_ADMIN():
	print ("   ")
	print (" ========================= Menú - Administrador =========================")
	print ("   ")
	print ("   1. Gestion de locales")
	print ("   2. Crear cuentas de dueños de locales")
	print ("   3. Aprobar/Denegar solicitud de descuento")
	print ("   4. Gestión de novedades")
	print ("   5. Reporte de utilización de descuentos")
	print ("   0. Salir")
	print ("   ")


def SUBMENU_1():
	print ("   ")
	print (" ---------- - ---------- - ---------- Gestión de Locales ---------- - ---------- - ----------")
	print ("   ")
	print ("     a) Crear locales")
	print ("     b) Modificar local")
	print ("     c) Eliminar local")
	print ("     d) Mapa de locales")
	print ("     e) Volver")
	print ("   ")


def MODULO_GL():
	global opGL

	opGL = input(" Ingrese la opción deseada (a-e): ")
	while opGL < "a" or opGL > "e":
		opGL = input(" Respuesta inválida. Ingrese la opción deseada (a-e): ")

	while opGL != "e":
		clear()
		if opGL == "a":
			CREACION_DE_LOCALES()
		elif opGL == "b":
			MODIFICAR_LOCALES()
		elif opGL == "c":
			ELIMINAR_LOCALES()
		else:
			MAPA_DE_LOCALES()

		SUBMENU_1()
		opGL = input(" Ingrese la opción deseada (a-e): ")
		while opGL < "a" or opGL > "e":
			opGL = input(" Respuesta inválida. Ingrese la opción deseada (a-e): ")
	clear()


def SUBMENU_2():
	print ("   ")
	print (" ---------- - ---------- - ---------- Gestión de Novedades ---------- - ---------- - ----------")
	print ("   ")
	print ("     a) Crear novedades")
	print ("     b) Modificar novedad")
	print ("     c) Eliminar novedad")
	print ("     d) Ver reporte de novedades")
	print ("     e) Volver")
	print ("   ")


def MODULO_GN():
	global opGN

	opGN = input(" Ingrese la opción deseada (a-e): ")
	while opGN < "a" or opGN > "e":
		opGN = input(" Respuesta inválida. Ingrese la opción deseada (a-e): ")

	while opGN != "e":
		clear()
		if opGN == "a":
			print (" ========== - ========== - ========== Creación de Novedades ========== - ========== - ==========")
			RTA()
		elif opGN == "b":
			print (" ========== - ========== - ========== Modificación de Novedades ========== - ========== - ==========")
			RTA()
		elif opGN == "c":
			print (" ========== - ========== - ========== Eliminación de Novedades ========== - ========== - ==========")
			RTA()
		else:
			print (" ========== - ========== - ========== Reporte de Novedades ========== - ========== - ==========")
			RTA()

		SUBMENU_2()
		opGN = input(" Ingrese la opción deseada (a-e): ")
		while opGN < "a" or opGN > "e":
			opGN = input(" Respuesta inválida. Ingrese la opción deseada (a-e): ")
	clear()


def RTA():
	print ("   ")
	print ("   En construcción...")
	print ("   ")




# Base de Datos

V = [["*"]*3 for i in range(100)]
F = [0]*100

F[0] = 1
V[0][0] = "admin@shopping.com"
V[0][1] = "12345"
V[0][2] = "administrador"

F[1] = 4
V[1][0] = "localA@shopping.com"
V[1][1] = "AAAA1111"
V[1][2] = "dueñoLocal"

F[2] = 6
V[2][0] = "localB@shopping.com"
V[2][1] = "BBBB2222"
V[2][2] = "dueñoLocal"

F[3] = 9
V[3][0] = "unCliente@shopping.com"
V[3][1] = "33xx33"
V[3][2] = "cliente"

Z = [["*"]*5 for i in range(50)]

M = [[0]*2 for i in range (50)]

R1 = [0]*3 
R2 = [0]*3 
T1 = ["*"]*3 
T2 = ["*"]*3 

T1[0] = "Indumentaria"
T1[1] = "Perfumería"
T1[2] = "Comida"



# Programa Principal

contveces = 0
numerocodlocal = 0
intentos = 3
cont = 0

from getpass import getpass
import os

while cont != 3:

	nombreUsuario = input(" Ingrese su nombre de usuario: ")
	claveUsuario = getpass(" Ingrese su clave: ")

	if nombreUsuario == V[0][0] and claveUsuario == V[0][1]:
		clear()
		
		MENU_ADMIN()
		op = int(input(" Ingrese la opción deseada (0-5): "))
		while op < 0 or op > 5:
			op = int(input(" Respuesta inválida. Ingrese la opción deseada (0-5): "))
		
		while op != 0:	
			clear()
			
			if op == 1:	
				SUBMENU_1()
				MODULO_GL()
			elif op == 2:
				print (" ---------- - ---------- - ---------- Crear cuentas de dueños de locales ---------- - ---------- - ----------")
				RTA()
			elif op == 3:
				print (" ---------- - ---------- - ---------- Aprobar/Denegar solicitud de descuento ---------- - ---------- - ----------")
				RTA()
			elif op == 4:
				SUBMENU_2()
				MODULO_GN()
			else:
				print (" ---------- - ---------- - ---------- Reporte de utilización de descuentos ---------- - ---------- - ----------")
				RTA()	

			MENU_ADMIN()
			op = int(input(" Ingrese la opción deseada (0-5): "))
			while op < 0 or op > 5:
				op = int(input(" Respuesta inválida. Ingrese la opción deseada (0-5): "))
		
		cont = 3

	elif nombreUsuario == V[1][0] and claveUsuario == V[1][1] or nombreUsuario == V[2][0] and claveUsuario == V[2][1]:
		clear()
		PROCED_DUEÑO()
		
		cont = 3

	elif nombreUsuario == V[3][0] and claveUsuario == V[3][1]:
		clear()
		PROCED_CLIENTE()
		
		cont = 3

	else: 
		cont = cont + 1
		intentosrest = intentos - cont
		print(" Usuario y/o contraseña incorrectos. Intentos Restantes:",intentosrest)

