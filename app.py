from flask import Flask, render_template, request
from openai import OpenAI
from dotenv import load_dotenv
import os, re, requests
from selecionar_persona import *

load_dotenv()

cliente = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
modelo = "gpt-4"

app = Flask(__name__)
contexto = open("dados/ecomart.txt", "r", encoding="utf-8").read()

def extrair_cep(texto: str):
    m = re.search(r"\b(\d{5}-?\d{3})\b", texto)
    return m.group(1).replace("-", "") if m else None

def buscar_endereco(cep: str):
    url = f"https://viacep.com.br/ws/{cep}/json/"
    r = requests.get(url, timeout=10)
    r.raise_for_status()
    dados = r.json()
    if dados.get("erro"):
        return None
    return dados

def bot(prompt, endereco=None):
    personalidade = personas[selecionar_persona(prompt)]
    prompt_sistema = f"""
Você é um chatbot de atendimento a clientes de um e-commerce.
Use apenas o contexto abaixo para responder.
Você deve adotar a personalidade abaixo.

# Contexto
{contexto}

# Persona
{personalidade}
"""
    if endereco:
        prompt_sistema += f"\n# Endereço do cliente (ViaCEP)\n{endereco}\n"

    resp = cliente.chat.completions.create(
        model=modelo,
        messages=[
            {"role": "system", "content": prompt_sistema},
            {"role": "user", "content": prompt},
        ],
        max_tokens=300,
        temperature=1
    )
    return resp.choices[0].message.content

@app.route("/chat", methods=["POST"])
def chat():
    prompt = request.json["msg"]

    cep = extrair_cep(prompt)
    endereco = buscar_endereco(cep) if cep else None

    return bot(prompt, endereco)

@app.route("/")
def home():
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)

