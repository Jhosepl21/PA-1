acum=0
sumapar=0
n=Number(prompt("INGRESE LA CANTIDAD TOTAL DE NUMEROS A SUMAR:"))
for(var i=1;i<=n;i++){
    num=Number(prompt("INGRESE EL ",i, "numero"))
    acum=acum+num
    if(num%2==0){
    sumapar=sumapar+num}
    }
document.write("LA SUMA TOTAL ES :",acum,"<br>")
document.write("LA SUMA DE LOS PARES ES:",sumapar)