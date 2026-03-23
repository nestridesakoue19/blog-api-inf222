from sqlalchemy import Column, Integer, String, Text
from database import Base
import datetime

class Article(Base):
    __tablename__ = "articles"

    id = Column(Integer, primary_key=True, index=True)
    titre = Column(String, index=True, nullable=False)
    contenu = Column(Text, nullable=False)
    auteur = Column(String, nullable=False)
    date = Column(String, default=lambda: datetime.date.today().isoformat())
    categorie = Column(String, index=True)
    tags = Column(String) # Stocké sous forme de chaîne (ex: "tech, web")
