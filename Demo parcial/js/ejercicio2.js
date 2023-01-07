
	var x = new Number();
	var n = new Number();
	var estado = new Boolean();
	var estado2 = new Boolean();
	estado = true;
	while (estado) {
		x = Number(prompt("Ingrese su codigo",'<BR/>'));
		if ((x==1024)) {
			document.write("Codigo Correcto",'<BR/>');
			estado = false;
		} else {
			document.write("Codigo Incorrecto",'<BR/>');
			estado = true;
		}
	}
	estado2 = true;
	while (estado2) {
		n = Number(prompt("Ingrese su contrase�a",'<BR/>'));
		if ((n==4567)) {
			document.write("contrase�a Correcto",'<BR/>');
			estado2 = false;
		} else {
			document.write("contrase�a Incorrecto",'<BR/>');
			estado2 = true;
		}
	}
