# 崩坏：星穹铁道 · 怪物基础配置 (MonsterConfig)

> 来源：gffice/StarRailData
> 游戏类型：回合制策略RPG
> 分类：数值配表
> 标签：星穹铁道, 角色数值, 光锥, 遗器, 怪物, 关卡

## 概述

星穹铁道怪物基础配置，共 **881** 条记录。

## 数据字段

```
MonsterID, MonsterTemplateID, MonsterName, MonsterIntroduction, MonsterBattleIntroduction, HardLevelGroup, EliteGroup, AttackModifyRatio, DefenceModifyRatio, HPModifyRatio, SpeedModifyRatio, StanceModifyRatio, SkillList, CustomValues, DynamicValues, DebuffResist, CustomValueTags, StanceWeakList, DamageTypeResistance, AbilityNameList, OverrideAIPath, OverrideAISkillSequence
```

## 数据样本（首条）

```json
{
  "MonsterID": 1002040,
  "MonsterTemplateID": 1002040,
  "MonsterName": {
    "Hash": 2132921139
  },
  "MonsterIntroduction": {
    "Hash": -1438824662
  },
  "MonsterBattleIntroduction": {
    "Hash": 371857150
  },
  "HardLevelGroup": 1,
  "EliteGroup": 1,
  "AttackModifyRatio": {
    "Value": 1
  },
  "DefenceModifyRatio": {
    "Value": 1
  },
  "HPModifyRatio": {
    "Value": 1
  },
  "SpeedModifyRatio": {
    "Value": 1
  },
  "StanceModifyRatio": {
    "Value": 1
  },
  "SkillList": [
    100204001
  ],
  "CustomValues": [],
  "DynamicValues": [],
  "DebuffResist": [],
  "CustomValueTags": [
    "W1_Soldier"
  ],
  "StanceWeakList": [
    "Wind",
    "Quantum"
  ],
  "DamageTypeResistance": [
    {
      "DamageType": "Physical",
      "Value": {
        "Value": 0.2
      }
    },
    {
      "DamageType": "Fire",
      "Value": {
        "Value": 0.2
      }
    },
    {
      "DamageType": "Ice",
      "Value": {
        "Value": 0.2
      }
    },
    {
      "DamageType": "Thunder",
      "Value": {
        "Value": 0.2
      }
    },
    {
      "DamageType": "Imaginary",
      "Value": {
        "Value": 0.2
      }
    }
  ],
  "AbilityNameList": [],
  "OverrideAIPath": "",
  "OverrideAISkillSequence": []
}
```

## 策划参考价值

可用于分析星穹铁道回合制战斗系统的怪物基础设计。
