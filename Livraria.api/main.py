from typing import List
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

# Modelo para os livros
class Book(BaseModel):
    title: str
    author: str
    isbn: str

# Armazenamento em memória
books: List[dict] = []

@app.get("/books")
async def list_books():
    """Retorna a lista de todos os livros cadastrados"""
    return {
        "status": "success",
        "message": "Livros recuperados com sucesso.",
        "data": books
    }

@app.get("/books/{book_id}")
async def get_book_by_id(book_id: int):
    """Retorna um livro específico pelo seu ID"""
    for book in books:
        if book["id"] == book_id:
            return {
                "status": "success",
                "message": "Livro recuperado com sucesso.",
                "data": book
            }
    raise HTTPException(status_code=404, detail="Livro não encontrado.")

@app.get("/books_search")
async def search_books_by_title(title: str):
    """Busca livros pelo título"""
    matching_books = [book for book in books if title.lower() in book["title"].lower()]
    if matching_books:
        return {
            "status": "success",
            "message": "Livros recuperados com sucesso.",
            "data": matching_books
        }
    raise HTTPException(status_code=404, detail="Nenhum livro encontrado com o título fornecido.")

@app.post("/books")
async def create_book(book: Book):
    """Adiciona um novo livro à lista de livros cadastrados"""
    new_book = {
        "id": len(books) + 1,  # Gera um ID simples
        **book.dict()
    }
    books.append(new_book)
    return {
        "status": "success",
        "message": "Livro adicionado com sucesso.",
        "data": new_book
    }

@app.put("/books/{book_id}")
async def update_book(book_id: int, book: Book):
    """Atualiza os detalhes de um livro existente pelo ID"""
    for existing_book in books:
        if existing_book["id"] == book_id:
            existing_book.update(book.dict())
            return {
                "status": "success",
                "message": "Livro atualizado com sucesso.",
                "data": existing_book
            }
    raise HTTPException(status_code=404, detail="Livro não encontrado.")

@app.delete("/books/{book_id}")
async def delete_book(book_id: int):
    """Remove um livro da lista pelo ID"""
    for index, book in enumerate(books):
        if book["id"] == book_id:
            deleted_book = books.pop(index)
            return {
                "status": "success",
                "message": "Livro removido com sucesso.",
                "data": deleted_book
            }
    raise HTTPException(status_code=404, detail="Livro não encontrado.")