# Freeciv(nation) · miao

> 来源：longturn/freeciv21
> 原始链接：https://github.com/longturn/freeciv21/blob/main/data/nation/miao.ruleset
> 分类：numerical
> 标签：文明, 4X策略, 规则集, nation

## 概述
Freeciv nation规则集的miao定义

## 正文
```ruleset
[nation_miao]

name=_("Miao")
plural=_("?plural:Miao")
groups="Asian", "Ancient"
legend=_("According to Chinese legend, the Yellow Emperor of Huaxia\
 battled and defeated Chi You, leader of the Nine Li tribe, at the Battle\
 of Zhuolu in the 26th century BCE. For the Miao people of modern-day China,\
 Chi You - whom they refer to as \"Txiv Yawg\" - is a mythical king and\
 founding father of their nation. Most Miao live in southern China, but\
 there is a significant diaspora in southeast Asian countries as well as\
 Europe and North America, of which many belong to the \"Hmong\"\
 sub-group.")

leaders = {
 "name",                "sex"
 "Haam Choj",           "Male"
 "Touby Lyfoung",       "Male"
 "Paj Cai Vwj",         "Male"
 "Vaj Tsoov Loom",      "Male"
 "Qin Liangyu",         "Female"
 "Txiv Yawg",           "Male"
}

flag="hainan"
flag_alt="-"
style = "Asian"

init_techs=""
init_buildings=""
init_units=""

civilwar_nations = "Cantonese", "Vietnamese", "Thai", "Laotian"

cities =
; Mountains with Miao population
 "Wuling (mountains)",
 "Miao (mountains)",
 "Yueliang (mountains)",
 "Ma (mountains)",
 "Da Miao (mountains)",
 "Wumeng (mountains)",

; Miao autonomous counties
 "Mayang",
 "Jingzhou",
 "Chengbu",
 "Songtao",
 "Yingjiang",
 "Wuchuan",
 "Daozhen",
 "Zhenning",
 "Ziyun",
 "Guanling",
 "Weining",
 "Pingbian",
 "Jinping",
 "Luquan",
 "Xiushan",
 "Youyang",
 "Qianjiang",
 "Pengshui",
 "Rongshui",
 "Longsheng",
 "Longlin",
 "Qiong",
 "Baoting"

```

## 策划参考价值
4X SLG鼻祖级数值参考：单位/建筑/科技树/文明特性。
