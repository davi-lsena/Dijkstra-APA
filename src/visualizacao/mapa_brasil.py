import geopandas as gpd
import matplotlib.pyplot as plt

def carregar_mapa_brasil():
    return gpd.read_file(
        "https://raw.githubusercontent.com/codeforamerica/click_that_hood/master/public/data/brazil-states.geojson"
    )


def centroides_por_uf(mapa):
    coords = {}

    for _, row in mapa.iterrows():
        uf = row["sigla"]
        centro = row.geometry.centroid
        coords[uf] = (centro.x, centro.y)

    return coords

def desenhar_mapa_base(mapa):
    fig, ax = plt.subplots(figsize=(12, 8), dpi=100)
    plt.subplots_adjust(right=0.75)

    mapa.plot(
        ax=ax,
        color="whitesmoke",
        edgecolor="black",
        linewidth=0.8
    )

    ax.set_title("Mapa do Brasil - Estados")
    ax.axis("off")

    return fig, ax


def desenhar_caminho(ax, caminho, coords, recebe_penalidade:bool=False, peso_penalidade:float = 1.5):
    distancia_total = 0
    linhas_legenda = []

    for cidade in caminho:
        x, y = coords[cidade.UF]
        ax.plot(x, y, "o", color="blue", markersize=2)
        ax.text(x, y, cidade.UF, fontsize=15, ha="center", va="center")

    for i in range(len(caminho) - 1):
        c1 = caminho[i]
        c2 = caminho[i + 1]

        x1, y1 = coords[c1.UF]
        x2, y2 = coords[c2.UF]

        dist, usa_barco = c1.arestas_saida[c2]

        # Penalidade
        penalidade = (peso_penalidade-1) * dist if usa_barco and recebe_penalidade else 0
        dist_exibida = dist + penalidade
        distancia_total += dist_exibida

        # Cor e tipo
        cor = "blue" if usa_barco else "black"
        tipo = "Barco" if usa_barco else "Terra"

        # Desenhar seta
        ax.annotate(
            "",
            xy=(x2, y2),
            xytext=(x1, y1),
            arrowprops=dict(
                arrowstyle="->",
                color=cor,
                linewidth=1.5
            )
        )

        xm = (x1 + x2) / 2
        ym = (y1 + y2) / 2

        texto_mapa = (
            f"{dist} + {int(penalidade)}"
            if usa_barco and recebe_penalidade else f"{dist}"
        )

        ax.text(
            xm,
            ym,
            texto_mapa,
            fontsize=10,
            color=cor,
            ha="center",
            va="center",
            bbox=dict(
                boxstyle="round,pad=0.2",
                fc="white",
                ec=cor,
                alpha=0.85
            )
        )

        linhas_legenda.append(
            f"{c1.UF} → {c2.UF} | {tipo} | {dist} + {int(penalidade)} = {int(dist_exibida)}"
            if usa_barco and recebe_penalidade
            else f"{c1.UF} → {c2.UF} | {tipo} | {dist}"
        )

    legenda_texto = "Rota por segmento\n\n"
    legenda_texto += "\n".join(linhas_legenda)
    legenda_texto += f"\n\nDistância total: {int(distancia_total)}"

    """ax.text(
        1.02, 0.5,
        legenda_texto,
        transform=ax.transAxes,
        fontsize=10,
        va="center",
        ha="left",
        bbox=dict(
            boxstyle="round,pad=0.5",
            fc="white",
            ec="black",
            alpha=0.9
        )
    )"""
    
    titulo = "Com penalidades" if recebe_penalidade else "Sem penalidades"

    ax.text(
        1.02, 0.95,
        titulo,
        transform=ax.transAxes,
        fontsize=12,
        fontweight="bold",
        va="top",
        ha="left"
    )

    ax.plot([1.02, 1.25], [0.93, 0.93], transform=ax.transAxes, color="black", lw=1)
    
    ax.text(
        1.02, 0.90,
        legenda_texto,
        transform=ax.transAxes,
        fontsize=10,
        va="top",
        ha="left"
    )