//Bruno Moretto, Vinicius Finger
function calculaAnuidade(mes, valor){
    if(mes == "1"){
        return valor;
    } else {
        return Number(valor) * (Math.pow((1+0.05), Number(mes)))
    }
}

console.log(calculaAnuidade(3, 1000))
