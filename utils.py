from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

ENGINE = create_engine("sqlite:///:memory:", echo=True)
Session = sessionmaker(bind=ENGINE)
Base = declarative_base()
