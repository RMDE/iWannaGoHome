# -*- coding: utf-8 -*-
from wtforms import StringField, IntegerField
from wtforms.validators import DataRequired, Regexp, NumberRange
from app.validator.base import BaseForm


class UserLoginForm(BaseForm):
    email = StringField(validators=[DataRequired(message='邮箱不能为空')])
    password = StringField(validators=[DataRequired(message='密码不能为空')])


class UserRegisterForm(BaseForm):
    email = StringField(
        validators=[DataRequired(message='邮箱不能为空'),
                    Regexp(r'^[A-Za-z0-9\.]+@[A-Za-z0-9]+\.[A-Za-z0-9]+$', message='邮箱格式错误')])

    password = StringField(
        validators=[DataRequired(message='密码不能为空'),
                    Regexp(r'^[A-Za-z0-9_\.*&$#@]{8,32}$', message='密码长度应为8-32或密码包含不可用字符')])


class PromotePrivilegeForm(BaseForm):
    email = StringField(validators=[DataRequired(message='邮箱不能为空')])
    # 用户权限提升等级数，负数就是降级
    promotion = StringField(validators=[DataRequired(message='权限提升等级数不能为空')])


class CreateMockForm(BaseForm):
    email = StringField(validators=[DataRequired(message='邮箱不能为空')])
    name = StringField(validators=[DataRequired(message='名称不能为空')])
    json = StringField(validators=[DataRequired(message='Json文本不能为空')])
    project = StringField(default=None)
    form = StringField(default=None)
    desc = StringField(default=None)


class CreateProjectForm(BaseForm):
    name = StringField(validators=[DataRequired(message='名称不能为空')])
    desc = StringField(validators=[DataRequired(message='描述不能为空')])
