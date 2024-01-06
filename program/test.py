import pandas as pd
import numpy as np

data_dict = {'JD': [2458135.5, 2458135.5, 2458135.5, 2458140.5, 2458140.5, 2458140.5, 2458240.5, 2458240.5, 2458240.5],
             'object': ['A1689', 'A1689', 'A2218', 'A1689', 'A1689', 'A2218', 'A1689', 'A370', 'A2218'],
             'band': ['J', 'K', 'J', 'J', 'K', 'J', 'J', 'K', 'J']}
df1 = pd.DataFrame(data_dict)
print(df1)