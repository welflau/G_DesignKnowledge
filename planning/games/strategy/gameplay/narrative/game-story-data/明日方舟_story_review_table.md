# 明日方舟 · 剧情回顾表 (story_review_table)

> 来源：Kengxxiao/ArknightsGameData
> 原始链接：https://github.com/Kengxxiao/ArknightsGameData
> 分类：gameplay
> 标签：明日方舟, 剧情数据, 叙事回顾

## 概述
明日方舟剧情回顾配置（可用于理解剧情系统结构）

## 正文
## 数据概览

- 文件大小：1714.6 KB
- 顶层键数量：456

## 样本数据

```json
{
  "id": "1stact",
  "name": "骑兵与猎人",
  "entryType": "ACTIVITY",
  "actType": "ACTIVITY_STORY",
  "startTime": 1559181600,
  "endTime": -1,
  "startShowTime": 1560974400,
  "endShowTime": -1,
  "remakeStartTime": 1601539200,
  "remakeEndTime": 1602705599,
  "storyEntryPicId": "storyEntryPic_act1d0",
  "storyPicId": null,
  "storyMainColor": null,
  "customType": 0,
  "storyCompleteMedalId": null,
  "rewards": [],
  "infoUnlockDatas": [
    {
      "storyReviewType": "NONE",
      "storyId": "1stact_level_a001_01_beg",
      "storyGroup": "1stact",
      "storySort": 1,
      "storyDependence": null,
      "storyCanShow": 1,
      "storyCode": "GT-1",
      "storyName": "日正当中",
      "storyPic": null,
      "storyInfo": "info/activities/a001/level_a001_01_beg",
      "storyCanEnter": 1,
      "storyTxt": "activities/a001/level_a001_01_beg",
      "avgTag": "行动前",
      "unLockType": "BY_START_TIME",
      "costItemType": "NONE",
      "costItemId": null,
      "costItemCount": 0,
      "stageCount": 1,
      "requiredStages": [
        {
          "stageId": "a001_01",
          "minState": "PLAYED",
          "maxState": "COMPLETE"
        }
      ]
    },
    {
      "storyReviewType": "NONE",
      "storyId": "1stact_level_a001_01_end",
      "storyGroup": "1stact",
      "storySort": 2,
      "storyDependence": "1stact_level_a001_01_beg",
      "storyCanShow": 1,
      "storyCode": "GT-1",
      "storyName": "日正当中",
      "storyPic": null,
      "storyInfo": "info/activities/a001/level_a001_01_end",
      "storyCanEnter": 1,
      "storyTxt": "activities/a001/level_a001_01_end",
      "avgTag": "行动后",
      "unLockType": "BY_START_TIME",
      "costItemType": "NONE",
      "costItemId": null,
      "costItemCount": 0,
      "stageCount": 1,
      "requiredStages": [
        {
          "stageId": "a001_01",
          "minState": "PASS",
          "maxState": "COMPLETE"
        }
      ]
    },
    {
      "storyReviewType": "NONE",
      "storyId": "1stact_level_a001_02_beg",
      "storyGroup": "1stact",
      "storySort": 3,
      "storyDependence": "1stact_level_a001_01_end",
      "storyCanShow": 1,
      "storyCode": "GT-2",
      "storyName": "察言观色",
      "storyPic": null,
      "storyInfo": "info/activities/a001/level_a001_02_beg",
      "storyCanEnter": 1,
      "storyTxt": "activities/a001/level_a001_02_beg",
      "avgTag": "行动前",
      "unLockType": "BY_START_TIME",
      "costItemType": "NONE",
      "costItemId": null,
      "costItemCount": 0,
      "stageCount": 1,
      "requiredStages": [
        {
          "stageId": "a001_02",
          "minState": "PLAYED",
          "maxState": "COMPLETE"
        }
      ]
    },
    {
      "storyReviewType": "NONE",
      "storyId": "1stact_level_a001_02_end",
      "storyGroup": "1stact",
      "storySort": 4,
      "storyDependence": "1stact_level_a001_02_beg",
      "storyCanShow": 1,
      "storyCode": "GT-2",
      "storyName": "察言观色",
      "storyPic": null,
      "storyInfo": "info/activities/a001/level_a001_02_end",
      "storyCanEnter": 1,
      "storyTxt": "activities/a001/level_a001_02_end",
      "avgTag": "行动后",
      "unLockType": "BY_START_TIME",
      "costItemType": "NONE",
      "costItemId": null,
      "costItemCount": 0,
      "stageCount": 1,
      "requiredStages": [
        {
          "stageId": "a001_02",
          "minState": "PASS",
          "maxState": "COMPLETE"
        }
      ]
    },
    {
      "storyReviewType": "NONE",
      "storyId": "1stact_level_a001_03_beg",
      "storyGroup": "1stact",
      "storySort": 5,
      "storyDependence": "1stact_level_a001_02_end",
      "storyCanShow": 1,
      "storyCode": "GT-3",
      "storyName": "意外之旅",
      "storyPic": null,
      "storyInfo": "info/activities/a001/level_a001_03_beg",
      "storyCanEnter": 1,
      "storyTxt": "activities/a001/level_a001_03_beg",
      "avgTag": "行动前",
      "unLockType": "BY_START_TIME",
      "costItemType": "NONE",
      "costItemId": null,
      "costItemCount": 0,
      "stageCount": 1,
      "requiredStages": [
        {
          "stageId": "a001_03",
          "minState": "PLAYED",
          "maxState": "COMPLETE"
        }
      ]
    },
    {
      "storyReviewType": "NONE",
      "storyId": "1stact_level_a001_03_end",
      "storyGroup": "1stact",
      "storySort": 6,
      "storyDependence": "1stact_level_a001_03_beg",
      "storyCanShow": 1,
      "storyCode": "GT-3",
      "storyName": "意外之旅",
      "storyPic": null,
      "storyInfo": "info/activities/a001/level_a001_03_end",
      "storyCanEnter": 1,
      "storyTxt": "activities/a001/level_a001_03_end",
      "avgTag": "行动后",
      "unLockType": "BY_START_TIME",
      "costItemType": "NONE",
      "costItemId": null,
      "costItemCount": 0,
      "stageCount": 1,
      "requiredStages": [
        {
          "stageId": "a001_03",
          "minState": "PASS",
          "maxState": "COMPLETE"
        }
      ]
    },
    {
      "storyReviewType": "NONE",
      
```


## 策划参考价值
剧情回顾系统的数据结构参考。
