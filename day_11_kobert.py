# pip install sentence-transformers
from sentence_transformers import SentenceTransformer,util


model = SentenceTransformer('snunlp/KR-SBERT-V40K-klueNLI-augSTS')

sentence1="현장 검사 해줘"
sentence2="현장검사해봐"

"""
tensor 생김새:
[0.e-6, 0.0001, 0.31....]
model.encode() 이 함수 하나로, 사람이 쓰는 문장이 엄청 어려운 숫자로 변했다
"""
embedding1=model.encode(sentence1,convert_to_tensor=True)
embedding2=model.encode(sentence2,convert_to_tensor=True)

similarity=util.pytorch_cos_sim(embedding1,embedding2)

# 1.0 == 100%, 0.0 == 0% -0.1이면 상관 없음
print(f"유사도: {similarity.item()}")