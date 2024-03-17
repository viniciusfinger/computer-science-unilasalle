// Bruno Moretto e Vinicius Finger

console.log(mask(0.30000000000000004));

function mask(valor) {
    return `R$${valor.toFixed(2).replace('.', ',')}`;
}