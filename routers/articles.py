from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List, Optional
import models, schemas
from database import get_db

router = APIRouter(prefix="/api/articles", tags=["Articles"])

# Créer un article [cite: 46, 48]
@router.post("/", response_model=schemas.ArticleResponse, status_code=status.HTTP_201_CREATED)
def create_article(article: schemas.ArticleCreate, db: Session = Depends(get_db)):
    db_article = models.Article(**article.dict())
    db.add(db_article)
    db.commit()
    db.refresh(db_article)
    return db_article

# Rechercher un article (doit être placé AVANT l'endpoint avec {id}) [cite: 89, 91]
@router.get("/search", response_model=List[schemas.ArticleResponse])
def search_articles(query: str, db: Session = Depends(get_db)):
    articles = db.query(models.Article).filter(
        models.Article.titre.contains(query) | models.Article.contenu.contains(query)
    ).all()
    return articles

# Lire/afficher les articles avec filtres [cite: 51, 54, 55]
@router.get("/", response_model=List[schemas.ArticleResponse])
def get_articles(categorie: Optional[str] = None, auteur: Optional[str] = None, date: Optional[str] = None, db: Session = Depends(get_db)):
    query = db.query(models.Article)
    if categorie: query = query.filter(models.Article.categorie == categorie)
    if auteur: query = query.filter(models.Article.auteur == auteur)
    if date: query = query.filter(models.Article.date == date)
    return query.all()

# Lire un article unique [cite: 57, 59]
@router.get("/{id}", response_model=schemas.ArticleResponse)
def get_article(id: int, db: Session = Depends(get_db)):
    article = db.query(models.Article).filter(models.Article.id == id).first()
    if not article:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Article non trouvé")
    return article

# Modifier un article [cite: 61, 62]
@router.put("/{id}", response_model=schemas.ArticleResponse)
def update_article(id: int, article_update: schemas.ArticleUpdate, db: Session = Depends(get_db)):
    db_article = db.query(models.Article).filter(models.Article.id == id).first()
    if not db_article:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Article non trouvé")
    
    update_data = article_update.dict(exclude_unset=True)
    for key, value in update_data.items():
        setattr(db_article, key, value)
        
    db.commit()
    db.refresh(db_article)
    return db_article

# Supprimer un article [cite: 86, 87]
@router.delete("/{id}", status_code=status.HTTP_200_OK)
def delete_article(id: int, db: Session = Depends(get_db)):
    db_article = db.query(models.Article).filter(models.Article.id == id).first()
    if not db_article:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Article non trouvé")
    db.delete(db_article)
    db.commit()
    return {"message": "Article supprimé avec succès"}
