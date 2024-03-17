//Bruno Moretto, Vinicius Finger
//Pacote usado: prompt-sync

const prompt = require('prompt-sync')();

function calculaNumeros(primeiroNumero, operacao, segundoNumero){
    switch(operacao){
        case "+":
            return Number(primeiroNumero) + Number(segundoNumero);
        case "-":
            return Number(primeiroNumero) - Number(segundoNumero);
        case "*":
            return Number(primeiroNumero) * Number(segundoNumero);
        case "/":
            return Number(primeiroNumero) / Number(segundoNumero);
        default:
            throw new Error("Operação inválida.");
    }
}

function recebeValores(){
    let primeiroNumero = prompt("Insira um número: ");
    let segundoNumero = prompt("Insira outro número: ");
    let operacao = prompt("Insira uma operação (+, -, * ou /): ");
    return {primeiroNumero, segundoNumero, operacao}
}

function printaResultado(resultado){
    console.log("O resultado é " + resultado);
}

let valores = recebeValores();
let resultado = calculaNumeros(valores.primeiroNumero, valores.operacao, valores.segundoNumero);
printaResultado(resultado);