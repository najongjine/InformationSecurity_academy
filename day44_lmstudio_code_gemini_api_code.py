"""
Docker - 
가상 윈도우
uv, venv, conda도 GPU 사용 모듈들을 설치해서 쓸때 한계가 옴
CUDA 버전 셋팅까지 건들수가 없기 때문
그러면 결국 파이썬 버전 하나와, pip install 로 가야하는데,
서버 하나에다가 파이썬이랑 모듈들을 고정 시켜버리면,
다른 서비스나 모듈을 사용 못하는 문제가 생김.

그래서 복잡하더라도, 가상 OS를 도입 해야하는데,
그게 바로 도커.
쉽게 말하면 컴퓨터 하나 안에 리눅스 10~1000개 셋팅 가능
각각의 가상 OS는 서로를 침범하지 않음

그리고 많은 기업들이 docker를 쓰는 이유가, OS 자체를 업로드 할수도 있고
download 해서 고대로 딸깍 실행 가능


LMstudio, ollama, **vllm** -
얘네들은 뭐냐면, 오픈소스 llm 을 쉽게 서버화 해주는 도구
실무에서는 vllm을 많이 쓴다고 합니다.
왜냐면, vllm은 멀티 GPU가 있을경우, 알아서 멀티 GPU로 실행을 해준다고 합니다
vllm도 lmstudio 처럼, 오픈소스 llm을 쉽게 서버화 시켜줘요
"""

"""
LLM 파인튜닝 -

1. PEFT-
기존 LLM 모델은 고대로 뉍두고, 일부 레이어만 학습시켜서 모델 위에
덧붙이기


2. RAG-
[시스템]
너는 내 회사 상담 봇이야. 내 회사에 관련된것만 질문을 답변해줘야되

[문서]
-쥐약
-뱀약

[사용자 질문]
저희집에 뱀이 많아요
"""

"""
https://colab.research.google.com/drive/1gSK_TtWOnu8INomqqsuMQZNzzYCszvAO?usp=sharing
- PEFT 예제 코드

결과는 참담하게 실패.

1. 모델의 한계. 기본 모델이 안좋으면, 학습도 개판이됨
2. 좋은 모델을 돌릴려면 결국 GPU가 받쳐주고, colab이 아닌곳에서 실행 해야함

실무에서는 unsloth 라는놈을 이용해서 파인튜닝을 한대요
"""

"""
-- 1. 카테고리 테이블 생성
CREATE TABLE t_category (
    id SERIAL PRIMARY KEY,             -- 카테고리 ID (자동 증가)
    category_name VARCHAR(100) NOT NULL -- 카테고리 이름
);

-- 2. 상품 테이블 생성
CREATE TABLE t_product (
    id SERIAL PRIMARY KEY,             -- 상품 ID (자동 증가)
    product_name VARCHAR(200) NOT NULL, -- 상품 이름
    category_id INT NOT NULL,           -- 카테고리 ID (FK)
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- 생성일
    description TEXT,                   -- 상품 설명
    CONSTRAINT fk_category
        FOREIGN KEY (category_id)
        REFERENCES t_category (id)
        ON UPDATE CASCADE
        ON DELETE RESTRICT
);

https://colab.research.google.com/drive/1CwGNcVS3gAzHZ_vmdbOa64SQ6TKdOMc1?usp=sharing
"""