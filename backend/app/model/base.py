# -*- coding: utf-8 -*-
from cymysql.err import ProgrammingError
from datetime import datetime
from sqlalchemy import Column, DateTime, Boolean

from app.lib.orm import db
from app.lib.error_code import NotFound, DatabaseError


class Base(db.Model):
    __abstract__ = True

    # 创建时间
    create_time = Column(DateTime, default=datetime.now(), nullable=False)
    # 更新时间
    update_time = Column(DateTime, default=datetime.now(), onupdate=datetime.now(), nullable=False)
    # 软删除
    deleted = Column(Boolean, default=False)

    @classmethod
    def delete(cls, key, value):
        table_name = cls.__name__.lower()
        sql = "update {} set deleted=1 where {} = {}".format(table_name, key, value)
        if not isinstance(value, int):
            sql = "update {} set deleted=1 where {} = '{}'".format(table_name, key, value)
        try:
            with db.auto_commit():
                db.session.execute(sql)
        except ProgrammingError as e:
            print(e)
            return DatabaseError()

    @classmethod
    def fetch_all(cls, **kwargs):
        all = cls.query.filter_by(**kwargs).all()
        if not all:
            raise NotFound()
        return all
