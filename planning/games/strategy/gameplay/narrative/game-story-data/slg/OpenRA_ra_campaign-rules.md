# 红色警戒 · campaign-rules

> 来源：OpenRA/OpenRA
> 原始链接：https://github.com/OpenRA/OpenRA
> 分类：gameplay
> 标签：红色警戒, RTS, 任务简报, 战役
> 游戏类型：RTS

## 概述
红色警戒的campaign-rules——RTS战役/任务简报叙事

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
RTS游戏战役叙事的数据结构：任务简报、胜利条件、故事文本如何与关卡绑定。
