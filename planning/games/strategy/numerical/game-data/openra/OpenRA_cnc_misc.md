# OpenRA(命令与征服) · misc 单位规则

> 来源：OpenRA/OpenRA
> 原始链接：https://github.com/OpenRA/OpenRA/blob/bleed/mods/cnc/rules/misc.yaml
> 分类：numerical
> 标签：红色警戒, RTS, 单位属性, YAML规则, 命令与征服

## 概述
命令与征服的misc单位/建筑属性定义（YAML格式）

## 正文
```yaml
CRATE.plain:
	Inherits: ^Crate
	ScriptTriggers:

CRATE:
	Inherits: ^Crate
	Crate:
		Duration: 6000
	GiveCashCrateAction:
		Amount: 1000
		SelectionShares: 20
		UseCashTick: true
	RevealMapCrateAction:
		SelectionShares: 1
		Sequence: reveal-map
	ExplodeCrateAction@fire:
		Weapon: Napalm.Crate
		SelectionShares: 5
	GrantExternalConditionCrateAction@cloak:
		SelectionShares: 5
		Sequence: cloak
		Condition: cloak-crate-collected
	GiveBaseBuilderCrateAction:
		SelectionShares: 0
		NoBaseSelectionShares: 50
		Units: mcv
	ExplodeCrateAction:
		Weapon: Atomic
		SelectionShares: 1
	GiveUnitCrateAction:
		Units: vice
		Owner: Creeps
		SelectionShares: 10
	LevelUpCrateAction:
		Levels: 4
		SelectionShares: 12

WCRATE:
	Inherits: ^Crate
	Tooltip:
		Name: actor-wcrate-name
	RenderSprites:
		Image: wcrate

SCRATE:
	Inherits: ^Crate
	Tooltip:
		Name: actor-scrate-name

mpspawn:
	Interactable:
	EditorOnlyTooltip:
		Name: actor-mpspawn-name
	Immobile:
		OccupiesSpace: false
	WithSpriteBody:
	RenderSpritesEditorOnly:
	BodyOrientation:
		QuantizedFacings: 1
	MapEditorData:
		Categories: System
	RequiresSpecificOwners:
		ValidOwnerNames: Neutral

waypoint:
	Interactable:
	EditorOnlyTooltip:
		Name: actor-waypoint-name
	Immobile:
		OccupiesSpace: false
	WithSpriteBody:
	RenderSpritesEditorOnly:
	BodyOrientation:
		QuantizedFacings: 1
	MapEditorData:
		Categories: System

fact.colorpicker:
	Inherits: FACT
	-Buildable:
	-MapEditorData:
	-BaseBuilding:
	-Encyclopedia:
	RenderSprites:
		Image: fact
		Palette: colorpicker

CAMERA:
	Interactable:
	EditorOnlyTooltip:
		Name: actor-camera-name
	WithSpriteBody:
	RenderSpritesEditorOnly:
	BodyOrientation:
		QuantizedFacings: 1
	Immobile:
		OccupiesSpace: false
	RevealsShroud:
		Range: 10c0
		Type: CenterPosition
	MapEditorData:
		Categories: System

CAMERA.small:
	Interactable:
	EditorOnlyTooltip:
		Name: actor-camera-small-name
	WithSpriteBody:
	RenderSpritesEditorOnly:
		Image: camera
	BodyOrientation:
		QuantizedFacings: 1
	Immobile:
		OccupiesSpace: false
	Health:
		HP: 100000
	HitShape:
	RevealsShroud:
		Range: 6c0
		Type: CenterPosition
	MapEditorData:
		Categories: System

FLARE:
	Immobile:
		OccupiesSpace: false
	RevealsShroud:
		Range: 3c0
		Type: CenterPosition
	RenderSprites:
		Image: smokland
		Palette: terrain
	WithSpriteBody:
		StartSequence: open
	HiddenUnderFog:
		Type: CenterPosition
	Tooltip:
		Name: actor-flare-name
		ShowOwnerRow: false
	BodyOrientation:
		QuantizedFacings: 1
	MapEditorData:
		Categories: System
	Interactable:

```

## 策划参考价值
RTS单位数值设计的教科书级参考：血量/攻击/射程/造价/建造时间。
