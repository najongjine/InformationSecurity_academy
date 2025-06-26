# pip install sentence-transformers
from sentence_transformers import SentenceTransformer,util
import torch


model = SentenceTransformer('snunlp/KR-SBERT-V40K-klueNLI-augSTS')

user_input="배송은 얼마나 걸려요?"
user_embedding=model.encode(user_input,convert_to_tensor=True)

# embedding.pt 읽기. 컴퓨터보고 알아서 읽어라
data=torch.load('question_embeddings.pt')

# 컴퓨터 입장에서 문장
saved_embeddings=data['embeddings']
# DB 입장에서 정해준 문장
saved_ids=data['ids']
# 사람입장에서 정해준 문장
saved_questions=data['questions']

# 문장끼리의 유사도 비교. 뒤에 0 붙은건, 이 함수 만든 사람이 자료구조 이상하게 짜서...
cos_sim=util.pytorch_cos_sim(user_embedding,saved_embeddings)[0]
# 유사도 배열중에 가장 유사한거 1개 추출
top_k=torch.topk(cos_sim,k=1)
# 가장 유사한 벡터의 인덱스를 정수로 추출   top_idx = 1 
top_idx=top_k.indices[0].item()
print(f"가장 유사한 질문:{saved_questions[top_idx]}")
print(f"DB ID:{saved_ids[top_idx]}")
print(f"유사도 점수:{top_k.values[0].item()}")