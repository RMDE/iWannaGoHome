# -*- coding: utf-8 -*-
from flask import jsonify

from app.lib.auth import auth
from app.lib.error_code import DatabaseError, Success
from app.lib.permission import Ring, Permission
from app.lib.redprint import Redprint
from app.model.project import Project
from app.schema.schema import ProjectSchema, MockSchema
from app.validator.form import CreateProjectForm

api = Redprint('project')


# 创建一个项目
@api.route('', methods=['POST'])
@auth.login_required
@Permission.require(Ring.Member)
def create_project():
    form = CreateProjectForm().execute_validate()
    result = Project.insert(form)
    if result:
        return Success()
    else:
        return DatabaseError()


# 获取一个项目的信息
@api.route('/<int:id>', methods=['GET'])
def get_project(id):
    project = Project.fetch_project(id)
    project_schema = ProjectSchema()
    return jsonify(project_schema.dump(project).data)


# 更新一个项目的信息
@api.route('/<int:id>', methods=['PUT'])
@auth.login_required
@Permission.require(Ring.Member)
def update_project(id):
    form = CreateProjectForm().execute_validate()
    result = Project.update_project(id, form)
    if result:
        return Success()
    else:
        return DatabaseError()


# 获取项目列表
@api.route('/all', methods=['GET'])
def get_all_projects():
    projects = Project.fetch_all()
    project_schema = ProjectSchema()
    # 排除mock中的json字段
    mock_schema = MockSchema(exclude=['json'])
    project_list = []
    for project in projects:
        data = project_schema.dump(project).data
        # 获取mocks，进行序列化操作
        mocks = project.mocks
        data['mocks'] = []
        for mock in mocks:
            data['mocks'].append(mock_schema.dump(mock).data)
        project_list.append(data)
    return jsonify(project_list)


# 获取某个项目下的所有Mock数据
@api.route('/<int:id>/mocks', methods=['GET'])
def get_mocks_in_project(id):
    project = Project.fetch_project(id)
    mock_schema = MockSchema()
    mocks = project.mocks
    mocks_data = []
    for mock in mocks:
        mocks_data.append(mock_schema.dump(mock).data)
    return jsonify(mocks_data)
