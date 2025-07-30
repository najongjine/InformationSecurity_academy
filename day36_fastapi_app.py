"""
파이썬 서버를 application(돈거래, 데이터 적재) 이런게 안쓰는이유
1. 설치해야할 모듈들이 너무 많고, 표준화 되지도 않음
2. 간단한 SELECT 코드도 직관이지 않고 어려움.
   특히 데이터가 어떻게 생겼는지 알려주질 않으니,
   GPT랑 에러 안나는 코드 찾을때까지 어마어마한 노가다가 들어감
3. AI module 들이 무거우니, CI/CD 가 안됨.
   CI/CD 뜻: 서버 점검 없이 재시작 1초만에 끝

실전에선
[SpringBoot, .NetCore, Nodejs]
얘네들이 마스터 서버가 되서, DB 관리, 사용자 요청 처리
왠만한거 다 하고, 특수 AI 기능만, 파이썬 서버와 소통해요


pip install fastapi
pip install "uvicorn[standard]"
pip install sqlalchemy psycopg2 
pip install sqlalchemy psycopg2-binary
pip install sqlacodegen
pip install orjson
"""
from fastapi import FastAPI, Depends
import uvicorn
from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker, Session
from fastapi.responses import JSONResponse
from fastapi.responses import ORJSONResponse
from fastapi import Request


# ✅ DB 접속 정보
DATABASE_URL = "postgresql://postgres:aaaa@localhost:5432/t_test1"

# ✅ SQLAlchemy 엔진/세션 설정
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# ✅ FastAPI 앱
app = FastAPI()

# ✅ DB 세션을 의존성으로 주입
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# ✅ 실제 라우터
@app.get("/raw")
def read_raw_query(db: Session = Depends(get_db)):
    result = db.execute(text("SELECT * FROM t_test1"))
    rows = result.mappings().all()
    return [dict(row) for row in rows]  # ✅ orjson이 datetime도 자동 처리

# ✅ INSERT 라우터
@app.post("/raw-insert2")
async def insert_raw_alt(req: Request, db: Session = Depends(get_db)):
    body = await req.json()  # 👈 Hono 스타일
    print(body)  # dict로 나옴: {"name": "홍길동", "age": 25, ...}

    query = text("""
        INSERT INTO t_test1 (name, age, created_at)
        VALUES (:name, :age, :created_at)
    """)
    db.execute(query, body)  # ✅ 바로 dict로 넘김
    db.commit()
    return {"message": "Insert successful"}

# ✅ 실행
if __name__ == "__main__":
    uvicorn.run("app:app", host="0.0.0.0", port=8000, reload=True)
