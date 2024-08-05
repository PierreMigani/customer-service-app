import os

class Config:
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL', 'postgresql://postgres:password@db-service:5432/email_categorizer')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
