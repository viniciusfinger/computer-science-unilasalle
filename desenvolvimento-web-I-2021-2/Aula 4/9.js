// Bruno Moretto e Vinicius Finger

console.log(aumentaSalario('C', 1500))

function aumentaSalario(plano, salarioAtual) {
    switch (plano) {
        case 'A':
            salarioAtual *= 1.10;
            return mask(salarioAtual);
        case 'B':
            salarioAtual *= 1.15;
            return mask(salarioAtual);
        case 'C':
            salarioAtual *= 1.20;
            return mask(salarioAtual);
        default:
            return 'Este é um plano inválido!';
    }
}

function mask(valor) {
    return `R$${valor.toFixed(2).replace('.', ',')}`;
}