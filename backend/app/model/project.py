# -*- coding: utf-8 -*-
from datetime import datetime

from sqlalchemy import Column, Integer, Text, String

from app.lib.orm import db
from app.model.base import Base


class Project(Base):
    id = Column(Integer, primary_key=True)
    name = Column(String(64), nullable=True, unique=True)
    mocks = db.relationship('Mock', backref=db.backref('project', lazy="joined"), lazy='joined')
    desc = Column(Text)
    markdown = Column(Text)

    # GET
    @staticmethod
    def fetch_project(project_id):
        project = Project.query.filter_by(id=project_id).first_or_404()
        return project

    # UPDATE
    @staticmethod
    def update_project(project_id, form):
        project = Project.query.filter_by(id=project_id).first_or_404()
        new_project_name = None
        new_project_desc = None
        new_project_markdown = None
        if 'name' in form:
            new_project_name = form['name']
        if 'desc' in form:
            new_project_desc = form['desc']
        if 'markdown' in form:
            new_project_markdown = form['markdown']
        try:
            with db.auto_commit():
                if new_project_name:
                    project.name = new_project_name
                if new_project_desc:
                    project.desc = new_project_desc
                if new_project_markdown:
                    project.markdown = new_project_markdown
                # 更新时间
                project.update_time = datetime.now()
        except IndentationError as e:
            print(e)
            return False
        return True

    # CREATE
    @staticmethod
    def insert(form):
        try:
            with db.auto_commit():
                project = Project(name=form['name'])
                if 'desc' in form:
                    project.desc = form['desc']
                if 'markdown' in form:
                    project.markdown = form['markdown']
                db.session.add(project)
        except IndentationError as e:
            print(e)
            return False
        return True
