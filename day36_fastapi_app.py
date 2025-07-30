"""
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

# ✅ 실행
if __name__ == "__main__":
    uvicorn.run("app:app", host="0.0.0.0", port=8000, reload=True)
