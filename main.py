from flask import Flask, request, jsonify
from models.protein_design import design_protein
from models.synthesis_pathway_optimization import optimize_synthesis_pathway
from models.reaction_condition_optimization import optimize_reaction_conditions
from models.evaluation import evaluate_protein_synthesis

app = Flask(__name__)

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()
    protein_sequence = data['protein_sequence']
    predicted_structure = design_protein(protein_sequence)
    predicted_pathway = optimize_synthesis_pathway(protein_sequence)
    predicted_conditions = optimize_reaction_conditions(predicted_pathway)
    evaluation = evaluate_protein_synthesis(protein_sequence, predicted_structure, predicted_pathway, predicted_conditions)
    return jsonify({
        'protein_sequence': protein_sequence,
        'predicted_structure': predicted_structure,
        'predicted_pathway': predicted_pathway,
        'predicted_conditions': predicted_conditions,
        'evaluation': evaluation.to_dict(orient='records')
    })

if __name__ == "__main__":
    app.run(debug=True)