# SLG 游戏策划知识库 · 应用架构设计

> 版本：v1.0 | 2026-04-16
> 核心理念：知识库 → Skills化 → 三层接入（超轻量/轻量/中度）

---

## 一、整体架构

```
┌─────────────────────────────────────────────────────────────┐
│                    接入层 (Integration Layer)                 │
│                                                             │
│  ┌──────────┐  ┌──────────┐  ┌──────────────────────────┐  │
│  │ 超轻量级  │  │  轻量级   │  │       中度应用            │  │
│  │ Skills   │  │  插件     │  │    多平台策划能力嵌入      │  │
│  │ 单独调用  │  │ CodeBuddy│  │  AI游戏生成平台           │  │
│  │          │  │ WorkBuddy│  │  Unity/UE对接             │  │
│  │          │  │ With     │  │  美术资产生成对接          │  │
│  └────┬─────┘  └────┬─────┘  └──────────┬───────────────┘  │
│       │             │                    │                   │
└───────┼─────────────┼────────────────────┼───────────────────┘
        │             │                    │
        ▼             ▼                    ▼
┌─────────────────────────────────────────────────────────────┐
│                  编排层 (Orchestration Layer)                 │
│                                                             │
│  ┌─────────────────────────────────────────────────────┐    │
│  │              GameDesign Agent (主Agent)               │    │
│  │                                                     │    │
│  │  职责：理解用户意图 → 拆解任务 → 调度Skills → 整合输出  │    │
│  │  模式：                                              │    │
│  │    A. 对话模式 — 创意讨论/方案评审/需求澄清            │    │
│  │    B. 生成模式 — 策划案/数值表/文案 生成               │    │
│  │    C. 验证模式 — 数值校验/平衡性分析/一致性检查         │    │
│  │    D. 导出模式 — 对接Unity/UE/美术资产生成             │    │
│  └──────────────────────┬──────────────────────────────┘    │
│                         │                                    │
│                    Skills调度                                │
│                         │                                    │
└─────────────────────────┼────────────────────────────────────┘
                          │
                          ▼
┌─────────────────────────────────────────────────────────────┐
│                   能力层 (Skills Layer)                       │
│                                                             │
│  ┌─────────┐ ┌─────────┐ ┌─────────┐ ┌─────────┐          │
│  │ Skill-1 │ │ Skill-2 │ │ Skill-3 │ │ Skill-4 │          │
│  │ 剧情策划 │ │ 玩法策划 │ │ 数值策划 │ │ 系统策划 │          │
│  └────┬────┘ └────┬────┘ └────┬────┘ └────┬────┘          │
│       │           │           │           │                 │
│  ┌─────────┐ ┌─────────┐ ┌─────────┐ ┌─────────┐          │
│  │ Skill-5 │ │ Skill-6 │ │ Skill-7 │ │ Skill-8 │          │
│  │ 品类知识 │ │ 竞品分析 │ │ 导出对接 │ │ 验证校验 │          │
│  └────┬────┘ └────┬────┘ └────┬────┘ └────┬────┘          │
│       │           │           │           │                 │
└───────┼───────────┼───────────┼───────────┼─────────────────┘
        │           │           │           │
        ▼           ▼           ▼           ▼
┌─────────────────────────────────────────────────────────────┐
│                   知识层 (Knowledge Layer)                    │
│                                                             │
│  ┌───────────┐ ┌───────────┐ ┌───────────┐ ┌───────────┐   │
│  │ gameplay/ │ │  system/  │ │numerical/ │ │comprehen/ │   │
│  │ 玩法知识库 │ │ 系统知识库 │ │ 数值知识库 │ │ 综合知识库 │   │
│  │   4条     │ │  67条     │ │  875条    │ │  125条    │   │
│  └───────────┘ └───────────┘ └───────────┘ └───────────┘   │
│                                                             │
│  知识检索方式：标签匹配 + 语义搜索 + 结构化查询               │
└─────────────────────────────────────────────────────────────┘
```

---

## 二、Skills 体系设计

### 2.1 Skills 总览

