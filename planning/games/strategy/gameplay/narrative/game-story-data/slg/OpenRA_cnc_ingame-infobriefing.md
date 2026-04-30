# 命令与征服 · ingame-infobriefing

> 来源：OpenRA/OpenRA
> 原始链接：https://github.com/OpenRA/OpenRA
> 分类：gameplay
> 标签：命令与征服, RTS, 任务简报, 战役
> 游戏类型：RTS

## 概述
命令与征服的ingame-infobriefing——RTS战役/任务简报叙事

## 正文
```yaml
Container@MAP_PANEL:
	Height: PARENT_HEIGHT
	Width: PARENT_WIDTH
	Logic: GameInfoBriefingLogic
	Children:
		Background@PREVIEW_BG:
			X: (PARENT_WIDTH - WIDTH) / 2
			Y: 15
			Width: 362
			Height: 202
			Background: panel-black
			Children:
				MapPreview@MAP_PREVIEW:
					Width: 360
					Height: 200
					X: 1
					Y: 1
					IgnoreMouseOver: True
					IgnoreMouseInput: True
					ShowSpawnPoints: False
		ScrollPanel@MAP_DESCRIPTION_PANEL:
			X: 15
			Y: 228
			Width: PARENT_WIDTH - 30
			Height: PARENT_HEIGHT - 228 - 15
			Children:
				Label@MAP_DESCRIPTION:
					X: 4
					Y: 2
					Width: PARENT_WIDTH - 32

```

## 策划参考价值
RTS游戏战役叙事的数据结构：任务简报、胜利条件、故事文本如何与关卡绑定。
