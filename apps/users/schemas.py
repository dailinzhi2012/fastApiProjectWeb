from dataclasses import Field

from pydantic import BaseModel


class LoginForm(BaseModel):
    username: str = Field(description="用户名", min_length=6, max_length=20)
    password: str = Field(description="密码", min_length=6, max_length=10)

class RegisterForm (BaseModel):
    confirm_password: str = Field(description="确认密码", min_length=6, max_length=10)
    email: str = Field(defalt="", description="邮箱")
    nickname: str = Field(default="", description="昵称")
    mobile: str = Field(default="", description="手机号")


class UserInfoSchema(BaseModel):
    id: int = Field(description="用户ID")
    username: str = Field(description="用户名")
    email: str = Field(description="邮箱")
    nickname: str = Field(description="昵称")
    mobile: str = Field(description="手机号")
    is_active: bool = Field(description="是否激活")
    is_superuser: bool = Field(description="是否超级管理员")
