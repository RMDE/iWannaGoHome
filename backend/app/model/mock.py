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
    pid = Column(Integer, db.ForeignKey('project.id'), nullable=False)
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
    def insert(form):
        mock_name = form['name']
        # mock_uid = form['uid']
        mock_json = form['json']
        mock_uid = None
        mock_pid = None
        mock_form = None
        mock_desc = None
        if 'uid' in form:
            mock_pid = form['uid']
        elif 'email' in form:
            user = User.query.filter_by(email=form['email']).first()
            mock_uid = user.id
        if 'pid' in form:
            mock_pid = form['pid']
        elif 'project' in form:
            project = Project.query.filter_by(name=form['project']).first()
            mock_pid = project.id
        if 'form' in form:
            mock_form = form['form']
        if 'desc' in form:
            mock_desc = form['desc']
        try:
            with db.auto_commit():
                mock = Mock(name=mock_name, uid=mock_uid, json=mock_json, pid=mock_pid,
                            form=mock_form,
                            desc=mock_desc)
                db.session.add(mock)

        except IndentationError as e:
            print(e)
            return False
        return True
