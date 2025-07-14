import matplotlib.pyplot as plt

plt.plot(history.history['accuracy'], label='train_accuracy')
plt.plot(history.history['val_accuracy'], label='val_accuracy')
plt.title('model accuracy')
plt.xlabel('Epoch')
plt.ylabel('Accuracy')
plt.legend()
plt.show()

plt.plot(history.history['loss'], label='train_loss')
plt.plot(history.history['val_loss'], label='val_loss')
plt.title('model loss')
plt.xlabel('Epoch')
plt.ylabel('loss')
plt.legend()
plt.show()




import os
import json

save_dir='/content/drive/Mydrive/my_models/tensorflow_keras'
save_model_path=os.path.join(save_dir,'EffiB0_test.h5')
save_label_path=os.path.join(save_dir,'EffiB0_test.json')

if not os.path.exists(save_dir):
  os.madedirs(save_dir)
  print(f"폴더 생성됨: {save_dir}")

model.save(save_model_path)
with open(save_label_path,'w') as f:
  json.dump(class_list,f)
  print(f"클래스 이름 저장 완료:{save_label_path}")