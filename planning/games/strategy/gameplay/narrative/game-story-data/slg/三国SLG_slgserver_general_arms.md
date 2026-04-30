# 三国SLG · general_arms（slgserver）

> 来源：slgserver
> 原始链接：https://github.com/llr104/slgserver
> 分类：gameplay
> 标签：三国, SLG, 武将数据, 角色配置
> 游戏类型：SLG

## 概述
三国SLG项目的general_arms配置数据

## 正文
## 数据概览

- 文件：general_arms.json

- 键数：2

### 样本

```json
{
  "title": "兵种配置表",
  "arms": [
    {
      "id": 1,
      "name": "步兵",
      "condition": {
        "level": 1,
        "star_lv": 0
      },
      "change_cost": {
        "gold": 1000
      },
      "harm_ratio": [
        100,
        110,
        90,
        95,
        105,
        85,
        90,
        100,
        80
      ]
    },
    {
      "id": 2,
      "name": "弓兵",
      "condition": {
        "level": 1,
        "star_lv": 0
      },
      "change_cost": {
        "gold": 1000
      },
      "harm_ratio": [
        90,
        100,
        110,
        85,
        95,
        105,
        80,
        90,
        100
      ]
    },
    {
      "id": 3,
      "name": "骑兵",
      "condition": {
        "level": 1,
        "star_lv": 0
      },
      "change_cost": {
        "gold": 1000
      },
      "harm_ratio": [
        110,
        90,
        100,
        105,
        85,
        95,
        100,
        80,
        90
      ]
    },
    {
      "id": 4,
      "name": "轻步兵",
      "condition": {
        "level": 3,
        "star_lv": 0
      },
      "change_cost": {
        "gold": 5000
      },
      "harm_ratio": [
        105,
        115,
        95,
        100,
        110,
        90,
        95,
        105,
        85
      ]
    },
    {
      "id": 5,
      "name": "长弓兵",
      "condition": {
        "level": 3,
        "star_lv": 0
      },
      "change_cost": {
        "gold": 6000
      },
      "harm_ratio": [
        95,
        105,
        115,
        90,
        100,
        110,
        85,
        95,
        105
      ]
    },
    {
      "id": 6,
      "name": "轻骑兵",
      "condition": {
        "level": 3,
        "star_lv": 0
      },
      "change_cost": {
        "gold": 4000
      },
      "harm_ratio": [
        115,
        95,
        105,
        110,
        90,
        100,
        105,
        85,
        95
      ]
    },
    {
      "id": 7,
      "name": "重甲兵",
      "condition": {
        "level": 7,
        "star_lv": 0
      },
      "change_cost": {
        "gold": 14000
      },
      "harm_ratio": [
        110,
        120,
        90,
        105,
        115,
        95,
        100,
        110,
        90
      ]
    },
    {
      "id": 8,
      "name": "弩兵",
      "condition": {
        "level": 3,
        "star_lv": 0
      },
      "change_cost": {
        "gold": 6000
      },
      "harm_ratio": [
        100,
        110,
        120,
        95,
        105,
        115,
        90,
        100,
        110
      ]
    },
    {
      "id": 9,
      "name": "重骑兵",
      "condition": {
        "level": 7,
        "star_lv": 0
      },
      "change_cost": {
        "gold": 18000
      },
      "harm_ratio": [
        120,
        100,
        110,
        105,
        95,
        105,
        110,
        90,
        100
      ]
    }
  ]
}
```

## 策划参考价值
SLG武将/角色的数据结构参考。
