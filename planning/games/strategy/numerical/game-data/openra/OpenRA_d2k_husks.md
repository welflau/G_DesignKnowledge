# OpenRA(沙丘2000) · husks 单位规则

> 来源：OpenRA/OpenRA
> 原始链接：https://github.com/OpenRA/OpenRA/blob/bleed/mods/d2k/rules/husks.yaml
> 分类：numerical
> 标签：红色警戒, RTS, 单位属性, YAML规则, 沙丘2000

## 概述
沙丘2000的husks单位/建筑属性定义（YAML格式）

## 正文
```yaml
mcv.husk:
	Inherits: ^VehicleHusk
	Health:
		HP: 11000
	Tooltip:
		Name: actor-mcv-husk-name
	TransformOnCapture:
		IntoActor: mcv
	InfiltrateForTransform:
		IntoActor: mcv

harvester.husk:
	Inherits: ^VehicleHusk
	Tooltip:
		Name: actor-harvester-husk-name
	TransformOnCapture:
		IntoActor: harvester
	InfiltrateForTransform:
		IntoActor: harvester

siege_tank.husk:
	Inherits: ^VehicleHusk
	Tooltip:
		Name: actor-siege-tank-husk-name
	ThrowsParticle@turret:
		Anim: turret
	TransformOnCapture:
		IntoActor: siege_tank
	InfiltrateForTransform:
		IntoActor: siege_tank

missile_tank.husk:
	Inherits: ^VehicleHusk
	Tooltip:
		Name: actor-missile-tank-husk-name
	ThrowsParticle@turret:
		Anim: turret
	ThrowsParticle@debris01:
		Anim: tankdebris01
	ThrowsParticle@debris02:
		Anim: tankdebris02
	ThrowsParticle@debris03:
		Anim: tankdebris03
	ThrowsParticle@debris04:
		Anim: tankdebris04
	TransformOnCapture:
		IntoActor: missile_tank
	InfiltrateForTransform:
		IntoActor: missile_tank

sonic_tank.husk:
	Inherits: ^VehicleHusk
	Husk:
		Locomotor: vehicle
	Health:
		HP: 9000
	Tooltip:
		Name: actor-sonic-tank-husk-name
	ThrowsParticle@turret:
		Anim: turret
	ThrowsParticle@debris01:
		Anim: tankdebris01
	ThrowsParticle@debris02:
		Anim: tankdebris02
	ThrowsParticle@debris03:
		Anim: tankdebris03
	ThrowsParticle@debris04:
		Anim: tankdebris04
	TransformOnCapture:
		IntoActor: sonic_tank
	InfiltrateForTransform:
		IntoActor: sonic_tank

devastator.husk:
	Inherits: ^VehicleHusk
	Husk:
		Locomotor: devastator
	Health:
		HP: 10000
	Tooltip:
		Name: actor-devastator-husk-name
	TransformOnCapture:
		IntoActor: devastator
	InfiltrateForTransform:
		IntoActor: devastator

deviator.husk:
	Inherits: ^VehicleHusk
	Health:
		HP: 10000
	Tooltip:
		Name: actor-deviator-husk-name
	ThrowsParticle@turret:
		Anim: turret
		TurnSpeed: 150
	ThrowsParticle@debris01:
		Anim: tankdebris01
	ThrowsParticle@debris02:
		Anim: tankdebris02
	ThrowsParticle@debris03:
		Anim: tankdebris03
	ThrowsParticle@debris04:
		Anim: tankdebris04
	TransformOnCapture:
		IntoActor: deviator
	InfiltrateForTransform:
		IntoActor: deviator
	FireWarheads:
		Weapons: DeviatorGas
		Interval: 50
		StartCooldown: 100

^combat_tank.husk:
	Inherits: ^VehicleHusk
	Tooltip:
		Name: meta-combat-tank-husk-name
	ThrowsParticle@turret:
		Anim: turret

combat_tank_a.husk:
	Inherits: ^combat_tank.husk
	TransformOnCapture:
		IntoActor: combat_tank_a
	InfiltrateForTransform:
		IntoActor: combat_tank_a

combat_tank_h.husk:
	Inherits: ^combat_tank.husk
	TransformOnCapture:
		IntoActor: combat_tank_h
	InfiltrateForTransform:
		IntoActor: combat_tank_h

combat_tank_o.husk:
	Inherits: ^combat_tank.husk
	TransformOnCapture:
		IntoActor: combat_tank_o
	InfiltrateForTransform:
		IntoActor: combat_tank_o

```

## 策划参考价值
RTS单位数值设计的教科书级参考：血量/攻击/射程/造价/建造时间。
