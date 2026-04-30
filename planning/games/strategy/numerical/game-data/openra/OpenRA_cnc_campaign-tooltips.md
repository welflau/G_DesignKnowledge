# OpenRA(命令与征服) · campaign-tooltips 单位规则

> 来源：OpenRA/OpenRA
> 原始链接：https://github.com/OpenRA/OpenRA/blob/bleed/mods/cnc/rules/campaign-tooltips.yaml
> 分类：numerical
> 标签：红色警戒, RTS, 单位属性, YAML规则, 命令与征服

## 概述
命令与征服的campaign-tooltips单位/建筑属性定义（YAML格式）

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
RTS单位数值设计的教科书级参考：血量/攻击/射程/造价/建造时间。
