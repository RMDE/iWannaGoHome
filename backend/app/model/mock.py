# -*- coding: utf-8 -*-
from sqlalchemy import Column, Integer, Text, String

from app.lib.orm import db
from app.model.base import Base


class Mock(Base):
    id = Column(Integer, primary_key=True)
    name = Column(Text)
    json = Column(Text)
    creator = Column(String(32), db.ForeignKey('user.email'), nullable=False)

    @staticmethod
    def fetch_json(mock_id):
        mock = Mock.query.filter_by(id=mock_id).first_or_404()
        return mock.json

    @staticmethod
    def insert(mock_name, mock_creator, mock_json):
        try:
            with db.auto_commit():
                mock = Mock(name=mock_name, creator=mock_creator, json=mock_json)
                db.session.add(mock)

        except IndentationError as e:
            print(e)
            return False
        return True
