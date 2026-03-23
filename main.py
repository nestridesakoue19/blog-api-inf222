from fastapi import FastAPI
import models
from database import engine
from routers import articles

# Crée les tables dans la base de données
models.Base.metadata.create_all(bind=engine)

app = FastAPI(title="Blog API", description="API Backend pour gérer un blog simple")

# Inclure les routes
app.include_router(articles.router)
