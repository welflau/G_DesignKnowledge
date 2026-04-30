# 明日方舟 · 剧情配置表 (story_table)

> 来源：Kengxxiao/ArknightsGameData
> 原始链接：https://github.com/Kengxxiao/ArknightsGameData
> 分类：gameplay
> 标签：明日方舟, 剧情数据, 叙事配置

## 概述
明日方舟全剧情配置数据（章节/剧情ID/触发条件）

## 正文
## 数据概览

- 文件大小：1366.6 KB
- 顶层键数量：2290
- 顶层键列表（前30个）：

  - `obt/guide/beg/0_welcome_to_guide`
  - `obt/guide/beg/1a_guide_1to2`
  - `obt/guide/beg/1b_guide_1to2`
  - `obt/guide/beg/2_guide_to_home`
  - `obt/guide/l0-0/0_home_ui`
  - `obt/guide/l0-0/1_recruit_adv`
  - `obt/guide/l0-0/2_make_squad`
  - `obt/guide/l0-0/3_battle_ui`
  - `obt/guide/l0-1/0_mission_main`
  - `obt/guide/l0-1/1_training_level`
  - `obt/guide/l0-2/0_recruit_normal`
  - `obt/guide/l0-4/0_upgrade_char`
  - `obt/guide/l0-6/0_upgrade_skill`
  - `obt/guide/l0-9/0_mission_others`
  - `obt/guide/l0-10/0_weekly_daily`
  - `obt/guide/l0-11/0_building_init`
  - `obt/guide/l0-11/1a_slot_clean`
  - `obt/guide/l0-11/1b_slot_clean`
  - `obt/guide/l0-11/1c_slot_clean`
  - `obt/guide/l0-11/1d_slot_clean`
  - `obt/guide/l0-11/2a_build_elect`
  - `obt/guide/l0-11/2b_build_manu`
  - `obt/guide/l0-11/2c_build_trade`
  - `obt/guide/l0-11/3a_station_manu`
  - `obt/guide/l0-11/3b_op_manu`
  - `obt/guide/l0-11/3c_station_trade`
  - `obt/guide/l0-11/3d_op_trade`
  - `obt/guide/l1-1/0_building_control`
  - `obt/guide/l1-2/0_upgrade_char_again`
  - `obt/guide/l1-5/0_campaign_stage`

## 样本数据（`obt/guide/beg/0_welcome_to_guide`）

```json
{
  "id": "obt/guide/beg/0_welcome_to_guide",
  "needCommit": false,
  "repeatable": true,
  "disabled": false,
  "videoResource": false,
  "trigger": {
    "type": "GAME_START",
    "key": null,
    "useRegex": false
  },
  "condition": {
    "minProgress": 0,
    "maxProgress": -1,
    "minPlayerLevel": 1,
    "requiredFlags": [],
    "excludedFlags": [],
    "requiredStages": [
      {
        "stageId": "guide_01",
        "minState": "UNLOCKED",
        "maxState": "PLAYED"
      }
    ]
  },
  "setProgress": -1,
  "setFlags": [],
  "completedRewards": []
}
```


## 策划参考价值
游戏剧情配置表结构参考。
