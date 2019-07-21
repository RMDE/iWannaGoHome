# -*- coding: utf-8 -*-
from collections import namedtuple
from flask import current_app, g
from flask_httpauth import HTTPBasicAuth
from itsdangerous import TimedJSONWebSignatureSerializer, BadSignature, SignatureExpired
from app.lib.error_code import AuthFailed

auth = HTTPBasicAuth()

UserTuple = namedtuple('User', ['uid', 'scope'])


# auth装饰器，执行此函数进行token验证
# Authorization : Basic base64(username:password)
@auth.verify_password
def verify_password(token, _):
    user_info = verify_auth_token(token)
    if not user_info:
        return False
    else:
        # flask g 变量
        g.user = user_info
        return True


def verify_auth_token(token):
    s = TimedJSONWebSignatureSerializer(current_app.config['SECRET_KEY'])
    try:
        # 反向解密数据
        data = s.loads(token)
    except BadSignature:
        raise AuthFailed(msg='token is invalid')
    except SignatureExpired:
        raise AuthFailed(msg='token is expired')

    email = data['email']
    scope = data['scope']

    return UserTuple(email, scope)
