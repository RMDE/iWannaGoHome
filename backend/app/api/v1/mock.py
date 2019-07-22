# -*- coding: utf-8 -*-
from flask import Response, jsonify

from app.lib.auth import auth
from app.lib.error_code import DatabaseError, Success
from app.lib.permission import Permission, Ring
from app.lib.redprint import Redprint
from app.model.mock import Mock
from app.schema.schema import MockSchema
from app.validator.form import CreateMockForm

api = Redprint('mock')


# 获取单个Mock的json
@api.route('/<int:id>', methods=['GET'])
def get_mock(id):
    mock_json = Mock.fetch_json(mock_id=id)
    return Response(mock_json, mimetype='application/json')


# 获取所有mock
@api.route('/all', methods=['GET'])
def get_all_mock():
    all = Mock.fetch_all()
    mock_schema = MockSchema()
    return jsonify([mock_schema.dump(mock).data for mock in all])


# 创建mock
@api.route('', methods=['POST'])
@auth.login_required
@Permission.require(Ring.Member)
def create_mock():
    form = CreateMockForm().execute_validate()
    result = Mock.insert(form['name'], form['email'], form['json'])
    if result:
        return Success()
    else:
        return DatabaseError()


# 软删除mock
@api.route('/<int:id>', methods=['DELETE'])
@auth.login_required
@Permission.require(Ring.Member)
def delete_mock(id):
    Mock.delete('id', id)
    return Success()
