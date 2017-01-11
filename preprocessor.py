import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt
from datetime import datetime
import numpy as np

def load_and_sample_data():
    """
    Import data from the dataset
    :return: Dictionary samples
    """
    print('loading data...')
    data = pd.read_csv('./dataset/Link.csv')
    df_percent = data.sample(frac=0.001)
    return df_percent

def make_graph(data):
    """

    :param data:
    :return:
    """
    print('Building the graph...')
    B = nx.Graph()
    B.add_nodes_from(data['company_name'], bipartite=0)
    B.add_nodes_from(data['investor_name'], bipartite=1)
    B.add_weighted_edges_from(
        [(row['company_name'], row['investor_name'], 1) for idx, row in data.iterrows()],
        weight='weight'
    )