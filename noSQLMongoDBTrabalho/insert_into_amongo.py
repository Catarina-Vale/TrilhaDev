from pymongo import MongoClient

from sortstuffout import select_delete_candidates, select_insert_candidates

client = MongoClient("mongodb+srv://oiojoio:blabla89@repositories.d2klp.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")

db = client.get_database('Repositories')

resource = db.RepoNUser

def insert_repo_and_user(gituser,repolist):
    aquired_repos = []
    rawdata = resource.find({'Username': gituser})
    for entry in rawdata:
        aquired_repos.append(entry["Reponame"])
    
    delete_list = select_delete_candidates(aquired_repos,repolist)
    insert_list = select_insert_candidates(aquired_repos,repolist)

    for deletion in delete_list:
        print(f'{deletion} nao encontrado no git, deletando...')
        resource.delete_one({'Username': gituser, 'Reponame': deletion})

    for insertion in insert_list:
        print(f'novo repo pelo nome de {insertion} encontrado! Adicionando...')
        resource.insert_one({'Username': gituser, 'Reponame': insertion})

