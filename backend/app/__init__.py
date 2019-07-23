# -*- coding: utf-8 -*-

from flask import Flask
from flask_cors import CORS

from app.api.v1 import create_bp_v1


# 路由
def register_blueprints(app):
    app.register_blueprint(create_bp_v1())


# 数据库
# http://docs.jinkan.org/docs/flask/patterns/sqlalchemy.html
def register_db(app):
    from app.lib.orm import db
    db.init_app(app)
    with app.app_context():
        db.create_all()


# 序列化
# https://flask-marshmallow.readthedocs.io/en/latest/
def register_serializer(app):
    from app.lib.orm import ma
    ma.init_app(app)


def create_app():
    app = Flask(__name__)
    app.config.from_object('app.config.setting')
    app.config.from_object('app.config.secure')
    # 跨域资源访问配置
    CORS(app, resources={r"/v1/*": {"origins": "*"}})
    register_blueprints(app)
    register_db(app)
    register_serializer(app)
    return app
