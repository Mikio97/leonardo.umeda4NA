from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Permite que o frontend HTML faça requisições ao servidor

respostas = {
    "oi": "Olá! Como posso ajudar?",
    "qual seu nome": "Sou um chatbot que se comunica com um servidor Python!",
    "atendimento humano": "Ok! Um atendente humano assumirá a conversa."
}

@app.route("/chatbot", methods=["POST"])
def chatbot():
    dados = request.json
    pergunta = dados.get("pergunta", "").lower()
    resposta = respostas.get(pergunta, "Desculpe, não entendi.")
    return jsonify({"resposta": resposta})

if __name__ == "__main__":
    app.run(debug=True)
