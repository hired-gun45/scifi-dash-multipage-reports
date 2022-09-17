import plotly.express as px
import pandas as pd
from datetime import datetime
from data.data import data
import pytz

class home_fns:

    def update_line_chart(self, value, session, interval):
        print("about to load data for ", value)
        df, data_table, status, text = data.load_data(value)
        if len(df) == 0:
            return {}, [], status, text
        # change the timestamp into just hh:mm string
        for index in range(0, len(df)):
            dt_object = datetime.fromtimestamp(df.iat[index, 1])
            utc_dt = dt_object.astimezone(pytz.utc)
            localDatetime = utc_dt.astimezone(pytz.timezone('US/Eastern'))
            date_time = localDatetime.strftime("%H:%M")
            df.iat[index, 1] = date_time

        print("got data for " + value)
        print(df)
        col_names = df.columns[2:]
        fig = px.line(df, x="Time", y=col_names,
                    title="Bob\'s Cool Line Graph")
        fig.update_traces()
        return (fig, data_table, status, text)

home = home_fns()

