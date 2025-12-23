# APA - Trabalho Final
## Algoritmo de Dijkstra  
### Implementação sequencial VS Paralelização em GPU

## Contexto

Este projeto faz parte da disciplina **Análise e Projeto de Algoritmos (APA)** e tem como objetivo
estudar, implementar e analisar o algoritmo de **Dijkstra** na linguágem desejada, e compara-lo ao algoritmo apresentado no artigo disponivel em: https://arxiv.org/pdf/2504.17033.

Além disso o tema específico do projeto, conforme orientação, consiste em **avaliar o comportamento do algoritmo de Dijkstra em
ambiente sequencial (CPU)** e **compará-lo com uma implementação paralela utilizando GPU**,
ainda em desenvolvimento.

---

## Objetivos

- Implementar o algoritmo de **Dijkstra clássico** em Python;
- Aplicar o algoritmo a um **problema real de rotas geográficas**, utilizando dados de estados brasileiros (extraído manualmente do Google Maps);
- Visualizar o caminho mínimo obtido sobre o **mapa do Brasil**;
- Analisar custos de rotas, incluindo penalidades específicas (ex.: travessias por barco);
- Preparar a base conceitual e estrutural para:
  - comparação com versões paralelas em memória compartilhada;
  - comparação com uma implementação paralela em **GPU**.

---

## Algoritmos abordados

Atualmente implementado:
- **Dijkstra clássico (sequencial)**
- Implementação paralela em GPU (em construção).

---

## Descrição da implementação atual

A implementação atual modela o problema como um **grafo direcionado ponderado**, onde:

- Cada vértice representa uma **cidade/estado**;
- As arestas representam conexões entre cidades;
- Os pesos das arestas representam distâncias;
- Algumas rotas podem incluir **penalidades adicionais** (ex.: uso de transporte fluvial/barcos).

O algoritmo de Dijkstra é utilizado para encontrar o **caminho mínimo** entre uma origem e um destino,
predeterminados pelo usuário.

O resultado é apresentado de duas formas:
- **Texto**, com o detalhamento do caminho e das distâncias acumuladas;
- **Visualização gráfica**, com o caminho destacado sobre o mapa do Brasil.

## Ambiente de execução e dependências

O projeto foi desenvolvido em Python, com duas formas de configuração:

- **Ambiente Conda**, utilizado durante o desenvolvimento e experimentação.
- **Ambiente Python padrão**, permitindo a execução do projeto sem uso do Conda.

As dependências estão organizadas da seguinte forma:

- `environment.yml`: descreve o ambiente Conda completo utilizado durante o desenvolvimento;
- `requirements.txt`: lista as bibliotecas Python necessárias `.py`.
