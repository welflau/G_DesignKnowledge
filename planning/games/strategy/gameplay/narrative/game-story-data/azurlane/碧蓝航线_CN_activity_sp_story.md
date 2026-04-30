# 碧蓝航线(CN) · activity_sp_story

> 来源：AzurLaneTools/AzurLaneData
> 原始链接：https://github.com/AzurLaneTools/AzurLaneData
> 分类：gameplay
> 标签：碧蓝航线, 弹幕射击RPG, 叙事数据, CN
> 游戏类型：弹幕射击RPG

## 概述
碧蓝航线CN服activity_sp_story叙事数据

## 正文
## 碧蓝航线叙事数据（CN服）

- 文件：CN/ShareCfg/activity_sp_story.json
- 大小：142KB

- 键数：360

### 样本

```json
{
  "1": {
    "change_background": "star_level_bg_546",
    "change_bgm": "story-richang-light",
    "change_prefab": "",
    "id": 1,
    "label_key": "",
    "lock": "",
    "name": "EPS-1 演奏者的梦",
    "pre_event": "",
    "story": "HUANMENGJIANZOUQU1",
    "story_type": 1,
    "unlock_conditions": ""
  },
  "2": {
    "change_background": "star_level_bg_546",
    "change_bgm": "story-richang-light",
    "change_prefab": "",
    "id": 2,
    "label_key": "",
    "lock": [
      [
        4,
        1
      ]
    ],
    "name": "EPS-2 联合演习的邀约",
    "pre_event": [
      1
    ],
    "story": "HUANMENGJIANZOUQU2",
    "story_type": 1,
    "unlock_conditions": "完成前置剧情后解锁"
  },
  "3": {
    "change_background": "bg_story_shengmixieer_1",
    "change_bgm": "level-french1",
    "change_prefab": "",
    "id": 3,
    "label_key": "",
    "lock": [
      [
        4,
        2
      ]
    ],
    "name": "EPS-3 悠闲午餐会",
    "pre_event": [
      2
    ],
    "story": "HUANMENGJIANZOUQU3",
    "story_type": 1,
    "unlock_conditions": "完成前置剧情后解锁"
  }
}
```


## 策划参考价值
弹幕射击RPG的角色叙事/皮肤/秘书舰台词数据结构。
