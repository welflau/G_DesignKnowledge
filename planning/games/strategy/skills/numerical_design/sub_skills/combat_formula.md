# SubSkill: 战斗公式设计

## 触发条件
用户需求涉及：伤害计算、战斗公式、攻防关系、暴击、闪避、属性克制、技能伤害倍率

## 检索知识标签
["伤害公式", "战斗数值", "乘区体系", "教程"]

## 优先检索条目
1. `numerical/damage-formula/数值教程_第1章_*` — 战斗数值系统全貌
2. `numerical/damage-formula/伤害公式_原神_Damage_Formula_GI.md` — 乘区体系标杆
3. `numerical/damage-formula/伤害公式_星穹铁道_*` — 回合制伤害公式
4. `numerical/game-data/openra/OpenRA_ra_infantry.md` — RTS单位属性实例
5. `numerical/game-data/arknights/明日方舟_character_table.md` — 角色属性结构

## 输出模板
```markdown
## 战斗公式方案

### 1. 公式选型：[加法/乘法/乘区/混合]
[选型理由]

### 2. 核心伤害公式
$$Damage = ...$$

### 3. 参数说明
| 参数 | 含义 | 取值范围 | 来源 |
|------|------|---------|------|

### 4. 配表示例
| 单位ID | 基础攻击 | 攻击成长 | 暴击率 | 暴击倍率 |
|--------|---------|---------|--------|---------|

### 5. 设计验证
[DPS对比/Time-To-Kill分析/克制关系矩阵]
```