每个 Skill 是一个**独立可调用的能力单元**，内含 SubSkills。
Skill 之间可组合编排，也可单独使用。

```
GameDesign Agent
├── Skill-1: 剧情策划 (narrative_design)
│   ├── SubSkill: 世界观构建
│   ├── SubSkill: 角色设计
│   ├── SubSkill: 剧情大纲生成
│   ├── SubSkill: 任务/对话文案
│   └── SubSkill: 剧情一致性校验
│
├── Skill-2: 玩法策划 (gameplay_design)
│   ├── SubSkill: 核心循环设计
│   ├── SubSkill: 玩法机制选型
│   ├── SubSkill: 关卡/地图设计
│   ├── SubSkill: 交互流程设计
│   └── SubSkill: 玩法文档生成 (GDD片段)
│
├── Skill-3: 数值策划 (numerical_design)
│   ├── SubSkill: 战斗公式设计
│   ├── SubSkill: 成长曲线设计
│   ├── SubSkill: 经济系统建模
│   ├── SubSkill: 抽卡/概率设计
│   ├── SubSkill: 商业化数值
│   ├── SubSkill: 数值配表生成
│   └── SubSkill: 数值平衡验证
│
├── Skill-4: 系统策划 (system_design)
│   ├── SubSkill: 系统架构设计
│   ├── SubSkill: 功能模块拆解
│   ├── SubSkill: 系统文档生成 (GDD)
│   ├── SubSkill: 数据结构设计
│   └── SubSkill: UI/交互流程图
│
├── Skill-5: 品类知识 (genre_knowledge)
│   ├── SubSkill: SLG品类知识
│   ├── SubSkill: 肉鸽品类知识
│   ├── SubSkill: 塔防品类知识
│   ├── SubSkill: 卡牌品类知识
│   └── SubSkill: 品类混搭方案
│
├── Skill-6: 竞品分析 (competitor_analysis)
│   ├── SubSkill: 数值拆解
│   ├── SubSkill: 系统拆解
│   ├── SubSkill: 玩法对比
│   └── SubSkill: 数据检索 (从game-data中检索)
│
├── Skill-7: 导出对接 (export_bridge)
│   ├── SubSkill: Unity配表导出 (CSV/JSON/ScriptableObject)
│   ├── SubSkill: UE配表导出 (DataTable/JSON)
│   ├── SubSkill: 美术方向Brief生成
│   ├── SubSkill: UI列表导出
│   └── SubSkill: API格式输出 (供平台调用)
│
└── Skill-8: 验证校验 (validation)
    ├── SubSkill: 数值一致性校验
    ├── SubSkill: 经济平衡模拟
    ├── SubSkill: 战斗模拟验算
    ├── SubSkill: 文案风格一致性检查
    └── SubSkill: 系统完整性检查
```

### 2.2 各 Skill 与知识库的映射关系

```
Skill                    主知识库           辅助知识库
──────────────────────────────────────────────────────
Skill-1 剧情策划    →   comprehensive/    gameplay/
Skill-2 玩法策划    →   gameplay/         system/
Skill-3 数值策划    →   numerical/        gameplay/
Skill-4 系统策划    →   system/           numerical/
Skill-5 品类知识    →   gameplay/ + numerical/game-data/
Skill-6 竞品分析    →   numerical/game-data/ (全部游戏数据)
Skill-7 导出对接    →   system/           numerical/
Skill-8 验证校验    →   numerical/        system/
```

---

## 三、Skill 调用协议设计

### 3.1 统一调用接口

每个 Skill/SubSkill 遵循统一的输入输出协议，保证可独立调用也可被Agent编排：

