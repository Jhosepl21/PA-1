estado=true
var acum,n;
acum = 0
while(estado){
  n =Number(prompt("Ingrese un numero"))
  acum=acum+n

  resp=prompt("Desea agregar otro numero,si o no?")
  if (resp=="si")
    estado=true
  else
    estado=false
 
}
document.write("La suma de los numeros es:",acum)   