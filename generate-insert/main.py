import pandas as pd
import argparse

parser = argparse.ArgumentParser(description="Processa um arquivo Excel.")
parser.add_argument("file", help="Caminho para o arquivo Excel.")
args = parser.parse_args()


df = pd.read_excel("Tabela_One_Touch_Inativo.xlsx")

arquivo_saida = ".\Tabela_One_Touch_Inativo.xlsx"

arquivo_saida = arquivo_saida.split(".")
arquivo_saida = ".".join(arquivo_saida[:-1])
if arquivo_saida.startswith(".\\"):
    arquivo_saida = arquivo_saida[2:]

arquivo_saida = f"INSERT_{arquivo_saida}.sql"

tabela = "teste"
colunas = ["nome", "produto"]

with open(arquivo_saida, 'w') as file:
    for index, row in df.iterrows():
        valores = [row[coluna] for coluna in colunas]
        valores_formatados = ", ".join([f"'{valor}'" for valor in valores])
        query = f"INSERT INTO {tabela} VALUES ({valores_formatados} , 'N');"
        file.write(query + "\n")
