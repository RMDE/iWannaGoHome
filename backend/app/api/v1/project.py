# -*- coding: utf-8 -*-
from flask import jsonify

from app.lib.auth import auth
from app.lib.error_code import DatabaseError, Success
from app.lib.permission import Ring, Permission
from app.lib.redprint import Redprint
from app.model.project import Project
from app.schema.schema import ProjectSchema
from app.validator.form import CreateProjectForm

api = Redprint('project')


# 创建一个项目
@api.route('', methods=['POST'])
@auth.login_required
@Permission.require(Ring.Member)
def create_project():
    form = CreateProjectForm().execute_validate()
    result = Project.insert(form['name'], form['desc'])
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


# 获取项目列表
@api.route('/all', methods=['GET'])
def get_all_projects():
    projects = Project.fetch_all()
    project_schema = ProjectSchema(exclude=['desc', 'mock'])
    return jsonify([project_schema.dump(project).data for project in projects])
