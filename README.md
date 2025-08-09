# 📦 FestAPI

**FestAPI** é uma API REST desenvolvida com **FastAPI** e integrada a um banco de dados relacional **SQLite**. Ela permite realizar operações CRUD (Create, Read, Update, Delete) em uma tabela de produtos.

> Projeto desenvolvido como atividade avaliativa para as disciplinas de **Ciência de Dados** e **Banco de Dados**.

---

## 🚀 Funcionalidades

- ✅ `GET /status` – Verifica se a API está online  
- ➕ `POST /produto` – Cadastra um novo produto  
- 🔍 `GET /produto/{id}` – Busca um produto específico  
- ✏️ `PUT /produto/{id}` – Atualiza os dados de um produto  
- ❌ `DELETE /produto/{id}` – Remove um produto do banco

---

## 🧾 Estrutura da Tabela `produtos`

| Campo       | Tipo    | Descrição                  |
|-------------|---------|----------------------------|
| `id`        | int     | Identificador único        |
| `nome`      | string  | Nome do produto            |
| `preco`     | float   | Preço do produto           |
| `quantidade`| int     | Quantidade em estoque      |

---

