# OpenRA(命令与征服) · husks 单位规则

> 来源：OpenRA/OpenRA
> 原始链接：https://github.com/OpenRA/OpenRA/blob/bleed/mods/cnc/rules/husks.yaml
> 分类：numerical
> 标签：红色警戒, RTS, 单位属性, YAML规则, 命令与征服

## 概述
命令与征服的husks单位/建筑属性定义（YAML格式）

## 正文
```yaml
MCV.Husk:
	Inherits: ^Husk
	Tooltip:
		Name: actor-mcv-husk-name
	TransformOnCapture:
		IntoActor: mcv
	RenderSprites:
		Image: mcv.destroyed

HARV.Husk:
	Inherits: ^Husk
	Tooltip:
		Name: actor-harv-husk-name
	TransformOnCapture:
		IntoActor: harv
	RenderSprites:
		Image: harv.destroyed

APC.Husk:
	Inherits: ^Husk
	Tooltip:
		Name: actor-apc-husk-name
	TransformOnCapture:
		IntoActor: apc
	RenderSprites:
		Image: apc.destroyed

FTNK.Husk:
	Inherits: ^Husk
	Tooltip:
		Name: actor-ftnk-husk-name
	TransformOnCapture:
		IntoActor: ftnk
	RenderSprites:
		Image: ftnk.destroyed

ARTY.Husk:
	Inherits: ^LightHusk
	Tooltip:
		Name: actor-arty-husk-name
	TransformOnCapture:
		IntoActor: arty
	RenderSprites:
		Image: arty.destroyed

BGGY.Husk:
	Inherits: ^LightHusk
	Tooltip:
		Name: actor-bggy-husk-name
	TransformOnCapture:
		IntoActor: bggy
	RenderSprites:
		Image: bggy.destroyed

BIKE.Husk:
	Inherits: ^LightHusk
	Tooltip:
		Name: actor-bike-husk-name
	TransformOnCapture:
		IntoActor: bike
	RenderSprites:
		Image: bike.destroyed

JEEP.Husk:
	Inherits: ^LightHusk
	Tooltip:
		Name: actor-jeep-husk-name
	TransformOnCapture:
		IntoActor: jeep
	RenderSprites:
		Image: jeep.destroyed

LTNK.Husk:
	Inherits: ^Husk
	Tooltip:
		Name: actor-ltnk-husk-name
	ThrowsParticle@turret:
		Anim: turret
	TransformOnCapture:
		IntoActor: ltnk
	RenderSprites:
		Image: ltnk.destroyed

MTNK.Husk:
	Inherits: ^Husk
	Tooltip:
		Name: actor-mtnk-husk-name
	ThrowsParticle@turret:
		Anim: turret
	TransformOnCapture:
		IntoActor: mtnk
	RenderSprites:
		Image: mtnk.destroyed

HTNK.Husk:
	Inherits: ^Husk
	Tooltip:
		Name: actor-htnk-husk-name
	ThrowsParticle@turret:
		Anim: turret
	TransformOnCapture:
		IntoActor: htnk
	RenderSprites:
		Image: htnk.destroyed

MSAM.Husk:
	Inherits: ^LightHusk
	Tooltip:
		Name: actor-msam-husk-name
	ThrowsParticle@turret:
		Anim: turret
	TransformOnCapture:
		IntoActor: msam
	RenderSprites:
		Image: msam.destroyed

MLRS.Husk:
	Inherits: ^LightHusk
	Tooltip:
		Name: actor-mlrs-husk-name
	ThrowsParticle@turret:
		Anim: turret
	TransformOnCapture:
		IntoActor: mlrs
	RenderSprites:
		Image: mlrs.destroyed

STNK.Husk:
	Inherits: ^Husk
	Tooltip:
		Name: actor-stnk-husk-name
	TransformOnCapture:
		IntoActor: stnk
	RenderSprites:
		Image: stnk.destroyed
	FireWarheadsOnDeath:
		Weapon: UnitExplodeStealthTank
		EmptyWeapon: UnitExplodeStealthTank

TRUCK.Husk:
	Inherits: ^LightHusk
	Tooltip:
		Name: actor-truck-husk-name
	TransformOnCapture:
		IntoActor: truck
	RenderSprites:
		Image: truck.destroyed

```

## 策划参考价值
RTS单位数值设计的教科书级参考：血量/攻击/射程/造价/建造时间。
