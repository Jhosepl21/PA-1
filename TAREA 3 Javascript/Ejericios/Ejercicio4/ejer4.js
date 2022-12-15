var i;
var a=new Array(10);
for(i=1;i<=10;i++){
    a[i]=Math.floor(Math.random()*100);
}
document.write("los elementos del arreglo son: ","<br>");
for(i=1;i<=10;i++){
    document.write(a[i]," ");
}
document.write("<br>");
document.write("EN ORDEN INVERSO:","<br>");
for(i=10;i>=1;i--){
    document.write(a[i]," ");
}