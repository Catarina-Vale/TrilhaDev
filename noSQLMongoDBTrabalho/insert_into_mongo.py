from mongoengine import *
from sortstuffout import select_delete_candidates, select_insert_candidates

connect(host='mongodb+srv://oiojoio:@repositories.d2klp.mongodb.net/Repositories')

class User(Document):
    Usuario = StringField()
    Repositorio = ListField()


def insert_repo_and_user(gituser,repolist):
    entity_in_database = User.objects(Usuario = gituser).first()
    if entity_in_database is not None:
        print('Usuario ja cadastrado, atualizando...')
        entity_in_database.Repositorio = repolist
        entity_in_database.save()
    else:
        print('Novo usuario, cadastrando...')
        newuser = User(Usuario = gituser, Repositorio = repolist).save()



# for entity in User.objects:
#     print(entity.Usuario + ': ' + entity.Repositorio)

# find_him = User.objects(Repositorio = '513').first()

# if find_him is not None:
#     print('ferrou')

# else:
#     print('ferrou nada')


# print(find_him.Usuario)

# find_him.Usuario = 'JooJ'

# find_him.save()

# find_him = User.objects(Repositorio = '5').first()

# print(find_him.Usuario)
