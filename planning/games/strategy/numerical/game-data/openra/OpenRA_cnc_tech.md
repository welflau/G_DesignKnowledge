# OpenRA(命令与征服) · tech 单位规则

> 来源：OpenRA/OpenRA
> 原始链接：https://github.com/OpenRA/OpenRA/blob/bleed/mods/cnc/rules/tech.yaml
> 分类：numerical
> 标签：红色警戒, RTS, 单位属性, YAML规则, 命令与征服

## 概述
命令与征服的tech单位/建筑属性定义（YAML格式）

## 正文
```yaml
V19:
	Inherits: ^TechBuilding
	Selectable:
		Bounds: 1024, 1024
	CashTrickler:
		Amount: 10
		RequiresCondition: enabled
	Building:
		Footprint: x
		Dimensions: 1,1
	Health:
		HP: 80000
	Encyclopedia:
		Description: actor-v19.encyclopedia
		Order: 0
		Category: Civilian
		Scale: 2
		PreviewOwner: GDI
	Tooltip:
		Name: actor-v19.name
	TooltipDescription@ally:
		Description: actor-v19.captured-desc
		ValidRelationships: Ally
	TooltipDescription@other:
		Description: actor-v19.capturable-desc
		ValidRelationships: Neutral, Enemy
	SpawnActorOnDeath:
		Actor: V19.Husk
	UpdatesDerrickCount:
	GrantConditionOnCombatantOwner:
		Condition: enabled
	RenderSprites:
		PlayerPalette: derrick

V19.Husk:
	Inherits: ^CivBuildingHusk
	Interactable:
		Bounds: 1024, 1024
	WithSpriteBody:
	WithIdleOverlay:
		StartSequence: fire-start
		Sequence: fire-loop
	Building:
		Footprint: x
		Dimensions: 1,1
	Tooltip:
		Name: actor-v19-husk-name
	RenderSprites:
		PlayerPalette: derrick

HOSP:
	Inherits: ^TechBuilding
	Inherits@shape: ^2x2Shape
	Selectable:
		Bounds: 2048, 2048
	Building:
		Footprint: xx xx
		Dimensions: 2,2
	Health:
		HP: 250000
	Encyclopedia:
		Description: actor-hosp.encyclopedia
		Order: 10
		Category: Civilian
		Scale: 2
		PreviewOwner: GDI
	Tooltip:
		Name: actor-hosp.name
	TooltipDescription@ally:
		Description: actor-hosp.captured-desc
		ValidRelationships: Ally
	TooltipDescription@other:
		Description: actor-hosp.capturable-desc
		ValidRelationships: Neutral, Enemy
	SpawnActorOnDeath:
		Actor: HOSP.Husk
	WithBuildingBib:
		HasMinibib: true
	ProvidesPrerequisite@buildingname:

HOSP.Husk:
	Inherits: ^CivBuildingHusk
	Interactable:
		Bounds: 2048, 2048
	Building:
		Footprint: xx xx
		Dimensions: 2,2
	Tooltip:
		Name: actor-hosp-husk-name
	WithBuildingBib:
		HasMinibib: true

BIO:
	Inherits: ^TechBuilding
	Inherits@shape: ^2x2Shape
	Selectable:
		Bounds: 2048, 2048
	Building:
		Footprint: xx xx
		Dimensions: 2,2
	Health:
		HP: 250000
	Encyclopedia:
		Description: actor-bio.encyclopedia
		Order: 10
		Category: Civilian
		Scale: 2
		PreviewOwner: GDI
	Tooltip:
		Name: actor-bio.name
	TooltipDescription@ally:
		Description: actor-bio.captured-desc
		ValidRelationships: Ally
	TooltipDescription@other:
		Description: actor-bio.capturable-desc
		ValidRelationships: Neutral, Enemy
	SpawnActorOnDeath:
		Actor: BIO.Husk
	ProvidesPrerequisite@buildingname:

BIO.Husk:
	Inherits: ^CivBuildingHusk
	Interactable:
		Bounds: 2048, 2048
	Building:
		Footprint: xx xx
		Dimensions: 2,2
	Tooltip:
		Name: actor-bio-husk-name

MISS:
	Inherits: ^TechBuilding
	Inherits@shape: ^3x2Shape
	HitShape:
		UseTargetableCellsOffsets: false
		TargetableOffsets: 0,0,0, 840,0,0, 840,-1024,0, 420,768,0, -840,0,0, -840,-1024,0, -840,1024,0
	Selectable:
		Bounds: 3072, 2048
	Building:
		Footprint: xxx xxx
		Dimensions: 3,2
	Tooltip:
		Name: actor-miss.name
	Buildable:
		Queue: Building
		BuildPaletteOrder: 1000
		Prerequisites: ~disabled
	Valued:
		Cost: 0
	Health:
		HP: 80000
	Encyclopedia:
		Description: actor-miss.encyclopedia
		Order: 20
		Category: Civilian
		Scale: 2
		HideBuildable: true
		PreviewOwner: GDI
	RevealsShroud:
		Range: 13c0
	TooltipDescription@ally:
		Description: actor-miss.captured-desc
		ValidRelationships: Ally
	TooltipDescription@other:
		Description: actor-miss.capturable-desc
		ValidRelationships: Neutral, Enemy
	WithBuildingBib:
		HasMinibib: true
	WithMakeAnimation:
	ProvidesPrerequisite@buildingname:

```

## 策划参考价值
RTS单位数值设计的教科书级参考：血量/攻击/射程/造价/建造时间。
