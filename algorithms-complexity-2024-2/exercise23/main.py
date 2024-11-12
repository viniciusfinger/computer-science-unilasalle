import os
from zlib import crc32


def gera_relatorio(tamanho_vetor: int, hash_map_titulos: dict, hash_map_posicoes_titulos_com_nomes: dict):
    this_dir = os.path.dirname(os.path.abspath(__file__))
    relatorio_path = os.path.join(this_dir, f"relatorio_{tamanho_vetor}.txt")

    with open(relatorio_path, 'w', encoding='utf-8') as f:
        posicoes_nao_utilizadas = [i for i in range(tamanho_vetor) if i not in hash_map_titulos]
        if posicoes_nao_utilizadas:
            f.write("Posições não utilizadas:\n")
            for posicao in posicoes_nao_utilizadas:
                f.write(f"{posicao}\n")
        else:
            f.write("Todas as posições foram utilizadas.\n")

        f.write("\nPosições com lotação:\n")
        for indice, titulos in hash_map_titulos.items():
            if len(titulos) > 1:
                f.write(f"Posição {indice} tem {len(titulos)} títulos: {', '.join(titulos)}\n")

        f.write("\nPosições e nomes dos títulos da tabela hash_map_posicoes_titulos_com_nomes:\n")
        for titulo, posicao in hash_map_posicoes_titulos_com_nomes.items():
            f.write(f"Título: {titulo} - Posição: {posicao}\n")

def processa_livros(tamanho_vetor: int):
    hash_map_titulos = {}
    hash_map_posicoes_titulos_com_nomes = {}

    this_dir = os.path.dirname(os.path.abspath(__file__))
    livros_path = os.path.join(this_dir, "livros.txt")

    with open(livros_path, 'r', encoding='utf-8') as f:
        livros = [linha.strip() for linha in f]

        nomes = ["Vinicius", "Kauã", "Guilherme"]
        livros_com_nomes = []
        for nome in nomes:
            livros_com_nomes.append(f"ESTUDANDO COMPLEXIDADE COM {nome}")
            livros = livros + livros_com_nomes

        for titulo in livros:
            hash_titulo = crc32(titulo.encode())
            indice = hash_titulo % tamanho_vetor
            if indice not in hash_map_titulos:
                hash_map_titulos[indice] = []
            hash_map_titulos[indice].append(titulo)
            if titulo in livros_com_nomes:
                hash_map_posicoes_titulos_com_nomes[titulo] = indice
    
    return hash_map_titulos, hash_map_posicoes_titulos_com_nomes
 

tamanhos_vetor = [20, 131, 1021]

for tamanho_vetor in tamanhos_vetor:
    hash_map_titulos, hash_map_posicoes_titulos_com_nomes = processa_livros(tamanho_vetor=tamanho_vetor)
    gera_relatorio(tamanho_vetor, hash_map_titulos, hash_map_posicoes_titulos_com_nomes)

