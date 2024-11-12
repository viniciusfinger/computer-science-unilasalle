Estas instruções são parte do exercício EX23. São instruções separadas para facilitar. A entrega deste exercício deve ser realizada no formulário de entrega, onde tem outras questões. 
O formulário está em https://forms.gle/ha9gA2bFz1d8Bu2L6

Exercício de programação
Pode escolher a linguagem


HABILIDADES DE PROGRAMAÇÃO REQUERIDAS:
saber ler uma string, uma por linha, de um arquivo txt
usar uma função de redução (hash) sobre cada uma das strings
usar operador de resto para reduzir o hash ao intervalo do vetor
gerar um relatório sobre qual índice cada título usou ou contabilizar, índice por índice, quantas chaves ficaram

FUNÇÕES HASH TIPICAMENTE ENCONTRADAS NAS LINGUAGENS
md5: converte qualquer sequência binária, de qualquer coisa e de qualquer tamanho, em um número fixo de 128 bits.
CUIDADO AO USAR: como o md5 gera um número de 128 bits, muito maior que a capacidade da ULA, pode ser que a linguagem que você estiver usando não trabalhe com inteiros tão grandes
Python não tem frescura, trabalha nativamente com inteiros de qualquer tamanho
No C será necessário usar uma lib para big numbers, como o bn.h
No java será necessário usar uma classe Big Number
Em outras linguagens, não sei.
Veja o artigo Programação com números inteiros gigantes [Artigo]
crc32: converte qualquer sequência para um número de 32 bits. É usado para crc (verificação de erro) mas pode sim ser usado como hash. Se o teu vetor tivesse 4 bilhões de entradas, já poderia usar direto a saída do crc32 como índice (mas neste exercício o tamanho máximo do vetor é 1021 posições). No php e no C a função crc32 tem exatamente este nome (no C tem que inserir a lib zlib.h). No python eu encontrei também o zlib e o método zlib.crc32.
crc16: exatamente o mesmo que o crc32, mas gerando um número de 16 bits.



Exemplo feito no LINUX, linha de comando:
Livros títulos:
 "Apenas um teste"
"Entao, mais um livro de teste"
"Entao, outro teste"
"Livro de testes"
usando o hash crc32 que tenho implementado em php. Um vetor de apenas 7 posições (ver imagem com o resultado)

Veja que "Apenas um teste" fica na posição 0 do vetor, "Então, mais um livro de teste" na 4, "Então, outro teste" na posição 5 e "Livro de testes" fica na 0. A posição 0 tem dois títulos. Pos 1, 2, 3, e 6 não foram usadas para este exemplo


DEFINIÇÃO DO EXERCÍCIO
É parte do EX23 e deve ser entregue lá, junto com as demais questões. Pode ser feito em grupos de até 4 integrantes, desde que o grupo trabalhe nele em aula.

Considere os títulos de livros, muitos, disponibilizados em um arquivo (o arquivo está disponível em https://drive.google.com/file/d/1MEqKu7z-7ZHZnCWKouPsgBrZFlYFV18G/view). Este arquivo tem 1050 títulos não repetidos de livros.

Cada linha do arquivo tem um título único de um livro (string).

Adicione mais alguns títulos de livros que tenham a seguinte estrutura: 
"Estudando complexidade com NOME" 
onde nome é o nome individual de cada membro do grupo (Exemplo: "Estudando complexidade com Elgio Schlemer"). Um grupo com quatro integrantes terá 4 títulos a mais. O arquivo usado por um grupo com 4 integrantes terá 1054 títulos. Pode, se quiser, inserir estes títulos a mais dentro do código (para não alterar o arquivo fornecido).

Usando uma função de hash para converter string em inteiro (ver sugestões de funções existentes nas linguagens), veja em quais posições de um vetor cada título será armazenado para um vetor de:

A) 20 posições
B) 131 posições
C) 1021 posições

Veja se, para cada caso (A), (B) e (C) houveram posições do vetor que não foram usadas ou que houve "lotação" de alguma posição do vetor. Um mesmo título de livro mudou de posição no vetor em função do tamanho do vetor? Especificamente mostre, no relatório, onde os títulos que vocês criaram deve ficar no vetor.

Entregue o código fonte e suas conclusões.


UM EXEMPLO FEITO EM LINUX LINHA DE COMANDO
Apenas para servir de inspiração


Usei o comando bash:
N=111; cat livros2.txt | while read linha; do 
H=crc32.php "$linha";POS="$(($H % $N))"; 
printf "%-4d  %s\n" "$POS" "$linha"; done|sort -n


Onde: 
Eu já tenho o script php que gera hashes crc32 (o crc32.php) e vocês não tem.
defini uma variável N com o tamanho do vetor (no exemplo 111, ou seja, índices de 0 a 110)
usei cat para ler o arquivo e um while read para pegar linha por linha na variável linha
para cada "linha", chamei meu script php, obtive o hash de 32 bits de cada título
usando a calculadora interna do bash (invocada por $(( )) ) reduzi o hash 32 bits para um número de 0 a 110 (usando o operador de resto, passando N)
imprimi o índice do vetor e o título, ordenando numericamente (sort -n) as saídas
fiz um print de imagem apenas de uma mostra, pois o arquivo livros2.txt tinha 309 livros.