```yaml
# Skill 调用协议
skill_call:
  skill_id: "numerical_design"           # Skill标识
  sub_skill_id: "combat_formula"          # SubSkill标识（可选，不传则由Skill自行判断）
  intent: "设计一个SLG的战斗伤害公式"       # 用户意图/任务描述
  context:                                # 上下文（上游Skill输出、项目信息等）
    project_genre: "SLG"
    project_theme: "三国"
    previous_outputs: []                  # 前序Skill的输出
  parameters:                             # 任务参数
    damage_model: "乘法"                  # 特定参数
    include_defense: true
  output_format: "markdown"               # 输出格式：markdown / json / csv / unity_scriptable

# Skill 返回协议
skill_response:
  skill_id: "numerical_design"
  sub_skill_id: "combat_formula"
  status: "success"
  result:
    content: "..."                        # 主内容（MD/JSON/CSV）
    metadata:
      knowledge_refs: [...]               # 引用了哪些知识条目
      confidence: 0.85                    # 置信度
      suggestions: [...]                  # 建议后续调用的Skill
  exportable:                             # 可导出数据（供Skill-7使用）
    tables: [...]                         # 配表数据
    constants: {...}                      # 常量定义
    formulas: [...]                       # 公式定义
```

### 3.2 知识检索协议

SubSkill 调用知识库时的标准流程：

```
SubSkill 执行逻辑
│
├── 1. 意图解析 → 确定需要什么知识
│
├── 2. 知识检索 (三种方式)
│   ├── 标签匹配：按 [分类+标签] 精确检索
│   │   例：category="numerical", tags=["伤害公式", "乘区体系"]
│   │
│   ├── 语义搜索：对知识条目的"概述"和"正文"做向量检索
│   │   例：query="SLG兵种克制的伤害加成怎么设计"
│   │
│   └── 结构化查询：直接查game-data下的JSON配表
│       例：game="arknights", table="character_table", field="phases[0].attributesKeyFrames"
│
├── 3. 知识注入 → 将检索到的知识作为prompt context
│
├── 4. 生成/推理 → LLM 基于知识生成策划内容
│
└── 5. 输出标准化 → 按 skill_response 协议输出
```

---

## 四、三种接入形态详细设计

### 4.1 超轻量级 — Skills 单独调用

```
场景：策划在任意工具中（IDE、文档、聊天框）直接调用单个Skill
形态：类似ChatGPT的Function Calling / CodeBuddy的Skill

调用方式：
  用户："帮我设计一个SLG的资源产出公式"
  → 路由到 Skill-3 (数值策划) → SubSkill: 经济系统建模
  → 检索知识库 numerical/economy-model/ + numerical/game-data/
  → 输出策划方案

技术实现：
  - 每个Skill对应一个独立的 system prompt + 知识库切片
  - 打包为标准的 skill.json 定义文件
  - 可被任何支持skills协议的Agent框架加载
```

**Skill定义文件结构**：
```
skills/
├── narrative_design/
│   ├── skill.json              # Skill元信息（名称/描述/输入输出schema）
│   ├── system_prompt.md        # System Prompt
│   ├── sub_skills/
│   │   ├── world_building.md   # SubSkill的专项prompt
│   │   ├── character_design.md
│   │   └── ...
│   └── knowledge_slice.json    # 该Skill引用的知识条目ID列表
│
├── gameplay_design/
│   ├── skill.json
│   ├── system_prompt.md
│   ├── sub_skills/
│   └── knowledge_slice.json
│
├── numerical_design/
│   ├── skill.json
│   ├── system_prompt.md
│   ├── sub_skills/
│   │   ├── combat_formula.md
│   │   ├── growth_curve.md
│   │   ├── economy_model.md
│   │   ├── gacha_design.md
│   │   ├── monetization.md
│   │   ├── table_generation.md
│   │   └── balance_validation.md
│   └── knowledge_slice.json
│
├── system_design/
├── genre_knowledge/
├── competitor_analysis/
├── export_bridge/
└── validation/
```

### 4.2 轻量级 — 插件能力

```
场景：作为插件嵌入 CodeBuddy / WorkBuddy / With 等工具平台
形态：MCP Server 或 平台原生插件

能力边界：
  - 可调用单个Skill
  - 可调用Agent（多Skill编排）
  - 可访问完整知识库
  - 支持上下文持久化（项目级记忆）

技术实现：
  - MCP Server 模式：暴露 tools（每个Skill一个tool）
  - 插件模式：平台SDK集成，注册Skill列表
  - 知识库以 嵌入向量+MD文件 双模式存储
```

