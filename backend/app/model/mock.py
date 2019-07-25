# -*- coding: utf-8 -*-
from sqlalchemy import Column, Integer, Text, String, Enum

from app.lib.orm import db
from app.model.base import Base
from app.model.project import Project
from app.model.user import User


class Mock(Base):
    id = Column(Integer, primary_key=True)
    name = Column(Text)
    json = Column(Text)
    # 创建者
    uid = Column(Integer, db.ForeignKey('user.id'), nullable=False)
    # 所属项目
    pid = Column(Integer, db.ForeignKey('project.id'), nullable=True)
    # 图表的形式
    form = Column(String(32))
    # 描述
    desc = Column(Text)
    # 状态
    status = Column(Enum('abandoned', 'adopted', 'unresolved'), default='unresolved')

    @staticmethod
    def fetch_mock(mock_id):
        mock = Mock.query.filter_by(id=mock_id).first_or_404()
        return mock

    @staticmethod
    def fetch_json(mock_id):
        mock = Mock.query.filter_by(id=mock_id).first_or_404()
        return mock.json

    @staticmethod
    def update_mock(mock_id, form):
        mock = Mock.query.filter_by(id=mock_id).first_or_404()
        try:
            with db.auto_commit():
                def replace(key):
                    if key in form:
                        setattr(mock, key, form[key])

                to_replace = ['name', 'json', 'pid', 'form', 'desc']

                for item in to_replace:
                    replace(item)

                if 'project' in form:
                    project = Project.query.filter_by(name=form['project']).first()
                    mock.pid = project.id
        except IndentationError as e:
            print(e)
            return False
        return True

    @staticmethod
    def abandon(mock_id):
        mock = Mock.query.filter_by(id=mock_id).first_or_404()
        try:
            with db.auto_commit():
                mock.status = 'abandoned'
                mock.pid = None
        except IndentationError as e:
            print(e)
            return False
        return True

    @staticmethod
    def insert(form):
        try:
            with db.auto_commit():
                mock = Mock()

                def to_set(key):
                    if key in form:
                        setattr(mock, key, form[key])

                need_set = ['name', 'uid', 'pid', 'json', 'desc', 'form']

                for item in need_set:
                    to_set(item)

                if 'email' in form:
                    user = User.query.filter_by(email=form['email']).first()
                    mock.uid = user.id

                if 'project' in form:
                    project = Project.query.filter_by(name=form['project']).first()
                    mock.pid = project.id

                db.session.add(mock)

        except IndentationError as e:
            print(e)
            return False
        return True
