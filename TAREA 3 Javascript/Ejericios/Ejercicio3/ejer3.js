function saludar(){
    document.write("HOLA MUNDO","<br>")
}
function calculardoble(num){
    var res;
    res=num*2;
    return res;
}
function triplicar(num){
    num=num*3
}
var x;
document.write("LLAMANDO A LA FUNCION SALUDAR:","<BR/>");

saludar();
document.write("INGRESE EL VALOR NUMERO PARA X")
x=prompt("INGRESE EL NUMERO A TRABAJAR");
document.write("LLAMANDO A LA FUNCION CALULAR DOBLE","<BR/>")
document.write("EL DOBLE DE ",x, " es ",calculardoble(x),"<BR/>")
document.write("EL VALOR ORIGINAL DE X ES ",x,"<br>")
document.write("LLAMANDO A LA FUNION TRIPLICAR ")
triplicar(x);
document.write("EL NUEVO VALOR DE X ES",x);
