# SubSkill: 经济系统建模

## 触发条件
用户需求涉及：资源产出、货币体系、消耗设计、通胀控制、交易系统

## 检索知识标签
["经济系统", "通胀控制", "产出消耗", "PID控制"]

## 优先检索条目
1. `numerical/damage-formula/数值教程_第5章_*` — 游戏经济系统完整理论
2. `numerical/math-models/数学模型_model_03_economic_control.md` — PID通胀控制模型
3. `numerical/game-data/freeciv/Freeciv_civ2civ3_*_ruleset.md` — 文明经济规则
4. `numerical/game-data/openra/OpenRA_ra_defaults.md` — RTS经济参数

## 输出模板
```markdown
## 经济系统方案

### 1. 货币体系
| 货币 | 定位 | 产出途径 | 主要消耗 | 是否可交易 |
|------|------|---------|---------|-----------|

### 2. 资源产出模型
$Production(t) = ...$

### 3. 消耗水池设计
| 消耗点 | 消耗货币 | 消耗量级 | 频率 |
|--------|---------|---------|------|

### 4. 通胀控制机制
[回收手段/税收/衰减/PID参数]

### 5. 经济模拟（7日/30日/90日）
[资源存量曲线/通胀率预测]
```
