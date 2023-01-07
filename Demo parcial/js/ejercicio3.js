
var intentos, num_ingresado, num_secreto;
intentos = 10;
num_secreto = Math.floor(Math.random()*10)+1;
document.write("Adivine el numero (de 1 a 10):",'<BR/>');
num_ingresado = prompt("Adivine el numero (de 1 a 10):",'<BR/>');;
while (num_secreto!=num_ingresado && intentos>1) {
	if (num_secreto>num_ingresado) {
		document.write("Muy bajo",'<BR/>');
	} 
  else {
		document.write("Muy alto",'<BR/>');
	}
	num_ingresado = Number(prompt());
 }
if (num_secreto==num_ingresado) {
	document.write("Exacto! Usted adivino en ");
} 
else {
	document.write("El numero era: ",num_secreto,'<BR/>');
	}
