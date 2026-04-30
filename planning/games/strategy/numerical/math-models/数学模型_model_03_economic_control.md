# 经济系统通胀控制模型

> 来源：moppppp/models
> 原始链接：https://github.com/moppppp/models
> 分类：numerical
> 标签：数学模型, 经济系统, Python

## 概述
经济系统通胀控制模型

## 正文



<!-- ```markdown -->
# 模型三：经济系统通胀控制与动态平衡模型

## 1. 模型描述
长线运营游戏面临货币通胀问题。本模型建立**货币总量**与**活跃玩家数**的微分方程，并设计**PID控制器**动态调整产出系数，使通胀率稳定在目标值（如2%/年）。

- **货币存量** \( M(t) \)
- **活跃玩家数** \( N(t) \)
- **产出系数** \( \beta(t) \)（系统可调）
- **产出速率**：\( P = \alpha N \beta \)
- **消耗速率**：\( C = \gamma N \cdot \frac{1}{1+\kappa (M/N)} \)（人均货币越多，消耗意愿越低）
- **玩家变化**：自然增长 + 因货币偏离导致的流失
- **PID控制**：\( \frac{d\beta}{dt} = -k_p (\pi - \pi^*) - k_i \int (\pi - \pi^*) dt \)

## 2. 数学公式

### 微分方程
\[
\frac{dM}{dt} = \alpha N \beta - \gamma N \cdot \frac{1}{1+\kappa m}, \quad m = \frac{M}{N}
\]
\[
\frac{dN}{dt} = \lambda N \left(1-\frac{N}{K}\right) - \mu N \left|\frac{m - m^*}{m^*}\right|^\nu
\]
\[
\frac{d\beta}{dt} = -k_p (\pi - \pi^*) - k_i \int (\pi - \pi^*) dt, \quad \pi = \frac{1}{M}\frac{dM}{dt}
\]

### 参数示例
- \( \alpha = 100, \gamma = 80, \kappa = 0.005, \lambda = 0.02, K = 10^6, \mu = 0.1, m^* = 5000, \nu = 1, \pi^* = 0.02 \)
- PID: \( k_p = 0.1, k_i = 0.05 \)

## 3. Python代码（核心部分）
```python
import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

def system(state, t, params):
    M, N, beta, int_err = state
    m = M / max(N, 1e-5)
    P = params['alpha'] * N * beta
    C = params['gamma'] * N / (1 + params['kappa'] * m)
    dMdt = P - C
    natural = params['lam'] * N * (1 - N/params['K'])
    loss = params['mu'] * N * (abs((m - params['m_star'])/params['m_star']) ** params['nu'])
    dNdt = natural - loss
    pi = dMdt / max(M, 1e-5)
    err = pi - params['pi_star']
    d_beta = -params['kp'] * err - params['ki'] * int_err
    d_int_err = err
    return [dMdt, dNdt, d_beta, d_int_err]

params = {'alpha':100, 'gamma':80, 'kappa':0.005, 'lam':0.02, 'K':1e6,
          'mu':0.1, 'm_star':5000, 'nu':1, 'pi_star':0.02, 'kp':0.1, 'ki':0.05}
init = [5e6, 1e5, 1.0, 0.0]
t = np.linspace(0, 365, 1000)
sol = odeint(system, init, t, args=(params,))
M, N, beta = sol[:,0], sol[:,1], sol[:,2]
dMdt = np.gradient(M, t)
pi = dMdt / M

plt.figure()
plt.plot(t/30, pi)
plt.axhline(y=0.02, color='r', linestyle='--')
plt.xlabel('时间 (月)'); plt.ylabel('通胀率'); plt.title('PID控制下通胀率收敛')
plt.grid(True); plt.show()

## 策划参考价值
可直接复用的数值建模方法，含完整公式推导。
