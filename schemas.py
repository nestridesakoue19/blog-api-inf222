from pydantic import BaseModel, Field
from typing import Optional

class ArticleBase(BaseModel):
    titre: str = Field(..., min_length=1, description="Le titre ne peut pas être vide")
    contenu: str
    auteur: str = Field(..., min_length=1, description="L'auteur est obligatoire")
    categorie: str
    tags: str

class ArticleCreate(ArticleBase):
    pass

class ArticleUpdate(BaseModel):
    titre: Optional[str] = None
    contenu: Optional[str] = None
    categorie: Optional[str] = None
    tags: Optional[str] = None

class ArticleResponse(ArticleBase):
    id: int
    date: str

    class Config:
        orm_mode = True
