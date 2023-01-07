var i,acum,acumu,contapa,contaimpa;
acum=0;
acumu=0;
contapa=0;
contaimpa=0;
for(i=1;i<=10;i++){
    num=Number(prompt("Ingrese un numero"))
    if (num%2){
        acum+=num
        contapa=contapa+1}
    else
        acumu+=num;
        contaimpa=contaimpa+1;
}
document.write(acum/contapa,"<br>")
document.write(acumu/contaimpa)
