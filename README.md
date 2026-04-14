# 📋 People Management Web

Aplicação web desenvolvida com Flask para gerenciamento de pessoas, com autenticação de usuários, CRUD completo, paginação, busca, validações e deploy em produção.

---

## 🚀 Demonstração

Acesse o sistema online:  
👉 https://people-management-web.onrender.com

---

## 🖼️ Screenshots

### Login
![Login](assets/images/login.png)

### Dashboard
![Dashboard](assets/images/dashboard.png)

### Edit Person
![Edit Person](assets/images/edit-person.png)

---

## 🧠 Funcionalidades

- 🔐 Sistema de autenticação de usuários (login/logout)
- 👤 CRUD completo de pessoas
  - Adicionar
  - Editar
  - Remover
- 🔍 Busca por nome
- 📄 Paginação de resultados
- ⚠️ Validação de dados (nome e idade)
- 🔒 Senhas armazenadas com hash seguro
- 🧾 Mensagens de feedback para o usuário
- 🖱️ Confirmação antes de remover registros
- ⏳ Botões com estado de carregamento para melhor experiência do usuário

---

## 🏗️ Arquitetura do Projeto

O projeto segue uma organização modular inspirada em boas práticas de desenvolvimento:

    app/
    │
    ├── __init__.py        # Criação da aplicação (Application Factory)
    ├── models.py          # Modelos do banco de dados
    ├── routes.py          # Rotas principais do CRUD
    ├── auth.py            # Rotas de autenticação
    ├── services/          # Camada de lógica de negócio
    │   └── pessoa_service.py
    │
    ├── static/            # Arquivos estáticos (CSS, JS)
    ├── templates/         # Templates HTML (Jinja2)

    config.py              # Configurações da aplicação
    run.py                 # Inicialização do servidor
    requirements.txt       # Dependências do projeto

---

## 🧩 Tecnologias Utilizadas

- Python
- Flask
- Flask-Login
- Flask-SQLAlchemy
- Jinja2
- Bootstrap 5
- SQLite (desenvolvimento)
- PostgreSQL (produção)
- Render (deploy)

---

## 🔐 Segurança

- Senhas armazenadas com hash usando `werkzeug.security`
- `SECRET_KEY` configurada por variável de ambiente
- Proteção de rotas com `login_required`
- Gerenciamento seguro de sessão

---

## ⚙️ Como Rodar Localmente

### 1. Clone o repositório

    git clone https://github.com/Eduardo-S-Balbino/people-management-web.git
    cd people-management-web

### 2. Crie o ambiente virtual

    python -m venv venv
    venv\Scripts\activate

### 3. Instale as dependências

    pip install -r requirements.txt

### 4. Defina as variáveis de ambiente (opcional)

    set FLASK_ENV=development

### 5. Execute a aplicação

    python run.py

### 6. Acesse no navegador

    http://127.0.0.1:5000

---

## 🔑 Credenciais Padrão (Somente Desenvolvimento)

    Usuário: admin
    Senha: 1234

---

## 🌐 Deploy

A aplicação está hospedada na Render com:

- Banco PostgreSQL
- Variáveis de ambiente configuradas
- Deploy automático via GitHub

---

## 📈 Evolução do Projeto

Este projeto foi evoluindo progressivamente com a implementação de melhorias como:

- Estrutura inicial com Flask
- Sistema de autenticação
- Validações completas
- Paginação
- Refatoração para camada de serviço
- Melhorias de UX com feedback visual e loading
- Deploy em produção

---

## 👨‍💻 Autor

Desenvolvido por **Eduardo da Silva Balbino**

- GitHub: https://github.com/Eduardo-S-Balbino
- LinkedIn: https://www.linkedin.com/in/eduardo-da-silva-balbino-1611b3401/
- Portfólio: https://portfolio-ekgq.onrender.com/

---

## 📄 Licença

Este projeto foi criado para fins educacionais e de portfólio.