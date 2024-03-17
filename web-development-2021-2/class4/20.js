//Bruno Moretto, Vinicius Finger
let vetorA = [1,2,3,4]
let vetorB = [5,6,7,8]

function trocaPosicaoVetores(vetorA, vetorB){
    let i = 0;
    while (i < vetorA.length){
        vetorA.push(vetorB[0]);
        vetorB.push(vetorA[0]);
        vetorA.shift();
        vetorB.shift();
        i++;
    }
    
    console.log(vetorA)
    console.log(vetorB)
}

trocaPosicaoVetores(vetorA, vetorB)