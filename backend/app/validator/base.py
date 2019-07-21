# -*- coding: utf-8 -*-
from flask import request
from wtforms import Form
from werkzeug.datastructures import ImmutableMultiDict
from app.lib.error_code import ParameterException, PostMethodOnly


class BaseForm(Form):
    # 保存请求参数
    data = {}

    def __init__(self):
        self.data = request.get_json(silent=True)
        if self.data is None:
            self.data = request.form
        self.args = request.args.to_dict()
        super(BaseForm, self).__init__(data=self.data, **self.args)

    # 执行验证，验证输入信息是否符合要求
    def execute_validate(self):
        valid = super(BaseForm, self).validate()
        if not valid:
            # 参数错误
            raise ParameterException(msg=self.errors)
        return self.to_dict()

    # 将data转为dict，只有POST请求才有用
    def to_dict(self):
        if not self.data:
            raise PostMethodOnly()
        if isinstance(self.data, ImmutableMultiDict):
            return self.data.to_dict()
        else:
            return self.data
