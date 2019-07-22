# -*- coding: utf-8 -*-
from flask import Response

from app.lib.auth import auth
from app.lib.error_code import DatabaseError, Success
from app.lib.permission import Permission, Ring
from app.lib.redprint import Redprint
from app.model.mock import Mock
from app.validator.form import CreateMockForm

api = Redprint('mock')


@api.route('/<int:id>', methods=['GET'])
def get_mock(id):
    mock_json = Mock.fetch_json(mock_id=id)
    return Response(mock_json, mimetype='application/json')


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
