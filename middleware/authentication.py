from jwt import decode
from config import JWT_Config


def checkJwt(request):
    if request.authorization:
        token = request.authorization.token
        decodeToken = decode(token, JWT_Config['key'], JWT_Config['algorithm'])
        if decodeToken['user_id']:
            return ({
                'status': True,
                'user_id': decodeToken['user_id']
            })
        return ({
            'status': False,
            'message': 'User Not Found!'
        })
    return ({
        'status': False,
        'message': 'Please provide authentication token'
    })
