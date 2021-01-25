#FUNCIONES
def menu():
	print("(1)Limpieza de sillones")
	print("(2)Limpieza de sillas")
	print("(3)Limpieza de alfombras(superficies mayores a 80mts2 tienen una bonificación de $2000)")
	print("(4)Limpieza de carpetas")
	print("(5)Limpieza de interiores autos")
	op = int(input("Ingrese una opción \n" ">>"))
	return op 

def sillones(pesos_precio,cuerpos):
	return pesos_precio * cuerpos

def sillas():
	print("(1)Con respaldo")
	print("(2)Sin respaldo")
	op_sillas = int(input("Ingresa una opción:"))
	return op_sillas

def sillas_resp(precio_uni,cantidad):	
	return precio_uni * cantidad

def sillas_sin_resp(precio_uni,cantidad):	
	return precio_uni * cantidad	

def alfombras(precio,mts2):
	return precio * mts2

def carpetas():	
	print("(1) Carpeta Lana/Artesanal/Persas/Chinas/Otras(hechas a mano)")
	print("(2) Nylon/Polipropileno/Otras")
	op_carpetas = int(input("Ingresas una opción:"))
	return op_carpetas

def lana(precio_uni,mts2):	
	return precio_uni * mts2

def nylon(precio_uni,mts2):
	return precio_uni *mts2

def interiores_autos():
	print("(1)Auto")
	print("(2)Camioneta")
	op_int_autos = int(input("Ingresa una opción:"))
	return op_int_autos

def autos(precio):
	return precio
def camioneta(precio_camioneta):
	return precio_camioneta	


try:
	#INICIO de programa: MENÚ PRINCIPAL
	op = menu()
	#SILLONES Y TAPIZADOS
	if op == 1:	
		cuerpos = int(input("Cantidad de cuerpos:\n(IMPORTANTE:El mínimo a cobrar es de 3 cuerpos[$3300].)\n"))
		resultado = sillones(1100,cuerpos)
		print("El importe es:$" + str(resultado))		
	#SILLAS C/RESPALDO Y S/RESPALDO
	elif op == 2:
		op_sillas = sillas() 
		if op_sillas == 1:
			cantidad = int(input("Ingresa la cantidad de sillas a limpiar(mínimo a cobrar 4 sillas $3200):\n>>"))
			resultado_2 = sillas_resp(800,cantidad)
			print("El importe es:$" + str(resultado_2))
		else:	
			cantidad = int(input("Ingresa la cantidad de sillas a limpiar(mínimo a cobrar 4 sillas $3600):\n>>"))
			resultado_2 = sillas_resp(600,cantidad)
			print("El importe es:$" + str(resultado_2))			
	#ALFOMBRAS		
	elif op == 3:
		mts2 = int(input("Ingresa cantidad de mts2\n >>"))
		res_alf = alfombras(150,mts2)
		print("IMPORTE:$" + str(res_alf))
		if mts2 >= 80:
			print("BONIFICACIÓN: $2000 (por su cantidad de mts2)")
			print("PRECIO FINAL:$" + str((res_alf - 2000)))			
		else:
			print("No posees la cantidad de mts2 para la bonificación")			
	#CARPETAS
	elif op == 4:
		op_carpetas = carpetas()
		if op_carpetas == 1:
			mts2 = int(input("Ingrese cantidad de mts2:"))
			resultado = lana(340,mts2)
			print("Importe apróximado:$" + str(resultado))			
		else:	
			mts2 = int(input("Ingrese cantidad de mts2:"))
			resultado = nylon(310,mts2)
			print("Importe apróximado:$" + str(resultado))
			print("Todas las alfombras son medidas al momento de entregarlas")			
	#INTERIOR AUTOS(terminado, había surgido un error, pero me había olvidado del 'return' de interiores_autos())
	elif op == 5:
		op_int_autos = interiores_autos()
		if op_int_autos == 1:
			cantidad = 1
			resultado = autos(4500) 
			print("IMPORTE:$" + str(resultado))
		elif op_int_autos == 2:	
			cantidad = 1
			resultado = camioneta(6500)
			print("IMPORTE:$" + str(resultado))
		else:	
			print("***ERROR*** Tiene que ser un n° entre 1-2")
	#ÚLTIMA CONDICIÓN POR SI ESCRIBIERON UN DATO INVALIDO
	elif op > 5:		
		print("***DATO INVALIDO*** tiene que ser un n° entre 1-5")

#TRATAMIENTO DE ERRORES		
except ValueError:			
	print("***ERROR DATO INVALIDO***Tiene que ser un n°")
finally:
	print("Gracias por utilizar nuestra aplicación")
	print("ADVANCE CLEAN")