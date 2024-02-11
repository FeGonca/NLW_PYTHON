# NLW Expert Python

Projeto desenvolvido durante o evento NLW Experts na trilha Python da Rocketseat.


## Instalação

1. Clone o repositório:
```bash
git clone <repository_url>
```

2. Instale as dependências:
```bash
pip install -r requirements.txt
```

3. Ative o ambiente virtutal:
```bash
source <virtualenv_name>/bin/activate
```

4. Run the application:
```bash
python app.py
```

## Utilização
1. Envie uma requisição POST para o endpoint http://localhost:3000/create_tag com os código do produto no corpo da requisição.
2. A aplicação vai gerar uma imagem de código de barras para o produto e retornar a caminho da imagem.

## Explemplo de requisição
```json
{
    "product_code": "123-456-789"
}
````

## Exemplo de resposta
```json
{
  "data": {
    "type": "Tag Image",
    "count": 1,
    "path": "/path/to/barcode.png"
  }
}
```

## Tecnologias usadas
- Python
- Flask
- Barcode


Fique a vontade para usar e modificar!
