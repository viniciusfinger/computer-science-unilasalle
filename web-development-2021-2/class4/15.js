// Bruno Moretto e Vinicius Finger

const vetor = [1, 54, 15, 76, 92, 43, 321, 8, 86, 45];
let media = 0;

vetor.forEach(valor => media += valor);
media /= vetor.length;

console.log(`A média dos valores do vetor é ${media.toFixed(1)}`);