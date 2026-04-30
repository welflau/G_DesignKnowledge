# 崩坏：星穹铁道 · 关卡配置 (StageConfig)

> 来源：gffice/StarRailData
> 游戏类型：回合制策略RPG
> 分类：数值配表
> 标签：星穹铁道, 角色数值, 光锥, 遗器, 怪物, 关卡

## 概述

星穹铁道关卡配置，共 **15404** 条记录。

## 数据字段

```
StageID, StageType, StageName, HardLevelGroup, Level, LevelGraphPath, StageAbilityConfig, SubLevelGraphs, StageConfigData, MonsterList, LevelLoseCondition, LevelWinCondition, ForbidExitBattle, TrialAvatarList
```

## 数据样本（首条）

```json
{
  "StageID": 1,
  "StageType": "Mainline",
  "StageName": {
    "Hash": 2132921139
  },
  "HardLevelGroup": 1,
  "Level": 1,
  "LevelGraphPath": "Config/Level/TestLevel/ATestLevel_1_1.json",
  "StageAbilityConfig": [],
  "SubLevelGraphs": [],
  "StageConfigData": [
    {
      "DJBGPLLGOEF": "_Wave",
      "BOANKOCFAIM": "1"
    },
    {
      "DJBGPLLGOEF": "_IsEliteBattle",
      "BOANKOCFAIM": "0"
    }
  ],
  "MonsterList": [
    {
      "Monster0": 1002040
    }
  ],
  "LevelLoseCondition": [],
  "LevelWinCondition": [],
  "ForbidExitBattle": true,
  "TrialAvatarList": []
}
```

## 策划参考价值

可用于分析星穹铁道回合制战斗系统的关卡设计。
