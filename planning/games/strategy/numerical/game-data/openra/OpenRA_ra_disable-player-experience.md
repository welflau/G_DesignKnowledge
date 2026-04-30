# OpenRA(红色警戒) · disable-player-experience 单位规则

> 来源：OpenRA/OpenRA
> 原始链接：https://github.com/OpenRA/OpenRA/blob/bleed/mods/ra/rules/disable-player-experience.yaml
> 分类：numerical
> 标签：红色警戒, RTS, 单位属性, YAML规则, 红色警戒

## 概述
红色警戒的disable-player-experience单位/建筑属性定义（YAML格式）

## 正文
```yaml
^ExistsInWorld:
	GivesExperience:
		PlayerExperienceModifier: 0

^Building:
	RepairableBuilding:
		PlayerExperience: 0

E6:
	Captures:
		PlayerExperience: 0

THF:
	Captures:
		PlayerExperience: 0

SPEN:
	RepairsUnits:
		PlayerExperience: 0

SYRD:
	RepairsUnits:
		PlayerExperience: 0

FIX:
	RepairsUnits:
		PlayerExperience: 0

TRUK:
	DeliversCash:
		PlayerExperience: 0

^InfiltratableFake:
	InfiltrateForDecoration:
		PlayerExperience: 0

MSLO:
	InfiltrateForSupportPowerReset:
		PlayerExperience: 0

SPEN:
	InfiltrateForSupportPower:
		PlayerExperience: 0

SYRD:
	InfiltrateForSupportPower:
		PlayerExperience: 0

IRON:
	InfiltrateForSupportPowerReset:
		PlayerExperience: 0

DOME:
	InfiltrateForExploration:
		PlayerExperience: 0

ATEK:
	InfiltrateForSupportPowerReset:
		PlayerExperience: 0

WEAP:
	InfiltrateForSupportPower:
		PlayerExperience: 0

PROC:
	InfiltrateForCash:
		PlayerExperience: 0
		PlayerExperiencePercentage: 0

HPAD:
	InfiltrateForSupportPower:
		PlayerExperience: 0

AFLD:
	InfiltrateForSupportPower:
		PlayerExperience: 0

POWR:
	InfiltrateForPowerOutage:
		PlayerExperience: 0

APWR:
	InfiltrateForPowerOutage:
		PlayerExperience: 0

BARR:
	InfiltrateForSupportPower:
		PlayerExperience: 0

TENT:
	InfiltrateForSupportPower:
		PlayerExperience: 0

```

## 策划参考价值
RTS单位数值设计的教科书级参考：血量/攻击/射程/造价/建造时间。