**MCP Server tools 注册示例**：
```json
{
  "tools": [
    {
      "name": "game_narrative_design",
      "description": "游戏剧情策划：世界观构建、角色设计、剧情生成、文案撰写",
      "parameters": {
        "task": "string - 具体任务描述",
        "genre": "string - 游戏品类(SLG/Roguelike/...)",
        "context": "object - 项目上下文"
      }
    },
    {
      "name": "game_numerical_design",
      "description": "游戏数值策划：战斗公式、成长曲线、经济系统、配表生成",
      "parameters": {
        "task": "string",
        "genre": "string",
        "output_format": "markdown|json|csv|unity|unreal"
      }
    },
    {
      "name": "game_system_design",
      "description": "游戏系统策划：系统架构、GDD生成、功能模块拆解"
    },
    {
      "name": "game_competitor_analysis",
      "description": "竞品分析：数值拆解、系统对比、数据检索"
    },
    {
      "name": "game_export",
      "description": "导出对接：Unity/UE配表导出、美术Brief、UI列表"
    },
    {
      "name": "game_validate",
      "description": "验证校验：数值平衡模拟、经济系统压测、一致性检查"
    }
  ]
}
```

### 4.3 中度应用 — 多平台策划能力嵌入

```
场景：作为核心策划能力引擎，嵌入AI游戏生成平台
形态：Agent + Skills 完整链路，支持全流程编排

完整工作流示例（SLG策划案生成）：

用户输入："帮我做一个三国题材SLG手游的完整策划案"

Agent 编排：
  Step 1: Skill-5(品类知识/SLG) → 获取SLG品类框架和核心要素
  Step 2: Skill-1(剧情策划) → 世界观 + 核心角色设定
  Step 3: Skill-2(玩法策划) → 核心循环 + 玩法机制
  Step 4: Skill-4(系统策划) → 系统架构 + GDD框架
  Step 5: Skill-3(数值策划) → 战斗/经济/成长数值体系
  Step 6: Skill-8(验证校验) → 数值平衡验证
  Step 7: Skill-7(导出对接) → Unity配表 + 美术Brief + UI列表

每步的输出作为下步的context输入，形成完整策划案。
```

**平台API接口设计**：
```yaml
# REST API
POST /api/v1/design/create
{
  "project": {
    "name": "三国霸业",
    "genre": "SLG",
    "platform": "mobile",
    "theme": "三国"
  },
  "tasks": [
    {"skill": "gameplay_design", "sub_skill": "core_loop"},
    {"skill": "numerical_design", "sub_skill": "combat_formula"},
    {"skill": "system_design", "sub_skill": "gdd_generation"}
  ],
  "output": {
    "format": "full_gdd",
    "export_targets": ["unity_json", "art_brief", "ui_list"]
  }
}

# WebSocket (流式输出)
WS /api/v1/design/stream
→ 实时推送各Skill的生成进度和中间结果
```

---

## 五、知识库的运行时使用方式

### 5.1 知识库不是直接喂给LLM，而是按需检索注入

```
                    用户请求
                       │
                       ▼
              ┌─────────────────┐
              │  意图识别 & 路由  │
              └────────┬────────┘
                       │
                       ▼
              ┌─────────────────┐
              │  知识检索引擎     │
              │                 │
              │  输入：意图+品类  │
              │  策略：           │
              │  1. 先按标签过滤  │
              │  2. 再语义排序   │
              │  3. Top-K 召回   │
              └────────┬────────┘
                       │
              ┌────────┴────────┐
              │   检索结果        │
              │  (3~10条知识)     │
              └────────┬────────┘
                       │
                       ▼
              ┌─────────────────┐
              │  Prompt 组装     │
              │                 │
              │  = System Prompt │
              │  + 知识上下文     │
              │  + 用户请求      │
              │  + 输出格式要求   │
              └────────┬────────┘
                       │
                       ▼
              ┌─────────────────┐
              │   LLM 生成       │
              └────────┬────────┘
                       │
                       ▼
              ┌─────────────────┐
              │  后处理 & 校验    │
              │  (Skill-8)      │
              └─────────────────┘
```

