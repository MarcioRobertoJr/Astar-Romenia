# -*- coding: utf-8 -*-
# fase3_fronteira.py — Fase 3: o nó de busca e a fronteira, feitos à mão.
# Rode com: python fase3_fronteira.py

# ----- PASSO 1: importar os dados -----
from mapa import mapa_romenia, heuristica_bucareste

  #----- PASSO 2: montar o nó inicial e a fronteira -----
  # Um nó é uma tupla com 4 posições: (f, g, cidade, caminho)
inicio = 'Arad'
g = 0
h = heuristica_bucareste[inicio]
no_inicial = (g + h, g, inicio, [inicio])

fronteira = [no_inicial]
print('Fronteira no começo:', fronteira)

