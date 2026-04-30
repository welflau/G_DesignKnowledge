# SLG 游戏策划知识库

> 面向 AI 游戏策划能力的结构化知识库，覆盖数值、叙事、系统、玩法四大维度，支持 Agent-Skills-SubSkills 调用体系。

## 概览

| 指标 | 数据 |
|------|------|
| 知识条目总数 | 1,688 条 |
| 覆盖游戏品类 | 10+ 品类 |
| 覆盖游戏数量 | 50+ 款 |
| Skills 数量 | 8 个 Skill / 17 个 SubSkills |
| 原始数据源 | 54 个 GitHub 仓库 |
| 叙事模板 | 13 个品类专项模板 |
| GDD 模板 | 61 篇（15 章完整体系） |

## 目录结构

```
knowledge-base/
├── README.md                           # 本文件
├── ARCHITECTURE.md                     # 架构设计方案
├── SLG游戏策划知识库资源索引.md          # 资源索引总表
├── narrative_resources.md              # 叙事资源搜索清单
│
├── gameplay/                           # 📕 玩法知识库 (559条)
│   └── narrative/                      #    叙事体系
│       ├── methodology/                #    方法论/教程 (34条)
│       ├── worldbuilding/              #    世界观构建 (25条)
│       ├── story-structure/            #    故事结构 (15条)
│       ├── character-design/           #    角色设计 (10条)
│       ├── quest-design/               #    任务设计 (8条)
│       ├── interactive-narrative/      #    互动叙事 (13条)
│       ├── narrative-craft/            #    叙事手艺 (16条)
│       ├── dialogue-examples/          #    对话示例 (10条)
│       ├── game-design/                #    游戏设计Skills (60条)
│       └── game-story-data/            #    游戏剧情案例数据
│           ├── arknights-story/        #      明日方舟 (110条)
│           ├── genshin/                #      原神 (66条)
│           ├── pc-rpg/                 #      PC RPG 50+款 (93条)
│           ├── slg/                    #      SLG/RTS (45条)
│           ├── azurlane/               #      碧蓝航线 (22条)
│           ├── wuthering-narrative/    #      鸣潮 (13条)
│           ├── starrail/               #      星穹铁道 (7条)
│           ├── fgo/                    #      FGO (1条)
│           └── moba/                   #      MOBA (1条)
│
├── numerical/                          # 📘 数值知识库 (909条)
│   ├── damage-formula/                 #    伤害公式/教程 (30条)
│   ├── math-models/                    #    数学模型 (4条)
│   ├── balance/                        #    平衡方法论 (11条)
│   ├── monetization/                   #    商业化 (1条)
│   └── game-data/                      #    游戏数值配表 (866条)
│       ├── freeciv/                    #      文明 (704条)
│       ├── openra/                     #      红警 (87条)
│       ├── genshin/                    #      原神 (19条)
│       ├── starrail/                   #      星穹铁道 (18条)
│       ├── wuthering/                  #      鸣潮 (15条)
│       ├── azurlane/                   #      碧蓝航线 (12条)
│       ├── arknights/                  #      明日方舟 (9条)
│       ├── bluearchive/                #      蔚蓝档案 (1条)
│       └── clash-royale/               #      皇室战争 (1条)
│
├── system/                             # 📗 系统知识库 (86条)
│   ├── gdd-templates/                  #    GDD模板 (61条)
│   ├── narrative-templates/            #    叙事模板 (13条)
│   ├── narrative-tools/                #    叙事工具 (9条)
│   ├── combat-system/                  #    战斗系统 (3条)
│   └── slg-modules/                    #    SLG实战模块 (3条)
│
├── comprehensive/                      # 📙 综合知识库 (134条)
│   ├── project-mgmt/                   #    GameDevMind技术图谱 (125条)
│   └── narrative/                      #    GDC叙事索引 (10条)
│
├── skills/                             # 🛠 Skills体系
│   ├── _index.md                       #    Skills总索引
│   ├── numerical_design/               #    数值策划 (909条/4 SubSkills)
│   ├── narrative_design/               #    叙事设计 (675条/6 SubSkills)
│   ├── competitor_analysis/            #    竞品分析 (864条/1 SubSkill)
│   ├── genre_knowledge/                #    品类知识 (134条/1 SubSkill)
│   ├── system_design/                  #    系统策划 (86条/2 SubSkills)
│   ├── validation/                     #    验证校验 (2条/2 SubSkills)
│   ├── gameplay_design/                #    玩法策划 (0条/1 SubSkill)
│   └── export_bridge/                  #    导出对接 (0条/1 SubSkill)
│
├── scripts/                            # 🔧 解析脚本
│   ├── parse_all.py                    #    主解析脚本
│   ├── parse_narrative.py              #    叙事解析
│   ├── parse_narrative_supplement.py   #    叙事补充
│   ├── parse_narrative_games.py        #    游戏叙事数据
│   ├── parse_final_supplement.py       #    最终补充
│   ├── parse_pc_rpg_narrative.py       #    PC RPG叙事
│   ├── parse_pcrpg_real_content.py     #    PC RPG实质内容
│   ├── parse_gap_fill.py               #    补缺脚本
│   ├── quality_cleanup.py              #    质量清洗
│   └── build_skills.py                 #    Skills构建
│
└── raw-projects/                       # 📦 原始仓库 (54个, ~7GB)
    ├── ArknightsGameData/              #    明日方舟
    ├── GenshinData/                    #    原神
    ├── StarRailData/                   #    星穹铁道
    ├── WutheringData/                  #    鸣潮
    ├── OpenRA/                         #    红警
    ├── freeciv21/                      #    文明
    ├── numeric_planner_tutorial/       #    数值策划教程
    ├── Hoyoverse-Theorycrafting-Library/  # 米哈游伤害公式
    ├── jwynia-agent-skills/            #    57个创意叙事Skills
    ├── VideoGameDialogueCorpusPublic/  #    RPG对话语料库
    ├── ... (54个仓库)
    └── README: 见 SLG游戏策划知识库资源索引.md
```

