"""
RAG - LLM 모델을 파인튜닝 없이, 나만의 에이전트 상담원으로 변신 시켜주는 기술

1️⃣ GPT (Generative Pre-trained Transformer)
풀네임: Generative Pre-trained Transformer

한 줄 정의:
“미리 공부한(Pre-trained) Transformer 구조의 글 생성기(Generative)”

핵심 포인트:

Generative → 글, 코드, 시, 소설, 요약… 무언가를 “만들어내는” 능력

Pre-trained → 이미 엄청난 양의 텍스트를 학습해서 기초 지식을 갖춤

Transformer → 아래에서 배울, GPT의 뇌 구조

📌 예시

GPT-2, GPT-3, GPT-4 … 전부 Transformer를 뼈대로 만들어진 "글 쓰는 AI"

GPT는 Transformer의 특정 활용 버전이라고 생각하면 됨.

2️⃣ Transformer (트랜스포머)
한 줄 정의:
“문장을 한 번에 보고, 중요한 단어끼리 연결해서 의미를 이해하는 뇌 구조”

개발 배경:
예전 AI는 글을 왼쪽→오른쪽 순서로 하나씩 읽어서 멀리 떨어진 단어 관계를 잘 못 찾았어요.
Transformer는 "Self-Attention" 이라는 기술로
👉 “이 문장에서 어떤 단어가 서로 중요한 관계인지” 한 번에 계산해요.

📌 예시

“나는 사과를 먹었는데, 그것이 달았다.”

‘그것’이 ‘사과’랑 연결된다는 걸 멀리 떨어져 있어도 찾아냄.

💡 Transformer 구조는 문장을 **벡터(숫자)**로 바꾸고,
그 숫자들을 서로 비교해서 “이 단어가 저 단어와 얼마나 관련 있는지”를 계산해요.
이게 Attention 메커니즘이고, GPT의 핵심 뇌.

3️⃣ LLM (Large Language Model)
한 줄 정의:
“엄청나게 큰 Transformer 기반 언어 모델”

LLM은 그냥 Transformer를 엄청 크게 만든 버전이에요.
→ 파라미터(뉴런 연결선) 수가 수십억~수천억 개
→ 덕분에 인간처럼 다양한 주제의 글을 이해하고 생성 가능.

Transformer (기술, 뇌 구조)
   ↓
GPT (Transformer 기반으로 만든 생성형 AI)
   ↓
GPT-3, GPT-4 → LLM (매우 큰 GPT)



그러면 LLM은 사용자 질문을 다 기억해?

아니요. LLM 자체가 질문을 “다 기억”하는 건 아닙니다.
대화에서 기억처럼 보이는 건 사실 모델이 아니라, 
애플리케이션(챗봇 프로그램) 쪽에서 해주는 거예요.

📌 구조적으로 보면
LLM의 기본 동작

LLM은 입력 받은 텍스트를 "현재 프롬프트" 안에서만 이해합니다.

이전 대화 내용을 기억하려면, 이전 대화 내용도 매번 같이 보내줘야 해요.

즉, 대화 히스토리는 모델 속에 저장되지 않음
(학습이 아니라, 매번 입력으로 주는 것)

컨텍스트(Context)

LLM은 "한 번에 볼 수 있는 글 길이"가 정해져 있어요.
예: GPT-4 Turbo → 128k 토큰, GPT-3.5 → 16k 토큰

이 범위 안에 들어있는 내용만 기억하고, 범위를 넘으면 예전 내용이 잘립니다.

진짜 ‘기억’처럼 만들려면

앱 개발자가 이전 대화를 DB나 파일에 저장

사용자가 질문할 때, 관련된 과거 대화를 찾아서 LLM 입력에 붙임
→ 이게 RAG나 대화 메모리 관리 기술

💡 정리

LLM 자체 = 기억 없음. 오직 현재 입력(프롬프트)만 봄.

"대화를 기억하는 것처럼" 보이는 건 → 앱이 과거 기록을 계속 전달해주기 때문.

오래된 대화가 잘리는 이유 → 컨텍스트 길이 제한 때문.
"""

"""
UV 환경셋팅으로 새로운 프로젝트 만들기 예시:

pip install uv

uv init myproject

uv python install 3.10
uv python pin 3.10
uv venv --python 3.10

uv run python -V

uv pip install lmstudio

uv run python main.py
"""