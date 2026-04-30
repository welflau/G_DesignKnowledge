# 明日方舟 · 关卡配置表

> 来源：Kengxxiao/ArknightsGameData
> 原始链接：https://github.com/Kengxxiao/ArknightsGameData/blob/master/zh_CN/gamedata/excel/stage_table.json
> 分类：numerical
> 标签：明日方舟, 数据解包, 关卡配置表

## 概述
所有关卡的配置/难度/敌人配置

## 正文
## 数据结构概览

- 文件大小：17.3 MB
- 顶层键数量：31
- 顶层键列表（前50个）：

  - `stages`
  - `runeStageGroups`
  - `mapThemes`
  - `tileInfo`
  - `forceOpenTable`
  - `timelyStageDropInfo`
  - `overrideDropInfo`
  - `overrideUnlockInfo`
  - `timelyTable`
  - `stageValidInfo`
  - `stageFogInfo`
  - `stageStartConds`
  - `diffGroupTable`
  - `storyStageShowGroup`
  - `specialBattleFinishStageData`
  - `recordRewardData`
  - `apProtectZoneInfo`
  - `antiSpoilerDict`
  - `actCustomStageDatas`
  - `spNormalStageIdFor4StarList`
  - `storylines`
  - `storylineStorySets`
  - `storylineTags`
  - `storylineConst`
  - `cgGalleryDisplays`
  - `cgGalleryGroups`
  - `cgGalleryCgs`
  - `sixStarRuneData`
  - `sixStarMilestoneInfo`
  - `sixStarCompatibleInfo`
  - `conditionalDropInfo`

## 样本数据（第一个条目：`stages`）

