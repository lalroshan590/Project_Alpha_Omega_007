import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from utils.data_loader import load_reaction_condition_data

def train_reaction_condition_model(X_train, y_train):
    model = RandomForestRegressor(n_estimators=100, random_state=42)
    model.fit(X_train, y_train)
    return model

def optimize_reaction_conditions(model, synthesis_pathway):
    predicted_conditions = model.predict([synthesis_pathway])
    return predicted_conditions

if __name__ == "__main__":
    reaction_conditions = load_reaction_condition_data('data/reaction_conditions.csv')
    X_train, y_train = reaction_conditions['synthesis_pathway'], reaction_conditions['reaction_conditions']
    model = train_reaction_condition_model(X_train, y_train)
    model.save('models/reaction_condition_model.joblib')