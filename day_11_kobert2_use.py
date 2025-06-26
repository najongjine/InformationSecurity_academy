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

print(saved_ids)
print(saved_questions)