### 5.2 知识条目在各场景的使用举例

| 用户请求 | 路由Skill | 检索的知识条目 | 输出 |
|---------|----------|--------------|------|
| "设计SLG伤害公式" | Skill-3/战斗公式 | `numerical/damage-formula/伤害公式_原神_*.md` + `numerical/game-data/openra/*.md` | 伤害公式方案+参数表 |
| "参考明日方舟设计干员成长" | Skill-6/数值拆解 + Skill-3/成长曲线 | `numerical/game-data/arknights/明日方舟_character_table.md` | 成长曲线方案+配表 |
| "做SLG经济系统" | Skill-3/经济建模 | `numerical/math-models/数学模型_model_03_economic_control.md` + `numerical/数值教程_第5章*.md` | 经济系统方案+模拟 |
| "写一个完整的GDD" | Skill-4/GDD生成 | `system/gdd-templates/GDD模板_*.md` (全部) | 完整GDD文档 |
| "对比红警和文明的兵种设计" | Skill-6/竞品对比 | `numerical/game-data/openra/*.md` + `numerical/game-data/freeciv/*.md` | 对比分析报告 |
| "导出到Unity" | Skill-7/Unity导出 | (使用前序Skill的输出) | CSV/JSON/ScriptableObject |

---

## 六、落地路线图

### Phase 1：近期（Skill原型验证）

```
目标：完成核心Skills的prompt工程和知识库对接

Week 1-2:
  [x] 知识库构建完成（1071条）
  [ ] 编写8个Skill的system_prompt.md
  [ ] 编写每个SubSkill的专项prompt
  [ ] 为每个Skill配置knowledge_slice.json

Week 3-4:
  [ ] 以CodeBuddy Skill形式发布 Skill-1(剧情) + Skill-3(数值)
  [ ] 内部策划试用，收集反馈
  [ ] 基于反馈调整prompt和知识检索策略

产出物：
  skills/narrative_design/    → 可在CodeBuddy中直接@调用
  skills/numerical_design/    → 可在CodeBuddy中直接@调用
```

### Phase 2：中期（插件化 + 平台接入）

```
目标：8个Skill全量上线 + MCP Server + 平台API

Month 2-3:
  [ ] 完成全部8个Skill上线
  [ ] 搭建MCP Server，注册所有Skill为tools
  [ ] 实现知识库向量化（embedding），支持语义搜索
  [ ] 接入AI游戏生成平台，暴露REST/WS API
  [ ] 实现Skill-7导出能力（Unity/UE配表格式）

Month 3-4:
  [ ] Agent编排能力：多Skill串联生成完整策划案
  [ ] 项目级记忆：支持按项目持久化上下文
  [ ] 扩充肉鸽/卡牌品类知识库

产出物：
  mcp-server/                 → MCP Server（可被任何MCP客户端调用）
  api-server/                 → REST/WS API（供平台嵌入）
  skills/ (全量)              → 8个Skill完整定义
```

### Phase 3：未来（全链路打通）

```
目标：策划案 → 配表 → 美术Brief → 游戏资产 一键贯通

  [ ] Skill-7对接Unity Editor插件（一键导入配表）
  [ ] Skill-7对接UE DataTable导入
  [ ] Skill-7生成美术资产生成prompt（对接图片/模型生成平台）
  [ ] 以插件形式落地CodeBuddy/WorkBuddy/With
  [ ] 知识库持续扩充（新品类/新游戏数据/行业报告）

产出物：
  unity-plugin/               → Unity Editor Plugin
  ue-plugin/                  → UE Plugin
  codebuddy-skill/            → CodeBuddy原生Skill包
  workbuddy-plugin/           → WorkBuddy插件
```

---

## 七、Skill 定义文件标准 (skill.json)

