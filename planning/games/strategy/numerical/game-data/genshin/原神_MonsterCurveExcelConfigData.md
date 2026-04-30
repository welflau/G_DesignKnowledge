# 原神 · 怪物成长曲线 (MonsterCurveExcelConfigData)

> 来源：Sycamore0/GenshinData
> 游戏类型：开放世界ARPG
> 分类：数值配表
> 标签：原神, 角色数值, 武器, 圣遗物, 怪物, 经济系统

## 概述

原神怪物成长曲线，共 **200** 条记录。

## 数据字段

```
level, curveInfos
```

## 数据样本（首条）

```json
{
  "level": 1,
  "curveInfos": [
    {
      "type": "GROW_CURVE_HP",
      "arith": "ARITH_MULTI",
      "value": 5.36785888671875
    },
    {
      "type": "GROW_CURVE_ATTACK",
      "arith": "ARITH_MULTI",
      "value": 2.020519971847534
    },
    {
      "type": "GROW_CURVE_DEFENSE",
      "arith": "ARITH_MULTI",
      "value": 1.0099999904632568
    },
    {
      "type": "GROW_CURVE_STRIKE",
      "arith": "ARITH_ADD"
    },
    {
      "type": "GROW_CURVE_STRIKE_HURT",
      "arith": "ARITH_ADD"
    },
    {
      "type": "GROW_CURVE_ELEMENT",
      "arith": "ARITH_ADD"
    },
    {
      "type": "GROW_CURVE_KILL_EXP",
      "arith": "ARITH_MULTI",
      "value": 1.0
    },
    {
      "type": "GROW_CURVE_HP_LITTLEMONSTER",
      "arith": "ARITH_MULTI",
      "value": 1.0
    },
    {
      "type": "GROW_CURVE_MHP",
      "arith": "ARITH_MULTI",
      "value": 1.0
    },
    {
      "type": "GROW_CURVE_MATK",
      "arith": "ARITH_MULTI",
      "value": 1.0
    },
    {
      "type": "GROW_CURVE_HP_2",
      "arith": "ARITH_MULTI",
      "value": 5.404888153076172
    },
    {
      "type": "GROW_CURVE_ATTACK_2",
      "arith": "ARITH_MULTI",
      "value": 2.020524024963379
    },
    {
      "type": "GROW_CURVE_HP_ENVIRONMENT",
      "arith": "ARITH_MULTI",
      "value": 17.165605545043945
    }
  ]
}
```

## 策划参考价值

该配表可用于分析原神的怪物成长曲线设计，包括数值区间、成长曲线斜率、资源投放节奏等。
