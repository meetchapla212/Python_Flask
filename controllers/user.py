from bson.objectid import ObjectId
from flask import Blueprint, request, jsonify
from middleware.authentication import checkJwt
from db_connection import getDBClient
import json
dbClient = getDBClient()
db = dbClient.get_database('PythonApp')
user = Blueprint('user', __name__)


@user.get('/user')
def getUser():
    checkAuth = checkJwt(request)
    if checkAuth['status']:
        userId = checkAuth['user_id']
        objInstance = ObjectId(userId)
        userData = db.users.find_one({'_id': objInstance})
        if userData:
            data = {
                'username': userData['username'],
                'email': userData['email'],
                'firstname': userData['firstname'],
                'lastname': userData['lastname']
            }
            return ({
                'status': True,
                'message': 'User Data Get Successfully!',
                'data': data
            })
        return ({
            'status': False,
            'message': 'User Not Found!',
        })
    return ({
        'status': checkAuth['status'],
        'message': checkAuth['message'],
    })
