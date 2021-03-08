import requests

print("Digite o nome de usuário")
entrada = input()

print(f'Procurando em https://api.github.com/users/{entrada}/repos...\n')
proto = requests.get(f'https://api.github.com/users/{entrada}/repos')
proto = proto.json()

i = 0
for entry in proto:
    print(entry["name"])
    i += 1

print(f'No total temos {i} repositorios')