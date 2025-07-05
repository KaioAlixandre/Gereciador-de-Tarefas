# 📋 TWTodos

Aplicação web para organizar e controlar tarefas diárias com login seguro e interface simples.

---

## 🧰 Tecnologias Utilizadas

### 🖥️ Backend
- [x] Django 5
- [x] Django ORM
- [x] SQLite 
- [x] Django Admin

### 🎨 Frontend
- [x] HTML5
- [x] TailwindCSS
- [x] Templates Django

### 🔐 Autenticação
- Login padrão com sessões (sem JWT)

### 📦 Containerização
- Docker
- Docker Compose

---

## ✅ Funcionalidades

- [x] Cadastro e login de usuários
- [x] CRUD de tarefas (criar, editar, excluir, concluir)
- [x] Interface moderna e responsiva com TailwindCSS
- [x] Deploy com Docker

---

### ✅ Pré-requisitos

- [Git](https://git-scm.com/)
- [Docker](https://www.docker.com/) + Docker Compose
- Python 3.11+ instalado 
- `pip` instalado 

---

### 💻 Execução com Docker

Clone o repositório:

```bash
git clone https://github.com/KaioAlixanndre/TWTodos.git
cd Gerenciador-de-Tarefas
```

Inicie a aplicação:

```bash
docker-compose up --build
```

---

### 🌐 Acessos

- Acesse o sistema:  
  **http://localhost:8000/**


---

## 🗂️ Estrutura do Projeto

```
TWTodos/
├── backend/                 # Código backend Django
│   ├── manage.py
│   ├── twtodos/             # Projeto Django
│   └── tarefas/             # App de gerenciamento de tarefas
│
├── templates/               # Templates HTML com Tailwind
├── static/                  # Arquivos estáticos (CSS/JS)
├── Dockerfile               # Dockerfile para backend
├── docker-compose.yml       # Orquestrador dos serviços
└── README.md                # Documentação do projeto
```

---
