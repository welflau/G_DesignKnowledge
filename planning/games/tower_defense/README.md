# 明日方舟知识库

基于 [ArknightsGameData](https://github.com/Kengxxiao/ArknightsGameData) 项目解析生成的知识库。

## 知识库统计

- **总文件数**: 4000 个 Markdown 文件
- **生成时间**: 2026-04-16

## 知识库分类

### 1. 玩法知识库 (gameplay/) - 528 个条目
关卡玩法、活动机制、游戏模式等内容

| 子目录 | 内容 | 数量 |
|--------|------|------|
| activities/ | 活动信息 | 290 |
| stages/ | 关卡章节 | 238 |

### 2. 系统知识库 (system/) - 64 个条目
游戏系统、UI、功能模块等内容

| 子目录 | 内容 | 数量 |
|--------|------|------|
| gacha/ | 抽卡系统 | 51 |
| building/ | 基建系统 | 13 |

### 3. 数值知识库 (numerical/) - 3407 个条目
角色属性、技能数值、物品数据等内容

| 子目录 | 内容 | 数量 |
|--------|------|------|
| enemies/ | 敌人数据 | 1576 |
| skills/ | 技能数值 | 1324 |
| characters/ | 角色数值 | 430 |
| items/ | 物品数据 | 77 |

## 文件格式规范

所有知识条目采用 Markdown 格式，遵循统一的元数据头部：

```markdown
---
title: 条目标题
category: 分类名称
subcategory: 子分类
tags: [标签1, 标签2]
source_file: 原始数据文件路径
last_updated: 更新时间
---

# 正文内容
```

## 目录结构

```
knowledge_base/
├── README.md               # 本文件
├── gameplay/               # 玩法知识库
│   ├── stages/             # 关卡信息 (238个)
│   └── activities/         # 活动玩法 (290个)
├── system/                 # 系统知识库
│   ├── gacha/              # 抽卡系统 (51个)
│   └── building/           # 基建系统 (13个)
└── numerical/              # 数值知识库
    ├── characters/         # 角色数值 (430个)
    ├── skills/             # 技能数值 (1324个)
    ├── items/              # 物品数据 (77个)
    └── enemies/            # 敌人数据 (1576个)
```

## 数据来源

- 原始项目: https://github.com/Kengxxiao/ArknightsGameData
- 数据版本: zh_CN (中国服)
- 主要数据文件:
  - `excel/character_table.json` - 角色数据
  - `excel/skill_table.json` - 技能数据
  - `excel/stage_table.json` - 关卡数据
  - `excel/item_table.json` - 物品数据
  - `excel/enemy_handbook_table.json` - 敌人数据
  - `excel/gacha_table.json` - 抽卡数据
  - `excel/building_data.json` - 基建数据
  - `excel/activity_table.json` - 活动数据
