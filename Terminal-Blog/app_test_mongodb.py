import pymongo
from pprint import pprint

uri = "mongodb://192.168.56.100:27017"
client = pymongo.MongoClient(uri)
database = client["fullstack"]
collections = database["posts"]

#posts = collections.find({})
posts_list = [post for post in collections.find(({}))]



pprint(posts_list)