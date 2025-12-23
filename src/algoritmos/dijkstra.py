from math import inf

def dijkstra(cidades, origem:str, recebe_penalidade:bool = False, multiplicador_penalidade:float = 1.5):
    """
    Calcula a menor distancia 
    dijkstra(cidades, origem, recebe_penalidade, multiplicador_penalidade)

    cidades -> Lista de objetos Cidade
    origem -> String referente ao UF da cidade. Ex.: "RJ", "SP", "RS", "PE"
    recebe_penalidade -> Booleano que indica se barcos aumentam ou não o peso da distancia
    multiplicador_penalidade -> Indica a penalidade que barcos aplicam no peso sendo 1> incremental, e <1 decremental
    """
    # Dicinários de objetos cidade com os valores iniciais
    distancia = {cidade: inf for cidade in cidades}
    pai = {cidade: None for cidade in cidades}
    visitado = {cidade: False for cidade in cidades}

    distancia[origem] = 0

    while True:
        # Escolher a cidade não visitada com menor distância
        u = None
        menor_dist = inf

        for cidade in cidades:
            if not visitado[cidade] and distancia[cidade] < menor_dist:
                menor_dist = distancia[cidade]
                u = cidade

        # Se não achou nenhuma, terminou
        if u is None:
            break

        visitado[u] = True
        for v, (peso, usa_barco) in u.arestas_saida.items():
            if not visitado[v]:
                peso = peso*multiplicador_penalidade if usa_barco and recebe_penalidade else peso
                nova_dist = distancia[u] + peso
                if nova_dist < distancia[v]:
                    distancia[v] = nova_dist
                    pai[v] = u

    return distancia, pai

def construir_rota(pai, origem, destino):
    caminho = []
    atual = destino

    while atual is not None:
        caminho.append(atual)
        atual = pai[atual]

    caminho.reverse()

    if caminho[0] != origem:
        return None

    return caminho