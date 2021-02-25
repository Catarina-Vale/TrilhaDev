from mongoengine import *
from flask import Response
from conection import connect_and_provide
connect(host='mongodb+srv://oiojoio:blabla89@repositories.d2klp.mongodb.net/FlaskProject')

class User(Document):
    Usuario = StringField()
    Repositorio = ListField()

def get_all_repos_users():
    output = {}
    for entity in User.objects:
        output[entity.Usuario] = entity.Repositorio
    return output

def get_single_repos_user(gituser):
    find_them = User.objects(Usuario = gituser).first()
    if find_them is not None:
        # output = {}
        # output[find_them.Usuario] = find_them.Repositorio
        header = f'<h1>{find_them.Usuario}</h1>'
        body = ''
        for repos in find_them.Repositorio:
            body += f'\n<a href=https://www.youtube.com/watch?v=dQw4w9WgXcQ&ab_channel=RickAstleyVEVO>{repos}</a>'
        whole = header + body
        return whole
    else:
        return Response('<h1>User isnt resgistered, bub</h1>',status=404)

def post_repos_and_user(gituser):
    find_them = User.objects(Usuario = gituser).first()
    if find_them is not None:
        return Response('<h1>User already here bub, try PUT</h1>',status=400)
    else:
        repolist = connect_and_provide(gituser)
        if repolist == False:
            return Response('<h1>this user does not exist in git,bub</h1>',status=404)
        else:
            newuser = User(Usuario = gituser, Repositorio = repolist).save()
            return Response('<h1>User successfully registered, bub</h1>', status=200)

def put_repos_and_user(gituser):
    find_them = User.objects(Usuario = gituser).first()
    if find_them is not None:
        repolist = connect_and_provide(gituser)
        if repolist == False:
            return Response('<h1>Something went wrong and its my fault, bub</h1>',status=417)
        else:
            find_them.Repositorio = repolist
            find_them.save()
            return Response('<h1>Gituser successfully updated, bub</h1>',status=200)
    else:
        return Response('<h1>User not found, bub, try POST</h1>',status=404)

def delete_repos_and_user(gituser):
    find_them = User.objects(Usuario = gituser).first()
    if find_them is not None:
        find_them.delete()
        return Response('<h1>Gituser successfully deleted, bub</h1>',status=200)
    else:
        return Response('<h1>nothin to delete here</h1>',status=404)

