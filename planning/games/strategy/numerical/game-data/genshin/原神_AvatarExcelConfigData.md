# 原神 · 角色基础属性 (AvatarExcelConfigData)

> 来源：Sycamore0/GenshinData
> 游戏类型：开放世界ARPG
> 分类：数值配表
> 标签：原神, 角色数值, 武器, 圣遗物, 怪物, 经济系统

## 概述

原神角色基础属性，共 **98** 条记录。

## 数据字段

```
bodyType, scriptDataPathHash, iconName, sideIconName, qualityType, chargeEfficiency, LBODGAEPDMJ, initialWeapon, weaponType, NIPILHLOMDG, imageName, gachaCardNameHash, manekinPathHash, cutsceneShow, skillDepotId, staminaRecoverSpeed, candSkillDepotIds, manekinJsonConfigHash, manekinMotionConfig, descTextMapHash, avatarIdentityType, avatarPromoteId, avatarPromoteRewardLevelList, avatarPromoteRewardIdList, featureTagGroupID, infoDescTextMapHash, hpBase, attackBase, defenseBase, critical, criticalHurt, propGrowCurves, BCAGNCKHFOF, prefabPathHash, id, nameTextMapHash, NOLCALJMBOB, prefabPathRemoteHash, controllerPathHash, controllerPathRemoteHash, LODPatternName
```

## 数据样本（首条）

```json
{
  "bodyType": "BODY_GIRL",
  "scriptDataPathHash": 17851432353698653922,
  "iconName": "UI_AvatarIcon_Kate",
  "sideIconName": "UI_AvatarIcon_Side_Kate",
  "qualityType": "QUALITY_PURPLE",
  "chargeEfficiency": 1.0,
  "LBODGAEPDMJ": 4103218460519001272,
  "initialWeapon": 11101,
  "weaponType": "WEAPON_SWORD_ONE_HAND",
  "NIPILHLOMDG": 4090361390804372245,
  "imageName": "AvatarImage_Forward_Kate",
  "gachaCardNameHash": 11812712877647515855,
  "manekinPathHash": 8639279672678166211,
  "cutsceneShow": "",
  "skillDepotId": 101,
  "staminaRecoverSpeed": 25.0,
  "candSkillDepotIds": [],
  "manekinJsonConfigHash": 5815996370094428443,
  "manekinMotionConfig": 100,
  "descTextMapHash": 1731825193,
  "avatarIdentityType": "AVATAR_IDENTITY_NORMAL",
  "avatarPromoteId": 2,
  "avatarPromoteRewardLevelList": [
    1,
    3,
    5
  ],
  "avatarPromoteRewardIdList": [
    900011,
    900013,
    900015
  ],
  "featureTagGroupID": 10000001,
  "infoDescTextMapHash": 1731825193,
  "hpBase": 166.0,
  "attackBase": 5.0,
  "defenseBase": 8.0,
  "critical": 0.05000000074505806,
  "criticalHurt": 0.5,
  "propGrowCurves": [
    {
      "type": "FIGHT_PROP_BASE_HP",
      "growCurve": "GROW_CURVE_HP_S4"
    },
    {
      "type": "FIGHT_PROP_BASE_ATTACK",
      "growCurve": "GROW_CURVE_ATTACK_S4"
    },
    {
      "type": "FIGHT_PROP_BASE_DEFENSE",
      "growCurve": "GROW_CURVE_HP_S4"
    }
  ],
  "BCAGNCKHFOF": 16909531753469473678,
  "prefabPathHash": 16843554909179268631,
  "id": 10000001,
  "nameTextMapHash": 1857915418,
  "NOLCALJMBOB": 6345797410857021941,
  "prefabPathRemoteHash": 11423433385109518698,
  "controllerPathHash": 9975873023065425870,
  "controllerPathRemoteHash": 8121517168866487642,
  "LODPatternName": ""
}
```

## 策划参考价值

该配表可用于分析原神的角色基础属性设计，包括数值区间、成长曲线斜率、资源投放节奏等。
