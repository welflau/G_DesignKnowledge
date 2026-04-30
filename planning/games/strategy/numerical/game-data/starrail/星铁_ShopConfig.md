# 崩坏：星穹铁道 · 商店配置 (ShopConfig)

> 来源：gffice/StarRailData
> 游戏类型：回合制策略RPG
> 分类：数值配表
> 标签：星穹铁道, 角色数值, 光锥, 遗器, 怪物, 关卡

## 概述

星穹铁道商店配置，共 **54** 条记录。

## 数据字段

```
ShopID, ShopMainType, ShopType, ShopName, ShopDesc, ShopIconPath, ShopBar, ShopSortID, LimitType1, LimitValue1List, LimitValue2List, IsOpen, ScheduleDataID, HideRemainTime
```

## 数据样本（首条）

```json
{
  "ShopID": 101,
  "ShopMainType": "Main",
  "ShopType": 1,
  "ShopName": {
    "Hash": -33573267
  },
  "ShopDesc": {
    "Hash": 1455825039
  },
  "ShopIconPath": "SpriteOutput/TabIcon/Shop/ShopDrawcardIcon02.png",
  "ShopBar": "Shop101Page",
  "ShopSortID": 1,
  "LimitType1": "Level",
  "LimitValue1List": [
    1
  ],
  "LimitValue2List": [],
  "IsOpen": true,
  "ScheduleDataID": 300101,
  "HideRemainTime": true
}
```

## 策划参考价值

可用于分析星穹铁道回合制战斗系统的商店设计。
