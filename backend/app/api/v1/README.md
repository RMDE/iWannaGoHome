# Api

都是直接通过Http Status Code来反馈API请求结果状况

使用Http Basic Auth 作为用户身份认证，某些接口需要携带token访问

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

<details>
<summary>当邮箱和密码都正确时返回token</summary>

```json
status code = 200 
{
    "email": "admin@imhcl.cn",
    "token": "eyJ......"
}
```
</details>

<details>
<summary>当密码错误时返回</summary>

```json
status code = 401
{
    "msg": "authorization failed 👿",
    "request": "POST /v1/token"
}
```
</details>

<details>
<summary>当用户不存在</summary>

```json
status code = 404
{
    "msg": "用户不存在 🙄",
    "request": "POST /v1/token"
}
```
</details>

<details>
<summary>信息确实时略</summary>
</details>

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

<details>
<summary>当注册成功时</summary>

```json
status code = 200
{
    "msg": "ok 😆",
    "request": "POST /v1/user"
}
```
</details>


<details>
<summary>当请求数据不合要求</summary>

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
</details>


<details>
<summary>当邮注册用户箱重复时</summary>

```json
status code = 500
{
    "msg": "sorry, problems with database, this may happen when you insert conflicted or invalid data 😷",
    "request": "POST /v1/user"
}
```
</details>


### 提升用户权限

请求

> 只有管理员才能更改用户权限
>
> promotion 是权限级别提升数量，权限级别看 [permission.py](../../lib/permission.py)
>
> 请求时需要携带token

```
POST /v1/user/promote
Content-Disposition: form-data; name="email"
Content-Disposition: form-data; name="promotion"
```
返回

<details>
<summary>当请求成功时</summary>

```json
status code = 200
{
    "msg": "ok 😆",
    "request": "POST /v1/user/promote"
}
```
</details>



<details>
<summary>当非管理员请求这一操作时</summary>

```json
status code = 403
{
    "msg": "forbidden, not in scope 🤭",
    "request": "POST /v1/user/promote"
}
```
</details>
 


<details>
<summary>当promotion参数不合法时</summary>

```json
status code = 400
{
    "msg": "权限级别不在正常范围，请检查参数 😒",
    "request": "POST /v1/user/promote"
}
```
</details>


### 禁用用户

请求

> 需要参数email
> 需要携带token

```
DELETE /v1/user/email
```

## mock

mock 实质上就是接受一个json，保存到数据库中，然后按照特定的链接能返回之前定义的json

### 创建一个mock

请求
> email 为创建者邮箱
>
> name 为这个mock起一个名字
>
> json 就是一段json文本
>
> 请求时需要携带token


```
POST /v1/mock
Content-Disposition: form-data; name="email"
Content-Disposition: form-data; name="name"
Content-Disposition: form-data; name="json"
```
返回

### 获取mock列表

请求
> 列出所有mock的id、name、创建时间、修改时间

```
GET /v1/mock/all
```

返回

<details>
<summary>当操作成功时</summary>

```json
status code = 200
[
    {
        "create_time": "2019-07-22T12:31:11+00:00",
        "id": 1,
        "name": "test",
        "update_time": "2019-07-22T12:31:11+00:00",
        "user": 1
    },
    {
        "create_time": "2019-07-22T12:37:12+00:00",
        "id": 2,
        "name": "test again",
        "update_time": "2019-07-22T12:37:12+00:00",
        "user": 1
    }
]
```
</details>

### 删除一个mock

请求
> 传入需要删除的mock的id
>
> 请求时需要携带token
```
DELETE /v1/mock/id
```
返回

<details>
<summary>当操作成功时</summary>

```json
status code = 200
{
    "msg": "ok 😆",
    "request": "DELETE /v1/mock/1"
}
```
</details>
