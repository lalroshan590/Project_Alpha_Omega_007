import pandas as pd

def load_protein_data(file_path):
    return pd.read_csv(file_path)

def load_synthesis_pathway_data(file_path):
    return pd.read_csv(file_path)

def load_reaction_condition_data(file_path):
    return pd.read_csv(file_path)