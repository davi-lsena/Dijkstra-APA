from utils.io import carregarCSV, escolher_cidade
from algoritmos.dijkstra import dijkstra, construir_rota
from visualizacao.mapa_brasil import (
    carregar_mapa_brasil,
    centroides_por_uf,
    desenhar_mapa_base,
    desenhar_caminho
)
import matplotlib.pyplot as plt

def main():
    dados = carregarCSV("../data/processed/cidades.txt")
    cidades_por_uf = {c.UF.upper(): c for c in dados}
    
    origem = escolher_cidade(cidades_por_uf, "Digite a UF de origem: ")
    destino = escolher_cidade(cidades_por_uf, "Digite a UF de destino: ")

    
    #origem = next(c for c in dados if c.UF == "RJ")
    #destino = next(c for c in dados if c.UF == "MT")

    usaPenalidade = True
    penalidade = 1.5

    dist, pai = dijkstra(dados, origem, recebe_penalidade = usaPenalidade, multiplicador_penalidade = penalidade)
    caminho = construir_rota(pai, origem, destino)

    distancia_anterior = dist[origem]
    
    print(f"\nDijkstra - {origem.UF} → {destino.UF}\n")
    print(f"{'Cidade':<25} {'UF':<4} {'Trecho':>12} {'Acumulado':>14}")
    print("-" * 60)
    
    for c in caminho:
        trecho = dist[c] - distancia_anterior
        acumulado = dist[c]
    
        print(
            f"{c.Nome:<25} "
            f"{c.UF:<4} "
            f"{trecho:>12.1f} "
            f"{acumulado:>14.1f}"
        )
    
        distancia_anterior = dist[c]

    mapa = carregar_mapa_brasil()
    coords = centroides_por_uf(mapa)

    fig, ax = desenhar_mapa_base(mapa)
    desenhar_caminho(ax, caminho, coords, recebe_penalidade = usaPenalidade, peso_penalidade = penalidade)
    plt.show()

if __name__ == "__main__":
    main()