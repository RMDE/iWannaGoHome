# -*- coding: utf-8 -*-
import functools


class Redprint:
    # 构造函数
    def __init__(self, name):
        self.name = name
        self.mound = []

    def route(self, rule, **options):
        def decorator(f):
            @functools.wraps(f)
            def wrapper(*args, **kwargs):
                self.mound.append((f, rule, options))
                return f(*args, **kwargs)

            return wrapper

        return decorator

    # 注册函数
    def register(self, bp, url_prefix=None):
        # 如果没有传入url_prefix则使用红图的名称作为URL前缀
        if url_prefix is None:
            url_prefix = '/' + self.name

        for f, rule, options in self.mound:
            # f.__name__是备用值，如果options中没有"endpoint"则使用
            endpoint = options.pop("endpoint", f.__name__)
            bp.add_url_rule(url_prefix + rule, endpoint, f, **options)
