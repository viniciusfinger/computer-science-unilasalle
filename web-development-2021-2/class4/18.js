//Bruno Moretto, Vinicius Finger
let vetorPilha =[1,2,3,4,5]
let vetorAdiciona = [6,7,8,9,10]

function adiconaNaPilha(numero){
    vetorPilha.push(numero)
    console.log("inserindo o número " + numero + " na pilha.")
}

vetorAdiciona.forEach(adiconaNaPilha)

console.log("Pilha: " + vetorPilha);
console.log("Adiciona: " + vetorAdiciona);