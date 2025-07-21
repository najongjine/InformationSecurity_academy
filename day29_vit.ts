/**
 1. 데이터 준비
2. 모델 준비
3. 데이터를 모델이 우너하는 타입으로 바꿔주기
4. 모델을 파인튜닝 모드로 변경하기
5. 파인튜닝 시작
 */

wandb.ai apikey: cd3a959f4d15312bbe8f8fda20bd300f6f763a20

!pip install - U transformers datasets torchvision
pip install - U datasets huggingface_hub fsspec


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