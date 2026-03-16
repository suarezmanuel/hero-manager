from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import mapped_column
from utils import Base


class Power(Base):
    __tablename__ = 'powers'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    herold = mapped_column(ForeignKey("hero_model.id"))

    def __repr__(self) -> str:
        return "<Power(id='%s', name='%s', herold='%s')>" % (
            self.id, self.name, self.herold
        )
