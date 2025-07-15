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