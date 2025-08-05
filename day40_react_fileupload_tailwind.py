"""

"""

CREATE TABLE t_files (
    id SERIAL PRIMARY KEY,                  -- 고유 ID
    original_name VARCHAR DEFAULT '',            -- 업로드 당시 파일 이름
    stored_name VARCHAR DEFAULT '',              -- 디스크에 저장된 파일 이름 (UUID 등으로 저장)
    file_path VARCHAR DEFAULT '',                -- 파일 경로 (서버 내 절대경로 또는 상대경로)
    mime_type VARCHAR DEFAULT '',                         -- 파일 형식 (예: image/png)
    file_size BIGINT DEFAULT 0,                       -- 파일 크기 (바이트 단위)
    created_at TIMESTAMP DEFAULT NOW()    -- 업로드 시간
);