import plotly.figure_factory as ff
import pandas as pd

df=pd.read_csv("mobile.csv")
avg_rating=df["Avg Rating"].to_list()
fig=ff.create_distplot([avg_rating],["rating"],show_hist=False)
fig.show()

