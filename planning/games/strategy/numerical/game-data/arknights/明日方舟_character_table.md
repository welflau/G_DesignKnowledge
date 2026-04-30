# 明日方舟 · 干员属性表

> 来源：Kengxxiao/ArknightsGameData
> 原始链接：https://github.com/Kengxxiao/ArknightsGameData/blob/master/zh_CN/gamedata/excel/character_table.json
> 分类：numerical
> 标签：明日方舟, 数据解包, 干员属性表

## 概述
全干员基础属性/成长曲线/职业/稀有度/信赖加成

## 正文
## 数据结构概览

- 文件大小：12.7 MB
- 顶层键数量：1159
- 顶层键列表（前50个）：

  - `char_285_medic2`
  - `char_286_cast3`
  - `char_376_therex`
  - `char_4000_jnight`
  - `char_4077_palico`
  - `char_4091_ulika`
  - `char_4093_frston`
  - `char_4136_phonor`
  - `char_4188_confes`
  - `char_502_nblade`
  - `char_500_noirc`
  - `char_503_rang`
  - `char_501_durin`
  - `char_009_12fce`
  - `char_123_fang`
  - `char_240_wyvern`
  - `char_504_rguard`
  - `char_192_falco`
  - `char_208_melan`
  - `char_281_popka`
  - `char_209_ardign`
  - `char_122_beagle`
  - `char_514_rdfend`
  - `char_284_spot`
  - `char_124_kroos`
  - `char_211_adnach`
  - `char_507_rsnipe`
  - `char_121_lava`
  - `char_120_hibisc`
  - `char_212_ansel`
  - `char_506_rmedic`
  - `char_210_stward`
  - `char_505_rcast`
  - `char_278_orchid`
  - `char_141_nights`
  - `char_604_ccast`
  - `char_109_fmout`
  - `char_253_greyy`
  - `char_4051_akkord`
  - `char_328_cammou`
  - `char_469_indigo`
  - `char_4004_pudd`
  - `char_235_jesica`
  - `char_126_shotst`
  - `char_190_clour`
  - `char_133_mm`
  - `char_603_csnipe`
  - `char_118_yuki`
  - `char_440_pinecn`
  - `char_302_glaze`
  - ... 共1159个

## 样本数据（第一个条目：`char_285_medic2`）

