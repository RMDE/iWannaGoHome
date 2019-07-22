# -*- coding: utf-8 -*-
from app.lib.orm import ma
from app.model.user import User
from app.model.mock import Mock


class UserSchema(ma.ModelSchema):
    class Meta:
        model = User
        # 序列化时去掉字段
        exclude = ['deleted', 'password']


class MockSchema(ma.ModelSchema):
    class Meta:
        model = Mock
        exclude = ['deleted']
