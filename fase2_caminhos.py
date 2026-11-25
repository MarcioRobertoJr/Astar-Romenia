# -*- coding: utf-8 -*-
# fase2_caminhos.py — Fase 2: funções, custo de um caminho e os valores g, h e f.
# Rode com: python fase2_caminhos.py
# ----- PASSO 1: importar os dados -----

from mapa import mapa_romenia, heuristica_bucareste

# ----- PASSO 2: função que devolve o custo de UMA estrada -----
def custo_da_estrada(origem, destino):
   """Devolve os km da estrada origem -> destino, ou None se ela não existe."""
   for vizinho, custo in mapa_romenia[origem]:
     if vizinho == destino:
       return custo
   return None