```json
{
  "name": "Lancet-2",
  "description": "恢复友方单位生命，且不受<@ba.kw>部署数量</>限制，但再部署时间极长",
  "sortIndex": 491,
  "spTargetType": "NONE",
  "spTargetId": null,
  "canUseGeneralPotentialItem": false,
  "canUseActivityPotentialItem": false,
  "potentialItemId": "p_char_285_medic2",
  "activityPotentialItemId": null,
  "classicPotentialItemId": null,
  "nationId": "rhodes",
  "groupId": null,
  "teamId": null,
  "mainPower": {
    "nationId": "rhodes",
    "groupId": null,
    "teamId": null
  },
  "subPower": null,
  "displayNumber": "RCX2",
  "appellation": "Lancet-2",
  "position": "RANGED",
  "tagList": [
    "支援机械",
    "治疗"
  ],
  "itemUsage": "罗德岛医疗机器人Lancet-2，被工程师可露希尔派遣来执行战地医疗任务。",
  "itemDesc": "她知道自己是一台机器人。",
  "itemObtainApproach": "招募寻访",
  "isNotObtainable": false,
  "isSpChar": false,
  "maxPotentialLevel": 5,
  "rarity": "TIER_1",
  "profession": "MEDIC",
  "subProfessionId": "physician",
  "trait": null,
  "phases": [
    {
      "characterPrefabKey": "char_285_medic2",
      "rangeId": "3-1",
      "maxLevel": 30,
      "attributesKeyFrames": [
        {
          "level": 1,
          "data": {
            "maxHp": 261,
            "atk": 42,
            "def": 16,
            "magicResistance": 0.0,
            "cost": 3,
            "blockCnt": 1,
            "moveSpeed": 1.0,
            "attackSpeed": 100.0,
            "baseAttackTime": 2.85,
            "respawnTime": 200,
            "hpRecoveryPerSec": 0.0,
            "spRecoveryPerSec": 1.0,
            "maxDeployCount": 1,
            "maxDeckStackCnt": 0,
            "tauntLevel": 0,
            "massLevel": 0,
            "baseForceLevel": 0,
            "stunImmune": false,
            "silenceImmune": false,
            "sleepImmune": false,
            "frozenImmune": false,
            "levitateImmune": false,
            "disarmedCombatImmune": false,
            "fearedImmune": false,
            "palsyImmune": false,
            "attractImmune": false
          }
        },
        {
          "level": 30,
          "data": {
            "maxHp": 435,
            "atk": 70,
            "def": 27,
            "magicResistance": 0.0,
            "cost": 3,
            "blockCnt": 1,
            "moveSpeed": 1.0,
            "attackSpeed": 100.0,
            "baseAttackTime": 2.85,
            "respawnTime": 200,
            "hpRecoveryPerSec": 0.0,
            "spRecoveryPerSec": 1.0,
            "maxDeployCount": 1,
            "maxDeckStackCnt": 0,
            "tauntLevel": 0,
            "massLevel": 0,
            "baseForceLevel": 0,
            "stunImmune": false,
            "silenceImmune": false,
            "sleepImmune": false,
            "frozenImmune": false,
            "levitateImmune": false,
            "disarmedCombatImmune": false,
            "fearedImmune": false,
            "palsyImmune": false,
            "attractImmune": false
          }
        }
      ],
      "evolveCost": null
    }
  ],
  "skills": [],
  "displayTokenDict": null,
  "talents": [
    {
      "candidates": [
        {
          "unlockCondition": {
            "phase": "PHASE_0",
            "level": 1
          },
          "requiredPotentialRank": 0,
          "prefabKey": "1",
          "name": "救援喷雾·I",
          "description": "部署后立即恢复全场友方单位200点生命",
          "rangeId": null,
          "blackboard": [
            {
              "key": "value",
              "value": 200.0,
              "valueStr": null
            }
          ],
          "tokenKey": null,
          "isHideTalent": false
        },
        {
          "unlockCondition": {
            "phase": "PHASE_0",
            "level": 1
          },
          "requiredPotentialRank": 1,
          "prefabKey": "1",
          "name": "救援喷雾·II",
          "description": "部署后立即恢复全场友方单位260点生命",
          "rangeId": null,
          "blackboard": [
            {
              "key": "value",
              "value": 260.0,
              "valueStr": null
            }
          ],
          "tokenKey": null,
          "isHideTalent": false
        },
        {
          "unlockCondition": {
            "phase": "PHASE_0",
            "level": 1
          },
          "requiredPotentialRank": 2,
          "prefabKey": "1",
          "name": "救援喷雾·III",
          "description": "部署后立即恢复全场友方单位320点生命",
          "rangeId": null,
          "blackboard": [
            {
              "key": "value",
              "value": 320.0,
              "valueStr": null
            }
          ],
          "tokenKey": null,
          "isHideTalent": false
        },
        {
          "unlockCondition": {
            "phase": "PHASE_0",
            "level": 1
          },
          "requiredPotentialRank": 3,
          "prefabKey": "1",
          "name": "救援喷雾·IV",
          "description": "部署后立即恢复全场友方单位380点生命",
          "rangeId": null,
          "blackboard": [
            {
              "key": "value",
              "value": 380.0,
              "valueStr": null
            }
          ],
          "tokenKey": null,
          "isHideTalent": false
        },
        {
          "unlockCondition": {
            "phase": "PHASE_0",
            "level": 1
          },
          "requiredPotentialRank": 4,
          "prefabKey": "1",
          "name": "救援喷雾·V",
          "description": "部署后立即恢复全场友方单位440点生命",
          "rangeId": null,
          "blackboard": [
            {
              "key": "value",
              "value": 440.0,
              "valueStr": null
            }
          ],
          "tokenKey": null,
          "isHideTalent": false
        },
        {
          "unlockCondition": {
            "phase": "PHASE_0",
            "level": 1
          },
          "requiredPotentialRank": 5,
          "prefabKey": "1",
          "name": "救援喷雾·VI",
          "description": "部署后立即恢复全场友方单位500点生命",
          "rangeId": null,
          "blackboard": [
            {
              "key": "value",
              "value": 500.0,
              "valueStr": null
            }
          ],
          "tokenKey": null,
          "isHideTalent": false
        }
      ]
    }
  ],
  "potentialRanks": [
    {
      "type": "CUSTOM",
      "description": "天赋效果加强",
      "buff": null,
      "equivalentCost": null
    },
    {
      "type": "CUSTOM",
      "description": "天赋效果加强",
      "buff": null,
      "equivalentCost": null
    },
    {
      "type": "CUSTOM",
      "description": "天赋效果加强",
      "buff": null,
      "equivalentCost": null
    },
    {
      "type": "CUSTOM",
      "description": "天赋效果加强",
      "buff": null,
      "equivalentCost": null
    },
    {
      "type": "CUSTOM",
      "description": "天赋效果加强",
      "buff": null,
      "equivalentCost": null
    }
  ],
  "favorKeyFrames": [
    {
      "level": 0,
      "data": {
        "maxHp": 0,
        "atk": 0,
        "def": 0,
        "magicResistance": 0.0,
        "cost": 0,
        "blockCnt": 0,
        "moveSpeed": 0.0,
        "attackSpeed": 0.0,
        "baseAttackTime": 0.0,
        "respawnTime": 0,
        "hpRecoveryPerSec": 0.0,
        "spRecoveryPerSec": 0.0,
        "maxDeployCount": 0,
        "maxDeckStackCnt": 0,
        "tauntLevel": 0,
        "massLevel": 0,
        "baseForceLevel": 0,
        "stunImmune": false,
        "silenceImmune": false,
        "sleepImmune": false,
        "frozenImmune": false,
        "levitateImmune": false,
        "disarmedCombatImmune": false,
        "fearedImmune": false,
        "palsyImmune": false,
        "attractImmune": false
      }
    },
    {
      "level": 50,
      "data": {
        "maxHp": 100,
        "atk": 40,
        "def": 0,
        "magicResistance": 0.0,
        "cost": 0,
        "blockCnt": 0,
        "moveSpeed": 0.0,
        "attackSpeed": 0.0,
        "baseAttackTime": 0.0,
        "respawnTime": 0,
        "hpRecoveryPerSec": 0.0,
        "spRecoveryPerSec": 0.0,
        "maxDeployCount": 0,
        "maxDeckStackCnt": 0,
        "tauntLevel": 0,
        "massLevel": 0,
        "baseForceLevel"
```


## 策划参考价值
SLG策划参考：可用于分析角色成长体系、战斗数值框架、经济系统设计。
