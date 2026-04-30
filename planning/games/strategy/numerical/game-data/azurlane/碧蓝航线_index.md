# 碧蓝航线 · index

> 来源：MrLar/AzurLaneData
> 原始链接：https://github.com/MrLar/AzurLaneData/blob/master/docs/tech_groups/index.md
> 分类：numerical
> 标签：碧蓝航线, 数据解包, 舰船属性

## 概述
碧蓝航线数据文档：index

## 正文
---
title: Fleet Tech Groups Documentation
---

# Tech Group

Tech Group represents the data associated with a Fleet Technology in game:

|  Property  |                  Type                   |          Description          |
| :--------: | :-------------------------------------: | :---------------------------: |
|   **id**   |                `number`                 |     The ID of this group.     |
|  **name**  |                `string`                 |     Names of this group.      |
| **nation** |     [`Nation`](../common.md#nation)     | The Nation this group is for. |
| **levels** | [`TechGroupLevel[]`](#tech-group-level) |     Levels in this group.     |

Levels do not include the default starting level 0 as it does not contain any bonuses.

# Tech Group Level

Tech Group level represents a single level of a Tech Group:

|  Property   |                  Type                   |                                Description                                |
| :---------: | :-------------------------------------: | :-----------------------------------------------------------------------: |
| **points**  |                `number`                 |      Amount of fleet tech points needed from the respective nation.       |
| **bonuses** | [`FleetTechBonus[]`](#fleet-tech-bonus) | Bonuses this level grants. **The previous level is *replaced* entirely**. |

# Fleet Tech Bonus

Represents the bonus and points granted for a single fleet technology task. Contains the following
properties:

| Property  |                     Type                     |                   Description                    |
| :-------: | :------------------------------------------: | :----------------------------------------------: |
| **stat**  | [`TechStatKey`](../common.md#tech-stat-keys) |      The stat that gains a permanent bonus.      |
| **hulls** |        [`Hull[]`](../common.md#Hull)         | The hulls that benefit from the permanent bonus. |
| **value** |                   `number`                   |        The amount of the permanent bonus.        |


## 策划参考价值
舰船属性成长率/强化/装备数值体系参考。
