from typing import Optional
from pydantic import BaseModel as SCBaseModel
from datetime import date

class OperadoraSchema(SCBaseModel):
  id: Optional[int] = None
  registro_ans: str
  cnpj: str
  razao_social: str
  nome_fantasia: Optional[str] = None
  modalidade: Optional[str] = None
  logradouro: Optional[str] = None
  numero: Optional[str] = None
  complemento: Optional[str] = None 
  bairro: Optional[str] = None
  cidade: Optional[str] = None 
  uf: Optional[str] = None 
  cep: Optional[str] = None 
  ddd: Optional[str] = None 
  telefone: Optional[str] = None 
  fax: Optional[str] = None 
  endereco_eletronico: Optional[str] = None 
  representante: Optional[str] = None 
  cargo_representante: Optional[str] = None 
  regiao_de_comercializacao: Optional[int] = None
  data_registro_ans: Optional[date] = None

  class Config:
    from_attributes = True
