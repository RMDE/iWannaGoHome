# -*- coding: utf-8 -*-
from app.lib.exception import APIException


class Success(APIException):
    code = 200
    msg = 'ok 😆'


class DeleteSuccess(Success):
    code = 201


class ServerError(APIException):
    code = 500
    msg = 'sorry, we made a mistake 😁'


class ParameterException(APIException):
    code = 400
    msg = 'invalid parameter 😒'


class NotFound(APIException):
    code = 404
    msg = 'the resource are not found 🙄'


class DatabaseExistError(APIException):
    code = 400
    msg = 'same data exists 🤔'


class AuthFailed(APIException):
    code = 401
    msg = 'authorization failed 👿'


class Forbidden(APIException):
    code = 403
    msg = 'forbidden, not in scope 🤭'


class PostMethodOnly(APIException):
    code = 405
    msg = 'only post method is allowed 😩'


class CodeError(APIException):
    code = 555
    msg = 'code has fatal errors 😭'
