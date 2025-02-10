from pydantic.v1 import BaseSettings


class Settings(BaseSettings):
    database_url = "postgresql+psycopg2://postgres:postgres@localhost:5432/fitness"


settings = Settings(
    _env_file='.env',
    _env_file_encoding='utf-8'
)
