// Bruno Moretto e Vinicius Finger

const vetor = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10];

const vetorPar = vetor.filter(valor => valor % 2 === 0);
const vetorImpar = vetor.filter(valor => valor % 2 !== 0);

console.log(`Temos ${vetorPar.length} valores pares e ${vetorImpar.length} valores ímpares`);