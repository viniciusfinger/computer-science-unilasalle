// Bruno Moretto e Vinicius Finger

const notas = [8.5, 10, 2, 3.7, 6, 7.5, 5.5, 10.1, -3];

calculaConceito(notas);

function calculaConceito(notas) {
    notas.forEach((nota, index) => {
        if(nota < 0 || nota > 10) {
            console.log(`A nota ${index+1} precisa estar dentro do intervalo 0 e 10!`);
        } else if(nota <= 4.9) {
            console.log(`A nota ${index+1} de valor ${nota} teve o conceito ${'D'}`)
        } else if(nota <= 6.9) {
            console.log(`A nota ${index+1} de valor ${nota} teve o conceito ${'C'}`)
        } else if(nota <= 8.9) {
            console.log(`A nota ${index+1} de valor ${nota} teve o conceito ${'B'}`)
        } else {
            console.log(`A nota ${index+1} de valor ${nota} teve o conceito ${'A'}`)
        }
    })
}