🛒 EcoMart – Chatbot com IA (Flask + OpenAI)

Este projeto é um chatbot inteligente para e-commerce, desenvolvido em Python + Flask, integrado à API da OpenAI.
Ele responde perguntas dos clientes somente com base nos dados do e-commerce, usando um arquivo de contexto (ecomart.txt).

🚀 Funcionalidades
Chat web em tempo real
Integração com OpenAI (GPT)
Respostas baseadas em contexto do e-commerce
Frontend em HTML, CSS e JavaScript
Backend em Flask (API REST)
Arquitetura pronta para SaaS ou API

🧱 Estrutura do projeto
CHATBOT/
 ├── app.py
 ├── helpers.py
 ├── .env
 ├── dados/
 │    └── ecomart.txt
 ├── templates/
 │    └── index.html
 ├── static/
 │    ├── css/
 │    ├── js/
 │    └── img/
 └── venv/

⚙️ Requisitos
Python 3.9+
Conta na OpenAI
Chave de API
📦 Instalação
1️⃣ Criar ambiente virtual

Na pasta do projeto:
python -m venv venv

Ativar:
Windows
venv\Scripts\activate

Linux / Mac
source venv/bin/activate
2️⃣ Instalar dependências
pip install flask openai python-dotenv requests
3️⃣ Criar o arquivo .env
Na raiz do projeto, crie um arquivo .env:
OPENAI_API_KEY=sk-xxxxxxxxxxxxxxxxxxxx
Nunca publicar esse arquivo no GitHub.

🧠 Contexto do chatbot
Crie o arquivo:
dados/ecomart.txt

Exemplo:
A EcoMart é um e-commerce de produtos sustentáveis.
Vendemos garrafas térmicas, sacolas reutilizáveis e cosméticos naturais.
Tudo que o chatbot responderá virá apenas desse arquivo.

▶️ Executar o servidor
Na pasta CHATBOT:
python app.py

Acesse no navegador:
http://localhost:5000

🧪 Testar via Postman
POST
http://127.0.0.1:5000/chat

Headers
Content-Type: application/json

Body
{
  "msg": "Quais produtos vocês vendem?"
}

🔐 Segurança
A chave da OpenAI fica no .env
O chatbot só responde com base no ecomart.txt
Nenhuma pergunta fora do contexto será respondida

🌍 Possíveis expansões
Histórico de conversa
Login de usuários
Multi-loja
Base de dados
Deploy em AWS, Railway, Render, etc.

🧑‍💻 Desenvolvido com
Python
Flask
OpenAI
HTML, CSS, JavaScript