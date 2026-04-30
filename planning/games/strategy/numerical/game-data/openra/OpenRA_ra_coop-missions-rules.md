# OpenRA(红色警戒) · coop-missions-rules 单位规则

> 来源：OpenRA/OpenRA
> 原始链接：https://github.com/OpenRA/OpenRA/blob/bleed/mods/ra/rules/coop-missions-rules.yaml
> 分类：numerical
> 标签：红色警戒, RTS, 单位属性, YAML规则, 红色警戒

## 概述
红色警戒的coop-missions-rules单位/建筑属性定义（YAML格式）

## 正文
```yaml
Player:
	Shroud:
		FogCheckboxVisible: True
		ExploredMapCheckboxVisible: True
	PlayerResources:
		DefaultCashDropdownVisible: True
	LobbyPrerequisiteCheckbox@GLOBALBOUNTY:
		Visible: True
	LobbyPrerequisiteCheckbox@GLOBALFACTUNDEPLOY:
		Visible: True
	LobbyPrerequisiteCheckbox@REUSABLEENGINEERS:
		Visible: True
	DeveloperMode:
		CheckboxVisible: True

World:
	CrateSpawner:
		CheckboxVisible: True
	MapBuildRadius:
		AllyBuildRadiusCheckboxVisible: True
		BuildRadiusCheckboxVisible: True
	MapOptions:
		ShortGameCheckboxVisible: True
		TechLevelDropdownVisible: True
	TimeLimitManager:
		TimeLimitDropdownVisible: True

```

## 策划参考价值
RTS单位数值设计的教科书级参考：血量/攻击/射程/造价/建造时间。
