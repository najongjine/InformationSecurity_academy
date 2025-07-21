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