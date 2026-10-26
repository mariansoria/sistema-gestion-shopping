"""Trabajo Práctico nro 1 de AyED - ISI com 05"""
#Variables: int: contI, contP, contC, cont, op, Max, Min; char: opGL, opGN; str: opCrear, nombreLocal, ubicacionLocal, rubroLocal, rubroMax, rubroMin


def COMPARACION():
	
	global Max
	global Min
	global rubroMax
	global rubroMin

	global contI
	global contP
	global contC

	Max = 0
	Min = 0
	rubroMax = ""
	rubroMin = ""

	if contI == contP:
		if contI == contC:
			print("Los distintos rubros tienen la misma cantidad de locales.")
		else:
			if contI > contC:
				Max = contI
				Min = contC
				rubroMax = "Indumentaria y Perfumeria"
				rubroMin = "Comida"
			else:
				Max = contC
				Min = contI
				rubroMax = "Comida"
				rubroMin = "Indumentaria y Perfumeria"
	else:
		if contI > contP:
			if contI == contC:
				Max = contI
				Min = contP
				rubroMax = "Indumentaria y Comida"
				rubroMin = "Perfumeria"
			else:
				 if contI > contC:
				 	if contP == contC:
				 		Max = contI
				 		Min = contP
				 		rubroMax = "Indumentaria y Comida"
				 		rubroMin = "Perfumeria"
				 	else:
				 		if contP > contC:
				 			Max = contI
				 			Min = contC
				 			rubroMax = "Indumentaria"
				 			rubroMin = "Comida"
				 		else:
				 			Max = contI
				 			Min = contP
				 			rubroMax = "Indumentaria"
				 			rubroMin = "Perfumeria"
				 else:
				 	Max = contC
				 	Min = contP
				 	rubroMax = "Comida"
				 	rubroMin = "Perfumeria"
		else:
			if contP == contC:
				Max = contP
				Min = contI
				rubroMax = "Perfumeria y Comida"
				rubroMin = "Indumentaria"
			else:
				if contP > contC:
					if contI == contC:
						Max = contP
						Min = contI
						rubroMax = "Perfumeria"
						rubroMin = "Indumentaria y Comida"
					else:
						if contI > contC:
							Max = contP
							Min = contC
							rubroMax = "Perfumeria"
							rubroMin = "Comida"
						else:
							Max = contP
							Min = contI
							rubroMax = "Perfumeria"
							rubroMin = "Indumentaria"
				else:
					Max = contC
					Min = contI
					rubroMax = "Comida"
					rubroMin = "Indumentaria"
		print("                      ")
		print("El/Los rubro(s) que posee(n) mayor cantidad de locales es/son",rubroMax,"con un total de",Max,"y el/los rubro(s) que posee(n) menor cantidad de locales es/son",rubroMin,"con un total de",Min,".")
		print("                      ")


def CREACION_DE_LOCALES():

	global contI
	global contP
	global contC

	opCrear = input("Desea crear un local? (si o no): ")
	while opCrear != "si" and opCrear != "no":
		opCrear = input("Desea crear un local? (si o no): ")
	while opCrear != "no":
		nombreLocal = input("Ingresar el nombre del local a crear: ")
		ubicacionLocal = input("Ingresar ubicacion del local: ")
		rubroLocal = input("Ingresar rubro del local (Indumentaria/Perfumeria/Comida): ")
		while rubroLocal != "Indumentaria" and rubroLocal != "Perfumeria" and rubroLocal != "Comida":
			rubroLocal = input("Ingresar rubro del local (Indumentaria/Perfumeria/Comida): ")

		if rubroLocal == "Indumentaria":
			contI = contI + 1

		elif rubroLocal == "Perfumeria":
			contP = contP + 1

		else:
			contC = contC + 1

		opCrear = input("Desea crear otro local? (si o no): ")
		while opCrear != "si" and opCrear != "no":
			opCrear = input("Desea crear otro local? (si o no): ")

	COMPARACION()


def MENU():
	print ("-----------------------------------------")
	print ("MENU DE OPCIONES")
	print ("-----------------------------------------")
	print ("1. Gestion de locales")
	print ("2. Crear cuentas de dueños de locales")
	print ("3. Aprobar/Denegar solicitud de descuento")
	print ("4. Gestión de novedades")
	print ("5. Reporte de utilización de descuentos")
	print ("0. Salir")
	print ("-----------------------------------------")


def SUBMENU_1():
	print ("--------------------------")
	print ("MENU DE GESTION DE LOCALES")
	print ("--------------------------")
	print ("a) Crear locales")
	print ("b) Modificar local")
	print ("c) Eliminar local")
	print ("d) Volver")
	print ("--------------------------")


def MODULO_GL():

	global opGL

	opGL = input("Ingrese la opción deseada (a-d): ")
	while opGL < "a" or opGL > "d":
		opGL = input("Ingrese la opción deseada (a-d): ")

	while opGL != "d":
		if opGL == "a":
			CREACION_DE_LOCALES()
		elif opGL == "b":
			RTA()
		else:
			RTA()

		SUBMENU_1()
		opGL = input("Ingrese la opción deseada (a-d): ")
		while opGL < "a" or opGL > "d":
			opGL = input("Ingrese la opción deseada (a-d): ")


def SUBMENU_2():
	print ("----------------------------")
	print ("MENU DE GESTION DE NOVEDADES")
	print ("----------------------------")
	print ("a) Crear novedades")
	print ("b) Modificar novedad")
	print ("c) Eliminar novedad")
	print ("d) Ver reporte de novedades")
	print ("e) Volver")
	print ("----------------------------")


def MODULO_GN():

	global opGN

	opGN = input("Ingrese la opción deseada (a-e): ")
	while opGN < "a" or opGN > "e":
		opGN = input("Ingrese la opción deseada (a-e): ")

	while opGN != "e":
		if opGN == "a":
			RTA()
		elif opGN == "b":
			RTA()
		elif opGN == "c":
			RTA()
		else:
			RTA()

		SUBMENU_2()
		opGN = input("Ingrese la opción deseada (a-e): ")
		while opGN < "a" or opGN > "e":
			opGN = input("Ingrese la opción deseada (a-e): ")


def RTA():
	print ("------------------")
	print ("En construcción...")
	print ("------------------")



contI = 0
contP = 0
contC = 0

cont = 0

from getpass import getpass

while cont != 3:

	nombreUsuario = input("Ingrese su nombre de usuario: ")
	claveUsuario = getpass("Ingrese su clave: ")

	if nombreUsuario == "admin@shopping.com" and claveUsuario == "12345":
		
		MENU()
		op = int(input("Ingrese la opción deseada (0-5): "))
		while op < 0 or op > 5:
			op = int(input("Ingrese la opción deseada (0-5): "))
		
		while op != 0:	
			
			if op == 1:	
				SUBMENU_1()
				MODULO_GL()
			elif op == 2:	
				RTA()
			elif op == 3:	
				RTA()
			elif op == 4:
				SUBMENU_2()
				MODULO_GN()
			else:	
				RTA()	

			MENU()
			op = int(input("Ingrese la opción deseada (0-5): "))
			while op < 0 or op > 5:
				op = int(input("Ingrese la opción deseada (0-5): "))

		cont = 3

	else: 
		cont = cont + 1
		print("Usuario y/o contraseña incorrectos.")
