# OpenRA(沙丘2000) · aircraft 单位规则

> 来源：OpenRA/OpenRA
> 原始链接：https://github.com/OpenRA/OpenRA/blob/bleed/mods/d2k/rules/aircraft.yaml
> 分类：numerical
> 标签：红色警戒, RTS, 单位属性, YAML规则, 沙丘2000

## 概述
沙丘2000的aircraft单位/建筑属性定义（YAML格式）

## 正文
```yaml
carryall.reinforce:
	Inherits: ^Plane
	Valued:
		Cost: 1000
	UpdatesPlayerStatistics:
		AddToAssetsValue: false
	Tooltip:
		Name: actor-carryall-reinforce.name
	Health:
		HP: 20000
	Armor:
		Type: light
	Aircraft:
		CruiseAltitude: 2160
		CruisingCondition: cruising
		Speed: 170
		TurnSpeed: 16
		LandableTerrainTypes: Sand, Rock, Transition, Spice, SpiceSand, Dune, Concrete
		Repulsable: False
		AirborneCondition: airborne
		CanForceLand: false
		CanSlide: True
		VTOL: true
		IdleTurnSpeed: 5
		IdleSpeed: 115
	Targetable@GROUND:
		TargetTypes: Ground, Vehicle
		RequiresCondition: !airborne
	Targetable@AIRBORNE:
		TargetTypes: Air
		RequiresCondition: airborne
	SpawnActorOnDeath@CRUISING:
		Actor: carryall.husk
		RequiresCondition: cruising
	SpawnActorOnDeath@LANDING:
		Actor: carryall.huskVTOL
		RequiresCondition: !cruising
	Carryall:
		BeforeLoadDelay: 10
		BeforeUnloadDelay: 15
		LocalOffset: 0, 0, -128
	RenderSprites:
		Image: carryall
	ChangesHealth:
		Step: 50
		Delay: 3
		StartIfBelow: 50
	Buildable:
		BuildDuration: 750
		BuildDurationModifier: 100
		Description: actor-carryall-reinforce.description

carryall:
	Inherits: carryall.reinforce
	UpdatesPlayerStatistics:
		AddToAssetsValue: true
	-Carryall:
	AutoCarryall:
		BeforeLoadDelay: 10
		BeforeUnloadDelay: 15
		LocalOffset: 0, 0, -128
	Encyclopedia:
		Description: actor-carryall-encyclopedia
		Order: 230
		Category: Units
	Aircraft:
		MinAirborneAltitude: 400
	RevealsShroud@lifting_low:
		Range: 2c512
		Type: GroundPosition
		RequiresCondition: !airborne
	RevealsShroud@lifting_high:
		Range: 1c256
		Type: GroundPosition
		RequiresCondition: !cruising
	Buildable:
		Queue: Aircraft
		BuildPaletteOrder: 120

frigate:
	Inherits: ^Plane
	ParaDrop:
		DropRange: 1c0
	Interactable:
	Tooltip:
		Name: actor-frigate-name
	Aircraft:
		IdleBehavior: LeaveMap
		Speed: 189
		TurnSpeed: 16
		Repulsable: False
		MaximumPitch: 20
		CruiseAltitude: 2048
		VTOL: true
		TakeOffOnCreation: false
		CanHover: true
	-AppearsOnRadar:
	Cargo:
		MaxWeight: 20
		BetweenUnloadDelay: 15
	RejectsOrders:

ornithopter:
	Inherits: ^Plane
	Buildable:
		Prerequisites: upgrade.hightech
	AttackBomber:
		FacingTolerance: 8
	Armament:
		Weapon: OrniBomb
	Health:
		HP: 8000
	Armor:
		Type: light
	Encyclopedia:
		Description: actor-ornithopter.encyclopedia
		Order: 240
		Category: Units
	Aircraft:
		Speed: 224
		TurnSpeed: 8
		Repulsable: False
		CruiseAltitude: 1920
	Targetable:
		TargetTypes: Air
	AmmoPool:
		Ammo: 5
	Tooltip:
		Name: actor-ornithopter.name
	SpawnActorOnDeath:
		Actor: ornithopter.husk
	RejectsOrders:
	-MapEditorData:

ornithopter.husk:
	Inherits: ^AircraftHusk
	Tooltip:
		Name: actor-ornithopter-husk-name
	Aircraft:
		TurnSpeed: 20
		Speed: 224
	RenderSprites:
		Image: ornithopter
	FallsToEarth:
		MaximumSpinSpeed: 1
	FireProjectilesOnDeath@derbisshort:
		Weapons: Debris, Debris2
		Pieces: 1, 3
		Range: 1c0, 2c512
	FireProjectilesOnDeath@derbislong:
		Weapons: Debris, Debris2, Debris3, Debris4
		Pieces: 2, 4
		Range: 3c0, 6c0

carryall.husk:
	Inherits: ^AircraftHusk
	Tooltip:
		Name: actor-carryall-husk-name
	Aircraft:
		TurnSpeed: 16
		Speed: 144
		CanSlide: True
		VTOL: true
	RenderSprites:
		Image: carryall
	FireProjectilesOnDeath@derbisshort:
		Weapons: Debris, Debris2
		Pieces: 1, 3
		Range: 1c0, 2c512
	FireProjectilesOnDeath@derbislong:
		Weapons: Debris, Debris2, Debris3, Debris4
		Pieces: 2, 4
		Range: 3c0, 6c0

carryall.huskVTOL:
	Inherits: ^AircraftHusk
	Tooltip:
		Name: actor-carryall-huskvtol-name
	FallsToEarth:
		Moves: False
		Velocity: 0c128
	Aircraft:
		TurnSpeed: 16
		CanSlide: True
		VTOL: true
	RenderSprites:
		Image: carryall
	FireProjectilesOnDeath@derbisshort:
		Weapons: Debris, Debris2
		Pieces: 1, 3
		Range: 1c0, 2c512
	FireProjectilesOnDeath@derbislong:
		Weapons: Debris, Debris2, Debris3, Debris4
		Pieces: 2, 4
		Range: 3c0, 6c0

```

## 策划参考价值
RTS单位数值设计的教科书级参考：血量/攻击/射程/造价/建造时间。
