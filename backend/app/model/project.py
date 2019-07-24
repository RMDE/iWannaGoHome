# -*- coding: utf-8 -*-
from sqlalchemy import Column, Integer, Text, String

from app.lib.orm import db
from app.model.base import Base


class Project(Base):
    id = Column(Integer, primary_key=True)
    name = Column(String(64), nullable=True, unique=True)
    mocks = db.relationship('Mock', backref='project', lazy='dynamic')
    desc = Column(Text)

    @staticmethod
    def fetch_project(project_id):
        project = Project.query.filter_by(id=project_id).first_or_404()
        return project

    @staticmethod
    def insert(project_name, project_desc):
        try:
            with db.auto_commit():
                project = Project(name=project_name, desc=project_desc)
                db.session.add(project)
        except IndentationError as e:
            print(e)
            return False
        return True
