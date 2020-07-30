import requests
import sqlalchemy as sql
import pandas as pd

class ParseCSV:

    filepath = 0
    db_string = 0

    def __init__(self, filepath, db_string):
        self.filepath = filepath
        self.db_string = db_string

        self.chat_id = '*****'
        self.url = f'https://api.telegram.org/botTOKENBOT/sendMessage'

    # csv -> таблица
    def CSVtoTable(self, filepath):
        data = pd.read_csv(filepath, delimiter=',')
        return data

        #таблица -> бд
    def TableToDB(self, data, db_string):
        data.to_sql(con=db_string, name='tb_burden_countries_20200729', if_exists='replace')
        requests.post(self.url, dict(chat_id=self.chat_id, text="таблица загружена в бд"))

    #бд -> консоль
    def DBtoConsole(self, db_string):
        engine = sql.create_engine(db_string)
        res = engine.execute("select * FROM TB_burden_countries_20200729")
        requests.post(self.url, dict(chat_id=self.chat_id, text="таблица считана"))
        return res

    #выводим массив на экран
    def printDB(self, res):
        for item in res:
            print(item)