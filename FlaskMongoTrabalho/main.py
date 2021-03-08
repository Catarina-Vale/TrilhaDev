from conection import connect_and_provide

import Interact_with_nosql
from flask import Flask, request

app = Flask(__name__)

@app.route("/")
def helloworld():
    print('user accessed mainpage')
    return "Welcome, bub"

@app.route("/repos", methods = ['GET', 'POST'])
def mainfunction():
    if request.method == 'GET':
        print('user requested all users')
        return Interact_with_nosql.get_all_repos_users()
    elif request.method == 'POST':
        entrada = request.args.get('Username')
        print(f'user wants to post gituser {entrada}')
        return Interact_with_nosql.post_repos_and_user(entrada)

@app.route("/repos/<string:gituser>", methods = ['GET', 'PUT', 'DELETE', 'POST'])
def individualfunction(gituser):
    if request.method == 'GET':
        print(f'user requested gituser: {gituser}')
        return Interact_with_nosql.get_single_repos_user(gituser)
    elif request.method == 'PUT':
        print(f'user wants to update gituser {gituser}')
        return Interact_with_nosql.put_repos_and_user(gituser)
    elif request.method == 'DELETE':
        print(f'user wants to delete gituser {gituser}')
        return Interact_with_nosql.delete_repos_and_user(gituser)
    elif request.method == 'POST':
        print(f'user wants to post gituser {gituser}')
        return Interact_with_nosql.post_repos_and_user(gituser)

if __name__ == '__main__':
    print('listening in port 8000...')
    app.run(host='0.0.0.0',port=8000)
    print('Shut down')