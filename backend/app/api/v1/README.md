# Api
[TOC]



## token

用户登录时获取token，token是用户邮箱email和权限范围scope组成的字典加密后的结果

此token用与在执行敏感操作时判别用户权限

 请求：

```
POST /v1/token

Receive:
Content-Disposition: form-data; name="email"
Content-Disposition: form-data; name="password"
```

返回：

> 当邮箱和密码都正确时返回toekn

```json
status code = 200 
{
    "email": "admin@imhcl.cn",
    "token": "eyJ......"
}
```

>  当密码错误时返回

```json
status code = 401
{
    "msg": "authorization failed 👿",
    "request": "POST /v1/token"
}
```

> 当用户不存在

```json
status code = 404
{
    "msg": "用户不存在 🙄",
    "request": "POST /v1/token"
}
```

> 信息缺失时略

## user

注册用户、提升用户级别权限

### 注册用户

请求：

密码长度应为8-32或密码包含不可用字符

```
POST /v1/user
Content-Disposition: form-data; name="email"
Content-Disposition: form-data; name="password"
```

返回

> 当注册成功时

```json
status code = 200
{
    "msg": "ok 😆",
    "request": "POST /v1/user"
}
```

> 当请求数据不合要求

```json
status code = 400
{
    "msg": {
        "password": [
            "密码长度应为8-32或密码包含不可用字符"
        ]
    },
    "request": "POST /v1/user"
}
```

> 当邮注册用户箱重复时

```json
status code = 500
{
    "msg": "sorry, problems with database, this may happen when you insert conflicted or invalid data 😷",
    "request": "POST /v1/user"
}
```

### 提升用户权限

请求

> 只有管理员才能更改用户权限
>
> promotion 是权限级别提升数量，权限级别看 [permission.py](../../lib/permission.py)

```
POST /v1/user/promote
Content-Disposition: form-data; name="email"
Content-Disposition: form-data; name="promotion"
```
返回

> 当请求成功时

```json
status code = 200
{
    "msg": "ok 😆",
    "request": "POST /v1/user/promote"
}
```

> 当非管理员请求这一操作时

```json
status code = 403
{
    "msg": "forbidden, not in scope 🤭",
    "request": "POST /v1/user/promote"
}
```

> 当promotion参数不合法时

```json
status code = 400
{
    "msg": "权限级别不在正常范围，请检查参数 😒",
    "request": "POST /v1/user/promote"
}
```



