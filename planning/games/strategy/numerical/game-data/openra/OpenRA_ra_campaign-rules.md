# OpenRA(红色警戒) · campaign-rules 单位规则

> 来源：OpenRA/OpenRA
> 原始链接：https://github.com/OpenRA/OpenRA/blob/bleed/mods/ra/rules/campaign-rules.yaml
> 分类：numerical
> 标签：红色警戒, RTS, 单位属性, YAML规则, 红色警戒

## 概述
红色警戒的campaign-rules单位/建筑属性定义（YAML格式）

## 正文
```yaml
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
		DefaultCash: 0
	LobbyPrerequisiteCheckbox@GLOBALBOUNTY:
		Enabled: False
		Locked: True
		Visible: False
	LobbyPrerequisiteCheckbox@GLOBALFACTUNDEPLOY:
		Enabled: True
		Locked: True
		Visible: False
	LobbyPrerequisiteCheckbox@REUSABLEENGINEERS:
		Enabled: False
		Locked: True
		Visible: False
	DeveloperMode:
		CheckboxVisible: False
	ModularBot@CampaignAI:
		Name: bot-campaign-ai.name
		Type: campaign

World:
	CrateSpawner:
		CheckboxEnabled: False
		CheckboxLocked: True
		CheckboxVisible: False
	-SpawnStartingUnits:
	-MapStartingLocations:
	ObjectivesPanel:
		PanelName: MISSION_OBJECTIVES
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

E7:
	-Crushable:

E7.noautotarget:
	Inherits: E7
	-AutoTarget:
	-AutoTargetPriority@DEFAULT:
	-AutoTargetPriority@ATTACKANYTHING:
	AttackMove:
		-AssaultMoveCondition:
	RenderSprites:
		Image: E7

^Vehicle:
	Demolishable:

HARV:
	Harvester:
		SearchFromProcRadius: 50
		SearchFromHarvesterRadius: 50

^Crate:
	Crate:
		Duration: 0

MONEYCRATE:
	Tooltip:
		Name: actor-crate-name
	GiveCashCrateAction:
		Amount: 2000

FCOM:
	Capturable:
		Types: ~disabled
	-GivesBuildableArea:
	BaseProvider:
		Range: 0
	RepairableBuilding:
		RepairStep: 700
		PlayerExperience: 5
		RepairingNotification: Repairing
	WithBuildingRepairDecoration:
		Image: allyrepair
		Sequence: repair
		Position: Center
		Palette: player
		IsPlayerPalette: True

MISS:
	RevealsShroud:
		Range: 3c0
	-RevealsShroud@GAPGEN:

TRUK:
	Buildable:
		Prerequisites: ~disabled

Ant:
	Buildable:
		Prerequisites: ~disabled

Zombie:
	Buildable:
		Prerequisites: ~disabled

```

## 策划参考价值
RTS单位数值设计的教科书级参考：血量/攻击/射程/造价/建造时间。
