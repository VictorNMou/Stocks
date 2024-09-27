import yfinance as yf
import polars as pl
from tqdm import tqdm
import datetime
from connection import connection

def obter_dados(acao, start_date, end_date):
    dados = yf.download(acao, interval="1d",start=start_date, end=end_date)
    dados.reset_index(inplace = True)
    return pl.DataFrame(dados)

conn = connection.connection()

query = "select * from analytics.tickers"
acoes = conn.read_dataframe(query=query)
tk_list = pl.Series(acoes.select('ticker')).to_list()
end_date = datetime.datetime.today().date()

for acao in tqdm(tk_list):
    query = f"""select max(a."Date") as date from raw.acoes a where ticker = '{acao}'"""
    df = conn.read_dataframe(query=query)
    start_date = df.select("date").to_series()[0]
    start_date = start_date.date()
    if start_date < end_date:
        print(f"Baixando dados para: {acao}")
        dados = obter_dados(acao, start_date, end_date)
        dados = dados.with_columns(pl.lit(acao).alias('ticker')) 
        conn.insert_dataframe_in_database('raw.acoes',dados, 'append')
    else:
        print("Database Updated")