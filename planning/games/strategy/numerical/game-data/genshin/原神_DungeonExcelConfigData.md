# 原神 · 副本配置 (DungeonExcelConfigData)

> 来源：Sycamore0/GenshinData
> 游戏类型：开放世界ARPG
> 分类：数值配表
> 标签：原神, 角色数值, 武器, 圣遗物, 怪物, 经济系统

## 概述

原神副本配置，共 **1091** 条记录。

## 数据字段

```
id, nameTextMapHash, displayNameTextMapHash, descTextMapHash, type, sceneId, involveType, showLevel, limitLevel, levelRevise, passCond, reviveMaxCount, dayEnterCount, NCLKDKLALLO, passRewardPreviewID, settleCountdownTime, failSettleCountdownTime, quitSettleCountdownTime, settleShows, forbiddenRestart, settleUIType, recommendElementTypes, FCIHFKMEOFP, levelConfigMap, enterCostItems, LNOEMAGHKHE, cityID, entryPicPath, stateType, NFAKBEOGMBE, MHKKLAHHJNJ, KPAJMBIABHF, ILPDHCPNEBJ
```

## 数据样本（首条）

```json
{
  "id": 1,
  "nameTextMapHash": 1128700336,
  "displayNameTextMapHash": 3399830258,
  "descTextMapHash": 178671925,
  "type": "DUNGEON_PLOT",
  "sceneId": 20008,
  "involveType": "INVOLVE_ONLY_SINGLE",
  "showLevel": 5,
  "limitLevel": 1,
  "levelRevise": 4,
  "passCond": 8,
  "reviveMaxCount": 10,
  "dayEnterCount": 1,
  "NCLKDKLALLO": [
    {}
  ],
  "passRewardPreviewID": 10001,
  "settleCountdownTime": 999,
  "failSettleCountdownTime": 30,
  "quitSettleCountdownTime": 3,
  "settleShows": [
    "SETTLE_SHOW_NONE",
    "SETTLE_SHOW_NONE",
    "SETTLE_SHOW_NONE",
    "SETTLE_SHOW_BLACKSCREEN"
  ],
  "forbiddenRestart": true,
  "settleUIType": "SETTLE_UI_ON_FAIL",
  "recommendElementTypes": [
    "None",
    "None",
    "None",
    "None"
  ],
  "FCIHFKMEOFP": [],
  "levelConfigMap": {},
  "enterCostItems": [
    20011001,
    20011201,
    20011301,
    21010201
  ],
  "LNOEMAGHKHE": 2404742793,
  "cityID": 1,
  "entryPicPath": "UI_DungeonPic_Kaeya",
  "stateType": "DUNGEON_STATE_RELEASE",
  "NFAKBEOGMBE": "",
  "MHKKLAHHJNJ": "",
  "KPAJMBIABHF": 388980769,
  "ILPDHCPNEBJ": 2109597111
}
```

## 策划参考价值

该配表可用于分析原神的副本设计，包括数值区间、成长曲线斜率、资源投放节奏等。
