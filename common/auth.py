"""
用于用户认证和权限校验的公共模块
依赖：
pip install passlib[bcrypt]
pip install pyjwt

key:47f8c9308ef27360a22a700636a68398e2d188d4a00b2673866306249d05485d
"""
from passlib.context import CryptContext
import jwt
import time
from common import settings

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def create_token(userinfo: dict):
    # 过期时间
    expire = time.time() + settings.TOKEN_TIMEOUT
    userinfo["exp"] = expire
    # 使用pyjwt生成token
    return jwt.encode(userinfo, settings.SECRET_KEY, algorithm=settings.ALGORITHM)


def verify_token(token):
    """校验token"""
    try:
        data = jwt.decode(token, settings.SECRET_KEY, algorithms=[settings.ALGORITHM])
        return data
    except jwt.ExpiredSignatureError:
        return None


def verify_password(plain_password, hashed_password):
    """
    验证密码是否正确
    :param plain_password: 明文密码
    :param hashed_password: 加密后的密码
    :return: 验证结果
    """

    return pwd_context.verify(plain_password, hashed_password)


def get_password_hash(password):
    """
    获取密码的哈希值
    :param password: 明文密码
    :return: 加密后的密码
    """

    return pwd_context.hash(password)
