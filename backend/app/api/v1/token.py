# -*- coding: utf-8 -*-
from flask import current_app, jsonify

from app.lib.redprint import Redprint
from app.model.user import User
from app.validator.form import UserLoginForm
from itsdangerous import TimedJSONWebSignatureSerializer

api = Redprint('token')


@api.route('', methods=['POST'])
def get_token():
    # 验证输入格式
    form = UserLoginForm().execute_validate()
    # 验证账号，成果即返回{email,scope}
    user_info = User.verify(form['email'], form['password'])
    expiration = current_app.config['TOKEN_EXPIRATION']
    token = generator_token(user_info, expiration)
    result = {
        'email': user_info['email'],
        'token': token.decode('ascii')
    }
    return jsonify(result)


def generator_token(user_info, expiration=3600):
    # 生成令牌
    s = TimedJSONWebSignatureSerializer(current_app.config['SECRET_KEY'], expires_in=expiration)
    return s.dumps({
        'email': user_info['email'],
        'scope': user_info['scope'].name  # user_info['scope']得到的是一个{name,value}，对应枚举类中的设定
    })
