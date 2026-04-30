# 命令与征服 · campaign-tooltips

> 来源：OpenRA/OpenRA
> 原始链接：https://github.com/OpenRA/OpenRA
> 分类：gameplay
> 标签：命令与征服, RTS, 任务简报, 战役
> 游戏类型：RTS

## 概述
命令与征服的campaign-tooltips——RTS战役/任务简报叙事

## 正文
```yaml
^Vehicle:
	Tooltip:
		GenericVisibility: Enemy
		ShowOwnerRow: false

^Tank:
	Tooltip:
		GenericVisibility: Enemy
		ShowOwnerRow: false

^Helicopter:
	Tooltip:
		GenericVisibility: Enemy
		ShowOwnerRow: false

^Infantry:
	Tooltip:
		GenericVisibility: Enemy
		ShowOwnerRow: false

^Plane:
	Tooltip:
		GenericVisibility: Enemy
		ShowOwnerRow: false

^Ship:
	Tooltip:
		GenericVisibility: Enemy
		ShowOwnerRow: false

^Building:
	Tooltip:
		GenericVisibility: Enemy
		ShowOwnerRow: false

^Wall:
	Tooltip:
		ShowOwnerRow: false

^CivBuilding:
	Tooltip:
		GenericVisibility: Enemy, Neutral
		ShowOwnerRow: false

^CivBuildingHusk:
	Tooltip:
		GenericVisibility: Enemy, Neutral
		ShowOwnerRow: false

^TechBuilding:
	Tooltip:
		GenericVisibility: None
		ShowOwnerRow: false

^CommonHuskDefaults:
	Tooltip:
		GenericVisibility: Enemy, Ally, Neutral
		GenericStancePrefix: false
		ShowOwnerRow: false

^DINO:
	Tooltip:
		ShowOwnerRow: false

MISS:
	Tooltip:
		GenericVisibility: None
		ShowOwnerRow: False
	-TooltipDescription@ally:
	-TooltipDescription@other:

BIO:
	-TooltipDescription@ally:
	-TooltipDescription@other:

ARCO:
	Tooltip:
		GenericVisibility: None
		ShowOwnerRow: False

ARCO.Husk:
	Tooltip:
		GenericVisibility: None

V19.Husk:
	Tooltip:
		GenericVisibility: None

HOSP.Husk:
	Tooltip:
		GenericVisibility: None

BIO.Husk:
	Tooltip:
		GenericVisibility: None

```

## 策划参考价值
RTS游戏战役叙事的数据结构：任务简报、胜利条件、故事文本如何与关卡绑定。
