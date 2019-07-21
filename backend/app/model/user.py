# -*- coding: utf-8 -*-
from sqlalchemy import Column, Integer, String, Enum
from werkzeug.security import generate_password_hash, check_password_hash

from app.lib.error_code import AuthFailed
from app.lib.permission import Ring
from .base import Base, db


class User(Base):
    id = Column(Integer, primary_key=True)
    email = Column(String(32), unique=True)
    nickname = Column(String(32), unique=True)
    _password = Column('password', String(128))
    # 权限范围，使用普通的枚举类Ring，会自动把成员转为字典再取Key作为数据库中存在形式
    # 默认值无效，搞不懂
    scope = Column(Enum(Ring), default='Guest')

    @property
    def password(self):
        return self._password

    @password.setter
    def password(self, raw):
        self._password = generate_password_hash(raw)

    @staticmethod
    def register_by_email(email, password):
        try:
            with db.auto_commit():
                user = User()
                user.email = email
                user.password = password
                # 因为默认值无效，所以在注册这里初始化为Guest
                user.scope = 'Guest'
                db.session.add(user)
        except IndentationError as e:
            print(e)
            return False
        return True

    @staticmethod
    def verify(email, password):
        user = User.query.filter_by(email=email).first_or_404(msg_404='user not found')
        if check_password_hash(user._password, password):
            return {
                'email': user.email,
                'scope': user.scope
            }
        else:
            raise AuthFailed()

    pass
