# OpenRA(泰伯利亚之日) · critters 单位规则

> 来源：OpenRA/OpenRA
> 原始链接：https://github.com/OpenRA/OpenRA/blob/bleed/mods/ts/rules/critters.yaml
> 分类：numerical
> 标签：红色警戒, RTS, 单位属性, YAML规则, 泰伯利亚之日

## 概述
泰伯利亚之日的critters单位/建筑属性定义（YAML格式）

## 正文
```yaml
DOGGIE:
	Inherits@1: ^Infantry
	Inherits@2: ^RegularInfantryDeath
	Inherits@3: ^HealsOnTiberium
	Inherits@AUTOTARGET: ^AutoTargetGroundAssaultMove
	MapEditorData:
		Categories: Critter
	Tooltip:
		Name: actor-doggie-name
	Health:
		HP: 25000
	Selectable:
		Bounds: 724, 1448
	Valued:
		Cost: 100
	Armor:
		Type: Light
	RevealsShroud:
		Range: 4c0
	Mobile:
		Speed: 113
	Voiced:
		VoiceSet: Fiend
	Targetable:
		TargetTypes: Ground, Creep
	Armament:
		Weapon: FiendShard
	AttackFrontal:
		Voice: Attack
		FacingTolerance: 0
	AttackWander:
		WanderMoveRadius: 2
		MinMoveDelay: 200
		MaxMoveDelay: 600
	-SpawnActorOnDeath@FLAMEGUY:
	WithDeathAnimation@fire:
		DeathSequence: die-
		DeathTypes:
			FireDeath: burning
	HitShape:
		Type: Circle
			Radius: 213
	GrantConditionOnTerrain:
		Condition: hidingplace
		TerrainTypes: Tiberium, BlueTiberium
	GrantConditionOnMovement:
		Condition: moving
	GrantConditionOnAttack:
		ArmamentNames: primary
		Condition: attacking
	RenderSprites:
		Palette: greentiberium
	WithSpriteBody:
		RequiresCondition: hidingplace && !moving && !attacking
		StartSequence: laydown
		Sequence: hide
	WithInfantryBody:
		RequiresCondition: !hidingplace || moving || attacking

VISC_SML:
	Inherits: ^Visceroid
	Tooltip:
		Name: actor-visc-sml-name
	Health:
		HP: 20000
	AttackWander:
		WanderMoveRadius: 2
		MinMoveDelay: 30
		MaxMoveDelay: 60
	RenderSprites:
		Image: vissml
	Mobile:
		Locomotor: smallvisc
	Crushable:
		CrushClasses: visceroid-fusing
		WarnProbability: 0
		CrushedByFriendlies: True
	AutoCrusher:
		CrushClasses: visceroid-fusing
	TransformCrusherOnCrush:
		IntoActor: visc_lrg
		CrushClasses: visceroid-fusing

VISC_LRG:
	Inherits: ^Visceroid
	Inherits@CRATESTATS: ^CrateStatModifiers
	Inherits@AUTOTARGET: ^AutoTargetGroundAssaultMove
	Tooltip:
		Name: actor-visc-lrg-name
	Health:
		HP: 50000
	Armor:
		Type: Heavy
	RevealsShroud:
		Range: 4c0
	Armament:
		Weapon: SlimeAttack
		FireDelay: 10
	AutoTarget:
		ScanRadius: 5
	AttackFrontal:
		Voice: Attack
		FacingTolerance: 0
	AttackWander:
		WanderMoveRadius: 2
		MinMoveDelay: 25
		MaxMoveDelay: 50
	WithAttackAnimation:
		Sequence: attack
	RenderSprites:
		Image: vislrg

JFISH:
	Inherits: ^Visceroid
	Inherits@CRATESTATS: ^CrateStatModifiers
	Inherits@AUTOTARGET: ^AutoTargetGroundAssaultMove
	Tooltip:
		Name: actor-jfish-name
	Health:
		HP: 50000
	RevealsShroud:
		Range: 5c0
	Mobile:
		Speed: 72
		Locomotor: hover
	Armament:
		Weapon: Tentacle
		FireDelay: 10
	AutoTarget:
		ScanRadius: 5
	AttackFrontal:
		FacingTolerance: 0
	AttackWander:
		WanderMoveRadius: 6
		MinMoveDelay: 250
		MaxMoveDelay: 600
	WithAttackAnimation:
		Sequence: attack
	WithAttackOverlay@muzzle:
		Sequence: attack-shock
		Palette: bright
	RenderSprites:
		Image: floater
		Palette: player-nobright
	Selectable:
		Bounds: 965, 1930, 0, -301
	AmbientSound:
		SoundFiles: floatmov.aud, flotmov2.aud, flotmov3.aud, flotmov4.aud
		Delay: 150, 450
		Interval: 300, 800
	HitShape:
		Type: Circle
			Radius: 363
			VerticalTopOffset: 768

```

## 策划参考价值
RTS单位数值设计的教科书级参考：血量/攻击/射程/造价/建造时间。
