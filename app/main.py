from fastapi import FastAPI, Depends
from app.routes.Cheque import router as cheque_router
from app.routes.Chequera import router as chequera_router
from app import services
    
app = FastAPI()

services.create_tables()

app.include_router(chequera_router, tags=["Chequeras"])
app.include_router(cheque_router, tags=["Cheques"])
