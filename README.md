# 📋 People Management Web

Aplicação web completa para gerenciamento de pessoas, desenvolvida com **Flask**, com autenticação, banco de dados relacional e deploy em produção.

---

## 🚀 Acesse o projeto online

👉 https://people-management-web.onrender.com

---

## 🧠 Sobre o projeto

O **People Management Web** é uma aplicação CRUD (Create, Read, Update, Delete) que permite gerenciar pessoas com nome e idade, com sistema de autenticação e interface moderna.

O projeto foi evoluído passo a passo até atingir um nível profissional, incluindo:

* autenticação com sessão
* proteção de rotas
* banco PostgreSQL em produção
* paginação de dados
* validações completas
* interface responsiva com Bootstrap

---

## ⚙️ Funcionalidades

### 🔐 Autenticação

* Login de usuário
* Logout
* Proteção de rotas com Flask-Login
* Redirecionamento automático para login

### 👤 Gestão de Pessoas

* Adicionar pessoa
* Editar pessoa
* Remover pessoa
* Listagem completa

### 🔎 Busca

* Busca por nome com filtro dinâmico

### 📄 Paginação

* Exibição de 5 registros por página
* Navegação entre páginas
* Botões "Anterior" e "Próxima"

### ✅ Validações

* Nome não pode ser vazio
* Idade deve ser número válido (1 a 120)
* Evita duplicidade de nomes

### 🔒 Segurança

* Senhas protegidas com hash (`werkzeug.security`)
* Sessão autenticada
* Dados sensíveis protegidos

---

## 🛠️ Tecnologias utilizadas

* Python
* Flask
* Flask-SQLAlchemy
* Flask-Login
* SQLite (ambiente local)
* PostgreSQL (produção)
* Jinja2
* HTML5
* CSS3
* Bootstrap 5
* JavaScript
* Gunicorn (produção)
* Render (deploy)

---

## 🗄️ Banco de dados

O projeto utiliza dois bancos:

* **SQLite** → ambiente local
* **PostgreSQL** → produção (Render)

A troca é feita automaticamente via variável de ambiente:

```python
DATABASE_URL
```

---

## 📦 Estrutura do projeto

```
people-management-web/
│
├── app.py
├── requirements.txt
├── README.md
│
├── templates/
│   ├── index.html
│   └── login.html
│
├── static/
│   └── script.js
```

---

## ▶️ Como rodar o projeto localmente

### 1. Clonar o repositório

```bash
git clone https://github.com/Eduardo-S-Balbino/people-management-web.git
cd people-management-web
```

---

### 2. Criar ambiente virtual

```bash
python -m venv venv
```

Ativar:

```bash
venv\Scripts\activate
```

---

### 3. Instalar dependências

```bash
pip install -r requirements.txt
```

---

### 4. Rodar o projeto

```bash
python app.py
```

---

### 5. Acessar no navegador

```text
http://127.0.0.1:5000
```

---

## 🔑 Usuário padrão

Para testes locais:

```
Usuário: admin
Senha: 1234
```

⚠️ Em produção, as credenciais não são exibidas por segurança.

---

## 🌐 Deploy

O projeto está hospedado na **Render** com:

* Web Service (Flask + Gunicorn)
* Banco PostgreSQL
* Variáveis de ambiente configuradas

---

## 📈 Melhorias implementadas

* Interface moderna com Bootstrap
* Sistema de autenticação completo
* Migração para PostgreSQL
* Paginação de dados
* Validações robustas
* Segurança com hash de senha

---

## 🚀 Próximas melhorias

* Cadastro de novos usuários
* Recuperação de senha
* Upload de imagens
* API REST
* Modularização do projeto
* Testes automatizados

---

## 👨‍💻 Autor

Desenvolvido por:

**Eduardo da Silva Balbino**

---

## 📄 Licença

Este projeto é de uso educacional e para portfólio.
