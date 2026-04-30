# 多乘区伤害资源分配模型

> 来源：moppppp/models
> 原始链接：https://github.com/moppppp/models
> 分类：numerical
> 标签：数学模型, 伤害公式, Python

## 概述
多乘区伤害资源分配模型

## 正文



<!-- ```markdown -->
# 模型二：多乘区伤害模型下的资源最优分配

## 1. 模型描述
在《原神》《崩坏：星穹铁道》等游戏中，最终伤害由多个独立乘区相乘得到。每个乘区需要投入资源（如圣遗物词条、属性点），且收益边际递减。本模型求解在总资源固定的条件下，如何分配资源使得总伤害最大化。

- **攻击乘区**：\( A(x) = 1 + 0.05x - 0.0002x^2 \)
- **暴击率乘区**：\( p(y_1) = \min(0.012 y_1, 0.8) \)
- **暴击伤害乘区**：\( q(y_2) = 1.5 + 0.03 y_2 \)
- **暴击期望乘区**：\( B(y_1, y_2) = 1 + p(y_1)\cdot(q(y_2)-1) \)
- **增伤乘区**：\( C(z) = 1 + 0.04z - 0.00015z^2 \)
- **总资源**：\( x + y_1 + y_2 + z = 100 \)，各变量非负。

目标：最大化 \( F = A(x) \cdot B(y_1, y_2) \cdot C(z) \)。

## 2. 数学公式（优化条件）
利用拉格朗日乘数法，最优解处各乘区的对数导数（边际收益）相等：
\[
\frac{A'(x)}{A(x)} = \frac{\partial \ln B}{\partial y_1} = \frac{\partial \ln B}{\partial y_2} = \frac{C'(z)}{C(z)}
\]

由于约束非线性，采用数值优化求解。

## 3. Python代码
```python
import numpy as np
from scipy.optimize import minimize, Bounds

def damage(x):
    x_att, x_crate, x_cdmg, x_dmg = x
    A = 1 + 0.05*x_att - 0.0002*x_att**2
    crate = min(0.012*x_crate, 0.8)
    cdmg = 1.5 + 0.03*x_cdmg
    B = 1 + crate * (cdmg - 1)
    C = 1 + 0.04*x_dmg - 0.00015*x_dmg**2
    return A * B * C

R = 100
x0 = [25, 25, 25, 25]
cons = ({'type': 'eq', 'fun': lambda x: sum(x) - R})
bounds = Bounds([0,0,0,0], [R,R,R,R])
result = minimize(lambda x: -damage(x), x0, method='SLSQP', bounds=bounds, constraints=cons)
opt_x = result.x
opt_val = -result.fun

print("最优分配：攻击={:.2f}, 暴击率资源={:.2f}, 暴伤资源={:.2f}, 增伤={:.2f}".format(*opt_x))
print("最大伤害：{:.2f}".format(opt_val))

## 策划参考价值
可直接复用的数值建模方法，含完整公式推导。
