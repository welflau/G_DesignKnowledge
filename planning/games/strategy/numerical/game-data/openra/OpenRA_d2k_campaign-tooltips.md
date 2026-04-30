# OpenRA(沙丘2000) · campaign-tooltips 单位规则

> 来源：OpenRA/OpenRA
> 原始链接：https://github.com/OpenRA/OpenRA/blob/bleed/mods/d2k/rules/campaign-tooltips.yaml
> 分类：numerical
> 标签：红色警戒, RTS, 单位属性, YAML规则, 沙丘2000

## 概述
沙丘2000的campaign-tooltips单位/建筑属性定义（YAML格式）

## 正文
```yaml
^Vehicle:
	Tooltip:
		GenericVisibility: Enemy, Neutral
		NeutralPrefix: neutral-prefix
		ShowOwnerRow: false

^Tank:
	Tooltip:
		GenericVisibility: Enemy, Neutral
		NeutralPrefix: neutral-prefix
		ShowOwnerRow: false

^Infantry:
	Tooltip:
		GenericVisibility: Enemy, Neutral
		NeutralPrefix: neutral-prefix
		ShowOwnerRow: false

^Plane:
	Tooltip:
		GenericVisibility: Enemy, Neutral
		NeutralPrefix: neutral-prefix
		ShowOwnerRow: false

^Building:
	Tooltip:
		GenericVisibility: Enemy, Neutral
		NeutralPrefix: neutral-prefix
		ShowOwnerRow: false

^Husk:
	Tooltip:
		GenericVisibility: Enemy, Ally, Neutral
		GenericStancePrefix: false
		ShowOwnerRow: false

^Crate:
	Tooltip:
		ShowOwnerRow: false

wall:
	Tooltip:
		GenericVisibility: Enemy, Neutral
		NeutralPrefix: neutral-prefix
		ShowOwnerRow: false

```

## 策划参考价值
RTS单位数值设计的教科书级参考：血量/攻击/射程/造价/建造时间。
