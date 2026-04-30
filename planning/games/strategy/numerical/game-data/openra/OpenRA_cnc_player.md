# OpenRA(命令与征服) · player 单位规则

> 来源：OpenRA/OpenRA
> 原始链接：https://github.com/OpenRA/OpenRA/blob/bleed/mods/cnc/rules/player.yaml
> 分类：numerical
> 标签：红色警戒, RTS, 单位属性, YAML规则, 命令与征服

## 概述
命令与征服的player单位/建筑属性定义（YAML格式）

## 正文
```yaml
^BasePlayer:
	Shroud:
	PlayerResources:
		ResourceValues:
			Tiberium: 35
			BlueTiberium: 60

EditorPlayer:
	Inherits: ^BasePlayer

Player:
	Inherits: ^BasePlayer
	PlaceBuilding:
		NewOptionsNotification: NewOptions
		CannotPlaceNotification: BuildingCannotPlaceAudio
		NewOptionsTextNotification: notification-new-construction-options
		CannotPlaceTextNotification: notification-cannot-deploy-here
	TechTree:
	SupportPowerManager:
	ScriptTriggers:
	MissionObjectives:
		WinNotification: Win
		LoseNotification: Lose
		LeaveNotification: Leave
	ConquestVictoryConditions:
	PowerManager:
		SpeechNotification: LowPower
		TextNotification: notification-low-power
	AllyRepair:
	PlayerResources:
		CashTickUpNotification: CashTickUp
		CashTickDownNotification: CashTickDown
		SelectableCash: 2500, 5000, 7500, 10000, 20000
		DefaultCash: 7500
	DeveloperMode:
		CheckboxDisplayOrder: 9
	DamageNotifier:
		ValidTargets: Structure
		Notification: BaseAttack
		TextNotification: notification-base-under-attack
		AllyTextNotification: notification-ally-under-attack
	DamageNotifier@Unit:
		InvalidTargets: Structure
		NotifyInterval: 10000
	Shroud:
		FogCheckboxDisplayOrder: 3
	LobbyPrerequisiteCheckbox@GLOBALFACTUNDEPLOY:
		ID: factundeploy
		Label: checkbox-redeployable-mcvs.label
		Description: checkbox-redeployable-mcvs.description
		Enabled: True
		DisplayOrder: 7
		Prerequisites: global-factundeploy
	LobbyPrerequisiteCheckbox@GLOBALC17STEALTH:
		ID: C17-Stealth
		Label: checkbox-stealth-deliveries.label
		Description: checkbox-stealth-deliveries.description
		Enabled: False
		DisplayOrder: 8
		Prerequisites: global-C17-stealth
	PlayerStatistics:
	FrozenActorLayer:
	PlaceBeacon:
	ProvidesTechPrerequisite@low:
		Name: options-tech-level.low
		Prerequisites: techlevel.low
		Id: low
	ProvidesTechPrerequisite@medium:
		Name: options-tech-level.medium
		Prerequisites: techlevel.low, techlevel.medium
		Id: medium
	ProvidesTechPrerequisite@nosuper:
		Name: options-tech-level.no-powers
		Prerequisites: techlevel.low, techlevel.medium, techlevel.high
		Id: nopowers
	ProvidesTechPrerequisite@all:
		Name: options-tech-level.unrestricted
		Prerequisites: techlevel.low, techlevel.medium, techlevel.high, techlevel.superweapons
		Id: unrestricted
	GrantConditionOnPrerequisiteManager:
	ResourceStorageWarning:
		TextNotification: notification-silos-needed
	PlayerExperience:
	GameSaveViewportManager:
	PlayerRadarTerrain:

```

## 策划参考价值
RTS单位数值设计的教科书级参考：血量/攻击/射程/造价/建造时间。
