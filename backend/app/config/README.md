`secure.py`

涉及到数据库信息

```python
# -*- coding: utf-8 -*-

# 数据库连接地址
SQLALCHEMY_DATABASE_URI = 'mysql+cymysql://[user_name]:[password]@[host]/[database_name]'

# Flask 密钥
SECRET_KEY = b'C\xbb\xb0\x80\xcc<\xa6:Z\xa8\xe4\x0f\xdc<\x1d\x86=\xd3u\xcfg\x1aZ\x89'
```

emoji支持：

```
SQLALCHEMY_DATABASE_URI='mysql+cymysql://[user_name]:[password]@[host]/[database_name]?charset=utf8mb4'
```