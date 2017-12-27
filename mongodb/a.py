from pymongo import MongoClient

c = MongoClient('localhost', 27017)

db = c.cache

db.webpage.insert({'url':"asfhksjdfhksjdfhkdj", 'html':'dddfdfgtghfghrtdfgfg'})