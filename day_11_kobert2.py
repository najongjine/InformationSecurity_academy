# pip install sentence-transformers
from sentence_transformers import SentenceTransformer,util
import torch


model = SentenceTransformer('snunlp/KR-SBERT-V40K-klueNLI-augSTS')

# 파일 읽은거 데이터 구조로 규칙있게 쌓기
questions=[]
ids=[]

with open("questions.txt","r",encoding="utf-8") as f:
    """
    파일 전체를 f 라는 곳에 리스트로 담고
    엔터친 기준으로 하나씩 line에 담음
    """
    for line in f:
        # 공백 제거
        line=line.strip()
        print(f"line: {line}")
        if "__DB__id=" in line:
            question_part, id_part=line.split("__DB__id=")
            question=question_part.strip()
            db_id=int(id_part.strip())
            questions.append(question)
            ids.append(db_id)
print(questions)
print(ids)

# 임베딩 생성
embeddings=model.encode(questions,convert_to_tensor=True)

torch.save({
    'embeddings':embeddings,
    'ids':ids,
    'questions':questions
},'question_embeddings.pt')
print(f"임베딩 저장 완료 ! 총 {len(ids)} 개")