# -*- coding: utf-8 -*-
from app.lib.auth import auth
from app.lib.error_code import Success, DatabaseExistError, ParameterException
from app.lib.permission import Permission, Ring
from app.lib.redprint import Redprint
from app.model.user import User
from app.validator.form import UserRegisterForm, PromotePrivilegeForm
from app.lib.orm import db

api = Redprint("user")


@auth.login_required
@Permission.require(Ring.Member)
@api.route('', methods=['GET'])
def test():
    return 'hello'


# 注册用户
def register():
    form = UserRegisterForm().execute_validate()
    result = User.register_by_email(form['email'], form['password'])
    if result:
        return Success()
    else:
        return DatabaseExistError()


# 提升用户权限
def promote_privilege():
    form = PromotePrivilegeForm().validate()
    user = User.query.filter_by(email=form['email']).first_or_404()
    current_level = Ring[user.scope].value  # 转换成整形
    update_level = current_level + form['promotion']
    # 检查Ring枚举类里是否存在值为update_level的成员
    try:
        Ring(update_level)
    except ValueError as e:
        print(e)
        # 不存在抛出异常
        raise ParameterException()
    # 存在则修改数据库值
    with db.auto_commit():
        user.scope = update_level
    return Success()
