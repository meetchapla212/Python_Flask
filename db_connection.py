from pymongo.mongo_client import MongoClient
import certifi
from config import DB_Config


def getDBClient():
    connectionString = 'mongodb+srv://pythonapp:PythonApp@cluster0.kdbm3xa.mongodb.net/<db>?retryWrites=true&w=majority'
    client = MongoClient(connectionString, tlsCAFile=certifi.where())
    return client
