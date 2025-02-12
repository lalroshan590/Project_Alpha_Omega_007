import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from utils.data_loader import load_synthesis_pathway_data

def train_synthesis_pathway_model(X_train, y_train):
    model = RandomForestClassifier(n_estimators=100, random_state=42)
    model.fit(X_train, y_train)
    return model

def optimize_synthesis_pathway(model, protein_sequence):
    predicted_pathway = model.predict([protein_sequence])
    return predicted_pathway

if __name__ == "__main__":
    synthesis_pathways = load_synthesis_pathway_data('data/synthesis_pathways.csv')
    X_train, y_train = synthesis_pathways['protein_sequence'], synthesis_pathways['synthesis_pathway']
    model = train_synthesis_pathway_model(X_train, y_train)
    model.save('models/synthesis_pathway_model.joblib')