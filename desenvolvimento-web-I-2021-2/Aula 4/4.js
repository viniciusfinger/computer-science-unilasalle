//Bruno Moretto, Vinicius Finger
//Pacote usado: prompt-sync

const prompt = require('prompt-sync')();


function inputValoresDivisao(){
    let valoresDivisao = [];
    valoresDivisao.push(prompt("Insira o dividendo: "));
    valoresDivisao.push(prompt("Insira o divisor: "));
    return valoresDivisao;
}

function divideValores(valoresDivisao){
    let resultado = Math.trunc(valoresDivisao[0] / valoresDivisao[1]);
    let resto = valoresDivisao[0] % valoresDivisao[1];
    return {resultado, resto}
}

let valoresDivisao = inputValoresDivisao();
let resultados = divideValores(valoresDivisao);
console.log(resultados)