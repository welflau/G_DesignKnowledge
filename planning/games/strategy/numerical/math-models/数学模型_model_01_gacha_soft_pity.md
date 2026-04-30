# 抽卡软保底期望模型

> 来源：moppppp/models
> 原始链接：https://github.com/moppppp/models
> 分类：numerical
> 标签：数学模型, 抽卡概率, Python

## 概述
抽卡软保底期望模型

## 正文
# 模型一：抽卡软保底期望值计算模型

## 1. 模型描述
在商业化抽卡游戏中，为了保护玩家体验、提升付费意愿，常采用**概率递增（软保底）**机制：每次未抽到稀有物品，下一次抽到的概率按固定增量上升，直到达到100%必出。本模型求解在此机制下获得一张SSR的期望抽数。

- 基础概率：\( p_0 = 1\% = 0.01 \)
- 每次未出货增量：\( \Delta = 2\% = 0.02 \)
- 概率上限：1（即第 \( N \) 抽必出）

## 2. 数学公式

### 概率序列
\[
p_i = \min\left(p_0 + (i-1)\Delta,\ 1\right)
\]
代入数值：\( p_1 = 0.01, p_2 = 0.03, \dots, p_{50}=0.99, p_{51}=1 \)。

### 首次出货概率
设 \( Q_{k-1} = \prod_{i=1}^{k-1} (1-p_i) \) 为前 \( k-1 \) 次均未出货的概率。则
\[
P(\text{首次出货在 }k) = Q_{k-1} \cdot p_k
\]

### 期望抽数
\[
E = \sum_{k=1}^{50} k \cdot Q_{k-1} p_k \;+\; 51 \cdot Q_{50}
\]

数值结果：\( E \approx 34.62 \) 抽。

## 3. Python代码
```python
import matplotlib.pyplot as plt
import numpy as np

p0, delta, max_p = 0.01, 0.02, 1.0
prob_list = []
p = p0
while p < max_p:
    prob_list.append(p)
    p += delta
prob_list.append(1.0)
n = len(prob_list)   # 51

Q = 1.0
expected = 0.0
for k in range(1, n+1):
    p_k = prob_list[k-1]
    expected += k * Q * p_k
    Q *= (1 - p_k)

print(f"期望抽数: {expected:.4f}")

# 绘图
plt.figure(figsize=(12,4))
plt.subplot(1,2,1)
plt.plot(range(1, n+1), prob_list, 'bo-')
plt.xlabel('抽数'); plt.ylabel('单抽出货概率'); plt.title('软保底概率递增曲线')
plt.grid(True)

cum_prob = []
Q = 1.0
cum = 0.0
for k, p_k in enumerate(prob_list, 1):
    cum += Q * p_k
    cum_prob.append(cum)
    Q *= (1 - p_k)
plt.subplot(1,2,2)
plt.plot(range(1, n+1), cum_prob, 'r-')
plt.xlabel('抽数'); plt.ylabel('累积出货概率'); plt.title('软保底累积出货概率')
plt.grid(True)
plt.tight_layout()
plt.savefig('soft_pity.png')
plt.show()

## 策划参考价值
可直接复用的数值建模方法，含完整公式推导。
