import os

class Config:
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://username:password@localhost/dbname'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
