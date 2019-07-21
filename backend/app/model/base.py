# -*- coding: utf-8 -*-
from datetime import datetime
from sqlalchemy import Column, DateTime, Boolean

from app.lib.orm import db


class Base(db.Model):
    __abstract__ = True

    # 创建时间
    create_time = Column(DateTime, default=datetime.now(), nullable=False)
    # 更新时间
    update_time = Column(DateTime, default=datetime.now(), onupdate=datetime.now(), nullable=False)
    # 软删除
    deleted = Column(Boolean, default=False)
    pass
