import sqlalchemy as sa
import sqlalchemy.orm as orm

from app import config

engine = sa.create_engine(config.settings.db_url)

SessionLocal = orm.sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = orm.declarative_base()