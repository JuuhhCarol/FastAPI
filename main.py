from fastapi import FastAPI, HTTPException, Depends
from sqlalchemy.orm import Session
from database import SessionLocal, engine, Base
from models import Produto
from pydantic import BaseModel

app = FastAPI()

Base.metadata.create_all(bind=engine)

class ProdutoSchema(BaseModel):
    nome: str
    preco: float
    quantidade: int

class ProdutoResponse(ProdutoSchema):
    id: int
    class Config:
        orm_mode = True

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/status")
def status():
    return {"mensagem": "API funcionando"}

@app.post("/produto", response_model=ProdutoResponse)
def criar_produto(produto: ProdutoSchema, db: Session = Depends(get_db)):
    novo_produto = Produto(**produto.dict())
    db.add(novo_produto)
    db.commit()
    db.refresh(novo_produto)
    return novo_produto

@app.get("/produto/{id}", response_model=ProdutoResponse)
def obter_produto(id: int, db: Session = Depends(get_db)):
    produto = db.query(Produto).filter(Produto.id == id).first()
    if not produto:
        raise HTTPException(status_code=404, detail="Produto não encontrado")
    return produto

@app.put("/produto/{id}", response_model=ProdutoResponse)
def atualizar_produto(id: int, dados: ProdutoSchema, db: Session = Depends(get_db)):
    produto = db.query(Produto).filter(Produto.id == id).first()
    if not produto:
        raise HTTPException(status_code=404, detail="Produto não encontrado")
    for key, value in dados.dict().items():
        setattr(produto, key, value)
    db.commit()
    db.refresh(produto)
    return produto

@app.delete("/produto/{id}")
def remover_produto(id: int, db: Session = Depends(get_db)):
    produto = db.query(Produto).filter(Produto.id == id).first()
    if not produto:
        raise HTTPException(status_code=404, detail="Produto não encontrado")
    db.delete(produto)
    db.commit()
    return {"mensagem": "Produto removido com sucesso"}
