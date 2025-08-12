"""
https://colab.research.google.com/drive/1wi0tV1whDlU1FH2bNZ5P3P_NkkHQPY-U
- gpt-oss-20b 파인튜닝 colab 코드

https://colab.research.google.com/drive/1lOjq8E0Iihl3JfB1QieO4dbow9VnqpfJ?usp=sharing
- gpt-oss-20b 사용예제 colab 코드(T4 에선 메모리 이슈로 안돌아감)

https://colab.research.google.com/drive/1CwGNcVS3gAzHZ_vmdbOa64SQ6TKdOMc1?usp=sharing
- colab rag 코드


rag 시스템의 한계:
rag의 유사도 검색이 사람이 생각하는 유사도가 아님.
거리백터를 기준으로, 그나마 가까운거를 랜덤으로 3개정도 가져옴

이게 영어는 그나마 작동 하지만, 한국어는 성능이 많이 안좋음

rag 시스템이 멍청해도, 왜 질문과 관련이 없어 보이는데도, 무작정 가져오고 보냐?

LLM은 예전 인공지능과 많이 달라요.
instruction 프롬프트, 사용자 질문, rag 가 가져온 문서 이걸 사용해요.

예전 인공지능은 instruction prompt 가 하는역활이 없었다면,
llm 은 instruction prompt 가 AI모델을 작동시키는 역활까지 맡아요

그 이유는, instruction prompt 도 llm 입장에선 숫자이고,
숫자는 데이터이기 때문이죠

그리고 LLM 자체의 체급이 만능이기 때문에, 예전 인공지능 상식을 뛰어 넘어요

RAG + LLM 기법은 많이 쓰입니다.

이유가 구현방법이 너무 쉬워요.
LLM 체급 자체가 너무 좋기 때문에, 거진 LLM 파인튜닝 성능을 쉽게 낼수 있어요
"""