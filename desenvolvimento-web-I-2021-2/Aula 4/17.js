// Bruno Moretto e Vinicius Finger

console.log(contemCaracteresIguais('abc', 'estou testando'));

function contemCaracteresIguais(string1, string2) {
    string1 = string1.trim().toUpperCase();
    string2 = string2.trim().toUpperCase();

    let contains = true;
    let char = '';
    for(let i = 0; i < string1.length; i++) {
        char = string1.charAt(i);
        contains = string2.includes(char);
        if(!contains) {
            break;
        }
    }

    return contains;
}