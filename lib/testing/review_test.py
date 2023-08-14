from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Game, Review
from conftest import SQLITE_URL

class TestReview:
    '''Class Review in models.py'''

    @classmethod
    def setup_class(cls):
        '''Setup database session and test data'''

        # Start session, reset db
        cls.engine = create_engine(SQLITE_URL)
        Session = sessionmaker(bind=cls.engine)
        cls.session = Session()

        # Add test data
        cls.skyrim = Game(
            title="The Elder Scrolls V: Skyrim",
            platform="PC",
            genre="Adventure",
            price=20
        )

        cls.session.add(cls.skyrim)
        cls.session.commit()

        cls.skyrim_review = Review(
            score=10,
            comment="Wow, what a game",
            game_id=cls.skyrim.id
        )

        cls.session.add(cls.skyrim_review)
        cls.session.commit()

    def test_game_has_correct_attributes(self):
        '''Has attributes "id", "score", "comment", "game_id".'''
        assert (
            all(
                hasattr(
                    TestReview.skyrim_review, attr
                ) for attr in [
                    "id",
                    "score",
                    "comment",
                    "game_id",
                ]
            )
        )

    def test_knows_about_associated_game(self):
        '''Has attribute "game" that is the "Game" object associated with its game_id.'''
        assert (
            TestReview.skyrim_review.game == TestReview.skyrim
        )
