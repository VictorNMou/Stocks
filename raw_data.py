import yfinance as yf
import polars as pl
from tqdm import tqdm
from connection import connection

# Lista das ações a serem consideradas
acoes = [
    'AAPL', 'MSFT', 'NVDA', 'GOOGL', 'AMZN', 'META', 'TSM', 'AVGO', 'TSLA', 'TCEHY',  # EUA
    'VALE3.SA', 'PETR4.SA', 'ITUB4.SA', 'BBDC4.SA', 'ABEV3.SA', 'MGLU3.SA', 
    'B3SA3.SA', 'BPAC11.SA', 'WEGE3.SA', 'JBSS3.SA'  # Brasil
]

# Função para baixar os dados
def obter_dados(acao):
    dados = yf.download(acao, interval="1d")
    dados.reset_index(inplace = True)
    return pl.DataFrame(dados)

# Conectando ao banco de dados PostgreSQL
conn = connection.connection()#.create_connection()
# cursor = conn.cursor()

# Loop para obter os dados de cada ação e inserir no banco de dados
for acao in acoes:
    print(f"Baixando dados para: {acao}")
    dados = obter_dados(acao)
    
    conn.insert_dataframe_in_database('raw.acoes',dados, 'replace')

print("Dados importados e salvos no banco de dados com sucesso!")