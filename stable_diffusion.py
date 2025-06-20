import torch
from diffusers import StableDiffusionXLPipeline



# SDXL 모델 로드 (Base 모델)
pipe = StableDiffusionXLPipeline.from_pretrained(
    "stabilityai/stable-diffusion-xl-base-1.0",
    torch_dtype=torch.float16,
    variant="fp16",
    use_safetensors=True
).to("cuda")

# 프롬프트 작성
prompt = "a beautiful portrait of a woman in Pixar style, soft lighting, vibrant colors"
negative_prompt = "ugly, blurry, low quality, distorted"

# 이미지 생성
image = pipe(prompt=prompt, negative_prompt=negative_prompt).images[0]

# 저장 및 보기
image.save("sdxl_output.png")
image.show()
