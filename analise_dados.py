

import pandas as pd



def analisar_pagadores(caminho_arquivo):
    try:
        # Carregar os dados
        dados = pd.read_csv(caminho_arquivo, encoding="ISO-8859-1", sep=";")
        print("Arquivo carregado com sucesso!")

        # Converter Endividamento para número
        dados["Endividamento"] = dados["Endividamento"].astype(str).str.replace("%", "").astype(float)

        # Definir ordem de classificação dos pagadores
        ordem_pagadores = {
            "Excelente": 1,
            "Muito Bom": 2,
            "Bom": 3,
            "Regular": 4,
            "Ruim": 5,
            "Irregular": 6
        }

        # Criar coluna auxiliar para ordenação
        dados["Ranking"] = dados["Histórico de Pagamento"].map(ordem_pagadores)

        # Ordenar os clientes do melhor para o pior pagador
        dados_ordenados = dados.sort_values(by=["Ranking", "Endividamento"], ascending=[True, True])

        # Exibir os clientes ordenados
        print("Lista de Clientes do Melhor para o Pior Pagador:")
        print(dados_ordenados[["ID", "Nome", "Histórico de Pagamento", "Endividamento"]])

    except Exception as e:
        print(f"Erro ao processar os dados: {e}")

# Exemplo de uso
caminho_arquivo = r"C:\Users\rafae\Downloads\dados_processados.csv"
analisar_pagadores(caminho_arquivo)
