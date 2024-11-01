from pydantic_settings import BaseSettings

import logging


class Settings(BaseSettings):
    database_url: str

    class Config:
        env_file = ".env"


settings = Settings()

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
    handlers=[
        logging.FileHandler("./app/logs/app.log"),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger()

