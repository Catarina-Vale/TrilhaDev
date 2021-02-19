from Engine_to_azure import engine, Base

from repositories import Repository

from sqlalchemy.orm import sessionmaker

def select_delete_candidates(aquired_repos, repolist):
    delete_list = []
    for delete_candidate in aquired_repos:
            i = 0
            for current_repos in repolist:
                if current_repos == delete_candidate:
                    i = i + 1

            if i == 0:
                delete_list.append(delete_candidate)
    
    return delete_list

def select_insert_candidates(aquired_repos, repolist):
    insert_list = []
    for insert_candidate in repolist:
            i = 0
            for existing_repo in aquired_repos:
               if existing_repo == insert_candidate:
                    i = i + 1

            if i == 0:
                insert_list.append(insert_candidate)
    
    return insert_list

#gituser, repolist

def insert_repo_and_user(gituser, repolist):
    Session = sessionmaker(bind=engine)
    session = Session()
    raw_repos = session.query(Repository).filter(Repository.username == gituser).all()
    aquired_repos = []
    print('Repositorios ja armazenados deste usuario:')
    for repo in raw_repos:
        print(f'{repo.username}:{repo.reponame}')
        aquired_repos.append(repo.reponame)

    print(f'\nRepositorios do usuario adiquiridos no git: {repolist}\n')
    delete_list = select_delete_candidates(aquired_repos, repolist)
    insert_list = select_insert_candidates(aquired_repos, repolist)
    #print(delete_list)
    #print(insert_list)
    if delete_list is not None:
        for delete_this in delete_list:
            print(f'Usuario nao possui mais {delete_this} em sua conta, deletando...\n')
            session.query(Repository).filter(Repository.reponame == delete_this).delete()
    if insert_list is not None:
        for insert_this in insert_list:
            print(f'Novo repositorio pelo nome de {insert_this} encontrado, adicionando...\n')
            newadd = Repository(gituser, insert_this)
            session.add(newadd)
    session.commit()
    

    
#Base.metadata.create_all(engine)


#insert_repo_and_user()
