""" 
1. 데이터 준비
2. 모델 준비
3. 데이터를 모델이 원하는 타입으로 바꿔주기
4. 모델을 파인튜닝 모드로 변경하기
5. 파인튜닝 시작

wandb.ai apikey: cd3a959f4d15312bbe8f8fda20bd300f6f763a20

!pip install - U transformers datasets torchvision
pip install - U datasets huggingface_hub fsspec
"""




from transformers import ViTForImageClassification, AutoImageProcessor, TrainingArguments, Trainer
import torch
from torchvision import datasets, transforms
from torch.utils.data import DataLoader
import numpy as np
import os
from sklearn.metrics import accuracy_score

from google.colab import drive
drive.mount('/content/drive')

# 경로 설정
train_dir = "/content/drive/MyDrive/dataset/corn_leaf/train"
val_dir = "/content/drive/MyDrive/dataset/corn_leaf/validation"


# 데이터를 모델이 원하는 타입으로 바꿔주기
BATCH_SIZE = 8
EPOCHS = 10
IMG_HEIGHT = 384
IMG_WIDTH = 384

# ✅ Trainer가 기대하는 형식으로 바꿔주는 래퍼 클래스
class CustomDataset(torch.utils.data.Dataset):
    def __init__(self, dataset, processor):
        self.dataset = dataset
        self.processor = processor

    def __len__(self):
        return len(self.dataset)

    def __getitem__(self, idx):
        img, label = self.dataset[idx]
        encoding = self.processor(images=img, return_tensors="pt")
        return {
            "pixel_values": encoding["pixel_values"].squeeze(),
            "labels": label
        }

# 전처리기
checkpoint = "facebook/deit-base-distilled-patch16-384"
processor = AutoImageProcessor.from_pretrained(checkpoint)

from torchvision import datasets, transforms

transform = transforms.Compose([
    transforms.Resize((IMG_HEIGHT,IMG_WIDTH)),
    #transforms.CenterCrop(IMG_WIDTH), # ratio 유지 + center crop
    transforms.Lambda(lambda img: transforms.functional.pad( # 전체 ratio 유지
        img,
        padding=(
            (IMG_WIDTH - img.size[0]) // 2,  # left padding
            (IMG_WIDTH - img.size[1]) // 2,  # top padding
            (IMG_WIDTH - img.size[0] + 1) // 2,  # right padding
            (IMG_WIDTH - img.size[1] + 1) // 2   # bottom padding
        ),
        fill=0
    )),
    transforms.RandomHorizontalFlip(),
    transforms.RandomRotation(10),
    transforms.ColorJitter(brightness=0.2, contrast=0.2, saturation=0.2),
    #transforms.ToTensor(),
    #transforms.Normalize(mean=(0.5,0.5,0.5), std=(0.5,0.5,0.5))
])

train_dataset = datasets.ImageFolder(root=train_dir, transform=transform)
val_dataset = datasets.ImageFolder(root=val_dir, transform=transform)


train_ds = CustomDataset(train_dataset, processor)
val_ds = CustomDataset(val_dataset, processor)

# 데이터를 모델이 원하는 타입으로 바꿔주기 END



# 모델을 파인튜닝 모드로 변경하기
id2label = {i: label for i, label in enumerate(train_dataset.classes)}
label2id = {label: i for i, label in enumerate(train_dataset.classes)}

checkpoint = "facebook/deit-base-distilled-patch16-384"
model = ViTForImageClassification.from_pretrained(
    checkpoint,
    num_labels=len(train_dataset.classes),
    id2label=id2label,
    label2id=label2id
)

finetune_whole_model = False  # ← True면 앞부분까지 훈련, False면 출력층만

if not finetune_whole_model:
    for name, param in model.named_parameters():
        if "classifier" in name:
            param.requires_grad = True
        else:
            param.requires_grad = False
# 모델을 파인튜닝 모드로 변경하기 END


# 훈련하기
# 평가 지표
def compute_metrics(p):
    preds = np.argmax(p.predictions, axis=1)
    labels = p.label_ids
    acc = accuracy_score(labels, preds)
    return {"accuracy": acc}

# 훈련 인자
training_args = TrainingArguments(
    output_dir="./vit-cornleaf",
    per_device_train_batch_size=BATCH_SIZE,
    per_device_eval_batch_size=BATCH_SIZE,
    num_train_epochs=EPOCHS,
    eval_strategy="epoch",
    save_strategy="epoch",
    logging_dir="./logs",
    logging_steps=10,
    load_best_model_at_end=True,
    metric_for_best_model="accuracy",
    greater_is_better=True,
    push_to_hub=False,
    report_to="none"
)

# Trainer 구성
trainer = Trainer(
    model=model,
    args=training_args,
    train_dataset=train_ds,
    eval_dataset=val_ds,
    compute_metrics=compute_metrics
)

trainer.train()

# 저장
# 훈련하기 END


# 폴더가 없으면 자동으로 만들기
save_dir="/content/drive/MyDrive/my_models/vit/vit_deit384_cornleaf"
if not os.path.exists(save_dir):
    os.makedirs(save_dir)
    print(f"📂 폴더 생성됨: {save_dir}")

# 저장
model.save_pretrained(save_dir)
processor.save_pretrained(save_dir)
# 훈련하기 END


# 그래프
import matplotlib.pyplot as plt
import pandas as pd

# trainer.train() 실행 후
train_output = trainer.train()

# log_history에서 pandas DataFrame으로 변환
logs = pd.DataFrame(trainer.state.log_history)

# train/val loss와 accuracy만 필터링
train_loss = logs[logs['loss'].notnull()][['epoch', 'loss']]
eval_logs = logs[logs['eval_loss'].notnull()][['epoch', 'eval_loss', 'eval_accuracy']]

# ✅ 손실(loss) 그래프
plt.figure(figsize=(8, 5))
plt.plot(train_loss['epoch'], train_loss['loss'], label='Train Loss')
plt.plot(eval_logs['epoch'], eval_logs['eval_loss'], label='Validation Loss')
plt.xlabel('Epoch')
plt.ylabel('Loss')
plt.title('Training and Validation Loss')
plt.legend()
plt.grid()
plt.show()

# ✅ 정확도(accuracy) 그래프
plt.figure(figsize=(8, 5))
plt.plot(eval_logs['epoch'], eval_logs['eval_accuracy'], marker='o', label='Validation Accuracy')
plt.xlabel('Epoch')
plt.ylabel('Accuracy')
plt.title('Validation Accuracy')
plt.legend()
plt.grid()
plt.show()
# 그래프 END