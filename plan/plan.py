import io
import requests
import pandas as pd
dfs = pd.read_html('http://www.plan.uz.zgora.pl/grupy_plan.php?pId_Obiekt=22649',header=0)
df=dfs[0]
values=['Poniedziałek','Wtorek','Środa','Czwartek','Piątek','B']
print(df[df.PG.isin(values)])
