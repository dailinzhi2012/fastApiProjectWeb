import uvicorn
from fastapi import FastAPI
from tortoise.contrib.fastapi import register_tortoise

from common import settings

app = FastAPI(title="Web测试平台接口文档",
              description="FastAPi",
              version="0.0.1")




# 注册ORM模型
register_tortoise(app,
                  config=settings.TORTOISE_ORM,
                  modules={"models": ["models"]}
                  )

if __name__ == '__main__':
    uvicorn.run(app, host="0.0.0.0", prot=8000)
