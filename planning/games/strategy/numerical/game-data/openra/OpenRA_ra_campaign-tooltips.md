# OpenRA(红色警戒) · campaign-tooltips 单位规则

> 来源：OpenRA/OpenRA
> 原始链接：https://github.com/OpenRA/OpenRA/blob/bleed/mods/ra/rules/campaign-tooltips.yaml
> 分类：numerical
> 标签：红色警戒, RTS, 单位属性, YAML规则, 红色警戒

## 概述
红色警戒的campaign-tooltips单位/建筑属性定义（YAML格式）

## 正文
```yaml
^Vehicle:
	Tooltip:
		GenericVisibility: Enemy
		ShowOwnerRow: false

^Infantry:
	Tooltip:
		GenericVisibility: Enemy
		ShowOwnerRow: false

^Ship:
	Tooltip:
		GenericVisibility: Enemy
		ShowOwnerRow: false

^NeutralPlane:
	Tooltip:
		GenericVisibility: Enemy
		ShowOwnerRow: false

^Helicopter:
	Tooltip:
		GenericVisibility: Enemy
		ShowOwnerRow: false

^Building:
	Tooltip:
		GenericVisibility: Enemy
		ShowOwnerRow: false

^CivBuilding:
	Tooltip:
		ShowOwnerRow: false

^CivField:
	Tooltip:
		ShowOwnerRow: false

^TechBuilding:
	Tooltip:
		ShowOwnerRow: false

^Wall:
	Tooltip:
		ShowOwnerRow: false

^Husk:
	Tooltip:
		GenericVisibility: Enemy, Ally, Neutral
		GenericStancePrefix: false
		ShowOwnerRow: false

^PlaneHusk:
	Tooltip:
		GenericVisibility: Enemy, Ally, Neutral
		GenericStancePrefix: false
		ShowOwnerRow: false

^HelicopterHusk:
	Tooltip:
		GenericVisibility: Enemy, Ally, Neutral
		GenericStancePrefix: false
		ShowOwnerRow: false

^Crate:
	Tooltip:
		ShowOwnerRow: false

^Mine:
	Tooltip:
		GenericVisibility: Ally, Enemy
		ShowOwnerRow: false

FLARE:
	Tooltip:
		ShowOwnerRow: false

SPY:
	DisguiseTooltip:
		ShowOwnerRow: false

BIO:
	-TooltipDescription@ally:
	-TooltipDescription@other:

FCOM:
	Tooltip:
		GenericVisibility: Enemy
	-TooltipDescription@ally:
	-TooltipDescription@other:

MISS:
	Tooltip:
		Name: actor-technology-center-name
	-TooltipDescription@ally:
	-TooltipDescription@other:

HOSP:
	Tooltip:
		GenericVisibility: Enemy
	-TooltipDescription@ally:
	-TooltipDescription@other:

```

## 策划参考价值
RTS单位数值设计的教科书级参考：血量/攻击/射程/造价/建造时间。
