from app import database
from sqlalchemy import exc
import app.database as db

def create_tables():
    try:
        db.engine.connect().execute("SELECT 1 FROM your_table_name LIMIT 1")
    except exc.SQLAlchemyError:
        db.Base.metadata.create_all(bind=db.engine)

def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()