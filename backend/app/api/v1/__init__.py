# -*- coding: utf-8 -*-
from flask import Blueprint

from . import user, token, mock


def create_bp_v1():
    endpoints = [user, token, mock]
    bp = Blueprint('v1', __name__, url_prefix='/v1')

    def register(m):
        m.api.register(bp)
        pass

    for ep in endpoints:
        register(ep)

    return bp
