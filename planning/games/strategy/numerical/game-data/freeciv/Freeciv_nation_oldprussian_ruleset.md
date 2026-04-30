# Freeciv(nation) · oldprussian

> 来源：longturn/freeciv21
> 原始链接：https://github.com/longturn/freeciv21/blob/main/data/nation/oldprussian.ruleset
> 分类：numerical
> 标签：文明, 4X策略, 规则集, nation

## 概述
Freeciv nation规则集的oldprussian定义

## 正文
```ruleset
[nation_oldprussian]

name=_("Old Prussian")
plural=_("?plural:Old Prussians")
groups="Medieval", "European"
legend=_("The Prussians were Baltic peoples inhabiting the area between\
 the Pomerania, Mazovia, Lithuania and the Baltic Sea (Baltic coast between\
 the lower Vistula and lower Nemen). They were conquered and germanized by\
 the Teutonic Order.")
leaders = {
 "name",                "sex"
 "Auktuma",             "Male"
 "Divonis",             "Male"
 "Herkus Mantas",       "Male"
 "Richardas Glandas",   "Male"
 "Glapas",              "Male"
 "Komantas",            "Male"
}
flag="prusai"
flag_alt = "-"
style = "Celtic"

init_techs=""
init_buildings=""
init_units=""

conflicts_with="prussian"
civilwar_nations = "lithuanian" ; polanian

cities =
  "Truso",
"Sirgune",
"Graudings",  
"Elbings",
"Regneta",
"Orneta",
"Wangus",
"Kunnegsgarbs",       ; Königsberg/Kaliningrad
"Salpwange",
"Weluwa",
"Wiskiauten",
"Rast",
"Alna",
"Kwedins",
"Iluwa",
"Berents",
"Nydda",
"Wurmen",
"Kele",
"Susse",
"Pukis",
"Tuga",
"Laba"

```

## 策划参考价值
4X SLG鼻祖级数值参考：单位/建筑/科技树/文明特性。
