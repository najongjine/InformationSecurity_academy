"""
EfficientNetB0 모델 생성해서 갔닸르 준비 끝
include_top=False == 판단 부분은 내가 직접 정함
"""
base_model = EfficientNetB0(weights='imagenet', include_top=False, input_shape=(IMG_HEIGHT, IMG_WIDTH, 3))

"""
모델에 눈 부분
기존에 이미 훈련 잘 받았으니, 니네가 하던 대로 해
"""
for layer in base_model.layers:
    layer.trainable = False

# 미세조정
#for layer in base_model.layers[:-20]:  # 마지막 20개 레이어만 열기
#    layer.trainable = False


"""
커스터마이징 하고나면, 답안지가 기존에 했더거랑은 틀리니,
이번엔 이런~~ 가이드 라인을 따라
"""
x = base_model.output
x = GlobalAveragePooling2D()(x)
x = Dense(128, activation='relu')(x)
x = Dropout(0.5)(x)
x = Dense(64, activation='relu')(x)
x = Dropout(0.5)(x)
output_layer = Dense(3, activation='softmax')(x)

# 모델 빌드
model = Model(inputs=base_model.input, outputs=output_layer)
model.summary()





from tensorflow.keras.preprocessing.image import ImageDataGenerator
from tensorflow.keras.applications.densenet import preprocess_input

# 이미지 크기 및 배치 설정
IMG_SIZE = (224, 224)
BATCH_SIZE = 32

# ✅ 학습용 데이터 제너레이터
train_datagen = ImageDataGenerator(
    preprocessing_function=preprocess_input,
    rotation_range=15,
    width_shift_range=0.1,
    height_shift_range=0.1,
    shear_range=0.1,
    zoom_range=0.1,
    horizontal_flip=True,
    fill_mode='nearest'
)

# ✅ 검증용 데이터 제너레이터 (augmentation 없음)
val_datagen = ImageDataGenerator(
    preprocessing_function=preprocess_input
)

# ✅ 디렉터리에서 이미지 불러오기
train_dir = './train'         # 사용자 디렉토리 구조에 맞게 수정
validation_dir = './validation'

train_generator = train_datagen.flow_from_directory(
    train_dir,
    target_size=IMG_SIZE,
    batch_size=BATCH_SIZE,
    class_mode='categorical'  # 다중 클래스 분류
)

validation_generator = val_datagen.flow_from_directory(
    validation_dir,
    target_size=IMG_SIZE,
    batch_size=BATCH_SIZE,
    class_mode='categorical'
)




# 모델 준비다

# ✅ 사전학습된 DenseNet121 불러오기 (top 제거)
base_model = DenseNet121(weights='imagenet', include_top=False, input_shape=(224, 224, 3))

# ✅ 기존 가중치는 학습되지 않도록 잠금 (필요시 수정 가능)
base_model.trainable = False  # 처음에는 동결하고 이후 풀어서 미세조정

# ✅ 출력층 구성
x = base_model.output
x = GlobalAveragePooling2D()(x)
x = Dropout(0.5)(x)  # 과적합 방지를 위한 Dropout
output = Dense(NUM_CLASSES, activation='softmax')(x)

# ✅ 최종 모델 구성
model = Model(inputs=base_model.input, outputs=output)

# ✅ 1단계: 전체 모델을 훈련 가능하게 설정
base_model.trainable = True

# ✅ 2단계: 너무 많은 레이어를 훈련시키지 않도록 일부만 열기 (예: 마지막 30개 레이어만 학습)
for layer in base_model.layers[:-30]:  # 앞쪽 레이어는 동결
    layer.trainable = False

# ✅ 3단계: 컴파일 다시 하기 (새로 학습 가능하니까 옵티마이저 리셋)
model.compile(optimizer=Adam(learning_rate=1e-5),  # 너무 크게 하면 기존 가중치 다 날아감
              loss='categorical_crossentropy',
              metrics=['accuracy'])

# ✅ 모델 요약 확인
model.summary()
# 모델 준비다  END



# ✅ 파인튜닝 학습 시작
history = model.fit(
    train_generator,
    steps_per_epoch=train_generator.samples // BATCH_SIZE,
    validation_data=validation_generator,
    validation_steps=validation_generator.samples // BATCH_SIZE,
    epochs=10  # 원하는 만큼
)





"""
인공지능을 하면
이론은 사람이 알아들수 없고, 코드도 알아볼수 없을만큼 힘듬니다
예전에는 책학원 파서, 그것만 했어요

요즘에는 옛날처럼 책 A,B,C 사고 그거 합치기 안해요

내가 하려는 목적을 먼저 단계로 뽑아내고
예를들면 이미지 분류 파인튜닝은 
1. 데이터 준비
2. 모델 준비
3. 데이터를 모델이 우너하는 타입으로 바꿔주기
4. 모델을 파인튜닝 모드로 변경하기
5. 파인튜닝 시작

이 단계를 벗어나기 않아요

각 단계마다 코드 조금씩은 다를수 있어요.

특히, 3번은 많이 다를수도 있어요(크게 다르진 않아요. 이미지 불러오는 모듈중 살아남은건 2개밖에 없어요)

코드가 다르다고 겁낼 필요 없어요.
일단은 작동 시키는게 중요해요

GPT, Gemini, Claude, Grok 유료버전이 더 좋긴 해요
중요한건 뭘 써도 조립하는 단계에서 에러는 날거에요
그때마다, 중요한 부분이랑 에러메세지를 계속 질문하면서 고쳐 나가요

1단계의 최종 목적은 작동 시키기
2단계의 목적은 개선점, 취약점 보완하기

GPT 사용 안좋은 예:
"나는 DenseNet으로 질병 분류기 만들거야. 니가 만들어줘" <-- 범위가 너무 커서 아무거나 던져줌

GPT 사용 좋은 예:
"나는 DenseNet 으로 질병 분류기를 나만의 데이터로 파인튜닝 하고싶어. 어떤 단계들이 필요할까?"
"""