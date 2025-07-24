pip install -U insightface onnxruntime faiss-cpu scikit-learn






# ✅ 1. 라이브러리 설치 및 모델 준비


import cv2
import numpy as np
import pickle
from insightface.app import FaceAnalysis
from sklearn.metrics.pairwise import cosine_similarity
import faiss
import insightface

# ArcFace 모델 준비
model = FaceAnalysis(name='buffalo_l', providers=['CPUExecutionProvider'])  # CPU 버전
model.prepare(ctx_id=0)

load_path = "/content/drive/MyDrive/embedding/person"












# 🚀 인덱스 & 라벨 로딩
index = faiss.read_index(f"{load_path}/faiss_index.index")
with open(f"{load_path}/faiss_labels.pkl", "rb") as f:
    labels = pickle.load(f)

# 🚀 얼굴 임베딩 추출 함수
def get_face_embedding(image_path):
    img = cv2.imread(image_path)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    faces = model.get(img)
    if faces:
        return faces[0].embedding
    else:
        print("❌ 얼굴 인식 실패")
        return None

# 🚀 얼굴 예측 함수
def predict_person(image_path, top_k=1):
    embedding = get_face_embedding(image_path)
    if embedding is None:
        return

    # 정규화 (ArcFace는 코사인 유사도 기반)
    embedding = embedding.astype('float32')
    embedding /= np.linalg.norm(embedding)

    # 유사도 검색
    scores, indices = index.search(np.array([embedding]), top_k)
    for rank, (idx, score) in enumerate(zip(indices[0], scores[0])):
        print(f"TOP{rank+1}: {labels[idx]} (유사도: {score:.4f})")

# 🚀 사용 예시
predict_person("강호동1.png")
