# OpenRA(命令与征服) · disable-player-experience 单位规则

> 来源：OpenRA/OpenRA
> 原始链接：https://github.com/OpenRA/OpenRA/blob/bleed/mods/cnc/rules/disable-player-experience.yaml
> 分类：numerical
> 标签：红色警戒, RTS, 单位属性, YAML规则, 命令与征服

## 概述
命令与征服的disable-player-experience单位/建筑属性定义（YAML格式）

## 正文
```yaml
^ExistsInWorld:
	GivesExperience:
		PlayerExperienceModifier: 0

^BaseBuilding:
	RepairableBuilding:
		PlayerExperience: 0

^TechBuilding:
	RepairableBuilding:
		PlayerExperience: 0

E6:
	Captures:
		PlayerExperience: 0

HPAD:
	RepairsUnits:
		PlayerExperience: 0

FIX:
	RepairsUnits:
		PlayerExperience: 0

```

## 策划参考价值
RTS单位数值设计的教科书级参考：血量/攻击/射程/造价/建造时间。
