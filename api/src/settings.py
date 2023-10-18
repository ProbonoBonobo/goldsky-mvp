import os
from pydantic_settings import BaseSettings



class FastAPISettings(BaseSettings):
    pass

class AppSettings(BaseSettings):
    name: str = "Parasol API"
    conn_string: str = os.getenv("DB_CONN_STRING", "postgresql+asyncpg://localhost:5432/postgres")
    optimism_url: str = os.getenv("OPTIMISM_URL", 'http://44.232.21.2:8545')



class UvicornSettings(BaseSettings):
    host: str = os.getenv("HOST", "0.0.0.0")
    _port: str = os.getenv("PORT", "8000")

    @property
    def port(self):
        # if reading from .env, this will be a string and uvicorn will complain
        return int(self._port)




class Settings(BaseSettings):
    fastapi: FastAPISettings = FastAPISettings()
    uvicorn: UvicornSettings = UvicornSettings()

settings = Settings()
