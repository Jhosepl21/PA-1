var terminar
i=100
while (i>=0) {  
   numero=i
   i=i-2
   document.write(numero,"<br>")
   terminar=prompt(numero)
   if(terminar=='x'){
    alert("CONTADOR TERMINADO")
    break
   }
}