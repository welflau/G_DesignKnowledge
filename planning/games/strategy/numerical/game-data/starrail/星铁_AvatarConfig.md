# 崩坏：星穹铁道 · 角色基础配置 (AvatarConfig)

> 来源：gffice/StarRailData
> 游戏类型：回合制策略RPG
> 分类：数值配表
> 标签：星穹铁道, 角色数值, 光锥, 遗器, 怪物, 关卡

## 概述

星穹铁道角色基础配置，共 **47** 条记录。

## 数据字段

```
AvatarID, AvatarName, AvatarFullName, AdventurePlayerID, AvatarVOTag, Rarity, AvatarInitialSkinName, AvatarInitialSkinDesc, JsonPath, DamageType, SPNeed, ExpGroup, MaxPromotion, MaxRank, RankIDList, RewardList, RewardListMax, SkillList, AvatarBaseType, DefaultAvatarModelPath, DefaultAvatarHeadIconPath, AvatarSideIconPath, AvatarMiniIconPath, AvatarGachaResultImgPath, ActionAvatarHeadIconPath, UltraSkillCutInPrefabPath, UIAvatarModelPath, ManikinJsonPath, AvatarDesc, AIPath, SkilltreePrefabPath, DamageTypeResistance, Release, SideAvatarHeadIconPath, WaitingAvatarHeadIconPath, AvatarCutinImgPath, AvatarCutinBgImgPath, AvatarCutinFrontImgPath, AvatarCutinIntroText, AvatarDropOffset, AvatarTrialOffset, PlayerCardOffset, AssistOffset, AssistBgOffset, AvatarSelfShowOffset
```

## 数据样本（首条）

```json
{
  "AvatarID": 1001,
  "AvatarName": {
    "Hash": -531793651
  },
  "AvatarFullName": {
    "Hash": -1063124016
  },
  "AdventurePlayerID": 1001,
  "AvatarVOTag": "mar7th",
  "Rarity": "CombatPowerAvatarRarityType4",
  "AvatarInitialSkinName": {
    "Hash": 371857150
  },
  "AvatarInitialSkinDesc": {
    "Hash": 371857150
  },
  "JsonPath": "Config/ConfigCharacter/Avatar/Avatar_Mar_7th_00_Config.json",
  "DamageType": "Ice",
  "SPNeed": {
    "Value": 120
  },
  "ExpGroup": 1,
  "MaxPromotion": 6,
  "MaxRank": 6,
  "RankIDList": [
    100101,
    100102,
    100103,
    100104,
    100105,
    100106
  ],
  "RewardList": [
    {
      "ItemID": 11001,
      "ItemNum": 1
    },
    {
      "ItemID": 252,
      "ItemNum": 8
    }
  ],
  "RewardListMax": [
    {
      "ItemID": 252,
      "ItemNum": 20
    }
  ],
  "SkillList": [
    100101,
    100102,
    100103,
    100104,
    100106,
    100107
  ],
  "AvatarBaseType": "Knight",
  "DefaultAvatarModelPath": "Characters/CharacterPrefabs/Avatar/Mar_7th_00/Avatar_Mar_7th_00.prefab",
  "DefaultAvatarHeadIconPath": "SpriteOutput/AvatarIcon/1001.png",
  "AvatarSideIconPath": "SpriteOutput/AvatarRoundIcon/1001.png",
  "AvatarMiniIconPath": "SpriteOutput/AvatarMiniIcon/1001.png",
  "AvatarGachaResultImgPath": "SpriteOutput/AvatarDrawCardResult/1001.png",
  "ActionAvatarHeadIconPath": "SpriteOutput/AvatarIconTeam/1001B.png",
  "UltraSkillCutInPrefabPath": "UI/Battle/UltraSkillCutIn/UltraSkillCutIn_1001.prefab",
  "UIAvatarModelPath": "Characters/CharacterPrefabs/Manikin/Avatar/Mar_7th_00/Manikin_Avatar_Maid_Mar_7th_00.prefab",
  "ManikinJsonPath": "Config/ConfigCharacter/Manikin/Avatar/Manikin_Avatar_Mar_7th_00_Config.json",
  "AvatarDesc": {
    "Hash": 371857150
  },
  "AIPath": "Config/ConfigAI/Avatar_ComplexSkilll_AutoFight_AI.json",
  "SkilltreePrefabPath": "UI/Avatar/Widget/KnightSkillTreeGroup.prefab",
  "DamageTypeResistance": [],
  "Release": true,
  "SideAvatarHeadIconPath": "SpriteOutput/AvatarIconTeam/1001.png
```

## 策划参考价值

可用于分析星穹铁道回合制战斗系统的角色基础设计。
