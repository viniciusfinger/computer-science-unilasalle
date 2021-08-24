//Bruno Moretto, Vinicius Finger
//Pacote usado: prompt-sync

const prompt = require('prompt-sync')();



function inputLadosTriangulo(){
    let ladosTriangulo = []
    ladosTriangulo.push(prompt('Insira um lado do triângulo: '));
    ladosTriangulo.push(prompt('Insira mais um lado do triângulo: '));
    ladosTriangulo.push(prompt('Insira o terceiro lado do triângulo: '));
    return ladosTriangulo;
}

function classificaTriangulo(ladosTriangulo) {
    const [ladoA, ladoB, ladoC] = ladosTriangulo;
    if (ladoA == ladoB && ladoB == ladoC) {
        return "Triângulo Equilátero";
    } else if (ladoA == ladoB || ladoB == ladoC || ladoA == ladoC) {
        return "Triângulo Isóceles";
    } else {
        return "Triângulo Escaleno";
    }
}

let ladosTriangulo = inputLadosTriangulo();
let tipoTriangulo = classificaTriangulo(ladosTriangulo);

console.log(`O triângulo é um ${tipoTriangulo}`);

