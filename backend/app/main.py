from fastapi import FastAPI
from model import TestUserTable, TestUser
from db import session
from starlette.middleware.cors import CORSMiddleware  # CORSを回避するために必要
import uvicorn

app = FastAPI()

# CORSを回避するために設定
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


#　ユーザー情報一覧取得
@app.get("/api/test_users")
def get_user_list():
    users = session.query(TestUserTable).all()
    return users


# ユーザー情報取得(id指定)
@app.get("/api/test_users/{user_id}")
def get_user(user_id: int):
    user = session.query(TestUserTable).\
        filter(TestUserTable.id == user_id).first()
    return user


# ユーザ情報登録
@app.post("/api/test_users")
def post_user(user: TestUser):
    db_test_user = TestUser(name=user.name,email=user.email)
    session.add(db_test_user)
    session.commit()


# ユーザ情報更新
@app.put("/api/test_users/{user_id}")
def put_users(user: TestUser, user_id: int):
    target_user = session.query(TestUserTable).\
        filter(TestUserTable.id == user_id).first()
    target_user.name = user.name
    target_user.email = user.email
    session.commit()

@app.get("/api/hoge")
def index1():
    return {"message": "hogehoge"}
