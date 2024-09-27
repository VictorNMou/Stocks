from dotenv import load_dotenv
import os
from polars import DataFrame

class connection:

    def __init__(self) -> None:
        self.conn = self.__create_connection()

    def __create_connection(self):
        # Conectando ao banco de dados PostgreSQL

        load_dotenv()
        host = os.getenv('DB_HOST'),
        port = os.getenv('DB_PORT'),
        database = os.getenv('DB_NAME'),
        user = os.getenv('DB_USER'),
        password = os.getenv('DB_PASSWORD')
        host = host[0]
        port = port[0]
        database =database[0]
        user = user[0]

        conn = f"postgresql://{user}:{password}@{host}:{port}/{database}"

        return conn
    
    def insert_dataframe_in_database(self, tb_name: str, data: DataFrame, exists: str):
        """Method responsible for writing records stored in a DataFrame to a MySQL database.

        Args:
            tb_name (str): Table name in the database.
            data (DataFrame): DataFrame with data.
        """
        print(f'Insert: {tb_name}')
        connection = self.conn
        
        try:
            print()
            data.write_database(tb_name, 
                        connection = connection, 
                        if_table_exists = exists)

        
        except Exception as err:
            print(err)