## 知识库内容质量

| 层级 | 条目数 | 占比 | 典型内容 |
|------|--------|------|---------|
| 深度 (>50KB) | 124 | 7.3% | 明日方舟章节剧情脚本、巫师3 5万行对话、帝国图书馆13MB |
| 实质 (10-50KB) | 312 | 18.5% | 数值配表、教程章节、角色档案、伤害公式 |
| 中等 (5-10KB) | 263 | 15.6% | 单个配表、方法论文章、Skill定义 |
| 轻量 (1-5KB) | 911 | 54.0% | Freeciv规则文件、GDD模板、短Skill |
| 索引 (<1KB) | 81 | 4.8% | 规则/模板索引页 |

## 游戏品类覆盖

### 数值侧
| 品类 | 游戏 | 条目 | 数据深度 |
|------|------|------|---------|
| 4X策略SLG | 文明(Freeciv) | 704 | 完整规则集(单位/建筑/科技树) |
| RTS | 红警(OpenRA) | 87 | 完整单位YAML(血量/攻击/射程/造价) |
| 开放世界ARPG | 原神 | 19 | 角色/武器/圣遗物/怪物核心配表 |
| 回合制策略RPG | 星穹铁道 | 18 | 角色/光锥/遗器/怪物配表 |
| 开放世界ARPG | 鸣潮 | 15 | 角色/武器/声骸配表 |
| 弹幕射击RPG | 碧蓝航线 | 12 | 舰船属性/成长率/装备 |
| 塔防策略RPG | 明日方舟 | 9 | 干员/技能/敌人配表 |

### 叙事侧
| 品类 | 游戏 | 条目 | 数据亮点 |
|------|------|------|---------|
| 塔防策略RPG | 明日方舟 | 110 | 5314个剧情脚本聚合（91条>10KB） |
| PC RPG | 巫师3/哈迪斯/极乐迪斯科/天际等 | 93 | 巫师3 5万行对话、极乐迪斯科39MB DB |
| 开放世界ARPG | 原神 | 66 | 62本游戏内书籍全文 |
| 4X策略/SLG | 文明/三国/红警 | 45 | 国家设定+任务简报+武将配置 |
| 弹幕射击RPG | 碧蓝航线 | 22 | 皮肤台词/故事模板/语音文本 |
| 开放世界ARPG | 鸣潮 | 13 | 好感故事/语音台词/任务文本(中文) |
| 回合制策略RPG | 星穹铁道 | 7 | 主线对话/短信/角色资料 |

## 叙事模板清单

| 模板名 | 适用品类 |
|--------|---------|
| 世界观圣经 (Lore Bible) | 通用 |
| 角色设定表 | 通用 |
| NPC档案 | 通用 |
| 阵营势力设定 | 通用 |
| 剧情大纲 | 通用 |
| 任务脚本 | 通用 |
| 对话脚本格式 | 通用 |
| 对话风格指南 | 通用 |
| 赛季叙事 | SLG |
| SLG武将传记 | SLG/策略 |
| 肉鸽事件文本 | Roguelike |
| 开放世界收集物文本 | 开放世界/ARPG |
| MOBA英雄故事 | MOBA/竞技 |

## Skills 体系

```
Agent (GameDesign Agent)
├── 数值策划 Skill (909条, 4 SubSkills)
│   ├── combat_formula     战斗公式
│   ├── growth_curve       成长曲线
│   ├── economy_model      经济建模
│   └── gacha_probability  抽卡设计
├── 叙事设计 Skill (675条, 6 SubSkills)
│   ├── world_building     世界观构建
│   ├── character_design   角色设计
│   ├── story_structure    故事结构
│   ├── quest_design       任务设计
│   ├── dialogue_writing   对话撰写
│   └── narrative_validation 叙事校验
├── 竞品分析 Skill (864条, 1 SubSkill)
├── 品类知识 Skill (134条, 1 SubSkill)
├── 系统策划 Skill (86条, 2 SubSkills)
├── 验证校验 Skill (2条, 2 SubSkills)
│   ├── narrative_consistency_check 叙事一致性
│   └── numerical_validation        数值合理性
├── 玩法策划 Skill (待填充)
└── 导出对接 Skill (待填充)
```

## 应用场景

### 超轻量（Skill 单独调用）
直接加载单个 Skill 的 `system_prompt.md` + 按 `knowledge_slice.json` 检索知识条目。

### 轻量（插件/MCP）
以 MCP Server 形式暴露 Skills，供 CodeBuddy/WorkBuddy/With 等工具调用。

### 中度（平台嵌入）
作为游戏策划能力接入 AI 游戏生成平台，提供创意讨论、剧情生成、数值验证等全流程能力。

## 数据来源

所有知识条目均来自：
1. **GitHub 开源仓库**（54 个，含 MIT/GPL 等开源协议）
2. **公开 API**（Atlas Academy FGO API）
3. **公开技术文章**（网易游戏学院、腾讯大讲堂等已公开发表的文章）

**未编造任何内容。** 每条知识条目均标注了来源仓库和原始链接。

## 构建过程

1. GitHub 搜索 → 资源评估 → 51 个资源入选
2. `git clone --depth 1` 批量下载 54 个仓库
3. Python 脚本解析（`scripts/` 目录下 10 个脚本）
4. 结构化入库（按玩法/系统/数值/综合四大分类）
5. Skills 体系构建（8 Skill / 17 SubSkill）
6. 质量清洗（删除 170 条空壳，实质条目占比提升至 41.4%）
