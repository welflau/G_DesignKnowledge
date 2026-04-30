# 原神 · 武器基础属性 (WeaponExcelConfigData)

> 来源：Sycamore0/GenshinData
> 游戏类型：开放世界ARPG
> 分类：数值配表
> 标签：原神, 角色数值, 武器, 圣遗物, 怪物, 经济系统

## 概述

原神武器基础属性，共 **185** 条记录。

## 数据字段

```
weaponType, rankLevel, weaponBaseExp, skillAffix, weaponProp, awakenTexture, awakenLightMapTexture, awakenIcon, weaponPromoteId, storyId, awakenCosts, gachaCardNameHash, destroyRule, destroyReturnMaterial, destroyReturnMaterialCount, id, nameTextMapHash, descTextMapHash, icon, itemType, weight, rank, gadgetId
```

## 数据样本（首条）

```json
{
  "weaponType": "WEAPON_SWORD_ONE_HAND",
  "rankLevel": 1,
  "weaponBaseExp": 600,
  "skillAffix": [
    0,
    0
  ],
  "weaponProp": [
    {
      "propType": "FIGHT_PROP_BASE_ATTACK",
      "initValue": 23.2450008392334,
      "type": "GROW_CURVE_ATTACK_101"
    },
    {
      "type": "GROW_CURVE_CRITICAL_101"
    }
  ],
  "awakenTexture": "ART/Equip/AvatarEquip/Equip_Sword_Blunt/Equip_Sword_Blunt_OverrideTexture/Equip_Sword_Blunt_02_Tex_Diffuse",
  "awakenLightMapTexture": "ART/Equip/AvatarEquip/Equip_Sword_Blunt/Equip_Sword_Blunt_OverrideTexture/Equip_Sword_Blunt_02_Tex_Lightmap",
  "awakenIcon": "UI_EquipIcon_Sword_Blunt_Awaken",
  "weaponPromoteId": 11101,
  "storyId": 191101,
  "awakenCosts": [],
  "gachaCardNameHash": 5206550965894458167,
  "destroyRule": "DESTROY_RETURN_MATERIAL",
  "destroyReturnMaterial": [
    104011
  ],
  "destroyReturnMaterialCount": [
    1
  ],
  "id": 11101,
  "nameTextMapHash": 2410593283,
  "descTextMapHash": 3807468957,
  "icon": "UI_EquipIcon_Sword_Blunt",
  "itemType": "ITEM_WEAPON",
  "weight": 1,
  "rank": 10,
  "gadgetId": 50011101
}
```

## 策划参考价值

该配表可用于分析原神的武器基础属性设计，包括数值区间、成长曲线斜率、资源投放节奏等。
