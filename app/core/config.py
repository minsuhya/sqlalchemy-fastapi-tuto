import os
from dotenv import load_dotenv

load_dotenv()


class Settings:

    DB_USERNAME: str = os.getenv("DB_USERNAME")
    DB_PASSWORD: str = os.getenv("DB_PASSWORD")
    DB_HOST: str = os.getenv("DB_HOST")
    DB_PORT: int = os.getenv("DB_PORT")
    DB_DATABASE: str = os.getenv("DB_DATABASE")

    SQLALCHEMY_DATABASE_URL = f"mysql+pymysql://{DB_USERNAME}:{DB_PASSWORD}" \
        f"@{DB_HOST}:{DB_PORT}/{DB_DATABASE}"


settings = Settings()
