from core.configs import settings
from sqlalchemy import Column, Integer, String, Date
from datetime import date

class OperadoraModel(settings.DBBaseModel):
  __tablename__ = "operadoras"
  
  id: int = Column(Integer, primary_key=True, autoincrement=True)
  registro_ans: str = Column(String(6), unique=True, nullable=False)
  cnpj: str = Column(String(14), nullable=False)
  razao_social: str = Column(String(140), nullable=False)
  nome_fantasia: str = Column(String(140))
  modalidade: str = Column(String(40))
  logradouro: str = Column(String(40))
  numero: str = Column(String(20))
  complemento: str = Column(String(40))
  bairro: str = Column(String(30))
  cidade: str = Column(String(30))
  uf: str = Column(String(2))
  cep: str = Column(String(8))
  ddd: str = Column(String(4))
  telefone: str = Column(String(20))
  fax: str = Column(String(20))
  endereco_eletronico: str = Column(String(255))
  representante: str = Column(String(50))
  cargo_representante: str = Column(String(40))
  regiao_de_comercializacao: int = Column(Integer)
  data_registro_ans: date = Column(Date)
