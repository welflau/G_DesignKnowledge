# OpenRA(泰伯利亚之日) · husks 单位规则

> 来源：OpenRA/OpenRA
> 原始链接：https://github.com/OpenRA/OpenRA/blob/bleed/mods/ts/rules/husks.yaml
> 分类：numerical
> 标签：红色警戒, RTS, 单位属性, YAML规则, 泰伯利亚之日

## 概述
泰伯利亚之日的husks单位/建筑属性定义（YAML格式）

## 正文
```yaml
DSHP.Husk:
	Inherits: ^AircraftHusk
	Tooltip:
		Name: actor-dshp-husk-name
	Aircraft:
		TurnSpeed: 20
		Speed: 168
	-RenderSprites:
	RenderVoxels:
		Image: dshp

ORCA.Husk:
	Inherits: ^AircraftHusk
	Tooltip:
		Name: actor-orca-husk-name
	Aircraft:
		TurnSpeed: 20
		Speed: 186
	RenderSprites:
		Image: orca
	RenderVoxels:
		Image: orca

ORCA.Husk.EMP:
	Inherits: ORCA.Husk
	Inherits@EMP: ^EmpVisualEffects

ORCAB.Husk:
	Inherits: ^AircraftHusk
	Tooltip:
		Name: actor-orcab-husk-name
	Aircraft:
		TurnSpeed: 12
		Speed: 96
	FallsToEarth:
		MaximumSpinSpeed: 24
	RenderSprites:
		Image: orcab
	RenderVoxels:
		Image: orcab

ORCAB.Husk.EMP:
	Inherits: ORCAB.Husk
	Inherits@EMP: ^EmpVisualEffects

ORCATRAN.Husk:
	Inherits: ^AircraftHusk
	Tooltip:
		Name: actor-orcatran-husk-name
	Aircraft:
		TurnSpeed: 20
		Speed: 84
	RenderSprites:
		Image: orcatran
	RenderVoxels:
		Image: orcatran

ORCATRAN.Husk.EMP:
	Inherits: ORCATRAN.Husk
	Inherits@EMP: ^EmpVisualEffects

TRNSPORT.Husk:
	Inherits: ^AircraftHusk
	Tooltip:
		Name: actor-trnsport-husk-name
	Aircraft:
		TurnSpeed: 20
		Speed: 149
	RenderSprites:
		Image: trnsport
	RenderVoxels:
		Image: trnsport

TRNSPORT.Husk.EMP:
	Inherits: TRNSPORT.Husk
	Inherits@EMP: ^EmpVisualEffects

SCRIN.Husk:
	Inherits: ^AircraftHusk
	Tooltip:
		Name: actor-scrin-husk-name
	Aircraft:
		TurnSpeed: 12
		Speed: 168
	FallsToEarth:
		MaximumSpinSpeed: 24
	RenderSprites:
		Image: scrin
	RenderVoxels:
		Image: scrin

SCRIN.Husk.EMP:
	Inherits: SCRIN.Husk
	Inherits@EMP: ^EmpVisualEffects

APACHE.Husk:
	Inherits: ^AircraftHusk
	Tooltip:
		Name: actor-apache-husk-name
	Aircraft:
		TurnSpeed: 20
		Speed: 130
	WithIdleOverlay:
		Offset: 85,0,598
		Sequence: rotor
	RenderSprites:
		Image: apache
	RenderVoxels:
		Image: apache

APACHE.Husk.EMP:
	Inherits: APACHE.Husk
	Inherits@EMP: ^EmpVisualEffects

```

## 策划参考价值
RTS单位数值设计的教科书级参考：血量/攻击/射程/造价/建造时间。
