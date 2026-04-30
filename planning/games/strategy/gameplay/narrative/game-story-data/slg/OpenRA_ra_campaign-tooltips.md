# 红色警戒 · campaign-tooltips

> 来源：OpenRA/OpenRA
> 原始链接：https://github.com/OpenRA/OpenRA
> 分类：gameplay
> 标签：红色警戒, RTS, 任务简报, 战役
> 游戏类型：RTS

## 概述
红色警戒的campaign-tooltips——RTS战役/任务简报叙事

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
RTS游戏战役叙事的数据结构：任务简报、胜利条件、故事文本如何与关卡绑定。