```json
{
  "main_00-01": {
    "stageType": "MAIN",
    "difficulty": "NORMAL",
    "performanceStageFlag": "NORMAL_STAGE",
    "diffGroup": "NONE",
    "unlockCondition": [],
    "stageId": "main_00-01",
    "levelId": "Obt/Main/level_main_00-01",
    "zoneId": "main_0",
    "code": "0-1",
    "name": "坍塌",
    "description": "三点方向出现了敌人的先锋部队，请部署近战干员进行拦截。",
    "hardStagedId": "main_00-01#f#",
    "sixStarStageId": null,
    "dangerLevel": "LV.1",
    "dangerPoint": -1.0,
    "loadingPicId": "loading1",
    "canPractice": true,
    "canBattleReplay": true,
    "apCost": 6,
    "apFailReturn": 6,
    "maxSlot": -1,
    "etItemId": null,
    "etCost": -1,
    "etFailReturn": -1,
    "etButtonStyle": null,
    "apProtectTimes": 0,
    "diamondOnceDrop": 1,
    "practiceTicketCost": 1,
    "dailyStageDifficulty": -1,
    "expGain": 60,
    "goldGain": 60,
    "loseExpGain": 0,
    "loseGoldGain": 0,
    "passFavor": 6,
    "completeFavor": 6,
    "slProgress": 1,
    "displayMainItem": "",
    "hilightMark": false,
    "bossMark": false,
    "isPredefined": false,
    "isHardPredefined": false,
    "isSkillSelectablePredefined": false,
    "isStoryOnly": false,
    "appearanceStyle": "MAIN_NORMAL",
    "stageDropInfo": {
      "firstPassRewards": null,
      "firstCompleteRewards": null,
      "passRewards": null,
      "completeRewards": null,
      "displayRewards": [
        {
          "type": "TKT_RECRUIT",
          "id": "7001",
          "dropType": "ONCE"
        },
        {
          "type": "CARD_EXP",
          "id": "2001",
          "dropType": "NORMAL"
        },
        {
          "type": "DIAMOND",
          "id": "4002",
          "dropType": "COMPLETE"
        }
      ],
      "displayDetailRewards": [
        {
          "occPercent": "ALWAYS",
          "type": "TKT_RECRUIT",
          "id": "7001",
          "dropType": "ONCE"
        },
        {
          "occPercent": "ALWAYS",
          "type": "CARD_EXP",
          "id": "2001",
          "dropType": "NORMAL"
        },
        {
          "occPercent": "SOMETIMES",
          "type": "MATERIAL",
          "id": "30011",
          "dropType": "ADDITIONAL"
        },
        {
          "occPercent": "SOMETIMES",
          "type": "MATERIAL",
          "id": "30021",
          "dropType": "ADDITIONAL"
        },
        {
          "occPercent": "SOMETIMES",
          "type": "MATERIAL",
          "id": "30031",
          "dropType": "ADDITIONAL"
        },
        {
          "occPercent": "SOMETIMES",
          "type": "MATERIAL",
          "id": "30041",
          "dropType": "ADDITIONAL"
        },
        {
          "occPercent": "SOMETIMES",
          "type": "MATERIAL",
          "id": "30051",
          "dropType": "ADDITIONAL"
        },
        {
          "occPercent": "SOMETIMES",
          "type": "MATERIAL",
          "id": "30061",
          "dropType": "ADDITIONAL"
        },
        {
          "occPercent": "SOMETIMES",
          "type": "MATERIAL",
          "id": "3003",
          "dropType": "ADDITIONAL"
        },
        {
          "occPercent": "ALWAYS",
          "type": "CARD_EXP",
          "id": "2001",
          "dropType": "ADDITIONAL"
        },
        {
          "occPercent": "ALWAYS",
          "type": "DIAMOND",
          "id": "4002",
          "dropType": "COMPLETE"
        }
      ]
    },
    "canUseCharm": false,
    "canUseTech": false,
    "canUseTrapTool": false,
    "canUseBattlePerformance": false,
    "canUseFirework": false,
    "canMultipleBattle": true,
    "startButtonOverrideId": null,
    "isStagePatch": false,
    "mainStageId": "main_00-01",
    "extraCondition": null,
    "extraInfo": null,
    "sixStarBaseDesc": null,
    "sixStarDisplayRewardList": null,
    "advancedRuneIdList1": [],
    "advancedRuneIdList2": [],
    "useSpecialSizeMapPreview": false
  },
  "main_00-01#f#": {
    "stageType": "MAIN",
    "difficulty": "FOUR_STAR",
    "performanceStageFlag": "NORMAL_STAGE",
    "diffGroup": "NONE",
    "unlockCondition": [
      {
        "stageId": "main_02-08",
        "completeState": "PASS"
      },
      {
        "stageId": "main_00-01",
        "completeState": "COMPLETE"
      }
    ],
    "stageId": "main_00-01#f#",
    "levelId": "Obt/Main/level_main_00-01",
    "zoneId": "main_0",
    "code": "0-1",
    "name": "坍塌",
    "description": "<@lv.fs>附加条件：</>\\n部署费用不自然回复",
    "hardStagedId": null,
    "sixStarStageId": null,
    "dangerLevel": "-",
    "dangerPoint": -1.0,
    "loadingPicId": "loading1",
    "canPractice": true,
    "canBattleReplay": false,
    "apCost": 6,
    "apFailReturn": 6,
    "maxSlot": -1,
    "etItemId": null,
    "etCost": -1,
    "etFailReturn": -1,
    "etButtonStyle": null,
    "apProtectTimes": 0,
    "diamondOnceDrop": 1,
    "practiceTicketCost": 3,
    "dailyStageDifficulty": -1,
    "expGain": 60,
    "goldGain": 60,
    "loseExpGain": 0,
    "loseGoldGain": 0,
    "passFavor": 6,
    "completeFavor": 6,
    "slProgress": 0,
    "displayMainItem": "",
    "hilightMark": false,
    "bossMark": false,
    "isPredefined": false,
    "isHardPredefined": false,
    "isSkillSelectablePredefined": false,
    "isStoryOnly": false,
    "appearanceStyle": "MAIN_NORMAL",
    "stageDropInfo": {
      "firstPassRewards": null,
      "firstCompleteRewards": null,
      "passRewards": null,
      "completeRewards": null,
      "displayRewards": [
        {
          "type": "DIAMOND",
          "id": "4002",
          "dropType": "COMPLETE"
        }
      ],
      "displayDetailRewards": [
        {
          "occPercent": "ALWAYS",
          "type": "DIAMOND",
          "id": "4002",
          "dropType": "COMPLETE"
        }
      ]
    },
    "canUseCharm": false,
    "canUseTech": false,
    "canUseTrapTool": false,
    "canUseBattlePerformance": false,
    "canUseFirework": false,
    "canMultipleBattle": false,
    "startButtonOverrideId": null,
    "isStagePatch": false,
    "mainStageId": "main_00-01#f#",
    "extraCondition": null,
    "extraInfo": null,
    "sixStarBaseDesc": null,
    "sixStarDisplayRewardList": null,
    "advancedRuneIdList1": [],
    "advancedRuneIdList2": [],
    "useSpecialSizeMapPreview": false
  },
  "tr_01": {
    "stageType": "MAIN",
    "difficulty": "NORMAL",
    "performanceStageFlag": "NORMAL_STAGE",
    "diffGroup": "NONE",
    "unlockCondition": [
      {
        "stageId": "main_00-01",
        "completeState": "PASS"
      }
    ],
    "stageId": "tr_01",
    "levelId": "Obt/Training/level_training_1",
    "zoneId": "main_0",
    "code": "TR-1",
    "name": "战地医疗 ",
    "description": "学习医疗干员的使用方法。",
    "hardStagedId": null,
    "sixStarStageId": null,
    "dangerLevel": "-",
    "dangerPoint": -1.0,
    "loadingPicId": "loadingS",
    "canPractice": false,
    "canBattleReplay": false,
    "apCost": 0,
    "apFailReturn": 0,
    "maxSlot": -1,
    "etItemId": null,
    "etCost": -1,
    "etFailReturn": -1,
    "etButtonStyle": null,
    "apProtectTimes": 0,
    "diamondOnceDrop": 1,
    "practiceTicketCost": -1,
    "dailyStageDifficulty": -1,
    "expGain": 0,
    "goldGain": 0,
    "loseExpGain": 0,
    "loseGoldGain": 0,
    "passFavor": 0,
    "completeFavor": 0,
    "slProgress": 2,
    "displayMainItem": "",
    "hilightMark": false,
    "bossMark": false,
    "isPredefined": true,
    "isHardPredefined": false,
    "isSkillSelectablePredefined": false,
    "isStoryOnly": false,
    "appearanceStyle": "TRAINING",
    "stageDropInfo": {
      "firstPassRewards": null,
      "firstCompleteRewards": null,
      "passRewards": null,
      "completeRewards": null,
      "displayRewards": [
        {
          "type": "CHAR",
          "id": "char_120_hibisc",
          "dropType": "ONCE"
        },
        {
          "type": "DIAMOND",
          "id": "4002",
          "dropType": "COMPLETE"
        }
      ],
      "displayDetailRewards": [
        {
          "occPercent": "ALWAYS",
          "type": "CHAR",
          "id": "char_120_hibisc",
 
```


## 策划参考价值
SLG策划参考：可用于分析角色成长体系、战斗数值框架、经济系统设计。
