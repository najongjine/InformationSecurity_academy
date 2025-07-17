# 60% 이하면 예측 실패 안내 띄우기
if uploaded_file is not None:
    # 이미지 로딩
    img = Image.open(uploaded_file).convert('RGB')
    st.image(img, caption='업로드된 이미지', use_column_width=True)

    # 전처리
    IMG_HEIGHT = 224
    IMG_WIDTH = 224
    img = img.resize((IMG_WIDTH, IMG_HEIGHT))
    img_array = image.img_to_array(img)
    img_array = preprocess_input(img_array)
    img_array = np.expand_dims(img_array, axis=0)

    # 예측
    predictions = model.predict(img_array)
    pred_probs = predictions[0]
    max_prob = np.max(pred_probs)
    predicted_class = class_names[np.argmax(pred_probs)]

    # 출력
    if max_prob <= 0.6:
        st.markdown("### ⚠️ 학습한 클래스가 아니거나, 분류를 실패했습니다.")
    else:
        st.markdown(f"### ✅ 예측 결과: **{predicted_class}**")

    st.markdown("### 🔢 클래스별 확률")
    for i, prob in enumerate(pred_probs):
        st.write(f"{class_names[i]}: {prob:.4f}")
