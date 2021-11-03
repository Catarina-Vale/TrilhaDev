from mongoengine import *
from flask import Response
from conection import connect_and_provide
connect(host='mongodb+srv://oiojoio:@repositories.d2klp.mongodb.net/FlaskProject')

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
        output = {}
        output[find_them.Usuario] = find_them.Repositorio
        return output
    else:
        return Response('User isnt resgistered, bub',status=404)

def post_repos_and_user(gituser):
    find_them = User.objects(Usuario = gituser).first()
    if find_them is not None:
        return Response('User already here bub, try PUT',status=400)
    else:
        repolist = connect_and_provide(gituser)
        if repolist == False:
            return Response('this user does not exist in git,bub',status=404)
        else:
            newuser = User(Usuario = gituser, Repositorio = repolist).save()
            return Response('User successfully registered, bub', status=200)

def put_repos_and_user(gituser):
    find_them = User.objects(Usuario = gituser).first()
    if find_them is not None:
        repolist = connect_and_provide(gituser)
        if repolist == False:
            return Response('Something went wrong and its my fault, bub',status=417)
        else:
            find_them.Repositorio = repolist
            find_them.save()
            return Response('Gituser successfully updated, bub',status=200)
    else:
        return Response('User not found, bub, try POST',status=404)

def delete_repos_and_user(gituser):
    find_them = User.objects(Usuario = gituser).first()
    if find_them is not None:
        find_them.delete()
        return Response('Gituser successfully deleted, bub',status=200)
    else:
        return Response('nothin to delete here',status=404)
    return "under construction"

