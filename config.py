import os

class Config:
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL', 'mysql://user:pass@localhost/votingapp')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
