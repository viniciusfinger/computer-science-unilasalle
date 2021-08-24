//Bruno Moretto, Vinicius Finger
const vetorExemplo = [-4,-5,-6,8,1,2,3,-1,5];

var globalTotalNegativos = 0;

function verificaNegativo(num){
    if (num < 0){
        globalTotalNegativos += 1;
    }
}

vetorExemplo.forEach(verificaNegativo);
console.log(globalTotalNegativos)
