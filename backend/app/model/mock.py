# -*- coding: utf-8 -*-
from sqlalchemy import Column, Integer, Text, String

from app.lib.orm import db
from app.model.base import Base


class Mock(Base):
    id = Column(Integer, primary_key=True)
    name = Column(Text)
    json = Column(Text)
    # 创建者
    user_email = Column(String(32), db.ForeignKey('user.email'), nullable=False)
    # 所属项目
    project_name = Column(String(64), db.ForeignKey('project.name'))
    # 图表的形式
    form = Column(String(32))
    # 描述
    desc = Column(Text)

    @staticmethod
    def fetch_mock(mock_id):
        mock = Mock.query.filter_by(id=mock_id).first_or_404()
        return mock

    @staticmethod
    def fetch_json(mock_id):
        mock = Mock.query.filter_by(id=mock_id).first_or_404()
        return mock.json

    @staticmethod
    def insert(form):
        mock_name = form['name']
        mock_email = form['email']
        mock_json = form['json']
        mock_project = None
        mock_form = None
        mock_desc = None
        if 'project' in form:
            mock_project = form['project']
        if 'form' in form:
            mock_form = form['form']
        if 'desc' in form:
            mock_desc = form['desc']
        try:
            with db.auto_commit():
                mock = Mock(name=mock_name, user_email=mock_email, json=mock_json, project_name=mock_project,
                            form=mock_form,
                            desc=mock_desc)
                db.session.add(mock)

        except IndentationError as e:
            print(e)
            return False
        return True
