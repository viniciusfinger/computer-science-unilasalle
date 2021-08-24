// Bruno Moretto e Vinicius Finger

const vetor = [1, 54, 15, 76, 92, 43, 22, 8, 86, 45];

const maiorValor = vetor.reduce((valor1, valor2) => valor1 > valor2 ? valor1 : valor2);
const menorValor = vetor.reduce((valor1, valor2) => valor1 < valor2 ? valor1 : valor2);

console.log(`Maior valor é ${maiorValor} e o menor valor é ${menorValor}`);