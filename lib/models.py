from sqlalchemy import ForeignKey, Column, Integer, String, MetaData
from sqlalchemy.orm import relationship, backref, declarative_base
#from sqlalchemy.ext.declarative import declarative_base

convention = {
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
}
metadata = MetaData(naming_convention=convention)

#Base = declarative_base(metadata=metadata)
Base = declarative_base(metadata=metadata, class_registry=dict())


class Game(Base):
    __tablename__ = 'games'

    id = Column(Integer(), primary_key=True)
    title = Column(String())
    genre = Column(String())
    platform = Column(String())
    price = Column(Integer())

    reviews = relationship('Review', backref=backref('game'))

    def __repr__(self):
        return f'Game(id={self.id}, title={self.title}, platform={self.platform})'

class Review(Base):
    __tablename__ = 'reviews'

    id = Column(Integer(), primary_key=True)
    score = Column(Integer())
    comment = Column(String())
    game_id = Column(Integer(), ForeignKey('games.id'))

    def __repr__(self):
        return f'Review(id={self.id}, score={self.score}, game_id={self.game_id})'

if __name__ == '__main__':
    engine = create_engine('sqlite:///one_to_many.db')
    Base.metadata.create_all(engine)  # This line creates the tables

    Session = sessionmaker(bind=engine)
    session = Session()