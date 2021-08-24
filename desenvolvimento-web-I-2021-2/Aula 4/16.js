//Bruno Moretto, Vinicius Finger
const vetorInteiro = [1,2,3,4];
const vetorString = ["5,6,7,8"];
const vetorDouble = [10.1, 2.3, 4.7, 5.9];

function concatenarVetores(vetorUm, vetorDois){
    return vetorUm.concat(vetorDois);
}

console.log(concatenarVetores(vetorInteiro, vetorDouble));