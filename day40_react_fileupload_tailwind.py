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

"""
## images: [
  File {
    size: 2502,       
    type: 'image/png',
    name: '4.png',
    lastModified: 1754371016609
  },
  File {
    size: 3268,
    type: 'image/png',
    name: '8_black.png',
    lastModified: 1754371016610
  }
]
## imageUrlList:  [
  {
    original_name: '4.png',
    stored_name: '9d98d25a-1a42-4b2c-8e61-88b6536b294c.png',
    file_path: 'C:\\Users\\itg\\Documents\\Hono\\Hono_test1_academy\\uploads\\9d98d25a-1a42-4b2c-8e61-88b6536b294c.png',
    mime_type: 'image/png',
    file_size: 2502
  },
  {
    original_name: '8_black.png',
    stored_name: '59db7d34-b6e3-4bcd-86e3-5aea547751c2.png',
    file_path: 'C:\\Users\\itg\\Documents\\Hono\\Hono_test1_academy\\uploads\\59db7d34-b6e3-4bcd-86e3-5aea547751c2.png',
    mime_type: 'image/png',
    file_size: 3268
  }
]
"""