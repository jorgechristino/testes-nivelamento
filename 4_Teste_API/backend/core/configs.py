from pydantic_settings import BaseSettings
from sqlalchemy.ext.declarative import declarative_base
from typing import ClassVar
from sqlalchemy.orm.decl_api import DeclarativeMeta

class Settings(BaseSettings):
  """
  Configurações gerais usadas na aplicação
  """
  API_V1_STR: str = '/api/v1'
  DB_URL: str = "postgresql+asyncpg://postgres:user123@localhost:5432/testes"
  DBBaseModel: ClassVar[DeclarativeMeta] = declarative_base()

  class Config:
    case_sensitive = True

settings: Settings = Settings()