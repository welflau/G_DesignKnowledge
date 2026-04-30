# OpenRA(沙丘2000) · disable-player-experience 单位规则

> 来源：OpenRA/OpenRA
> 原始链接：https://github.com/OpenRA/OpenRA/blob/bleed/mods/d2k/rules/disable-player-experience.yaml
> 分类：numerical
> 标签：红色警戒, RTS, 单位属性, YAML规则, 沙丘2000

## 概述
沙丘2000的disable-player-experience单位/建筑属性定义（YAML格式）

## 正文
```yaml
^ExistsInWorld:
	GivesExperience:
		PlayerExperienceModifier: 0

^Building:
	RepairableBuilding:
		PlayerExperience: 0

engineer:
	Captures:
		PlayerExperience: 0

repair_pad:
	RepairsUnits:
		PlayerExperience: 0

```

## 策划参考价值
RTS单位数值设计的教科书级参考：血量/攻击/射程/造价/建造时间。
