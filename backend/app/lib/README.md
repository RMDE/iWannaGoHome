- `auth.py` Http Basic Auth 验证
- `exception.py` ApiException类，继承自Flask内置的HttpException，返回API 异常信息
  - `error_code.py` 继承自 ApiException，定义不同错误类别
- `orm.py` 关系映射
- `permission.py` 用户权限等级验证，类似CPU Ring Privilege，数值越小权限越大，主要是定义一个装饰器

- `redprint.py` 定义路由

