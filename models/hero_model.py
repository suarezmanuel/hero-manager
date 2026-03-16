from sqlalchemy import Integer, String, Boolean, DateTime
from sqlalchemy.orm import mapped_column, Mapped
from utils import Base


class Hero(Base):
    __tablename__ = 'heroes'
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[String] = mapped_column(String)
    suit_color: Mapped[String] = mapped_column(String)
    has_cape: Mapped[Boolean] = mapped_column(Boolean)
    last_mission: Mapped[DateTime] = mapped_column(DateTime, nullable=True)
    is_retired: Mapped[Boolean] = mapped_column(Boolean, nullable=False)

    def __repr__(self) -> str:
        return "<Hero(id='%s', name='%s', \
        suit_color='%s', has_cape='%s', \
        last_mission='%s', is_retired='%s')>" % (
            self.id, self.name, self.suit_color, self.has_cape,
            self.last_mission, self.is_retired
        )
