# FGO · 从者叙事数据结构（特性标签/技能命名/绊系统）

> 来源：atlasacademy/fgo-game-data-api
> 原始链接：https://api.atlasacademy.io/
> 分类：gameplay
> 标签：FGO, 回合制RPG, 角色设定, 特性标签, 叙事机制一体化
> 游戏类型：回合制RPG

## 概述
FGO从者数据结构深度分析：特性标签如何桥接叙事与机制、技能命名叙事化、绊等级驱动叙事消费。

## 正文
## FGO 从者叙事数据结构（Atlas Academy API）

以阿尔托莉雅·潘德拉贡(Saber)为例，展示FGO的角色叙事数据组织方式。

### 角色基础设定
| 字段 | 含义 | 示例值 |
|------|------|--------|
| name | 全名 | アルトリア・ペンドラゴン |
| battleName | 战斗简称 | アルトリア |
| className | 职阶 | saber |
| gender | 性别 | female |
| attribute | 属性 | earth（地） |

### 能力值面板（世界观强度表现）
```
Strength（筋力）: B
Endurance（耐久）: B
Agility（敏捷）: B
Magic（魔力）: A
Luck（幸运）: A+
NP（宝具）: A++
Policy: lawful（秩序）
Personality: good（善）
```

### 特性标签系统（traits）——叙事与机制的桥梁
```
dragon（龙）、saberface、arthur、king（王）、
knightsOfTheRound（圆桌骑士）、FSNServant（FSN从者）、
riding（骑乘）、humanoid（人形）
```
> 关键设计：特性标签既是**叙事设定**（她是龙之血统的王），也是**机制锚点**（对龙特攻技能生效）。
> 这是"叙事-机制一体化"的优秀范例。

### 技能叙事化命名体系
| 技能 | 名称 | 叙事含义 |
|------|------|---------|
| Skill 1 | カリスマ B（Charisma B） | 作为王的领导力 |
| Skill 2 | 魔力放出 A（Mana Burst A） | 龙之魔力的爆发 |
| Skill 2强化 | 竜の炉心 B（Dragon's Core B） | 觉醒龙的本质 |
| Skill 3 | 直感 A（Instinct A） | 战场直觉 |
| Skill 3强化 | 輝ける路 EX（Shining Road EX） | 走向理想之路 |

> 技能名从"通用能力"→"个人特色"的强化路径，本身就是角色成长的叙事。

### 绊等级系统——长线叙事激励
```
bondGrowth: [0, 15000, 22500, 30000, 45000, 155000, ...]
```
每个绊等级解锁新的角色故事文本，10级绊解锁专属礼装。
这是"用机制驱动叙事消费"的经典设计。

### 完整数据结构树
```
servant
├── 基础信息 (id, name, class, rarity, stats)
├── traits[] (特性标签 ← 叙事设定与机制的桥梁)
├── skills[] (技能 ← 叙事化命名+效果)
│   └── functions[] → buffs[] → svals[]
├── ascensionAdd (灵基差异 ← 角色形象演变的叙事)
├── extraAssets (全套立绘 ← 视觉叙事)
├── bondGrowth[] (绊等级 ← 长线叙事激励)
├── valentineScript (情人节剧情 ← 社交叙事)
└── lore (角色传说/设定文本)
```


## 策划参考价值
叙事与机制一体化设计的教科书案例。特性标签系统值得SLG借鉴（兵种特性=叙事设定+克制机制）。
