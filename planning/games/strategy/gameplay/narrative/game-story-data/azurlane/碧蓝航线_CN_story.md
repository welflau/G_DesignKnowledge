# 碧蓝航线(CN) · story

> 来源：AzurLaneTools/AzurLaneData
> 原始链接：https://github.com/AzurLaneTools/AzurLaneData
> 分类：gameplay
> 标签：碧蓝航线, 弹幕射击RPG, 叙事数据, CN
> 游戏类型：弹幕射击RPG

## 概述
碧蓝航线CN服story叙事数据

## 正文
## 碧蓝航线叙事数据（CN服）

- 文件：CN/GameCfg/story.json
- 大小：63629KB

- 键数：6859

### 样本

```json
{
  "1060600": {
    "bgm": "battle-boss-4",
    "fleet_prefab": {
      "main_unitList": [
        {
          "configId": 900133,
          "equipment": [
            false,
            false,
            false
          ],
          "id": 1,
          "level": 120,
          "properties": {
            "air": 0,
            "antiaircraft": 300,
            "armor": 1150,
            "cannon": 200,
            "dodge": 0,
            "durability": 66744,
            "hit": 140,
            "luck": 38,
            "reload": 83,
            "speed": 31,
            "torpedo": 0
          },
          "skinId": 900133,
          "tmpID": 900133
        },
        {
          "configId": 900134,
          "equipment": [
            false,
            false,
            false
          ],
          "id": 2,
          "level": 120,
          "properties": {
            "air": 0,
            "antiaircraft": 300,
            "armor": 1890,
            "cannon": 230,
            "dodge": 96,
            "durability": 68377,
            "hit": 140,
            "luck": 14,
            "reload": 83,
            "speed": 28.3,
            "torpedo": 0
          },
          "skinId": 900134,
          "tmpID": 900134
        }
      ],
      "vanguard_unitList": [
        {
          "configId": 900132,
          "energy": 10,
          "equipment": [
            false,
            false,
            false
          ],
          "exp": 10,
          "id": 1,
          "level": 120,
          "oil_at_end": 55,
          "properties": {
            "air": 0,
            "antiaircraft": 310,
            "armor": 98,
            "cannon": 1000,
            "dodge": 164,
            "durability": 85567,
            "hit": 140,
            "luck": 70,
            "reload": 830,
            "speed": 31.5,
            "torpedo": 150
          },
          "skills": [
            {
              "id": 4,
              "level": 1
            }
          ],
          "skinId": 900132,
          "tmpID": 900132
        }
      ]
    },
    "id": 1060600,
    "stages": [
      {
        "backGroundStageID": 1,
        "enemyArea": [],
        "failCondition": 1,
        "fleetCorrdinate": [
          -80,
          0,
          75
        ],
        "mainUnitPosition": {
          "-1": [
            [
              15,
              0,
              58
            ],
            [
              15,
              0,
              78
            ],
            [
              15,
              0,
              38
            ]
          ],
          "1": [
            [
              -105,
              0,
              58
            ],
            [
              -105,
              0,
              78
            ],
            [
              -105,
              0,
              38
            ]
          ]
        },
        "passCondition": 1,
        "playerArea": [
          -70,
          20,
          37,
          68
        ],
        "stageIndex": 1,
        "timeCount": 600,
        "totalArea": [
          -70,
          20,
          90,
          70
        ],
        "waves": [
          {
            "preWaves": [],
            "triggerParams": {
              "timeout": 0.5
            },
            "triggerType": 1,
            "waveIndex": 300
          },
          {
            "preWaves": [],
            "triggerParams": {
              "bgm": "battle-boss-4"
            },
            "triggerType": 5,
            "waveIndex": 400
          },
          {
            "preWaves": [
              300
            ],
            "triggerParams": {
              "id": "DONGHUO14"
            },
            "triggerType": 3,
            "waveIndex": 200
          },
          {
            "conditionType": 0,
            "preWaves": [
              200
            ],
            "spawn": [
              {
                "buffList": [
                  8001,
                  8007
                ],
                "corrdinate": [
                  -6,
                  0,
                  55
                ],
                "delay": 0,
                "monsterTemplateID": 10070502,
                "moveCast": true
              },
              {
                "buffList": [
                  8001,
                  8007
                ],
                "corrdinate": [
                  0,
                  0,
                  75
                ],
                "delay": 0,
                "monsterTemplateID": 10070503,
                "moveCast": true
              },
              {
                "buffList": [
                  8001,
                  8007
                ],
                "corrdinate": [
                  0,
                  0,
                  35
                ],
                "delay": 0,
                "monsterTemplateID": 10070503,
                "moveCast": true
              },
              {
                "buffList": [
                  8001,
                  8
```


## 策划参考价值
弹幕射击RPG的角色叙事/皮肤/秘书舰台词数据结构。
