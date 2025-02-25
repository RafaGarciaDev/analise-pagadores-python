import csv

def analisar_csv(arquivo_csv):
    with open(arquivo_csv, newline='', encoding='utf-8') as arquivo:
        leitor = csv.reader(arquivo)
        cabecalho = next(leitor)  # Lê a primeira linha como cabeçalho
        
        print("Índices das colunas:")
        for indice, nome_coluna in enumerate(cabecalho):
            print(f"Índice {indice}: {nome_coluna}")

# Exemplo de uso
arquivo_csv = r"C:\Users\rafae\Downloads\dados_processados (1).csv"  # Substitua pelo nome do seu arquivo
analisar_csv(arquivo_csv)
