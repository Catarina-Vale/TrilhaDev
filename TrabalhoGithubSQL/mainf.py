from conection import connect_and_provide
from sqlconection import insert_repo_and_user

server = 'alexandre-server.database.windows.net'
database = 'oiojoio'
username = 'cloudadmin'
password =  'D0ffy123'
driver = '{ODBC Driver 17 for SQL Server}'
#Importing both Request and SQL functions to the main function
def mainfunc(entrada):

    repolist = connect_and_provide(gituser)
    #Gathering the result of the request function in either a list or False if git user doesnt exist
    if repolist == False:
        return
    else:
        insert_repo_and_user(server,database,username,password, driver, gituser, repolist)
#If all goes well the function that interacts with azureDB will be called
print("Digite o nome de usuário")

gituser = input()

mainfunc(gituser)