```json
{
  "id": "numerical_design",
  "name": "数值策划",
  "version": "1.0.0",
  "description": "游戏数值策划能力：战斗公式、成长曲线、经济系统、抽卡概率、商业化数值、配表生成、平衡验证",
  "author": "GameDesign-AI",
  "tags": ["数值", "策划", "SLG", "平衡"],

  "sub_skills": [
    {
      "id": "combat_formula",
      "name": "战斗公式设计",
      "prompt_file": "sub_skills/combat_formula.md",
      "knowledge_tags": ["伤害公式", "战斗数值", "乘区体系"],
      "knowledge_games": ["arknights", "genshin", "openra"],
      "output_formats": ["markdown", "json", "latex"]
    },
    {
      "id": "growth_curve",
      "name": "成长曲线设计",
      "prompt_file": "sub_skills/growth_curve.md",
      "knowledge_tags": ["成长曲线", "经验", "属性", "突破"],
      "knowledge_games": ["arknights", "genshin", "fgo"],
      "output_formats": ["markdown", "json", "csv"]
    },
    {
      "id": "economy_model",
      "name": "经济系统建模",
      "prompt_file": "sub_skills/economy_model.md",
      "knowledge_tags": ["经济系统", "通胀控制", "产出消耗"],
      "knowledge_games": ["freeciv", "openra"],
      "output_formats": ["markdown", "json", "python"]
    },
    {
      "id": "gacha_design",
      "name": "抽卡/概率设计",
      "prompt_file": "sub_skills/gacha_design.md",
      "knowledge_tags": ["抽卡概率", "保底", "掉落"],
      "knowledge_games": ["arknights", "genshin", "fgo"],
      "output_formats": ["markdown", "json"]
    },
    {
      "id": "monetization",
      "name": "商业化数值",
      "prompt_file": "sub_skills/monetization.md",
      "knowledge_tags": ["商业化", "付费深度", "定价"],
      "output_formats": ["markdown", "json"]
    },
    {
      "id": "table_generation",
      "name": "数值配表生成",
      "prompt_file": "sub_skills/table_generation.md",
      "knowledge_tags": ["配表", "数据结构"],
      "output_formats": ["csv", "json", "unity_scriptable", "ue_datatable"]
    },
    {
      "id": "balance_validation",
      "name": "数值平衡验证",
      "prompt_file": "sub_skills/balance_validation.md",
      "knowledge_tags": ["平衡", "PVP", "Meta"],
      "output_formats": ["markdown", "json", "python"]
    }
  ],

  "knowledge_base": {
    "primary": "numerical/",
    "secondary": ["gameplay/", "system/"],
    "retrieval_strategy": {
      "method": "hybrid",
      "tag_weight": 0.4,
      "semantic_weight": 0.6,
      "top_k": 8
    }
  },

  "interfaces": {
    "standalone": true,
    "mcp_tool": true,
    "rest_api": true,
    "codebuddy_skill": true,
    "workbuddy_plugin": true
  }
}
```

---

## 八、知识库维护与扩展

### 扩展新品类

```bash
# 以"肉鸽品类"为例
# 1. 在raw-projects下载肉鸽相关数据
git clone --depth 1 https://github.com/xxx/SlaytTheSpireData.git

# 2. 在知识库中增加品类子目录
mkdir -p gameplay/genre-design/roguelike
mkdir -p numerical/game-data/slay-the-spire

# 3. 在scripts/中增加解析逻辑
# 4. 运行 python3 scripts/parse_all.py

# 5. 在Skill-5(品类知识)中新增SubSkill
#    skills/genre_knowledge/sub_skills/roguelike.md
```

### 扩展新游戏数据

```bash
# 以"星穹铁道"为例
git clone --depth 1 https://github.com/gffice/StarRailData.git
mkdir -p numerical/game-data/starrail
# 在parse_all.py中增加 parse_starrail() 函数
```

### 知识条目质量保证

```
每个知识条目必须包含：
  ✅ 来源可追溯（仓库+文件路径+URL）
  ✅ 分类和标签准确
  ✅ 正文内容完整不截断
  ✅ 策划参考价值说明

定期维护：
  - 每月检查数据仓库更新，重新抓取
  - 每季度根据策划反馈调整分类和标签体系
  - 新游戏上线时及时补充竞品数据
```
