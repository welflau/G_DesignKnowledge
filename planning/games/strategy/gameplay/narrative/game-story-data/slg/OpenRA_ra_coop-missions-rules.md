# 红色警戒 · coop-missions-rules

> 来源：OpenRA/OpenRA
> 原始链接：https://github.com/OpenRA/OpenRA
> 分类：gameplay
> 标签：红色警戒, RTS, 任务简报, 战役
> 游戏类型：RTS

## 概述
红色警戒的coop-missions-rules——RTS战役/任务简报叙事

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
RTS游戏战役叙事的数据结构：任务简报、胜利条件、故事文本如何与关卡绑定。
