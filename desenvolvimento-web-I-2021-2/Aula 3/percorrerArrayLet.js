//Nomes: Vinícius Finger (201920133), Bruno Moretto (201920129)
const funcs = []

for (let i = 0; i < 10; i++){
    funcs.push(function (){
        console.log(i)
    })
}

funcs[1]()
funcs[3]()