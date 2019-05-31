import numpy as np
import matplotlib.pyplot as plt

X = []
S = []
G = []
T = 3600
tau = 0.1

# 겹치는 패킷을 카운트 하는 함수
def max_overlapping(intervals):
    current_max = 0
    current_overlap = 0
    i, j = 0, 0
    while i < len(intervals) and j < len(intervals):
        if X_start[i] < X_end[j]:
            current_overlap += 1
            current_max = max(current_max, current_overlap)
            i += 1
        else:
            current_overlap -= 1
            j += 1
    return current_max

# x는 사건수를 조정하기 위함
for x in range(0, 100000, 100):
    N = 0
    U = np.random.rand(N)
    X = [-1 * np.log(i) * (T / (N + x)) for i in U]
    X.sort()
    X_start = X
    X_end = [val + tau for val in X]
    packets_cnt = N + x - max_overlapping(X) # 겹치지 않는 패킷의 수를 카운트함
    G = np.append(G, (packets_cnt) /T*tau) # G(attempts per packet time)
    
S = np.append(S, G * np.exp(-2 * G)) # S(successful transmissions per packet time)

# 그래프
plt.plot(G, S, color = 'blue')
plt.title('Pure ALOHA')
plt.xlabel('G')
plt.ylabel('S')
plt.show()

# G와 S값 출력
#print(G)
#print(S)