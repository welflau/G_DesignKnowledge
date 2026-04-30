# 碧蓝航线 · research

> 来源：MrLar/AzurLaneData
> 原始链接：https://github.com/MrLar/AzurLaneData/blob/master/docs/ships/research.md
> 分类：numerical
> 标签：碧蓝航线, 数据解包, 舰船属性

## 概述
碧蓝航线数据文档：research

## 正文
---
title: Ship Research Data Documentation
---

# PR Data

Data for all research ships. Contains the following properties:

|  Property  |                      Type                       |                                                             Description                                                              |
| :--------: | :---------------------------------------------: | :----------------------------------------------------------------------------------------------------------------------------------: |
| **stats?** | [`BasicShipStats`](./index.md#basic-ship-stats) | **(Optional)** Stats granted by development milestones. These are at Dev0, Dev10, Dev20 and Dev30 for each limit break respectively. |
| **fate?**  |            [`FateData`](#fate-data)             |                            **(Optional)** Data for fate simulation. Absent if the ship does not have one.                            |

# Fate Data

Represents the data for a ships fate simulation under the assumption that it is fate sim 5. Contains
the following properties:

|  Property  |                          Type                           |                                Description                                |
| :--------: | :-----------------------------------------------------: | :-----------------------------------------------------------------------: |
| **stats**  |     [`BasicShipStats`](./index.md#basic-ship-stats)     | Stats granted by all Fate Simulation levels up to and including FateSim5. |
| **skills** | [`SkillUpgradeData[]`](../common.md#skill-upgrade-data) |                        List of all Skill Upgrades.                        |
|  **date**  |                        `number`                         |                   Release date of this Fate Simulation.                   |


## 策划参考价值
舰船属性成长率/强化/装备数值体系参考。
