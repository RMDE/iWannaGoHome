from app import create_app
from app.lib.error_code import ServerError
from app.lib.exception import APIException

app = create_app()


# 全局异常处理，Exception捕捉全部异常，有可能是ApiException, HttpException
@app.errorhandler(Exception)
def global_exception(e):
    if isinstance(e, APIException):
        return e
    from werkzeug.exceptions import HTTPException
    if isinstance(e, HTTPException):
        code = e.code
        msg = e.description + ' 🤭'
        return APIException(msg, code)
    else:
        if not app.config['DEBUG']:
            return ServerError()
        else:
            raise e


if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)
