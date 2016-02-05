import numpy as np
import scipy as sp
import pandas as pd
import matplotlib as plt
from collections import Counter

class BayesianNetwork(object):

    def __init__(self):
        self.data = pd.DataFrame()
        self.pdf = dict()
        self.cpd = dict()
        self.structure = list()
        
    def read_from_dataframe(self, df, col_names):
        self.data = df
        self.data.columns = col_names
        
    def generate_pdf(self):
        pdf = self.pdf
        data = self.data
        for column in data.columns:
            pdf[column] = pd.DataFrame.from_dict(dict(Counter(data[column])),
                                                orient='index')
            pdf[column] = pdf[column]/pdf[column].sum()
            pdf[column].columns = ['P('+column+')']
            
    def generate_graph(self, graph):
        self.structure = graph
        data = self.data
        for node in graph:
            this = node[0]
            parents = list()
            parents.extend(node[1])
            parents.append(this)
            df = data[parents]
            df['COPY'] = df[this]
            self.cpd[this] = pd.pivot_table(df, index=node[1], values='COPY',
                                   columns=[this], fill_value=0,
                                    aggfunc=[np.sum])


graph = [('AAGE', ['ACLSWKR', 'ADTIND'])]

columns = ['AAGE', 'ACLSWKR', 'ADTIND', 'ADTOCC', 'AHGA', 'AHRSPAY', 'AHSCOL',
'AMARITL', 'AMJIND', 'AMJOCC', 'ARACE', 'AREORGN', 'ASEX', 'AUNMEM', 'AUNTYPE',
 'AWKSTAT', 'CAPGAIN', 'CAPLOSS', 'DIVVAL', 'FILESTAT', 'GRINREG', 'GRINST',
 'HHDFMX', 'HHDREL', 'MARSUPWT', 'MIGMTR1', 'MIGMTR3', 'MIGMTR4', 'MIGSAME',
 'MIGSUN', 'NOEMP', 'PARENT', 'PEFNTVTY', 'PEMNTVTY', 'PENATVTY', 'PRCITSHP',
 'SEOTR', 'VETQVA', 'VETYN', 'WKSWORK', 'YEAR', 'GRSINC']

bn = BayesianNetwork()
bn.read_from_dataframe(pd.read_csv('data/census/census-income.data.csv',
                                   header=0), columns)
                                   
bn.data.describe()
bn.generate_pdf()
# print(bn.pdf['AAGE'])
tbl = bn.generate_graph(graph)