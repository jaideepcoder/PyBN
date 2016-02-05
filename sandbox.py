import pandas as pd
from BaysianNetwork import *

data = pd.read_csv('data/census/census-income.data.csv', header=0)

bn = BayesianNetwork()

bn.read_from_dataframe(data)

print(bn.data)