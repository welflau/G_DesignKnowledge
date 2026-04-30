# 碧蓝航线 · ghost equip

> 来源：MrLar/AzurLaneData
> 原始链接：https://github.com/MrLar/AzurLaneData/blob/master/docs/ships/ghost_equip.md
> 分类：numerical
> 标签：碧蓝航线, 数据解包, 舰船属性

## 概述
碧蓝航线数据文档：ghost_equip

## 正文
---
title: Ship Ghost Equip Documentation
---

# Ghost Equipment Data

Represents the data for a ghost equipment of a ship. These equipments cannot be removed or upgraded in any way. Some ships have these via skills or simply built in. Contains the following properties:

|      Property       |    Type    |                                                                                                                                                  Description                                                                                                                                                   |
| :-----------------: | :--------: | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------: |
|       **id**        |  `number`  |                      Equipment ID of this ghost weapon. These IDs are represented in [`default_equips`](https://github.com/MrLar/AzurLaneData/tree/main/data/default_equips.json).<br>If `obtainable` is `true` it is instead represented in [`equipments`](../../data/equipments.json).                       |
|      **level**      |  `number`  |                                                                                                          0-indexed level of this ghost weapon. i.E. a skill stating Lv.10 would have this equal to 9.                                                                                                          |
|   **efficiency**    |  `number`  |                                                                                                                                 The efficiency of this ghost weapon (decimal).                                                                                                                                 |
|     **skill?**      |  `number`  |                                   **(Optional)** ID of the Skill that grants this weapon.<br>If this is present `level` should be ignored and the skills level minus 1 should be used.<br>If `level_override` is present the `level_override[skill lvl - 1]` should be used.                                   |
| **level_override?** | `number[]` |                                                                                                                         **(Optional)** Enhancement level to use at given skill level.                                                                                                                          |
|  **id_override?**   | `number[]` | **(Optional)** Default equip IDs to use instead of `id` for each enhance level. Used for ghost weapons with notable differences between levels.<br>If present `level` (with respect to the notes in `skill` and `level_override`) is used to index this property and the effective enhance level is always +0. |


## 策划参考价值
舰船属性成长率/强化/装备数值体系参考。
