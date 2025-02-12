import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, LSTM, Embedding
from sklearn.preprocessing import LabelEncoder
from utils.data_loader import load_protein_data

def build_protein_design_model(input_shape):
    model = Sequential([
        Embedding(input_dim=21, output_dim=128, input_length=input_shape),
        LSTM(128, return_sequences=True),
        LSTM(128),
        Dense(128, activation='relu'),
        Dense(1, activation='linear')
    ])
    model.compile(optimizer='adam', loss='mse')
    return model

def train_protein_design_model(model, X_train, y_train, epochs=10, batch_size=32):
    model.fit(X_train, y_train, epochs=epochs, batch_size=batch_size)
    return model

def design_protein(model, protein_sequence):
    encoder = LabelEncoder()
    encoder.fit(['A', 'T', 'C', 'G'])
    encoded_sequence = encoder.transform(list(protein_sequence))
    encoded_sequence = tf.keras.preprocessing.sequence.pad_sequences([encoded_sequence], maxlen=50)
    predicted_structure = model.predict(encoded_sequence)
    return predicted_structure

if __name__ == "__main__":
    proteins = load_protein_data('data/proteins.csv')
    X_train, y_train = proteins['protein_sequence'], proteins['protein_structure']
    model = build_protein_design_model(50)
    model = train_protein_design_model(model, X_train, y_train)
    model.save('models/protein_design_model.h5')