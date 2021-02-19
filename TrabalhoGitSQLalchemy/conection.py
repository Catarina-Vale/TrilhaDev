
import requests

def connect_and_provide(entrada):
    print(f'Procurando em https://api.github.com/users/{entrada}/repos...\n')
    proto = requests.get(f'https://api.github.com/users/{entrada}/repos')
    #conecting and gathering results
    if proto.status_code == 200:
        print('Encontrado!')
        proto = proto.json()
        out = []
        for scan in proto:
            out.append(scan["name"]) #adding all repositories into a list
        return out
    #Processing and sending said results
    else:
        print('Usuario nao encontrado.')
        return False
