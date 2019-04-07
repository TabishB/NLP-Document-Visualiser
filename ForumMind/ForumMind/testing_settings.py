from .settings import *
from mongomock import *

print('running test settings.')
#Keep this here for pymongos sake
TEST_MONGO_DATABASE = {
    'db': 'testdb',
    'host': 'mongomock://localhost',
    'port': 27017,
}

print('disconnecting from main database...')
#Ensure that the main database is disconnected
mongoengine.connection.disconnect()

print('Creating test database for alias \'testdb\'...')
#connect to a test database
mongoengine.connect('testdb', host='mongomock://localhost')

# # import mongoengine

# TEST_MONGO_DATABASE = {
#     'db': 'test',
#     'host': 'mongomock://localhost',
#     'port': 27017,
# }
# mongoengine.connection.disconnect()
# mongoengine.connect('testdb', host='mongomock://localhost')
