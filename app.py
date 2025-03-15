from flask import Flask, request, jsonify
from transformers import pipeline

app = Flask(name)

# Load the model (GPT-2 as a basic model)
model = pipeline("text-generation", model="gpt2")

@app.route('/generate', methods=['POST'])
def generate():
    data = request.json
    prompt = data.get("prompt", "")
    
    # Generate text
    result = model(prompt, max_length=100, num_return_sequences=1)
    return jsonify({"generated_text": result[0]['generated_text']})

if name == "main":
    app.run(host='0.0.0.0', port=5000)