# 数据库配置
DATABASE = {
    "host": "127.0.0.1",
    "port": 3306,
    "user": "root",
    "password": "root",
    "database": "webtest01"
}
# 项目中的所有应用的models
INSTALLED_APPS = [
    "apps.users.models",
    'apps.projects.models'
]
#  tortoise的基本配置
TORTOISE_ORM = {
    "connections": {
        "default": {
            "engine": "tortoise.backends.mysql",
            "credentials": DATABASE
        },
    },
    "apps": {
        "models": {
            "models": ["aerich.models", *INSTALLED_APPS],
            "default_connection": "default",
        },
    },
}


# ======================token配置========================
# 64位秘钥
SECRET_KEY = "47f8c9308ef27360a22a700636a68398e2d188d4a00b2673866306249d05485d"
# 加密算法
ALGORITHM = "HS256"
# token过期时间
TOKEN_TIMEOUT = 60 * 60 * 24 * 7  # 7天