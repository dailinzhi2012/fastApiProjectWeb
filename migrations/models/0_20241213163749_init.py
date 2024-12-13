from tortoise import BaseDBAsyncClient


async def upgrade(db: BaseDBAsyncClient) -> str:
    return """
        CREATE TABLE IF NOT EXISTS `aerich` (
    `id` INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
    `version` VARCHAR(255) NOT NULL,
    `app` VARCHAR(100) NOT NULL,
    `content` JSON NOT NULL
) CHARACTER SET utf8mb4;
CREATE TABLE IF NOT EXISTS `users` (
    `id` INT NOT NULL PRIMARY KEY AUTO_INCREMENT COMMENT '用户id',
    `username` VARCHAR(255) NOT NULL  COMMENT '用户名',
    `password` VARCHAR(255) NOT NULL  COMMENT '密码',
    `nickname` VARCHAR(255) NOT NULL  COMMENT '昵称' DEFAULT '',
    `email` VARCHAR(255) NOT NULL  COMMENT '邮箱' DEFAULT '',
    `mobile` VARCHAR(255) NOT NULL  COMMENT '手机号' DEFAULT '',
    `is_active` BOOL NOT NULL  COMMENT '是否激活' DEFAULT 1,
    `is_superuser` BOOL NOT NULL  COMMENT '是否超级管理员' DEFAULT 0,
    `created_at` DATETIME(6) NOT NULL  COMMENT '创建时间' DEFAULT CURRENT_TIMESTAMP(6) ON UPDATE CURRENT_TIMESTAMP(6)
) CHARACTER SET utf8mb4 COMMENT='用户表';"""


async def downgrade(db: BaseDBAsyncClient) -> str:
    return """
        """
