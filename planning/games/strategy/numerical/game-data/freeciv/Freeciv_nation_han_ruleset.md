# Freeciv(nation) · han

> 来源：longturn/freeciv21
> 原始链接：https://github.com/longturn/freeciv21/blob/main/data/nation/han.ruleset
> 分类：numerical
> 标签：文明, 4X策略, 规则集, nation

## 概述
Freeciv nation规则集的han定义

## 正文
```ruleset
[nation_han]

name=_("Han")
plural=_("?plural:Han")
groups="Ancient", "Medieval", "Early Modern", "Asian"
legend=_("The Han people are the majority ethnic group in China, tracing\
 their lineage back to \"Yandi\" (the Yan Emperor) and \"Huangdi\" (the\
 Yellow Emperor), legendary god-kings of prehistory.")

leaders = {
 "name",                "sex"
 "Wu Zetian",           "Female"
 "Li Shimin",           "Male"
 "Liu Bei",             "Male"
 "Liu Bang",            "Male"
 "Qin Shihuang",        "Male"
 "Shun",                "Male"
 "Yao",                 "Male"
 "Da Yu",               "Male"
 "Huangdi",             "Male" ; Yellow Emperor
 "Yandi",               "Male" ; Yan Emperor
}

ruler_titles = {
 "government",      "male_title",      "female_title"
 "Monarchy",        _("Emperor %s"),      _("Empress Dowager %s")
 "Democracy",       _("Chancellor %s"),   _("?female:Chancellor %s")
 "Communism",       _("Chairman %s"),     _("Chairwoman %s")
}

flag="han"
flag_alt="china"
style = "Asian"

init_techs=""
init_buildings=""
init_units=""

conflicts_with="Chinese"
civilwar_nations=
; /* People's Republic of China */
"Chinese",
; /* Republic of China */
"Taiwanese",

"Korean", "Vietnamese", "Miao", "Zhuang", "Cantonese"

cities =
; Xia dynasty
 "Song",
 "Yangcheng",
 "Chu",
 "Qiongshi",
 "Zhen",
 "Diqiu",
 "Yuan",
 "Laoqiu",
 "Xihe",
 "Zhen",
 "Henan",
; Shang dynasty
 "Bo",
 "Fan",
 "Dishi",
 "Shang",
 "Shangqiu",
 "Yin",
 "Xiao",
 "Xiang",
 "Xing",
 "Bi",
 "Yan",
; Zhou dynasty
 "Gong",
; Qin dynasty
 "Xiquanqiu",
 "Pingyang",
 "Yong",
 "Jingyang",
 "Liyang",
 "Xianyang",
; Han dynasty
 "Luoyang",
 "Liyang",
 "Chang'an",
 "Xu",
; Jin dynasty
 "Jiankang",
; Song dynasty
 "Dongjing",
 "Lin'an",
; Ming dynasty
 "Beijing",
 "Fuzhou",
 "Zhaoqing"

```

## 策划参考价值
4X SLG鼻祖级数值参考：单位/建筑/科技树/文明特性。
