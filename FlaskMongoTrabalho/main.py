from conection import connect_and_provide

import Interact_with_nosql
from flask import Flask, request

app = Flask(__name__)

@app.route("/")
def helloworld():
    print('user accessed mainpage')
    return "Hello world!"

@app.route("/repos", methods = ['GET', 'POST'])
def mainfunction():
    if request.method == 'GET':
        print('user requested all users')
        return Interact_with_nosql.get_all_repos_users()
    elif request.method == 'POST':
        print(f'user wants to post gituser {}')
        return Interact_with_nosql.post_repos_and_user(request)

if __name__ == '__main__':
    print('listening in port 5000...')
    app.run(host='0.0.0.0',port=5000)
    print('Shut down')