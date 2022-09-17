import requests
import json
import pandas as pd

class Data:
    def __init__(self):
        return

    def stash_data(self, date):
        out_url = "/tmp/timeseries.csv"

        url = 'https://gi8st4xbib.execute-api.us-east-2.amazonaws.com/request'
        myobj = {
            "operation": "get_transaction_timeseries",
            "args": {
                "file_info": {
                    "day": date,
                    "bucket_name": "scifi-trades",
                    "file_name": date + "/trades/positions.json"
                }
            }
        }

        response = requests.post(url, json = myobj)
        response_text = json.loads(response.text)
        if (response_text.get("errorMessage")):
            return  "Error", response_text["errorMessage"]
        elif not response.status_code == 200:
            return "Error", response.text
        else:
            out = open(out_url,"w")
            out.writelines(response_text["body"]["results"])
            out.close()
            return "Success", out_url

    def get_table(self, df):
        last_row = df.iloc[-1]
        t = last_row["Time"]
        open_prices = df.query("`Time` == @t.T and `Datatype` == 'calculated_open_price'")
        close_prices = df.query("`Time` == @t.T and `Datatype` == 'calculated_close_price'")
        col_names = df.columns[3:-1]
        table = []
        for col_name in col_names:
            open_price = open_prices.iloc[0][col_name]
            close_price = close_prices.iloc[0][col_name]
            table.append({
                "symbol": col_name,
                "opening_price": open_price,
                "closing_price": close_price
            })

        return table

    def load_data(self, date):
        status, text = self.stash_data(date)
        if status == "Error":
            if "(NoSuchKey)" in text:
                text = "No data found for this day"
                df = {}
            return {}, [], status, text
        df = pd.read_csv(text)
        if len(df) == 0:
            status = "Warning"

        data_table = self.get_table(df)
        df = df.query("Datatype == 'calculated_pnl'")
        df = df.drop(['Datatype'], axis=1)
        df = df.drop(['Portfolio'], axis=1)
        df.reindex()
        return df, data_table, status, ""

data = Data()