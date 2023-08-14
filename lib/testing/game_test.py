from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import pytest
from conftest import SQLITE_URL  # Make sure you import the necessary variable
from models import Game, Review

class TestGame:
    @classmethod
    def setup_class(cls):
        '''Class Game in models.py'''

        # start session, reset db
        cls.engine = create_engine(SQLITE_URL)
        Session = sessionmaker(bind=cls.engine)
        cls.session = Session()

        # add test data
        cls.mario_kart = Game(
            title="Mario Kart",
            platform="Switch",
            genre="Racing",
            price=60
        )

        cls.session.add(cls.mario_kart)
        cls.session.commit()

        mk_review_1 = Review(
            score=10,
            comment="Wow, what a game",
            game_id=cls.mario_kart.id
        )

        mk_review_2 = Review(
            score=8,
            comment="A classic",
            game_id=cls.mario_kart.id
        )

        cls.session.bulk_save_objects([mk_review_1, mk_review_2])
        cls.session.commit()

    def test_game_has_correct_attributes(self):
        '''has attributes "id", "title", "platform", "genre", "price".'''
        assert (
            all(
                hasattr(
                    TestGame.mario_kart, attr
                ) for attr in [
                    "id",
                    "title",
                    "platform",
                    "genre",
                    "price"
                ]
            )
        )

    def test_has_associated_reviews(self):
        '''has two reviews with scores 10 and 8.'''
        assert (
            len(TestGame.mario_kart.reviews) == 2 and
            TestGame.mario_kart.reviews[0].score == 10 and
            TestGame.mario_kart.reviews[1].score == 8
        )
