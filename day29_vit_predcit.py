"""
!pip install transformers
"""

from google.colab import drive
drive.mount('/content/drive')

from transformers import AutoFeatureExtractor, AutoModelForImageClassification

model_path = "/content/drive/MyDrive/my_models/vit_cat_dog_horse1"

# Feature Extractor (이미지 전처리기) 로드
extractor = AutoFeatureExtractor.from_pretrained(model_path)

# Fine-tuned 모델 로드
model = AutoModelForImageClassification.from_pretrained(model_path)


from PIL import Image
import requests
from io import BytesIO

from PIL import Image
from transformers import ViTForImageClassification, AutoImageProcessor
import torch
import torch.nn.functional as F

# 1. 이미지 열기
image = Image.open("/content/drive/MyDrive/dataset/adv_cat_non_targeted.png").convert("RGB")

# 2. 모델과 processor 로드
model = ViTForImageClassification.from_pretrained("/content/drive/MyDrive/my_models/vit_cat_dog_horse1")
processor = AutoImageProcessor.from_pretrained("/content/drive/MyDrive/my_models/vit_cat_dog_horse1")

# 3. 이미지 전처리
inputs = processor(images=image, return_tensors="pt")

# 4. 예측
with torch.no_grad():
    outputs = model(**inputs)
    logits = outputs.logits

# 5. softmax로 확률 계산
probs = F.softmax(logits, dim=-1)
max_prob, predicted_class_idx = probs.max(dim=-1)

predicted_label = model.config.id2label[predicted_class_idx.item()]
confidence = max_prob.item()

# 6. 결과 출력
print(f"Predicted class: {predicted_label}")
print(f"Confidence: {confidence:.4f}")

# 7. 알 수 없음 처리
threshold = 0.61  # 자신감이 70% 이하이면 '알 수 없음'
if confidence < threshold:
    print("Result: 알 수 없음 (신뢰도 낮음)")
else:
    print(f"Result: {predicted_label}")
