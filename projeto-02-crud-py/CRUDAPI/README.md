# API para produtos

este API registra e devolve produtos, ele possui descrição e preço

# Requisitos

Mongoengine, Flask, pymongo

Um simples pip install deve fazer o truque

# Usabilidade

após abrir o servidor localizado no main.py, a porta ouvida é a 5000. acessando o localhost:5000 você sera jogado na main page, que não tem nada alem de um greeting

acessando o endereço /products pode-se interagir com os metodos GET PUT POST e DELETE, com os valores 'Name' para nome do produto 'Desc' para a descrição e 'Value' para o valor, nota-se que Value apenas aceita floats