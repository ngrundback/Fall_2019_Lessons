'''
Given the above, write code using Python (Pandas library) to show what percent of active stores were fraudulent by day.
Some clarifications:

We want one value for each day in the month.
A store can be fraudulent and active on same day. E.g. they could generate revenue until 10AM, then be flagged as fradulent from 10AM onward.
'''


import pandas as pd
import numpy as np

data = [[1, '07/19', 'fraud', 10000], [2, '07/19', 'open', 15000], [3, '07/19', 'open', 2000],
        [1, '07/20', 'open', 10000], [2, '07/20', 'fraud', 10000], [3, '07/20', 'open', 2000]]
df = pd.DataFrame(data, columns = ['store_id', 'date', 'status', 'reveune'])
print(df)

active = df[df.reveune>0].copy()
#print(active)
active['fraud'] = active.status == 'fraud'
print(active)
# calculate the % of active users that were fraudulent by date
fr = active.groupby('date').fraud.mean()*100
print(fr)
