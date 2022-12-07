while True:
	print("MENU DE OPCIONES")
	print("   1. Literatura")
	print("   2. Cine")
	print("   3. Música")
	print("   4. Videojuegos")
	print("   5. Salir")
    
	print("ELIJA UNA OPCION 1-5:")
	op=float(input())

	if op==1:
		print("LECTURAS RECOMENDADAS")
		print("+ Esperándolo a Tito y otros cuentos de fúbol (Eduardo Sacheri)")
		print("+ El juego de Ender (Orson Scott Card)")
		print("el sueño de los heroes")
	elif op==2:
		print("Películas recomendables:")
		print(" + Matrix (1999)")
		print(" + El último samuray (2003)")
		print(" + Cars (2006)")
	elif op==3:
		print("Discos recomendables:")
		print(" + Despedazado por mil partes (La Renga, 1996)")
		print(" + Búfalo (La Mississippi, 2008)")
		print(" + Gaia (Mägo de Oz, 2003)")
	elif op==4:
		print("Videojuegos clásicos recomendables")
		print(" + Día del tentáculo (LucasArts, 1993)")
		print(" + Terminal Velocity (Terminal Reality/3D Realms, )")
		print(" + Death Rally (Remedy/Apogee, 1996)")
	elif op==5:
		print("Gracias, vuelva prontos")
	else:
		print("OPCION NO VALIDA")
	print("presione enter para continuar")
	input()
	if op==5:
		break
