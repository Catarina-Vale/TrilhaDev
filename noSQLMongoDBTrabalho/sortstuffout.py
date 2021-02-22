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