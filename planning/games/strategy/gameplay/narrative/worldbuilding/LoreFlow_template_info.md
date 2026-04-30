# LoreFlow模板 · info

> 来源：Galygious/Lore-Flow
> 原始链接：https://github.com/Galygious/Lore-Flow
> 分类：gameplay
> 标签：世界观构建, 模板

## 概述
LoreFlow的.json模板文件

## 正文
```json
{
	"fixed": {
		"file_version": "{{.Info.ProductVersion}}"
	},
	"info": {
		"0000": {
			"ProductVersion": "{{.Info.ProductVersion}}",
			"CompanyName": "{{.Info.CompanyName}}",
			"FileDescription": "{{.Info.ProductName}}",
			"LegalCopyright": "{{.Info.Copyright}}",
			"ProductName": "{{.Info.ProductName}}",
			"Comments": "{{.Info.Comments}}"
		}
	}
}
```

## 策划参考价值
世界观条目的结构化模板参考。
