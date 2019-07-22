# -*- coding: utf-8 -*-
from app.lib.orm import ma
from app.model.user import User
from app.model.mock import Mock


class UserSchema(ma.ModelSchema):
    class Meta:
        model = User
        exclude = ['deleted', 'password']


class MockSchema(ma.ModelSchema):
    class Meta:
        model = Mock
        exclude = ['deleted']
