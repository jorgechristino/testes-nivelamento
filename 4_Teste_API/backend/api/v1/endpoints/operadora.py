from typing import List
from fastapi import APIRouter, status, Depends, HTTPException, Response
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from models.operadora_model import OperadoraModel
from schemas.operadora_schema import OperadoraSchema
from core.deps import get_session

router = APIRouter()

# POST Operadora
@router.post('/', status_code=status.HTTP_201_CREATED, response_model=OperadoraSchema)
async def post_operadora(operadora: OperadoraSchema, db: AsyncSession = Depends(get_session)):
  new_operadora = OperadoraModel(
    registro_ans=operadora.registro_ans,
    cnpj=operadora.cnpj,
    razao_social=operadora.razao_social,
    nome_fantasia=operadora.nome_fantasia,
    modalidade=operadora.modalidade,
    logradouro=operadora.logradouro,
    numero=operadora.numero,
    complemento=operadora.complemento,
    bairro=operadora.bairro,
    cidade=operadora.cidade,
    uf=operadora.uf,
    cep=operadora.cep,
    ddd=operadora.ddd,
    telefone=operadora.telefone,
    fax=operadora.fax,
    endereco_eletronico=operadora.endereco_eletronico,
    representante=operadora.representante,
    cargo_representante=operadora.cargo_representante,
    regiao_de_comercializacao=operadora.regiao_de_comercializacao,
    data_registro_ans=operadora.data_registro_ans,
  )

  db.add(new_operadora)
  await db.commit()
  return new_operadora
  
# GET Operadoras
@router.get('/', response_model=List[OperadoraSchema])
async def get_operadoras(db: AsyncSession = Depends(get_session)):
  async with db as session:
    query = select(OperadoraModel)
    result = await session.execute(query)
    operadoras: List[OperadoraModel] = result.scalars().all()

    return operadoras
  
# Buscar Operadoras
@router.get('/search', response_model=List[OperadoraSchema], status_code=status.HTTP_200_OK)
async def buscar_operadoras(termo: str, num_resultados: int = 10, db: AsyncSession = Depends(get_session)):
  async with db as session:
    query = select(OperadoraModel).filter(
      (OperadoraModel.razao_social.ilike(f"%{termo}%")) |
      (OperadoraModel.nome_fantasia.ilike(f"%{termo}%")) 
    ).limit(num_resultados)
    result = await session.execute(query)
    operadoras: List[OperadoraModel] = result.scalars().all()

    if operadoras:
      return operadoras
    else:
      raise HTTPException(detail='Operadora não encontrada.', status_code=status.HTTP_404_NOT_FOUND)

# GET Operadora
@router.get('/{operadora_id}', response_model=OperadoraSchema, status_code=status.HTTP_200_OK)
async def get_operadora(operadora_id:int, db: AsyncSession = Depends(get_session)):
  async with db as session:
    query = select(OperadoraModel).filter(OperadoraModel.id == operadora_id)
    result = await session.execute(query)
    operadora = result.scalar_one_or_none()

    if operadora:
      return operadora
    else:
      raise HTTPException(detail='Operadora não encontrada.', status_code=status.HTTP_404_NOT_FOUND)
    
# PUT Operadora
@router.put('/{operadora_id}', response_model=OperadoraSchema, status_code=status.HTTP_202_ACCEPTED)
async def put_operadora(operadora_id:int, operadora: OperadoraSchema, db: AsyncSession = Depends(get_session)):
  async with db as session:
    query = select(OperadoraModel).filter(OperadoraModel.id == operadora_id)
    result = await session.execute(query)
    operadora_up = result.scalar_one_or_none()

    if operadora_up:
      operadora_up.cnpj=operadora.cnpj
      operadora_up.razao_social=operadora.razao_social
      operadora_up.nome_fantasia=operadora.nome_fantasia
      operadora_up.modalidade=operadora.modalidade
      operadora_up.logradouro=operadora.logradouro
      operadora_up.numero=operadora.numero
      operadora_up.complemento=operadora.complemento
      operadora_up.bairro=operadora.bairro
      operadora_up.cidade=operadora.cidade
      operadora_up.uf=operadora.uf
      operadora_up.cep=operadora.cep
      operadora_up.ddd=operadora.ddd
      operadora_up.telefone=operadora.telefone
      operadora_up.fax=operadora.fax
      operadora_up.endereco_eletronico=operadora.endereco_eletronico
      operadora_up.representante=operadora.representante
      operadora_up.cargo_representante=operadora.cargo_representante
      operadora_up.regiao_de_comercializacao=operadora.regiao_de_comercializacao
      operadora_up.data_registro_ans=operadora.data_registro_ans

      await session.commit()
      
      return operadora_up
    else:
      raise HTTPException(detail='Operadora não encontrada.', status_code=status.HTTP_404_NOT_FOUND)
    
# DELETE Operadora
@router.delete('/{operadora_id}', status_code=status.HTTP_204_NO_CONTENT)
async def delete_operadora(operadora_id:int, db: AsyncSession = Depends(get_session)):
  async with db as session:
    query = select(OperadoraModel).filter(OperadoraModel.id == operadora_id)
    result = await session.execute(query)
    operadora_del = result.scalar_one_or_none()

    if operadora_del:
      await session.delete(operadora_del)
      await session.commit()

      return Response(status_code=status.HTTP_204_NO_CONTENT)
    else:
      raise HTTPException(detail='Operadora não encontrada.', status_code=status.HTTP_404_NOT_FOUND)
    