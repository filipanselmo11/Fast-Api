from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()



@app.get('/saudacao/{nome}')
def saudacao(nome: str):
    texto = f'Olá {nome}, tudo em paz'
    return {"mensagem": texto }

@app.get('/quadrado/{numero}')
def quadrado(numero: int):
    resultado = numero * numero
    texto = f'O quadrado de {numero} é {resultado}'

    return {"mensagem": texto}


@app.get('/dobro')
def dobro(valor: int):
    resultado = 2 * valor
    return {"resultado": f'O dobro de {valor} é {resultado}'}

@app.get('/area-retangulo') # ?nome=valor
def area_retangulo(largura: int, altura: int = 1):
    area = largura * altura
    return {'area': area}


class Produto(BaseModel):
    nome: str
    preco: float

@app.post('/produtos')
def produtos(produto: Produto):
    return {'mensagem': f'Produto ({produto.nome} - R$ {produto.preco}) cadastrado com sucesso'}