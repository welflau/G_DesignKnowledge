# 命令与征服 · campaign

> 来源：OpenRA/OpenRA
> 原始链接：https://github.com/OpenRA/OpenRA
> 分类：gameplay
> 标签：命令与征服, RTS, 任务简报, 战役
> 游戏类型：RTS

## 概述
命令与征服的campaign——RTS战役/任务简报叙事

## 正文
```yaml
lst:
	idle:
		Filename: lst.shp
		Start: 0
		Facings: 1
		ZOffset: -1024
	icon:
		Filename: lsticnh.tem

boat:
	Defaults:
		Filename: boat.shp
	left:
		Facings: 32
	damaged-left:
		Start: 32
		Facings: 32
	critical-left:
		Start: 64
		Facings: 32
	wake-left:
		Filename: wake.shp
		Start: 6
		Length: 6
		Offset: 1,2
		Tick: 120
	right:
		Start: 96
		Facings: 32
	damaged-right:
		Start: 128
		Facings: 32
	critical-right:
		Start: 160
		Facings: 32
	wake-right:
		Filename: wake.shp
		Length: 6
		Offset: -1,2
		Tick: 120
	icon:
		Filename: boaticnh.tem

```

## 策划参考价值
RTS游戏战役叙事的数据结构：任务简报、胜利条件、故事文本如何与关卡绑定。
