# 碧蓝航线 · fleet tech

> 来源：MrLar/AzurLaneData
> 原始链接：https://github.com/MrLar/AzurLaneData/blob/master/docs/ships/fleet_tech.md
> 分类：numerical
> 标签：碧蓝航线, 数据解包, 舰船属性

## 概述
碧蓝航线数据文档：fleet_tech

## 正文
---
title: Ship Fleet Tech Documentation
---

# Fleet Tech

Contains information about bonuses and points granted for each fleet tech task of a ship. Contains
the following properties:

|       Property        |                          Type                           |                                                              Description                                                              |
| :-------------------: | :-----------------------------------------------------: | :-----------------------------------------------------------------------------------------------------------------------------------: |
|      **collect**      |     [`ShipFleetTechBonus`](#ship-fleet-tech-bonus)      |                                                  Bonus Data for collecting the ship.                                                  |
|       **level**       |     [`ShipFleetTechBonus`](#ship-fleet-tech-bonus)      |                                           Bonus Data for reaching level 120 with the ship.                                            |
|    **limit_break**    | [`Partial(ShipFleetTechBonus)`](#ship-fleet-tech-bonus) |                 Bonus Data for reaching max limit break with the ship.<br>**Only contains "pts" at time of writing.**                 |
| **sort_data.class**\* |                        `number`                         | The ID of the sort class this ship belongs to in `fleet_tech_sort.json` can be mapped to [`FleetTechSortData`](#fleet-tech-sort-data) |
| **sort_data.index**\* |                        `number`                         |                                                   The sort index within that class                                                    |

\* Sorting is not perfectly reproducable by all sorting implementations due to the fact that lua sort is unstable (but consistent).

# Ship Fleet Tech Bonus

Represents the bonus and points granted for a single fleet technology task of a ship.
It extends [`FleetTechBonus`](../tech_groups/index.md#fleet-tech-bonus) and additionally provides: 

| Property |   Type   |                                          Description                                           |
| :------: | :------: | :--------------------------------------------------------------------------------------------: |
| **pts**  | `number` | Amount of tech points granted. To establish what nation these go towards use the ships nation. |


# Fleet Tech Sort Data
Represents the data relevant for sorting ships the same way as they appear in the Technology menu in game. It provides:

|   Property    |              Type               |                                      Description                                      |
| :-----------: | :-----------------------------: | :-----------------------------------------------------------------------------------: |
|  **primary**  |            `number`             | The primary sort index. The game uses this to sort highest primary to lowest primary. |
| **secondary** |            `number`             | The secondary sort index. If primary is the same the game ascendingly sorts by this.  |
|  **nation**   | [`Nation`](../common.md#nation) |                           The nation this class belongs to.                           |


## 策划参考价值
舰船属性成长率/强化/装备数值体系参考。
