# 崩坏：星穹铁道 · 怪物技能配置 (MonsterSkillConfig)

> 来源：gffice/StarRailData
> 游戏类型：回合制策略RPG
> 分类：数值配表
> 标签：星穹铁道, 角色数值, 光锥, 遗器, 怪物, 关卡

## 概述

星穹铁道怪物技能配置，共 **1198** 条记录。

## 数据字段

```
SkillID, SkillName, IconPath, SkillDesc, SkillTypeDesc, SkillTag, PhaseList, ExtraEffectIDList, DamageType, SkillTriggerKey, SPHitBase, DelayRatio, ParamList, AttackType, AI_CD, AI_ICD
```

## 数据样本（首条）

```json
{
  "SkillID": 100204001,
  "SkillName": {
    "Hash": -971210765
  },
  "IconPath": "SpriteOutput/SkillIcons/1001/SkillIcon_1001_Maze.png",
  "SkillDesc": {
    "Hash": -2007296235
  },
  "SkillTypeDesc": {
    "Hash": 616571728
  },
  "SkillTag": {
    "Hash": 492104905
  },
  "PhaseList": [
    1
  ],
  "ExtraEffectIDList": [],
  "DamageType": "Physical",
  "SkillTriggerKey": "Skill01",
  "SPHitBase": {
    "Value": 10
  },
  "DelayRatio": {
    "Value": 1
  },
  "ParamList": [
    {
      "Value": 3
    },
    {
      "Value": 0.5
    },
    {
      "Value": 2
    }
  ],
  "AttackType": "Normal",
  "AI_CD": 1,
  "AI_ICD": 1
}
```

## 策划参考价值

可用于分析星穹铁道回合制战斗系统的怪物技能设计。
