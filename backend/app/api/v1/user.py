# -*- coding: utf-8 -*-
from app.lib.auth import auth
from app.lib.error_code import Success, DatabaseExistError, ParameterException
from app.lib.permission import Permission, Ring
from app.lib.redprint import Redprint
from app.model.user import User
from app.validator.form import UserRegisterForm, PromotePrivilegeForm
from app.lib.orm import db

api = Redprint("user")


@api.route('', methods=['GET'])
@auth.login_required
def test():
    return 'hello'


# 注册用户
@api.route('', methods=['POST'])
def register():
    form = UserRegisterForm().execute_validate()
    result = User.register_by_email(form['email'], form['password'])
    if result:
        return Success()
    else:
        return DatabaseExistError()


# 提升用户权限
@api.route('/promote', methods=['POST'])
@auth.login_required
@Permission.require(Ring.Administrator)
def promote_privilege():
    form = PromotePrivilegeForm().execute_validate()
    user = User.query.filter_by(email=form['email']).first_or_404()
    current_level = Ring[user.scope.name].value  # 转换成整形
    update_level = current_level - int(form['promotion'])  # 因为数值小的权限大，所以是减
    # 检查Ring枚举类里是否存在值为update_level的成员
    try:
        Ring(update_level)
    except ValueError as e:
        print(e)
        # 不存在抛出异常
        raise ParameterException(msg='权限级别不在正常范围，请检查参数 😒')
    # 存在则修改数据库值
    with db.auto_commit():
        user.scope = Ring(update_level)
    return Success()
