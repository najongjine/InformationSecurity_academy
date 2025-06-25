import numpy as np

# 처리할 문장들
sentences=[
    "나는 밥을 먹었다",
    "너는 밥을 안 먹었다",
    "나는 학교에 갔다"
]

# 단어 사전 만들기(word -> index)
word_to_index={}
index=0

for sentence in sentences:
    words=sentence.split()
    for word in words:
        if word not in word_to_index:
            word_to_index[word]=index
            index+=1

print(f"단어사전: {word_to_index}")

# 문장을 숫자 백터로 바꾸기 (문장 -> 정수 리스트)
vectorized_sentences=[]

for sentence in sentences:
    words = sentence.split()

    """
    vector = [
        word_to_index["나는"],     # 1
        word_to_index["밥을"],     # 2
        word_to_index["먹었다"]    # 3
    ]
    == vector = [1, 2, 3]
    """
    vector = [word_to_index[word] for word in words]
    vectorized_sentences.append(vector)

print(f"숫자 벡터화:", vectorized_sentences)

# 길이를 맞춰서 Numpy 배열로 변환 (padding)
"""
vectorized_sentences = [
    [1, 2, 3],        # 첫 번째 문장 (길이 3)
    [4, 5],           # 두 번째 문장 (길이 2)
    [6, 7, 8, 9]      # 세 번째 문장 (길이 4)
]
한 문장씩 길이 확인하면:
len([1, 2, 3]) → 3  
len([4, 5]) → 2  
len([6, 7, 8, 9]) → 4
"""
max_len = max(len(v) for v in vectorized_sentences)
print(f"max_leng: {max_len}")

"""
sentences 개수만큼 줄(row)을 만들고,
max_len 길이만큼 칸(column)을 만들어서
모두 0으로 채운 2차원 배열을 만드는 코드입니다.

sentences = [
    ["나는", "밥을", "먹었다"],
    ["너는", "잤다"]
]
# 각 문장 → 숫자로 바꾸고 나면:
vectorized_sentences = [
    [1, 2, 3],
    [4, 5]
]
# 가장 긴 문장의 길이
max_len = 3

# 문장 개수
len(sentences) = 2

# 만들고 싶은 배열의 크기 → (2줄, 3칸)
"""
padded_array=np.zeros((len(sentences),max_len),dtype=int)
print(f"padded_array.shape : {padded_array.shape}") # (3,4)
"""
지금까지의 padded_array:
[
    [0,0,0,0]
    [0,0,0,0]
    [0,0,0,0]
]
"""

for i,vector in enumerate(vectorized_sentences):
    padded_array[i,:len(vector)]=vector

print(f"numpy sentence:")
print(padded_array)
