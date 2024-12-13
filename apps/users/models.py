from tortoise import models, fields


class Users(models.Model):
    id = fields.IntField(pk=True, auto_increment=True, description="用户id")
    username = fields.CharField(max_length=255, description="用户名")
    password = fields.CharField(max_length=255, description="密码")
    email = fields.CharField(max_length=255, description="邮箱", default="")
    mobile = fields.CharField(max_length=255, description="手机号", default="")
    is_active = fields.BooleanField(default=True, description="是否激活")
    is_superuser = fields.BooleanField(default=False, description="是否超级管理员")
    created_at = fields.DatetimeField(auto_now=True, description="创建时间")
