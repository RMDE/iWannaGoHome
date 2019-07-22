# -*- coding: utf-8 -*-
import functools
from enum import Enum, unique
from flask import g

from app.lib.error_code import Forbidden, CodeError


# 权限级别Ring环，仿CPU Ring
@unique
class Ring(Enum):
    Administrator = 0
    Member = 2
    Guest = 3


class Permission:

    # 必须在auth.login_require后面使用，
    # 因为需要用到g这个全局变量，在auth里g.user保存当前用户信息
    @classmethod
    def require(cls, ring):
        def permission_decorator(f):
            @functools.wraps(f)
            def wrapper(*args, **kwargs):
                # 判断全局变量g是否存在user
                if hasattr(g, 'user'):
                    user = g.user
                    scope = user.scope
                    if Ring[scope].value <= ring.value:
                        return f(*args, **kwargs)
                    else:
                        raise Forbidden()
                else:
                    raise CodeError()

            return wrapper

        return permission_decorator

    pass
