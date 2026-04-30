# OpenRA(泰伯利亚之日) · player 单位规则

> 来源：OpenRA/OpenRA
> 原始链接：https://github.com/OpenRA/OpenRA/blob/bleed/mods/ts/rules/player.yaml
> 分类：numerical
> 标签：红色警戒, RTS, 单位属性, YAML规则, 泰伯利亚之日

## 概述
泰伯利亚之日的player单位/建筑属性定义（YAML格式）

## 正文
```yaml
^BasePlayer:
	Shroud:
	PlayerResources:
		ResourceValues:
			Tiberium: 25
			BlueTiberium: 40
			Veins: 0

EditorPlayer:
	Inherits: ^BasePlayer

Player:
	Inherits: ^BasePlayer
	TechTree:
	GrantConditionOnPrerequisiteManager:
	ClassicProductionQueue@Building:
		Type: Building
		DisplayOrder: 0
		BuildDurationModifier: 120
		LowPowerModifier: 300
		ReadyAudio: ConstructionComplete
		ReadyTextNotification: notification-construction-complete
		LimitedAudio: BuildingInProgress
		LimitedTextNotification: notification-unable-to-comply-building-in-progress
		QueuedAudio: Building
		OnHoldAudio: OnHold
		CancelledAudio: Cancelled
		SpeedUp: True
	ClassicProductionQueue@Support:
		Type: Support
		DisplayOrder: 1
		BuildDurationModifier: 120
		LowPowerModifier: 300
		ReadyAudio: ConstructionComplete
		ReadyTextNotification: notification-construction-complete
		LimitedAudio: BuildingInProgress
		LimitedTextNotification: notification-unable-to-comply-building-in-progress
		QueuedAudio: Building
		OnHoldAudio: OnHold
		CancelledAudio: Cancelled
		SpeedUp: True
	ClassicProductionQueue@Vehicle:
		Type: Vehicle
		DisplayOrder: 3
		BuildDurationModifier: 120
		LowPowerModifier: 300
		ReadyAudio: UnitReady
		ReadyTextNotification: notification-unit-ready
		LimitedAudio: BuildingInProgress
		LimitedTextNotification: notification-unable-to-comply-building-in-progress
		QueuedAudio: Training
		OnHoldAudio: OnHold
		CancelledAudio: Cancelled
		SpeedUp: True
	ClassicProductionQueue@Infantry:
		Type: Infantry
		DisplayOrder: 2
		BuildDurationModifier: 120
		LowPowerModifier: 300
		ReadyAudio: UnitReady
		ReadyTextNotification: notification-unit-ready
		LimitedAudio: BuildingInProgress
		LimitedTextNotification: notification-unable-to-comply-building-in-progress
		QueuedAudio: Training
		OnHoldAudio: OnHold
		CancelledAudio: Cancelled
		SpeedUp: True
	ClassicProductionQueue@Air:
		Type: Air
		DisplayOrder: 4
		BuildDurationModifier: 120
		LowPowerModifier: 300
		ReadyAudio: UnitReady
		ReadyTextNotification: notification-unit-ready
		LimitedAudio: BuildingInProgress
		LimitedTextNotification: notification-unable-to-comply-building-in-progress
		QueuedAudio: Training
		OnHoldAudio: OnHold
		CancelledAudio: Cancelled
		SpeedUp: True
	PlaceBuilding:
		NewOptionsNotification: NewOptions
		CannotPlaceNotification: BuildingCannotPlaceAudio
		NewOptionsTextNotification: notification-new-construction-options
		CannotPlaceTextNotification: notification-cannot-deploy-here
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
		InsufficientFundsNotification: InsufficientFunds
		InsufficientFundsTextNotification: notification-insufficient-funds
		CashTickUpNotification: CashTickUp
		CashTickDownNotification: CashTickDown
	DeveloperMode:
		CheckboxEnabled: true
		CheckboxDisplayOrder: 8
	Shroud:
		FogCheckboxDisplayOrder: 3
	LobbyPrerequisiteCheckbox@GLOBALFACTUNDEPLOY:
		ID: factundeploy
		Label: checkbox-redeployable-mcvs.label
		Description: checkbox-redeployable-mcvs.description
		Enabled: True
		DisplayOrder: 7
		Prerequisites: global-factundeploy
	FrozenActorLayer:
	DamageNotifier:
		ValidTargets: Building
		Notification: BaseAttack
		TextNotification: notification-base-under-attack
		AllyTextNotification: notification-ally-under-attack
		AllyNotification: OurAllyIsUnderAttack
	DamageNotifier@Unit:
		InvalidTargets: Building
		NotifyInterval: 10000
	HarvesterAttackNotifier:
		TextNotification: notification-harvester-under-attack
	PlayerStatistics:
	PlaceBeacon:
		Palette: effect
		IsPlayerPalette: false
		BeaconSequence: idle
		ArrowSequence:
		CircleSequence:
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
	ResourceStorageWarning:
		TextNotification: notification-silos-needed
	PlayerExperience:
	GameSaveViewportManager:
	PlayerRadarTerrain:

```

## 策划参考价值
RTS单位数值设计的教科书级参考：血量/攻击/射程/造价/建造时间。
