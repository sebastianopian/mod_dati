import pandas as pd

data_dict = {'JD': [2458135.5, 2458135.5, 2458135.5, 2458140.5, 2458140.5, 2458140.5, 2458240.5, 2458240.5, 2458240.5],
             'object': ['A1689', 'A1689', 'A2218', 'A1689', 'A1689', 'A2218', 'A1689', 'A370', 'A2218'],
             'band': ['J', 'K', 'J', 'J', 'K', 'J', 'J', 'K', 'J']}
df1 = pd.dataframe(data_dict)
df1