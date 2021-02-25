import requests
atributes = []
payload = {}
r = requests.get('https://www.dnd5eapi.co/api/spells/acid-arrow')
r = r.raw

for att in r:
   atributes.append(att)


print(r)
print(atributes)
