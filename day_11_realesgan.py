# pip install realesrgan

from PIL import Image
from realesrgan import RealESRGANer
import torch

# cuda gpu 있으면 그거쓰고, 없으면 cpu써
device=torch.device('cuda' if torch.cuda.is_available() else 'cpu')

model=RealESRGANer(device,scale=4)
model.load_weights('RealESRGAN_x4.pth')