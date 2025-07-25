"""
Scikit - 이건 숫자, 수치등을 가지고 예측하는 모델
linear regression, logistic regression, 
XGBoost -> XGRegression

Tensorflow, Keras -
[0.1,0.01,0.51..] Neural... Network
10100101 int, string, bool 
Keras 는 tensorflow 라는 AI 전용 언어를, 사람이 쓸수 있게
어느정도 쉽게 해준 프레임워크

tensorflow, keras 는 GPU가 필요하긴 한데,
그렇게 비싼 GPU는 요구하지 않아요
즉, 살짝 가벼워요
transformer 가 나오기 전에 유행했었어요
이놈을 쓰면, scikit 할수 없었던, 이미지, 자연어 처리를
간단하게 할수 있다

pytorch, transformer - 요거는 나중에



AI로 뭘 할수있냐

- 회귀 (돈, 금액, 가치 예측)
* XGBoost

- 분류(이미지)
* CNN, Vision Transformer

- 객체탐지
* YOLO

- 언어처리
- 음성인식
* LLM(GPT)

- 강화학습
* DeepLearningCNN || Q-Learning

인터넷이나 GPT 한테 AI 검색 해보면 드럽게 많이도 용어가 나와요
하지만 그 수많은 모델들 중에서 살아남은 놈은 얼마 없어요


자연어	     GPT             	요약, 생성, 번역, 챗봇
이미지 분류	  ViT, CNN	        사진 분류, 품질 검사
객체 탐지	  YOLO              cctv, 자율주행
얼굴 인식	  ArcFace, FaceNet	인증, 추적
이미지 생성	  Stable Diffusion	이미지 합성, 아트 생성

https://colab.research.google.com/drive/1AbFTCu7f0RlZXXcmqI770oLEAf5ozoNW?usp=sharing

컴퓨터가 이해하는 모델 레이어

conv2d 는 이미지 numpy 데이터를 3*3 크기의 32개의 필더로 1칸씩 이동하면서
행렬곱한 특징데이터를 남김.
maxpooling은 행렬의 크기를 줄임

사람이 이해하는거~
model.sequential() 이건 공장 지으려고 땅 하나 준비
conv2d(32 ....) 이건 32개의 특정 특징만 볼수있는 돋보기 32개(곡선, 직선, 검은색, 흰색)
이걸 사용하면 1장의 이미지에서 32개의 새로운 특징이미지가 생성됨
maxpooling은 이미지 크기를 줄이고, 흰색1,흰색2,흰색3,흰색4 이런짓을 컴퓨터에게
자제시킴

"""