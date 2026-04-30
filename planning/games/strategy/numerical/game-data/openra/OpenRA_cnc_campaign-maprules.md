# OpenRA(命令与征服) · campaign-maprules 单位规则

> 来源：OpenRA/OpenRA
> 原始链接：https://github.com/OpenRA/OpenRA/blob/bleed/mods/cnc/rules/campaign-maprules.yaml
> 分类：numerical
> 标签：红色警戒, RTS, 单位属性, YAML规则, 命令与征服

## 概述
命令与征服的campaign-maprules单位/建筑属性定义（YAML格式）

## 正文
```yaml
World:
	-SpawnStartingUnits:
	-MapStartingLocations:
	-CrateSpawner:
	ObjectivesPanel:
		PanelName: MISSION_OBJECTIVES
	MapCreeps:
		CheckboxVisible: False
		CheckboxLocked: True
		CheckboxEnabled: False
	MapBuildRadius:
		AllyBuildRadiusCheckboxVisible: False
		AllyBuildRadiusCheckboxLocked: True
		AllyBuildRadiusCheckboxEnabled: False
		BuildRadiusCheckboxVisible: False
		BuildRadiusCheckboxLocked: True
		BuildRadiusCheckboxEnabled: True
	MapOptions:
		ShortGameCheckboxVisible: False
		ShortGameCheckboxLocked: True
		ShortGameCheckboxEnabled: False
		TechLevelDropdownVisible: False
		TechLevelDropdownLocked: True
	TimeLimitManager:
		TimeLimitDropdownVisible: False

Player:
	-ConquestVictoryConditions:
	MissionObjectives:
		EarlyGameOver: true
		GameOverDelay: 3000
	Shroud:
		FogCheckboxVisible: False
		FogCheckboxLocked: True
		FogCheckboxEnabled: True
		ExploredMapCheckboxVisible: False
		ExploredMapCheckboxLocked: True
		ExploredMapCheckboxEnabled: False
	PlayerResources:
		DefaultCashDropdownVisible: False
		DefaultCashDropdownLocked: True
		DefaultCash: 5000
	LobbyPrerequisiteCheckbox@GLOBALFACTUNDEPLOY:
		Enabled: False
		Locked: True
		Visible: False
	LobbyPrerequisiteCheckbox@GLOBALC17STEALTH:
		Enabled: False
		Locked: True
		Visible: False
	DeveloperMode:
		CheckboxVisible: False
	ModularBot@CampaignAI:
		Name: bot-campaign-ai.name
		Type: campaign

airstrike.proxy:
	AirstrikePower:
		Icon: airstrike
		StartFullyCharged: True
		ChargeInterval: 3000
		SquadSize: 3
		QuantizedFacings: 8
		Name: actor-hq.airstrikepower-name
		Description: actor-hq.airstrikepower-description
		EndChargeSpeechNotification: AirstrikeReady
		SelectTargetSpeechNotification: SelectTarget
		InsufficientPowerSpeechNotification: InsufficientPower
		IncomingSpeechNotification: EnemyPlanesApproaching
		EndChargeTextNotification: notification-airstrike-ready
		SelectTargetTextNotification: notification-select-target
		InsufficientPowerTextNotification: notification-insufficient-power
		IncomingTextNotification: notification-enemy-planes-approaching
		UnitType: a10
		DisplayBeacon: True
		BeaconPoster: airstrike
		DisplayRadarPing: True
		CameraActor: camera
		ArrowSequence: arrow
		ClockSequence: clock
		CircleSequence: circles
		SupportPowerPaletteOrder: 10

MoneyCrate:
	Inherits: ^Crate
	Tooltip:
		Name: actor-moneycrate-name
	GiveCashCrateAction:
		Amount: 2000
		Sequence: dollar
		UseCashTick: true
	RenderSprites:
		Image: wcrate

TRUCK:
	Buildable:
		Prerequisites: ~disabled

MISS:
	Inherits: ^CivBuilding
	RevealsShroud:
		Range: 3c0

```

## 策划参考价值
RTS单位数值设计的教科书级参考：血量/攻击/射程/造价/建造时间。
