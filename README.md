# 📋 People Management Web

Aplicação web desenvolvida com Flask para gerenciamento de pessoas, permitindo adicionar, buscar, editar e remover registros com persistência em banco de dados SQLite.

---

## 🚀 Funcionalidades

- Adicionar pessoas
- Buscar pessoas por nome
- Editar dados de uma pessoa
- Remover pessoas com confirmação
- Persistência de dados com SQLite
- Feedback visual com mensagens (Flash)

---

## 🛠️ Tecnologias utilizadas

- Python
- Flask
- Flask-SQLAlchemy
- HTML5
- CSS3
- JavaScript
- SQLite
- Git & GitHub

---

## 📁 Estrutura do projeto

```
people-management-web/
│
├── app.py
├── pessoas.json (legado - pode ser removido)
├── README.md
│
├── instance/
│   └── pessoas.db
│
├── static/
│   ├── style.css
│   └── script.js
│
├── templates/
│   └── index.html
```

---

## ⚙️ Como executar o projeto

### 1. Clonar o repositório

```
git clone https://github.com/Eduardo-S-Balbino/people-management-web.git
cd people-management-web
```

### 2. Criar ambiente virtual (opcional, mas recomendado)

```
python -m venv venv
venv\Scripts\activate
```

### 3. Instalar dependências

```
pip install -r requirements.txt
```

### 4. Executar o projeto

```
python app.py
```

### 5. Acessar no navegador

```
http://127.0.0.1:5000
```

---

## 🧠 Conceitos aplicados

- CRUD completo com Flask
- Integração com banco de dados SQLite
- ORM com SQLAlchemy
- Templates com Jinja2
- Separação entre backend e frontend
- Manipulação de formulários
- Feedback de ações com mensagens flash
- Estrutura organizada de projeto

---

## 📈 Evolução do projeto

Este projeto representa uma evolução prática de:

- armazenamento em JSON ➜ banco de dados SQLite  
- operações simples ➜ CRUD completo  
- interface básica ➜ interface estilizada e interativa  

---

## 📌 Melhorias futuras

- Autenticação de usuários
- API REST
- Responsividade (mobile)
- Testes automatizados
- Deploy em nuvem (Render, Railway ou Vercel)

---

## 👨‍💻 Autor

Eduardo da Silva Balbino

Projeto desenvolvido como parte do portfólio para evolução em desenvolvimento web.

---

## ⭐ Observação

Este projeto foi desenvolvido com foco em aprendizado prático e evolução contínua, demonstrando boas práticas iniciais de desenvolvimento web com Flask.