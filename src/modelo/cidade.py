class Cidade:
    def __init__(self, Nome, UF):
        self.Nome = Nome
        self.UF = UF
        self.arestas_saida = {}

    def __repr__(self):
        saidas = "\n"
        for cidade, (dist, usa_barco) in self.arestas_saida.items():
            saidas += (
                f"\t→ {cidade.UF:<3} | "
                f"Distancia: {dist:>5} | "
                f"Usa barco: {'Sim' if usa_barco else 'Não'}\n"
            )

        return (
            f"-- {self.Nome} ({self.UF}) --\n"
            f"Arestas de saída:{saidas}\n"
        )

    def __hash__(self):
        return hash(self.UF)

    def __eq__(self, outra):
        return isinstance(outra, Cidade) and self.UF == outra.UF
        

    def adicionar_aresta(self, destino, distancia, usa_barco):
        self.arestas_saida[destino] = (distancia, usa_barco)