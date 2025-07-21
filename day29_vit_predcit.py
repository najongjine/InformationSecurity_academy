"""
!pip install -q transformers timm
"""
# 2. Colab에서 이미지 업로드
from google.colab import files
from PIL import Image
import torch
import numpy as np
from transformers import Trainer, AutoImageProcessor, ViTForImageClassification
import torch.nn.functional as F

from google.colab import drive
drive.mount('/content/drive')

# 업로드 버튼으로 이미지 선택
uploaded = files.upload()
image_path = list(uploaded.keys())[0]
image = Image.open(image_path).convert("RGB")

# 3. 모델과 Processor 불러오기
model_path = "/content/drive/MyDrive/my_models/vit_cat_dog_horse1"
model = ViTForImageClassification.from_pretrained(model_path)
processor = AutoImageProcessor.from_pretrained(model_path)

# 4. 입력 데이터 전처리 (Trainer가 기대하는 형태로 변환)
inputs = processor(images=image, return_tensors="pt")

# 5. Trainer 사용해서 예측
trainer = Trainer(model=model)

# Trainer.predict()는 Dataset 형식만 받음 → 단일 예측용 Dataset 생성
class SingleImageDataset(torch.utils.data.Dataset):
    def __init__(self, inputs):
        self.inputs = inputs

    def __getitem__(self, idx):
        return {k: v.squeeze(0) for k, v in self.inputs.items()}

    def __len__(self):
        return 1

dataset = SingleImageDataset(inputs)
output = trainer.predict(dataset)

# 6. 결과 해석
logits = output.predictions
probs = F.softmax(torch.tensor(logits), dim=-1)
max_prob, pred_idx = torch.max(probs, dim=-1)

predicted_label = model.config.id2label[pred_idx.item()]
confidence = max_prob.item()

print(f"\n✅ 예측 결과: {predicted_label}")
print(f"🔎 신뢰도: {confidence:.4f}")

# 7. 알 수 없음 처리
threshold = 0.61
if confidence < threshold:
    print("❌ Result: 알 수 없음 (신뢰도 낮음)")
else:
    print(f"✅ Result: {predicted_label}")