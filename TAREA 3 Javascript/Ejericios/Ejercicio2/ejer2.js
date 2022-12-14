
var acum, dato, i, n, prom;
document.write("INGRESANDO LOS DATOS","</br>")
n = Number(prompt("Ingrese la cantidad de datos:"));
acum = 0;
for (i=1;i<=n;i++) {
	dato = Number(prompt("Ingrese el dato "));
    document.write("El dato ",i," es ",dato,"<br>")
	acum = acum+dato;
	}
prom = acum/n;
document.write("El promedio es: ",prom,'<BR/>');