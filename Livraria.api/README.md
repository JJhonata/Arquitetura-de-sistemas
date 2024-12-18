# API de Gestão de Livros 📚

Esta API, desenvolvida com o framework **FastAPI**, permite gerenciar uma lista de livros. A API oferece funcionalidades básicas de CRUD (Criar, Ler, Atualizar, Excluir) para livros, com armazenamento em memória.

## Funcionalidades ✨

- **Listar todos os livros**: Exibe todos os livros cadastrados.
- **Recuperar livro por ID**: Obtém os detalhes de um livro específico.
- **Adicionar um novo livro**: Permite cadastrar um novo livro com título, autor e ISBN.
- **Atualizar um livro existente**: Modifica as informações de um livro através do seu ID.
- **Excluir um livro**: Remove um livro da lista através de seu ID.

## Endpoints 🌐

### 1. Listar Todos os Livros 📋
**Método**: `GET /books`

Recupera todos os livros cadastrados na base de dados.

**Exemplo de resposta:**

```json
{
  "status": "success",
  "message": "Livros recuperados com sucesso.",
  "data": [...]
}
```

### 2. Recuperar Livro pelo ID 🔍
**Método**: `GET /books/{book_id}`

Recupera os detalhes de um livro específico pelo seu ID.

**Exemplo de resposta (caso encontrado):**

```json
{
  "status": "success",
  "message": "Livro recuperado com sucesso.",
  "data": {...}
}
```

**Exemplo de resposta (caso não encontrado):**

```json
{
  "status": "error",
  "message": "Livro não encontrado."
}
```

### 3. Adicionar um Novo Livro ➕
**Método**: `POST /books`

Adiciona um novo livro à lista de livros.

**Corpo da requisição (JSON):**

```json
{
  "title": "Título do Livro",
  "author": "Autor do Livro",
  "isbn": "ISBN do Livro"
}
```

**Exemplo de resposta:**

```json
{
  "status": "success",
  "message": "Livro adicionado com sucesso.",
  "data": {...}
}
```

### 4. Atualizar um Livro ✏️
**Método**: `PUT /books/{book_id}`

Atualiza as informações de um livro existente pelo seu ID.

**Corpo da requisição (JSON):**

```json
{
  "title": "Novo Título",
  "author": "Novo Autor",
  "isbn": "Novo ISBN"
}
```

**Exemplo de resposta:**

```json
{
  "status": "success",
  "message": "Livro atualizado com sucesso.",
  "data": {...}
}
```

**Exemplo de resposta (caso não encontrado):**

```json
{
  "status": "error",
  "message": "Livro não encontrado."
}
```

### 5. Deletar um Livro ❌
**Método**: `DELETE /books/{book_id}`

Deleta um livro da lista usando o seu ID.

**Exemplo de resposta:**

```json
{
  "status": "success",
  "message": "Livro removido com sucesso.",
  "data": {...}
}
```

**Exemplo de resposta (caso não encontrado):**

```json
{
  "status": "error",
  "message": "Livro não encontrado."
}
```

## Como Rodar 🚀

### Pré-requisitos

- **Python 3.9+**: Certifique-se de ter o Python instalado na sua máquina.
- **FastAPI** e **Uvicorn**: Instale as dependências necessárias para rodar a API.

### Passos para Execução

1. **Clone o repositório**:

   ```bash
   git clone https://github.com/seu-repositorio-url.git
   cd seu-repositorio
   ```

2. **Instale as dependências**:

   ```bash
   pip install -r requirements.txt
   ```

3. **Inicie o servidor**:

   Execute o seguinte comando para rodar o servidor de desenvolvimento:

   ```bash
   uvicorn main:app --reload
   ```

4. **Acesse a documentação da API**:

   - Documentação interativa (Swagger UI): [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
   - Documentação Redoc: [http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc)

## Licença 📜

Este projeto está licenciado sob a Licença MIT. Consulte o arquivo LICENSE para mais detalhes.