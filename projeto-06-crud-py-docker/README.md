# Trabalho crud serverless, registro de produtos

Este projeto é parte da trilha dev, com o propósito de utilizar os metodos serverless oferecidos pelo azure functions
O programa recebe requests http para registrar, listar, editar e deletar itens numa database

## Requerimentos

Apenas uma ferramenta para acessar os protocolos http no link oferecido na cloud

### Links e parametros para registro

GET-ALL https://oiojoio-crud-api.azurewebsites.net/api/products/
Retorna um json com todos os produtos registrados
GET-ONE https://oiojoio-crud-api.azurewebsites.net/api/products/{nome}
Returna um json com apenas o produto procurado por nome
POST https://oiojoio-crud-api.azurewebsites.net/api/products/ params: Name:, Desc:, Value:
Resgitra um produto na database, com os parametros de nome, descriçao e valor
PUT https://oiojoio-crud-api.azurewebsites.net/api/products/ params: Name:, Desc:, Value:
Atualiza um produto na database, com os parametros de nome, descriçao e valor
DELETE https://oiojoio-crud-api.azurewebsites.net/api/products/{nome}
Delete o produto cujo nome foi dado da database