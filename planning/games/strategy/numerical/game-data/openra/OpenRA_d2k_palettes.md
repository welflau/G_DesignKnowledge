# OpenRA(沙丘2000) · palettes 单位规则

> 来源：OpenRA/OpenRA
> 原始链接：https://github.com/OpenRA/OpenRA/blob/bleed/mods/d2k/rules/palettes.yaml
> 分类：numerical
> 标签：红色警戒, RTS, 单位属性, YAML规则, 沙丘2000

## 概述
沙丘2000的palettes单位/建筑属性定义（YAML格式）

## 正文
```yaml
^Palettes:
	PaletteFromFile:
		Name: terrain
		Filename: PALETTE.BIN
	PaletteFromFile@d2k:
		Name: d2k
		Filename: PALETTE.BIN
		ShadowIndex: 1
		CursorPalette: true
	PaletteFromFile@chrome:
		Name: chrome
		Filename: PALETTE.BIN
		ShadowIndex: 3
		AllowModifiers: false
	PaletteFromFile@effect:
		Name: effect
		Filename: PALETTE.BIN
		ShadowIndex: 1
		AllowModifiers: false
	ColorPickerPalette@colorpicker:
		Name: colorpicker
		BasePalette: d2k
		RemapIndex: 255, 254, 253, 252, 251, 250, 249, 248, 247, 246, 245, 244, 243, 242, 241, 240
		AllowModifiers: false
	PlayerColorPalette:
		BasePalette: d2k
		RemapIndex: 255, 254, 253, 252, 251, 250, 249, 248, 247, 246, 245, 244, 243, 242, 241, 240
	MenuPostProcessEffect:
		FadeInLength: 4
	FlashPostProcessEffect:
	ColorPickerColorShift:
		BasePalette: colorpicker
		MinHue: 0.32
		MaxHue: 0.34
	PlayerColorShift:
		BasePalette: player

```

## 策划参考价值
RTS单位数值设计的教科书级参考：血量/攻击/射程/造价/建造时间。
