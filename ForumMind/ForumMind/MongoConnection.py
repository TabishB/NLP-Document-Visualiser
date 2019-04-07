from pymongo import MongoClient
import pprint
HOST = '249992.mlab.com'
PORT = 49992
DB_NAME = 'forummind'
UNAME = 'Shenin'
PW = 'Shenin99'

class MongoConnection(object):
    def __init__(self):
        # client = MongoClient(HOST, PORT, username = UNAME, password = PW)

        self.db = client[DB_NAME]

    def get_collection(self, name):
        self.collection = self.db[name]

class MyCollection(MongoConnection):
    
    def __init__(self):
        super(MyCollection, self).__init__
        self.get_collection('collection_name')


# client = MongoClient(HOST, PORT)
uri = 'mongodb://{}:{}@{}.mlab.com:{}/{}'.format(UNAME, PW, HOST, PORT, DB_NAME)
# print(uri)
client = MongoClient(uri)
db = client[DB_NAME]
print(db.name)
results = db['word_count'].findone()
print(results)
# for u in results:
#     print(u)