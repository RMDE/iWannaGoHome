# -*- coding: utf-8 -*-
from app.lib.error_code import NotFound, ServerError
from flask_sqlalchemy import SQLAlchemy as _SQLAlchemy, BaseQuery
from contextlib import contextmanager
from flask_marshmallow import Marshmallow


class SQLAlchemy(_SQLAlchemy):
    @contextmanager
    def auto_commit(self):
        try:
            yield
            self.session.commit()
        except Exception as e:
            db.session.rollback()
            # raise e
            print(e)
            raise ServerError()


class Query(BaseQuery):
    def filter_by(self, **kwargs):
        if 'deleted' not in kwargs.keys():
            # 过滤被软删除的项
            kwargs['deleted'] = False
        return super(Query, self).filter_by(**kwargs)

    def get_or_404(self, ident, msg_404=None):
        rv = self.get(ident)
        if not rv:
            if msg_404:
                raise NotFound(msg=msg_404)
            else:
                raise NotFound()
        return rv

    def first_or_404(self, msg_404=None):
        rv = self.first()
        if not rv:
            if msg_404:
                raise NotFound(msg=msg_404)
            else:
                raise NotFound()
        return rv


db = SQLAlchemy(query_class=Query)
ma = Marshmallow()
