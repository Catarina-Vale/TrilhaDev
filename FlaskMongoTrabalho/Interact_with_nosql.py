from pymongo import MongoClient


client = MongoClient("mongodb+srv://oiojoio:blabla89@repositories.d2klp.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")

db = client.get_database('FlaskProject')

master = db.SingleUser

def get_all_repos_users():
    allusers = list(master.find({}))
    return "guess what, under construction"

def get_single_repos_user(gituser):
    return "guess what, under construction"

def post_repos_and_user(gituser):
    return "under construction"

def put_repos_and_user(gituser):
    return "under construction"

def delete_repos_and_user(gituser):
    return "under construction"