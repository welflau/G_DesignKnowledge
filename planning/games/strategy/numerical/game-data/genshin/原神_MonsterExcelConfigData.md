# 原神 · 怪物基础属性 (MonsterExcelConfigData)

> 来源：Sycamore0/GenshinData
> 游戏类型：开放世界ARPG
> 分类：数值配表
> 标签：原神, 角色数值, 武器, 圣遗物, 怪物, 经济系统

## 概述

原神怪物基础属性，共 **1086** 条记录。

## 数据字段

```
monsterName, type, scriptDataPathHash, serverScript, LBODGAEPDMJ, affix, ai, isAIHashCheck, equips, hpDrops, killDropId, excludeWeathers, featureTagGroupID, mpPropID, skin, describeId, combatBGMLevel, entityBudgetLevel, hpBase, attackBase, defenseBase, fireSubHurt, grassSubHurt, waterSubHurt, elecSubHurt, windSubHurt, iceSubHurt, rockSubHurt, propGrowCurves, physicalSubHurt, BCAGNCKHFOF, prefabPathHash, id, nameTextMapHash, NOLCALJMBOB, prefabPathRemoteHash, controllerPathHash, controllerPathRemoteHash, campID, LODPatternName
```

## 数据样本（首条）

```json
{
  "monsterName": "Hili_None_01",
  "type": "MONSTER_ORDINARY",
  "scriptDataPathHash": 4553677246385808667,
  "serverScript": "",
  "LBODGAEPDMJ": 4026676864005180208,
  "affix": [],
  "ai": "sentry02",
  "isAIHashCheck": true,
  "equips": [
    0,
    0
  ],
  "hpDrops": [
    {
      "dropId": 22010010,
      "hpPercent": 60.0
    },
    {},
    {}
  ],
  "killDropId": 22010010,
  "excludeWeathers": "",
  "featureTagGroupID": 21010101,
  "mpPropID": 1,
  "skin": "",
  "describeId": 10101,
  "combatBGMLevel": 1,
  "entityBudgetLevel": 8,
  "hpBase": 13.583999633789062,
  "attackBase": 22.607999801635742,
  "defenseBase": 500.0,
  "fireSubHurt": 0.10000000149011612,
  "grassSubHurt": 0.10000000149011612,
  "waterSubHurt": 0.10000000149011612,
  "elecSubHurt": 0.10000000149011612,
  "windSubHurt": 0.10000000149011612,
  "iceSubHurt": 0.10000000149011612,
  "rockSubHurt": 0.10000000149011612,
  "propGrowCurves": [
    {
      "type": "FIGHT_PROP_BASE_HP",
      "growCurve": "GROW_CURVE_HP"
    },
    {
      "type": "FIGHT_PROP_BASE_ATTACK",
      "growCurve": "GROW_CURVE_ATTACK"
    },
    {
      "type": "FIGHT_PROP_BASE_DEFENSE",
      "growCurve": "GROW_CURVE_DEFENSE"
    }
  ],
  "physicalSubHurt": 0.10000000149011612,
  "BCAGNCKHFOF": 15212055206618285176,
  "prefabPathHash": 3473646457669116396,
  "id": 21010101,
  "nameTextMapHash": 2561869233,
  "NOLCALJMBOB": 2956196180941222287,
  "prefabPathRemoteHash": 2950433170534692371,
  "controllerPathHash": 13507751526928566456,
  "controllerPathRemoteHash": 5878507644683305958,
  "campID": 4001,
  "LODPatternName": ""
}
```

## 策划参考价值

该配表可用于分析原神的怪物基础属性设计，包括数值区间、成长曲线斜率、资源投放节奏等。
