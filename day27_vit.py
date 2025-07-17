"""
!pip install transformers datasets torchvision

pip install -U datasets huggingface_hub fsspec
"""

# 🟢 2. 필요한 라이브러리 불러오기
from transformers import ViTForImageClassification, ViTFeatureExtractor, TrainingArguments, Trainer
import torch
from torch.utils.data import DataLoader
from transformers import ViTForImageClassification, ViTFeatureExtractor