from modelo.cidade import Cidade

def carregarCSV(txt):
    with open(txt, 'r', encoding='utf-8') as arq:
        dados = arq.readlines()
    
    cidades = {}

    #Criar cidades
    for linha in dados:
        linha = linha.strip()
        aux = linha.split(",")

        nome = aux[0]
        uf = aux[1]

        cidades[uf] = Cidade(nome, uf)

    #Criar vizinhanças
    for linha in dados:
            linha = linha.strip()
            aux = linha.split(",")
    
            cidade_atual = cidades[aux[1]]
    
            for coluna in aux[2:]:
                usa_barco = False
    
                if coluna[0] == "*":
                    coluna = coluna[1:]
                    usa_barco = True
    
                destino_uf, dist = coluna.split(":")
                dist = int(dist)
    
                cidade_atual.adicionar_aresta(
                    cidades[destino_uf],
                    dist,
                    usa_barco
                )     
    return list(cidades.values())

def escolher_cidade(cidades_por_uf, mensagem):
    ufs = sorted(cidades_por_uf.keys())
    total = len(ufs)
    por_linha = (total + 2) // 3

    print("\nUFs disponíveis:")
    for i in range(0, total, por_linha):
        print(" | ".join(ufs[i:i + por_linha]))

    while True:
        uf = input(f"{mensagem} ").strip().upper()
        if uf in cidades_por_uf:
            return cidades_por_uf[uf]
        print(f"UF inválida: '{uf}'. Tente novamente.")