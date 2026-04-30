# OpenRA(泰伯利亚之日) · shared-support 单位规则

> 来源：OpenRA/OpenRA
> 原始链接：https://github.com/OpenRA/OpenRA/blob/bleed/mods/ts/rules/shared-support.yaml
> 分类：numerical
> 标签：红色警戒, RTS, 单位属性, YAML规则, 泰伯利亚之日

## 概述
泰伯利亚之日的shared-support单位/建筑属性定义（YAML格式）

## 正文
```yaml
NAPULS:
	Inherits: ^Support
	Inherits@IDISABLE: ^DisableOnLowPowerOrPowerDown
	Inherits@SHAPE: ^2x2Shape
	Valued:
		Cost: 1000
	Tooltip:
		Name: actor-napuls.name
	Buildable:
		Queue: Support
		BuildPaletteOrder: 110
		Prerequisites: radar, ~techlevel.superweapons
		Description: actor-napuls.description
	Building:
		Footprint: xx xx
		Dimensions: 2,2
	Health:
		HP: 50000
	Armor:
		Type: Heavy
	RevealsShroud:
		Range: 8c0
	Turreted:
		TurnSpeed: 40
		InitialFacing: 896
		RealignDelay: -1
	AttackTurreted:
		RequiresCondition: !build-incomplete && !empdisable && !disabled
	Armament:
		Weapon: EMPulseCannon
		LocalOffset: 212,0,1768
		LocalYaw: 0,100
	WithSpriteTurret:
		RequiresCondition: !build-incomplete
		Sequence: turret
	Power:
		Amount: -150
	RenderSprites:
		Image: napuls.gdi
		FactionImages:
			gdi: napuls.gdi
			nod: napuls.nod
	ProvidesPrerequisite@gdi:
		ResetOnOwnerChange: true
	ProvidesPrerequisite@gdi:
		Factions: gdi
		Prerequisite: napuls
	AttackOrderPower:
		PauseOnCondition: empdisable || disabled
		Cursor: emp
		Icon: emp
		ChargeInterval: 3375
		Name: actor-napuls.attackorderpower-name
		Description: actor-napuls.attackorderpower-description
		EndChargeSpeechNotification: EmPulseCannonReady
		SelectTargetSpeechNotification: SelectTarget
		EndChargeTextNotification: notification-emp-cannon-ready
		SelectTargetTextNotification: notification-select-target

```

## 策划参考价值
RTS单位数值设计的教科书级参考：血量/攻击/射程/造价/建造时间。
