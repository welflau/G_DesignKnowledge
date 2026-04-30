# 崩坏：星穹铁道 · 属性伤害类型 (DamageType)

> 来源：gffice/StarRailData
> 游戏类型：回合制策略RPG
> 分类：数值配表
> 标签：星穹铁道, 角色数值, 光锥, 遗器, 怪物, 关卡

## 概述

星穹铁道属性伤害类型，共 **7** 条记录。

## 数据字段

```
ID, DamageTypeName, DamageTypeIntro, DamageTypeIconPath, IconNatureForWeakActive, IconNatureForWeakUnactive, IconNatureColorSimple, IconNatureColor, IconNatureWhite, SPInfoEffFront, SPInfoEffFrontDouble, Color, ShaderColor, UnfullColor, LightColor, Light1Color, SkillBtnEff, SkillTreeLightColor, SkillTreeDecoColor, SkillTreeLeftPanelColor, SPMazeInfoEffFront, NormalDamage, CriticalDamage, SkillTreePanelPath, MazeEnterBattleWeakIconPath
```

## 数据样本（首条）

```json
{
  "ID": "Physical",
  "DamageTypeName": {
    "Hash": -1101149179
  },
  "DamageTypeIntro": {
    "Hash": 308550234
  },
  "DamageTypeIconPath": "SpriteOutput/UI/Nature/IconAttribute/IconAttributePhysical.png",
  "IconNatureForWeakActive": "SpriteOutput/UI/Nature/IconNatureForWeak/IconNatureWhitePhysical_2.png",
  "IconNatureForWeakUnactive": "SpriteOutput/UI/Nature/IconNatureForWeak/IconNatureWhitePhysical_1.png",
  "IconNatureColorSimple": "SpriteOutput/IconDamageType/IconDamageTypePhysical.png",
  "IconNatureColor": "SpriteOutput/UI/Nature/IconNatureColor/IconNaturePhysical.png",
  "IconNatureWhite": "SpriteOutput/UI/Nature/IconAttribute/IconAttributePhysical.png",
  "SPInfoEffFront": "UI/Battle/SPInfo/Eff_Front/SPInfoEff_Front_Physical.prefab",
  "SPInfoEffFrontDouble": "UI/Battle/SPInfo/Eff_Front/SPInfoEff_Front_Physical_Double.prefab",
  "Color": "#FFFFFF",
  "ShaderColor": "#FFFFFF",
  "UnfullColor": "#FFFFFF",
  "LightColor": "#B7B7B796",
  "Light1Color": "#828282D2",
  "SkillBtnEff": "UI/Battle/SkillButton/SkillBtnEff/SkillBtnEff_Physical.prefab",
  "SkillTreeLightColor": "#ecdcf7",
  "SkillTreeDecoColor": "#cbd9f2",
  "SkillTreeLeftPanelColor": "#3D3B3F",
  "SPMazeInfoEffFront": "UI/VXAsset/ShineEffCom_Physical.prefab",
  "NormalDamage": "#e1e1e1",
  "CriticalDamage": "#bababa",
  "SkillTreePanelPath": "SpriteOutput/UI/Avatar/SkillTree/AttributeColor/GradualPhysical.png",
  "MazeEnterBattleWeakIconPath": "SpriteOutput/UI/Nature/IconAttributeMiddle/IconAttributePhysical.png"
}
```

## 策划参考价值

可用于分析星穹铁道回合制战斗系统的属性伤害类型设计。
