import pyodbc

def insert_repo_and_user(server, database, username, password, driver, gituser, repolist):
        cnxn = pyodbc.connect('DRIVER='+driver+';PORT=1433;SERVER='+server+';PORT=1443;DATABASE='+database+';UID='+username+';PWD='+ password)
        cursor = cnxn.cursor()
        #conecting to azure db and setting up cursor
        aquired_repos = []
        cursor.execute(f"SELECT * from Repositories WHERE Username = ?", gituser)
        row = cursor.fetchone()
        while row:
            aquired_repos.append(str(row[1]))
            row = cursor.fetchone() #creating a list with all repositories in database
        
        print(aquired_repos)
        for delete_candidate in aquired_repos:
            i = 0
            for current_repos in repolist:
                if current_repos == delete_candidate:
                    i = i + 1

            if i == 0:
                print(f'removendo de repositories {gituser}, {delete_candidate}')
                cursor.execute(f"DELETE from repositories where Username=? and Reponame=?", (gituser, delete_candidate))
        #comparing DBs repositories with one fetched from web for any repos that need to be deleted
        for insert_candidate in repolist:
            i = 0
            for existing_repo in aquired_repos:
               if existing_repo == insert_candidate:
                    i = i + 1

            if i == 0:
                print(f'inserindo em repositories {gituser}, {insert_candidate}')
                cursor.execute(f"INSERT into Repositories(Username, Reponame) values (?,?)", (gituser, insert_candidate))
        #comparing DBs repositories with one fetched from web for any repos that need to be added
        cnxn.commit()
        cnxn.close()

