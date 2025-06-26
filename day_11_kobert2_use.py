# pip install sentence-transformers
from sentence_transformers import SentenceTransformer,util
import torch


model = SentenceTransformer('snunlp/KR-SBERT-V40K-klueNLI-augSTS')

user_input="배송은 얼마나 걸려요?"
user_embedding=model.encode(user_input,convert_to_tensor=True)

data=torch.load('question_embeddings.pt')
saved_embeddings=data['embeddings']
saved_ids=data['ids']
saved_questions=data['questions']

print(saved_embeddings)