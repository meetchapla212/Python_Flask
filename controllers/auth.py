from flask import Blueprint, request, jsonify
from db_connection import getDBClient
from bcrypt import gensalt, hashpw, checkpw
from jwt import encode, decode
from config import JWT_Config
import datetime

auth = Blueprint('auth', __name__)
dbClient = getDBClient()
db = dbClient.get_database('PythonApp')


@auth.post('/signup')
def signUp():
    if request.is_json:
        user = request.get_json()
        if user and user['email'] and user['password']:
            userExist = db.users.find_one({"email": user['email']})
            if userExist:
                return ({
                    "status": True,
                    "message": "User Already Registered!",
                })
            salt = gensalt(rounds=15)
            userBytes = user['password'].encode('utf-8')
            user['password'] = hashpw(userBytes, salt)
            result = db.users.insert_one(user)
            return ({
                "status": True,
                "message": "User Registered!",
                "data": {
                    'id': str(result.inserted_id)
                }
            })
        return ({
            "status": True,
            "message": "Please Provide Email and Password!",
        })


@auth.post('/login')
def login():
    if request.is_json:
        reqData = request.get_json()
        if reqData and reqData['email'] and reqData['password']:
            userData = db.users.find_one({'email': reqData['email']})
            if userData:
                userBytes = reqData['password'].encode('utf-8')
                if checkpw(userBytes, userData['password']):
                    token = encode(
                        {
                            "user_id": str(userData['_id']),
                            'exp': datetime.datetime.now() + datetime.timedelta(days=1)
                        }, JWT_Config['key'], JWT_Config['algorithm'])
                    return ({
                        "status": True,
                        "message": "User Login Successfully",
                        "data": {
                            'token': token
                        }
                    })
                return ({
                    "status": True,
                    "message": "Password Incorrect!",
                })
            return ({
                "status": True,
                "message": "User Not Found!",
            })
        return ({
            "status": True,
            "message": "Please Provide Email and Password!",
        })


@auth.post('/logout')
def logout():
    return 'Logout'
