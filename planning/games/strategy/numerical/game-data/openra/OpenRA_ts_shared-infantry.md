# OpenRA(泰伯利亚之日) · shared-infantry 单位规则

> 来源：OpenRA/OpenRA
> 原始链接：https://github.com/OpenRA/OpenRA/blob/bleed/mods/ts/rules/shared-infantry.yaml
> 分类：numerical
> 标签：红色警戒, RTS, 单位属性, YAML规则, 泰伯利亚之日

## 概述
泰伯利亚之日的shared-infantry单位/建筑属性定义（YAML格式）

## 正文
```yaml
E1:
	Inherits: ^Soldier
	Inherits@EXPERIENCE: ^GainsExperience
	Inherits@EXPHOSPITAL: ^InfantryExperienceHospitalOverrides
	Inherits@AUTOTARGET: ^AutoTargetGroundAssaultMove
	Buildable:
		Queue: Infantry
		BuildPaletteOrder: 10
		Prerequisites: ~barracks, ~techlevel.low
		Description: actor-e1.description
	Valued:
		Cost: 120
	Tooltip:
		Name: actor-e1.name
	UpdatesPlayerStatistics:
		AddToArmyValue: true
	Health:
		HP: 12500
	Mobile:
		Speed: 71
	Armament@PRIMARY:
		Weapon: Minigun
		RequiresCondition: !rank-elite
	Armament@ELITE:
		Weapon: M1Carbine
		RequiresCondition: rank-elite
	AttackFrontal:
		Voice: Attack
		FacingTolerance: 0
	WithSplitAttackPaletteInfantryBody:
		DefaultAttackSequence: attack
	ProducibleWithLevel:
		Prerequisites: barracks.upgraded
	RenderSprites:
		Image: e1.gdi
		FactionImages:
			gdi: e1.gdi
			nod: e1.nod
	RevealsShroud:
		Range: 5c0

E1R3:
	Inherits: E1
	RenderSprites:
		Image: e1.gdi
	ProducibleWithLevel:
		Prerequisites: techlevel.low
		InitialLevels: 3
	-Buildable:

ENGINEER:
	Inherits: ^Soldier
	Inherits@selection: ^SelectableSupportUnit
	Valued:
		Cost: 500
	Tooltip:
		Name: actor-engineer.name
	UpdatesPlayerStatistics:
		AddToArmyValue: true
	Buildable:
		Queue: Infantry
		BuildPaletteOrder: 40
		Prerequisites: ~barracks, ~techlevel.low
		Description: actor-engineer.description
	Voiced:
		VoiceSet: Engineer
	Mobile:
		Speed: 56
	Health:
		HP: 10000
	Passenger:
		CustomPipType: yellow
	InstantlyRepairs:
	RepairsBridges:
		RepairNotification: BridgeRepaired
		RepairTextNotification: notification-bridge-repaired
	CaptureManager:
	Captures:
		CaptureTypes: building
		PlayerExperience: 10
	RenderSprites:
		Image: engineer.gdi
		FactionImages:
			gdi: engineer.gdi
			nod: engineer.nod

FLAMEGUY:
	Inherits@1: ^ExistsInWorld
	Inherits@2: ^SpriteActor
	Mobile:
		Speed: 36
		Locomotor: flameguy
	HiddenUnderFog:
	WithInfantryBody:
		IdleSequences: run
	Health:
		HP: 16000
	ChangesHealth:
		Step: -1000
		StartIfBelow: 101
	ScaredyCat:
		PanicSequencePrefix:
	WithDeathAnimation:
		FallbackSequence: die
		UseDeathTypeSuffix: false
	HitShape:
	MapEditorData:
		Categories: System

```

## 策划参考价值
RTS单位数值设计的教科书级参考：血量/攻击/射程/造价/建造时间。
