import uvicorn
from fastapi import FastAPI

app = FastAPI(title="Web测试平台接口文档",
              description="FastAPi",
              version="0.0.1")

if __name__ == '__main__':
    uvicorn.run(app, host="0.0.0.0", prot=8000)
