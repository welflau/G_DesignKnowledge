# 明日方舟 · 技能数据表

> 来源：Kengxxiao/ArknightsGameData
> 原始链接：https://github.com/Kengxxiao/ArknightsGameData/blob/master/zh_CN/gamedata/excel/skill_table.json
> 分类：numerical
> 标签：明日方舟, 数据解包, 技能数据表

## 概述
所有技能的倍率/SP消耗/持续时间/升级数据

## 正文
## 数据结构概览

- 文件大小：10.1 MB
- 顶层键数量：1638
- 顶层键列表（前50个）：

  - `skcom_charge_cost[1]`
  - `skcom_charge_cost[2]`
  - `skcom_charge_cost[3]`
  - `skcom_assist_cost[2]`
  - `skcom_assist_cost[3]`
  - `skcom_atk_up[1]`
  - `skcom_atk_up[2]`
  - `skcom_atk_up[3]`
  - `skcom_def_up[1]`
  - `skcom_def_up[2]`
  - `skcom_def_up[3]`
  - `skcom_magic_rage[1]`
  - `skcom_magic_rage[2]`
  - `skcom_magic_rage[3]`
  - `skcom_quickattack[1]`
  - `skcom_quickattack[3]`
  - `skcom_heal_up[1]`
  - `skcom_heal_up[2]`
  - `skcom_heal_up[3]`
  - `skcom_heal_rage[3]`
  - `skcom_range_extend`
  - `skcom_heal_self[1]`
  - `skcom_heal_self[2]`
  - `skcom_heal_self[3]`
  - `skchr_midn_1`
  - `skchr_wyvern_1`
  - `skchr_kroos_1`
  - `skchr_spot_1`
  - `skchr_catap_1`
  - `skchr_akkord_1`
  - `skchr_akkord_2`
  - `skchr_nights_2`
  - `skchr_fmout_2`
  - `skchr_greyy_2`
  - `skchr_cammou_2`
  - `skchr_stward_1`
  - `skchr_indigo_1`
  - `skchr_indigo_2`
  - `skchr_pudd_2`
  - `skchr_jesica_1`
  - `skchr_jesica_2`
  - `skchr_shotst_1`
  - `skchr_shotst_2`
  - `skchr_clour_2`
  - `skchr_mm_1`
  - `skchr_mm_2`
  - `skchr_yuki_1`
  - `skchr_yuki_2`
  - `skchr_pinecn_1`
  - `skchr_pinecn_2`
  - ... 共1638个

## 样本数据（第一个条目：`skcom_charge_cost[1]`）

```json
{
  "skillId": "skcom_charge_cost[1]",
  "iconId": null,
  "hidden": false,
  "levels": [
    {
      "name": "冲锋号令·α型",
      "rangeId": null,
      "description": "立即获得<@ba.vup>{cost}</>点部署费用",
      "skillType": "AUTO",
      "durationType": "NONE",
      "spData": {
        "spType": "INCREASE_WITH_TIME",
        "levelUpCost": null,
        "maxChargeTime": 1,
        "spCost": 30,
        "initSp": 0,
        "increment": 1.0
      },
      "prefabId": "skcom_charge_cost",
      "duration": 0.0,
      "blackboard": [
        {
          "key": "cost",
          "value": 6.0,
          "valueStr": null
        }
      ]
    },
    {
      "name": "冲锋号令·α型",
      "rangeId": null,
      "description": "立即获得<@ba.vup>{cost}</>点部署费用",
      "skillType": "AUTO",
      "durationType": "NONE",
      "spData": {
        "spType": "INCREASE_WITH_TIME",
        "levelUpCost": null,
        "maxChargeTime": 1,
        "spCost": 29,
        "initSp": 0,
        "increment": 1.0
      },
      "prefabId": "skcom_charge_cost",
      "duration": 0.0,
      "blackboard": [
        {
          "key": "cost",
          "value": 6.0,
          "valueStr": null
        }
      ]
    },
    {
      "name": "冲锋号令·α型",
      "rangeId": null,
      "description": "立即获得<@ba.vup>{cost}</>点部署费用",
      "skillType": "AUTO",
      "durationType": "NONE",
      "spData": {
        "spType": "INCREASE_WITH_TIME",
        "levelUpCost": null,
        "maxChargeTime": 1,
        "spCost": 28,
        "initSp": 0,
        "increment": 1.0
      },
      "prefabId": "skcom_charge_cost",
      "duration": 0.0,
      "blackboard": [
        {
          "key": "cost",
          "value": 6.0,
          "valueStr": null
        }
      ]
    },
    {
      "name": "冲锋号令·α型",
      "rangeId": null,
      "description": "立即获得<@ba.vup>{cost}</>点部署费用",
      "skillType": "AUTO",
      "durationType": "NONE",
      "spData": {
        "spType": "INCREASE_WITH_TIME",
        "levelUpCost": null,
        "maxChargeTime": 1,
        "spCost": 27,
        "initSp": 3,
        "increment": 1.0
      },
      "prefabId": "skcom_charge_cost",
      "duration": 0.0,
      "blackboard": [
        {
          "key": "cost",
          "value": 6.0,
          "valueStr": null
        }
      ]
    },
    {
      "name": "冲锋号令·α型",
      "rangeId": null,
      "description": "立即获得<@ba.vup>{cost}</>点部署费用",
      "skillType": "AUTO",
      "durationType": "NONE",
      "spData": {
        "spType": "INCREASE_WITH_TIME",
        "levelUpCost": null,
        "maxChargeTime": 1,
        "spCost": 26,
        "initSp": 3,
        "increment": 1.0
      },
      "prefabId": "skcom_charge_cost",
      "duration": 0.0,
      "blackboard": [
        {
          "key": "cost",
          "value": 6.0,
          "valueStr": null
        }
      ]
    },
    {
      "name": "冲锋号令·α型",
      "rangeId": null,
      "description": "立即获得<@ba.vup>{cost}</>点部署费用",
      "skillType": "AUTO",
      "durationType": "NONE",
      "spData": {
        "spType": "INCREASE_WITH_TIME",
        "levelUpCost": null,
        "maxChargeTime": 1,
        "spCost": 25,
        "initSp": 3,
        "increment": 1.0
      },
      "prefabId": "skcom_charge_cost",
      "duration": 0.0,
      "blackboard": [
        {
          "key": "cost",
          "value": 6.0,
          "valueStr": null
        }
      ]
    },
    {
      "name": "冲锋号令·α型",
      "rangeId": null,
      "description": "立即获得<@ba.vup>{cost}</>点部署费用",
      "skillType": "AUTO",
      "durationType": "NONE",
      "spData": {
        "spType": "INCREASE_WITH_TIME",
        "levelUpCost": null,
        "maxChargeTime": 1,
        "spCost": 25,
        "initSp": 6,
        "increment": 1.0
      },
      "prefabId": "skcom_charge_cost",
      "duration": 0.0,
      "blackboard": [
        {
          "key": "cost",
          "value": 6.0,
          "valueStr": null
        }
      ]
    }
  ]
}
```


## 策划参考价值
SLG策划参考：可用于分析角色成长体系、战斗数值框架、经济系统设计。
