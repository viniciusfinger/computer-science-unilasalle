//Bruno Moretto, Vinicius Finger
//Pacote usado: prompt-sync
function validaDiaSemana(valorDiaSemana){
    switch (valorDiaSemana){
        case "1":
            return "Domingo";
        case "2":
            return "Segunda-Feira";
        case "3":
            return "Terça-Feira";
        case "4":
            return "Quarta-Feira";
        case "5": 
            return "Quinta-Feira";
        case "6":
            return "Sexta-Feira";
        case "7":
            return "Sábado";
    }
}

const prompt = require('prompt-sync')();

let valorDiaSemana = prompt("Insira o dia da semana: ");

console.log(`Hoje é ${validaDiaSemana(valorDiaSemana)}`)
