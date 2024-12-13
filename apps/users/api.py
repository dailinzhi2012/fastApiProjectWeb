from fastapi import APIRouter, HTTPException
from apps.users.schemas import RegisterForm, UserInfoSchema, LoginForm
from apps.users.models import Users
from common import auth

router = APIRouter(prefix="/api/users")


@router.post("/register", tags=["用户管理"], summary="用户注册", response_model=UserInfoSchema)
def register(item: RegisterForm):
    if item.password != item.password_confirm:
        raise HTTPException(status_code=422, detail="两次密码输入不一致")
    # 校验用户名是否存在
    if Users.objects(username=item.username).first():
        raise HTTPException(status_code=422, detail="用户名已存在")
    # 校验邮箱是否存在
    if Users.objects(email=item.email).first():
        raise HTTPException(status_code=422, detail="邮箱已存在")
    # 校验手机号是否存在
    if Users.objects(mobile=item.mobile).first():
        raise HTTPException(status_code=422, detail="手机号已存在")
    # 创建用户
    user = Users.create(
        username=item.username,
        password=auth.get_password_hash(item.password),
        email=item.email,
        mobile=item.mobile,
        nickname=item.nickname,
    )
    return UserInfoSchema(**user.__dict__)


@router.post("/register", tags=["用户管理"], summary="用户登录", response_model=LoginSchema)
async def login(item: LoginForm):
    """登录的逻辑"""


    user = await Users.get_or_none(username=item.username)
    if not user:
        raise HTTPException(status_code=422, detail="用户名或密码错误")
    if not auth.verify_password(item.password, user.password):
        raise HTTPException(status_code=422, detail="用户名或密码错误")
    uinfo = UserInfoSchema(**user.__dict__)
    # 账号名密码正确，生成token
    user.token = auth.create_access_token(user.id)
    return UserInfoSchema(**user.__dict__)
