from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI
from app.routers import slang, comic
from dotenv import load_dotenv

load_dotenv()
app = FastAPI()

# 🔥 CORS 설정 추가
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],  # 프론트엔드 주소
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(slang.router, prefix="/slang")
app.include_router(comic.router, prefix="/comic")

# @app.get("/")
# def read_root():
#   return{"message": "🎉 Welcome to JULMAR API!"}