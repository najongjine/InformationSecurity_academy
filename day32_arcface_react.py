# 🚀 Colab에서 최초 1회만 설치
!pip install - U insightface
!pip install onnxruntime
!pip install faiss - cpu




# 🚀 구글 드라이브 마운트
from google.colab import drive
drive.mount('/content/drive')



import insightface
import faiss
import cv2
import numpy as np
from pathlib import Path
import pandas as pd
import pickle
import albumentations as A
from albumentations.pytorch import ToTensorV2
import os

save_path = "/content/drive/MyDrive/embedding/person"
data_folder = "/content/drive/MyDrive/dataset/person/train"
os.makedirs(save_path, exist_ok = True)  # 폴더가 없으면 생성


# -*- coding: utf-8 -*-
"""ArcFace with FAISS"""

# 🚀 모델 준비 (GPU 사용 시 ctx_id=0)
model = insightface.app.FaceAnalysis(name='buffalo_l', providers=['CPUExecutionProvider'])
model.prepare(ctx_id=0)

augment = A.Compose([
    A.HorizontalFlip(p=0.5),
    A.RandomBrightnessContrast(p=0.3),
    A.Rotate(limit=15, p=0.3),
])

# 🚀 임베딩 추출 함수
def get_face_embedding(image_path: str, n_augment: int = 5):
    img = cv2.imread(str(image_path))
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

    embeddings = []

    # ✅ 원본 이미지 먼저 임베딩
    faces = model.get(img)
    if faces:
        embeddings.append(faces[0].embedding)
    else:
        print(f"❌ 얼굴 인식 실패 (원본): {image_path}")

    # ✅ 이후 증강 이미지들 임베딩
    for i in range(n_augment):
        augmented = augment(image=img)
        img_aug = augmented['image']
        faces = model.get(img_aug)
        if faces:
            embeddings.append(faces[0].embedding)
        else:
            print(f"❌ 얼굴 인식 실패 (증강 {i+1}): {image_path}")

    if embeddings:
        return np.mean(embeddings, axis=0)
    else:
        print(f"❌ 모든 시도 실패: {image_path}")
        return None



# 🚀 폴더 처리 함수
def process_folder(base_path):
    data = []
    base_path = Path(base_path)
    for person_dir in base_path.iterdir():
        if not person_dir.is_dir():
            continue
        label = person_dir.name
        print(f"▶ 폴더: {label}")
        count = 0
        for image_path in list(person_dir.glob("*")):
            if image_path.suffix.lower() not in [".jpg", ".jpeg", ".png"]:
                continue
            emb = get_face_embedding(image_path)
            if emb is not None:
                count += 1
                data.append({
                    "label": label,
                    "image_path": str(image_path),
                    "embedding": emb
                })
        print(f"✅ 얼굴 인식 성공 수: {count}")
    return pd.DataFrame(data)

# 🚀 데이터셋 생성
train_df = process_folder(data_folder)

# 🚀 embedding 스택
embeddings = np.stack(train_df['embedding'].values).astype('float32')
embeddings /= np.linalg.norm(embeddings, axis=1, keepdims=True)   # ⭐️ 정규화

# 🚀 FAISS 인덱스 생성 (코사인 유사도 ≈ 내적)
index = faiss.IndexFlatIP(embeddings.shape[1])
index.add(embeddings)

# 🚀 라벨 리스트 저장
labels = train_df['label'].tolist()

# 🚀 인덱스 저장
faiss.write_index(index, f"{save_path}/faiss_index.index")

# 🚀 라벨도 같이 저장
with open(f"{save_path}/faiss_labels.pkl", "wb") as f:
    pickle.dump(labels, f)

print("✅ FAISS 인덱스 & 라벨 저장 완료")

