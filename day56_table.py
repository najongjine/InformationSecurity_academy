"""
CREATE TABLE t_plants (
  id SERIAL PRIMARY KEY,                          -- 고유 식별자
  name VARCHAR(100) NOT NULL,                     -- 식물 이름 (예: 몬스테라)

  sunlight TEXT DEFAULT '',                                  -- 햇빛 / 조도 (예: 간접광, 직사광선 X)
  watering TEXT DEFAULT '',                                  -- 물주기 (예: 흙 2~3cm 마르면 관수)
  temperature TEXT DEFAULT '',                               -- 온도 (예: 18~27도, 15도 이하 주의)
  humidity TEXT DEFAULT '',                                  -- 습도 (예: 중간~높음 / 40~70%)
  soil TEXT DEFAULT '',                                      -- 토양 (예: 배수성 좋은 피트 + 펄라이트)
  fertilizer TEXT DEFAULT '',                                -- 비료 (예: 4주 간격 액체비료)
  repotting TEXT DEFAULT '',                                 -- 분갈이 (예: 2년에 1회, 봄)

  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

"""