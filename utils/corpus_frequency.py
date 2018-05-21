"""
this file has English corpus frequency data: http://norvig.com/ngrams/.  It's not immediately clear from what sources it was compiled, but will be sufficient.
"""
import numpy as np

df_corpus = pd.read_table('./utils/freq_dict.txt', sep='\t', header=None)
df_corpus.columns = ['word', 'count']
N = np.sum(df_corpus['count'])
df_corpus['freq'] = df_corpus['count']/N
