# OpenRA(沙丘2000) · starport 单位规则

> 来源：OpenRA/OpenRA
> 原始链接：https://github.com/OpenRA/OpenRA/blob/bleed/mods/d2k/rules/starport.yaml
> 分类：numerical
> 标签：红色警戒, RTS, 单位属性, YAML规则, 沙丘2000

## 概述
沙丘2000的starport单位/建筑属性定义（YAML格式）

## 正文
```yaml
mcv.starport:
	Inherits: mcv
	Buildable:
		Prerequisites: starport
		Queue: Starport
		BuildDuration: 0
	Valued:
		Cost: 2500
	-MapEditorData:
	RenderSprites:
		Image: mcv
	UpdatesPlayerStatistics:
		OverrideActor: mcv

harvester.starport:
	Inherits: harvester
	Buildable:
		Prerequisites: starport
		Queue: Starport
		BuildDuration: 0
	Valued:
		Cost: 1500
	-MapEditorData:
	RenderSprites:
		Image: harvester
	UpdatesPlayerStatistics:
		OverrideActor: harvester

trike.starport:
	Inherits: trike
	Buildable:
		Prerequisites: starport
		Queue: Starport
		BuildDuration: 0
	Valued:
		Cost: 315
	-MapEditorData:
	RenderSprites:
		Image: trike
	UpdatesPlayerStatistics:
		OverrideActor: trike

quad.starport:
	Inherits: quad
	Buildable:
		Prerequisites: starport
		Queue: Starport
		BuildDuration: 0
	Valued:
		Cost: 500
	-MapEditorData:
	RenderSprites:
		Image: quad
	UpdatesPlayerStatistics:
		OverrideActor: quad

siege_tank.starport:
	Inherits: siege_tank
	Buildable:
		Prerequisites: starport
		Queue: Starport
		BuildDuration: 0
	Valued:
		Cost: 1075
	-MapEditorData:
	RenderSprites:
		Image: siege_tank
	UpdatesPlayerStatistics:
		OverrideActor: siege_tank

missile_tank.starport:
	Inherits: missile_tank
	Buildable:
		Prerequisites: starport
		Queue: Starport
		BuildDuration: 0
	Valued:
		Cost: 1250
	-MapEditorData:
	RenderSprites:
		Image: missile_tank
	UpdatesPlayerStatistics:
		OverrideActor: missile_tank

combat_tank_a.starport:
	Inherits: combat_tank_a
	Buildable:
		Prerequisites: ~starport.atreides_combat
		Queue: Starport
		BuildDuration: 0
	Valued:
		Cost: 875
	-MapEditorData:
	RenderSprites:
		Image: combat_tank_a
	UpdatesPlayerStatistics:
		OverrideActor: combat_tank_a

combat_tank_h.starport:
	Inherits: combat_tank_h
	Buildable:
		Prerequisites: ~starport.harkonnen_combat
		Queue: Starport
		BuildDuration: 0
	Valued:
		Cost: 875
	-MapEditorData:
	RenderSprites:
		Image: combat_tank_h
	UpdatesPlayerStatistics:
		OverrideActor: combat_tank_h

combat_tank_o.starport:
	Inherits: combat_tank_o
	Buildable:
		Prerequisites: ~starport.ordos_combat
		Queue: Starport
		BuildDuration: 0
	Valued:
		Cost: 875
	-MapEditorData:
	RenderSprites:
		Image: combat_tank_o
	UpdatesPlayerStatistics:
		OverrideActor: combat_tank_o

carryall.starport:
	Inherits: carryall
	Buildable:
		Prerequisites: starport
		Queue: Starport
		BuildDuration: 0
	Valued:
		Cost: 1500
	-MapEditorData:
	UpdatesPlayerStatistics:
		OverrideActor: carryall

```

## 策划参考价值
RTS单位数值设计的教科书级参考：血量/攻击/射程/造价/建造时间。
