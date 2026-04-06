# 📋 People Management Web

Aplicação web desenvolvida com Flask para gerenciamento de pessoas, com autenticação de usuários, CRUD completo, paginação, banco de dados e deploy em produção.

---

## 🚀 Demonstração

🔗 Acesse o sistema online:
👉 https://people-management-web.onrender.com

---

## 🧠 Funcionalidades

* 🔐 Sistema de autenticação (login/logout)
* 👤 CRUD completo de pessoas

  * Adicionar
  * Editar
  * Remover
* 🔍 Busca por nome
* 📄 Paginação de resultados
* ⚠️ Validação de dados (nome e idade)
* 🔒 Senhas armazenadas com hash seguro
* 🧾 Mensagens de feedback para o usuário
* 🖱️ Confirmação antes de remover registros
* ⏳ Botões com estado de carregamento (UX melhorada)

---

## 🏗️ Arquitetura do Projeto

O projeto segue uma organização modular inspirada em boas práticas:

```
app/
│
├── __init__.py        # Criação da aplicação (factory)
├── models.py          # Modelos do banco de dados
├── routes.py          # Rotas principais (CRUD)
├── auth.py            # Autenticação
├── services/          # Camada de lógica de negócio
│   └── pessoa_service.py
│
├── static/            # Arquivos estáticos (CSS, JS)
├── templates/         # Templates HTML (Jinja2)
│
instance/
└── pessoas.db         # Banco SQLite local

config.py              # Configurações da aplicação
run.py                 # Inicialização do servidor
requirements.txt       # Dependências
```

---

## 🧩 Tecnologias utilizadas

* Python
* Flask
* Flask-Login
* Flask-SQLAlchemy
* Jinja2
* Bootstrap 5
* SQLite (desenvolvimento)
* PostgreSQL (produção)
* Render (deploy)

---

## 🔐 Segurança

* Senhas armazenadas com hash (`werkzeug.security`)
* `SECRET_KEY` configurada via variável de ambiente
* Proteção de rotas com `login_required`
* Sessões seguras

---

## ⚙️ Como rodar localmente

### 1. Clonar o projeto

```bash
git clone https://github.com/seu-usuario/people-management-web.git
cd people-management-web
```

---

### 2. Criar ambiente virtual

```bash
python -m venv venv
venv\Scripts\activate  # Windows
```

---

### 3. Instalar dependências

```bash
pip install -r requirements.txt
```

---

### 4. Definir variáveis de ambiente (opcional)

```bash
set FLASK_ENV=development
```

---

### 5. Rodar aplicação

```bash
python run.py
```

---

### 6. Acessar no navegador

```text
http://127.0.0.1:5000
```

---

## 🔑 Credenciais padrão (somente desenvolvimento)

```text
Usuário: admin
Senha: 1234
```

---

## 🌐 Deploy

A aplicação está hospedada na Render com:

* Banco PostgreSQL
* Variáveis de ambiente configuradas
* Build automático via GitHub

---

## 📈 Evolução do Projeto

Este projeto evoluiu progressivamente, incluindo:

* Estrutura inicial com Flask
* Implementação de autenticação
* Validações completas
* Paginação
* Refatoração para camada de serviço
* Melhorias de UX (feedback visual e loading)
* Deploy em produção

---

## 👨‍💻 Autor

Desenvolvido por **Eduardo da Silva Balbino**

---

## 📄 Licença

Este projeto é de uso educacional e para portfólio.
